"""
A small, fully local rule-based query engine.

No external AI API is called here — everything runs offline against the
in-memory PROPOSALS store using regex-based extraction. It understands:

  - "how many ..." -> answer with a count
  - "section 3" / "chapter 4"        -> filter by code section / chapter
  - "accepted" / "declined" / "under review" / "pending" -> filter by status
  - "changes made" / "changes were made" -> implies accepted (adopted) changes
  - "last 5 years" / "past 5 years" / "in 2 years" / "within 2 years" -> time window
  - "since 2023"                     -> filter from that year forward
  - a bare year like "2024"          -> filter to that calendar year
  - "last three" / "last 3"          -> limit result count to the N most recent
  - free text with no recognized filters -> falls back to keyword search
"""

import re
from datetime import date

from data.mock_data import PROPOSALS

NUM_WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "fifteen": 15, "twenty": 20,
}

STATUS_KEYWORDS = {
    "under review": "under_review",
    "in review": "under_review",
    "still pending": "under_review",
    "pending": "under_review",
    "accepted": "accepted",
    "approved": "accepted",
    "adopted": "accepted",
    "declined": "declined",
    "rejected": "declined",
    "denied": "declined",
}

STATUS_LABELS = {
    "accepted": "accepted",
    "under_review": "under review",
    "declined": "declined",
}


def _relevant_date(p):
    """The date most relevant to 'when did this happen' — decision date if
    the proposal has been decided, otherwise submission date."""
    return p.get("date_decided") or p.get("date_submitted")


def _parse_limit(text):
    # "last three changes", "last 3 proposals" — NOT "last 3 years"
    m = re.search(
        r"\blast\s+(\d+|" + "|".join(NUM_WORDS.keys()) + r")\b(?!\s*years?)",
        text,
    )
    if m:
        val = m.group(1)
        return int(val) if val.isdigit() else NUM_WORDS[val]
    return None


def _parse_years_window(text):
    m = re.search(r"\b(?:last|past)\s+(\d+)\s+years?\b", text)
    if m:
        return int(m.group(1))
    m = re.search(r"\b(?:in|within|over)\s+(?:the\s+)?(?:last\s+)?(\d+)\s+years?\b", text)
    if m:
        return int(m.group(1))
    return None


def _parse_since_year(text):
    m = re.search(r"\bsince\s+(20\d{2})\b", text)
    if m:
        return int(m.group(1))
    return None


def _parse_bare_year(text):
    m = re.search(r"\b(20\d{2})\b", text)
    if m:
        return int(m.group(1))
    return None


def _parse_section(text):
    m = re.search(r"section\s+([\d]+(?:\.\d+)*)", text)
    if m:
        return ("section", m.group(1))
    m = re.search(r"(?:§|sec\.?)\s*([\d]+(?:\.\d+)*)", text)
    if m:
        return ("section", m.group(1))
    m = re.search(r"chapter\s+([\d]+)", text)
    if m:
        return ("chapter", m.group(1))
    return None


def _parse_status(text):
    for kw, status in STATUS_KEYWORDS.items():
        if kw in text:
            return status
    # "changes made to the code" implies adopted/accepted changes
    if re.search(r"\bchanges?\s+(?:were\s+|have\s+been\s+)?made\b", text):
        return "accepted"
    return None


def run_query(raw_text):
    text = (raw_text or "").strip().lower()
    if not text:
        return {"interpretation": "Type a question about the code's history to get started.",
                "count": 0, "results": []}

    is_count_question = text.startswith("how many") or " how many" in text

    limit = _parse_limit(text)
    years_window = _parse_years_window(text)
    since_year = _parse_since_year(text) if not years_window else None
    bare_year = _parse_bare_year(text) if not years_window and not since_year else None
    section_filter = _parse_section(text)
    status_filter = _parse_status(text)

    results = list(PROPOSALS.values())
    interpretation_parts = []

    if section_filter:
        kind, value = section_filter
        if kind == "chapter":
            results = [p for p in results if p.get("chapter", "").lower().startswith(f"chapter {value}")]
            interpretation_parts.append(f"in Chapter {value}")
        else:
            results = [p for p in results if p.get("code_section", "").startswith(value)]
            interpretation_parts.append(f"affecting Section {value}")

    if status_filter:
        results = [p for p in results if p["status"] == status_filter]
        interpretation_parts.append(f'with status "{STATUS_LABELS[status_filter]}"')

    if years_window:
        cutoff = date.today().replace(year=date.today().year - years_window)
        results = [p for p in results if _relevant_date(p) and _relevant_date(p) >= cutoff.isoformat()]
        interpretation_parts.append(f"in the last {years_window} years")
    elif since_year:
        results = [p for p in results if _relevant_date(p) and _relevant_date(p) >= f"{since_year}-01-01"]
        interpretation_parts.append(f"since {since_year}")
    elif bare_year:
        results = [p for p in results if _relevant_date(p) and _relevant_date(p).startswith(str(bare_year))]
        interpretation_parts.append(f"in {bare_year}")

    # Fallback: no structured filters recognized at all -> plain keyword search
    if not section_filter and not status_filter and not years_window and not since_year and not bare_year:
        stopwords = {
            "how", "many", "what", "were", "was", "the", "last", "in", "to", "of", "a", "an",
            "have", "been", "has", "for", "on", "are", "changes", "change", "made", "did",
            "and", "or", "that", "this", "code", "with", "since", "years", "year", "show", "me",
        }
        keywords = [w for w in re.findall(r"[a-z0-9]+", text) if w not in stopwords and len(w) > 2]
        if keywords:
            def matches(p):
                haystack = " ".join([
                    p.get("title", ""), p.get("summary", ""), p.get("chapter", ""),
                    p.get("submitted_by", ""),
                ]).lower()
                return any(kw in haystack for kw in keywords)
            results = [p for p in results if matches(p)]
            interpretation_parts.append(f"matching \u201c{' '.join(keywords)}\u201d")

    results.sort(key=lambda p: _relevant_date(p) or "", reverse=True)
    total_count = len(results)

    if limit:
        results = results[:limit]

    filters_desc = " ".join(interpretation_parts) if interpretation_parts else "in the repository"

    if is_count_question:
        interpretation = f"Found {total_count} proposal(s) {filters_desc}."
    elif limit:
        interpretation = f"Showing the {min(limit, total_count)} most recent of {total_count} proposal(s) {filters_desc}."
    else:
        interpretation = f"Found {total_count} proposal(s) {filters_desc}."

    return {
        "interpretation": interpretation,
        "count": total_count,
        "results": [
            {
                "id": p["id"],
                "title": p["title"],
                "status": p["status"],
                "code_section": p.get("code_section"),
                "chapter": p.get("chapter"),
                "date_submitted": p.get("date_submitted"),
                "date_decided": p.get("date_decided"),
                "url": f"/proposal/{p['id']}",
            }
            for p in results
        ],
    }
