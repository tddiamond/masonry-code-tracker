import os
import re

from flask import (
    Flask, render_template, abort, request, redirect, url_for, flash, jsonify,
)
from werkzeug.utils import secure_filename

from data.mock_data import (
    CODE_CHAPTERS, PROPOSALS, get_all_proposals_by_status, get_proposal,
    add_submitted_proposal,
)
from data.query_engine import run_query

app = Flask(__name__)
app.secret_key = "nms-demo-secret-key-not-for-production"

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "data", "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)
ALLOWED_EXTENSIONS = {"pdf", "doc", "docx", "png", "jpg", "jpeg", "txt", "xlsx", "csv"}

TOKEN_RE = re.compile(r"\[\[(ACC|REV):([A-Z0-9\-]+)\]\](.*?)\[\[/\1\]\]", re.DOTALL)
TOKEN_ID_RE = re.compile(r"\[\[(?:ACC|REV):([A-Z0-9\-]+)\]\]")


def render_body(body_text):
    """Convert [[ACC:ID]]...[[/ACC]] / [[REV:ID]]...[[/REV]] tokens into
    clickable highlighted <span> markup."""

    def _sub(match):
        kind, pid, inner = match.group(1), match.group(2), match.group(3)
        css_class = "hl-accepted" if kind == "ACC" else "hl-review"
        label = "Accepted change" if kind == "ACC" else "Under review"
        proposal = PROPOSALS.get(pid, {})
        title = proposal.get("title", "")
        return (
            f'<a href="/proposal/{pid}" class="hl {css_class}" '
            f'data-proposal="{pid}" title="{label}: {title}">{inner}'
            f'<sup class="hl-tag">{pid}</sup></a>'
        )

    return TOKEN_RE.sub(_sub, body_text)


def _allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.context_processor
def inject_counts():
    return {
        "count_accepted": len(get_all_proposals_by_status("accepted")),
        "count_review": len(get_all_proposals_by_status("under_review")),
        "count_declined": len(get_all_proposals_by_status("declined")),
    }


@app.route("/")
def index():
    chapters = []
    all_sections = []

    for ch in CODE_CHAPTERS:
        sections = []
        ch_has_acc = False
        ch_has_rev = False

        for sec in ch["sections"]:
            has_acc = bool(re.search(r"\[\[ACC:", sec["body"]))
            has_rev = bool(re.search(r"\[\[REV:", sec["body"]))
            referenced_ids = set(TOKEN_ID_RE.findall(sec["body"]))

            # Proposals targeting this section that aren't already inline in
            # the body text (e.g. newly user-submitted ones) surface as
            # pending chips beneath the section instead.
            extra_proposals = [
                p for p in PROPOSALS.values()
                if p.get("code_section") == sec["id"]
                and p["id"] not in referenced_ids
                and p["status"] in ("accepted", "under_review")
            ]
            extra_proposals.sort(key=lambda p: p.get("date_submitted", ""), reverse=True)

            if any(p["status"] == "accepted" for p in extra_proposals):
                has_acc = True
            if any(p["status"] == "under_review" for p in extra_proposals):
                has_rev = True

            ch_has_acc = ch_has_acc or has_acc
            ch_has_rev = ch_has_rev or has_rev

            sections.append({
                **sec,
                "html": render_body(sec["body"]),
                "has_acc": has_acc,
                "has_rev": has_rev,
                "extra_proposals": extra_proposals,
            })
            all_sections.append({
                "id": sec["id"],
                "label": f'{sec["heading"]} ({ch["number"]})',
            })

        chapters.append({**ch, "sections": sections, "has_acc": ch_has_acc, "has_rev": ch_has_rev})

    return render_template("index.html", chapters=chapters, all_sections=all_sections)


@app.route("/submit-proposal", methods=["POST"])
def submit_proposal():
    title = request.form.get("title", "").strip()
    code_section = request.form.get("code_section", "").strip()
    custom_section = request.form.get("custom_section", "").strip()
    if code_section == "__other__":
        code_section = custom_section

    submitted_by = request.form.get("submitted_by", "").strip() or "Anonymous Submitter"
    summary = request.form.get("summary", "").strip()
    old_text = request.form.get("old_text", "").strip()
    proposed_text = request.form.get("proposed_text", "").strip()

    if not title or not code_section or not summary or not proposed_text:
        flash("Please fill in the title, code section, summary, and proposed text before submitting.", "error")
        return redirect(url_for("index") + "#submit-proposal")

    attachment_filename = None
    file = request.files.get("attachment")
    if file and file.filename:
        if not _allowed_file(file.filename):
            flash("Attachment type not supported. Allowed: pdf, doc, docx, png, jpg, txt, xlsx, csv.", "error")
            return redirect(url_for("index") + "#submit-proposal")
        filename = secure_filename(file.filename)
        base, ext = os.path.splitext(filename)
        save_name = filename
        i = 1
        while os.path.exists(os.path.join(UPLOAD_DIR, save_name)):
            save_name = f"{base}_{i}{ext}"
            i += 1
        file.save(os.path.join(UPLOAD_DIR, save_name))
        attachment_filename = save_name

    chapter_label = None
    for ch in CODE_CHAPTERS:
        for sec in ch["sections"]:
            if sec["id"] == code_section:
                chapter_label = f'{ch["number"]} — {ch["title"]}'

    proposal = add_submitted_proposal(
        title=title,
        code_section=code_section,
        chapter_label=chapter_label,
        submitted_by=submitted_by,
        summary=summary,
        old_text=old_text,
        proposed_text=proposed_text,
        attachment_filename=attachment_filename,
    )

    flash(f"Proposal {proposal['id']} submitted and is now under review.", "success")
    return redirect(url_for("proposal_detail", pid=proposal["id"]))


@app.route("/api/query")
def api_query():
    q = request.args.get("q", "")
    return jsonify(run_query(q))


@app.route("/proposal/<pid>")
def proposal_detail(pid):
    proposal = get_proposal(pid)
    if not proposal:
        abort(404)
    return render_template("proposal_detail.html", p=proposal)


@app.route("/repository")
def repository():
    status_filter = request.args.get("status", "all")
    query = request.args.get("q", "").strip().lower()

    all_props = list(PROPOSALS.values())

    if status_filter != "all":
        all_props = [p for p in all_props if p["status"] == status_filter]

    if query:
        def matches(p):
            haystack = " ".join([
                p.get("title", ""), p.get("id", ""), p.get("code_section", ""),
                p.get("chapter", ""), p.get("submitted_by", ""),
                p.get("summary", "")
            ]).lower()
            return query in haystack
        all_props = [p for p in all_props if matches(p)]

    all_props.sort(key=lambda p: p.get("date_submitted", ""), reverse=True)

    return render_template(
        "repository.html",
        proposals=all_props,
        status_filter=status_filter,
        query=request.args.get("q", ""),
    )


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
