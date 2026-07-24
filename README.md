# NMS Code Provenance Tracker (Proof of Concept)

A demo platform for the **National Masonry Society** showing how AI-assisted
tracking could tie every clause of the masonry code back to the proposal that
created it — including full committee correspondence, votes, and a searchable
archive of **declined** proposals so past reasoning isn't lost if a topic
comes back up in a future code cycle.

> **All content is mock data.** The code text, proposal numbers, names, dates,
> and correspondence in this repo are fictional and built only to demonstrate
> the concept.

## What it does

- **Code Viewer** (`/`) — renders mock sections of a fictional "NMS-500"
  masonry standard.
  - Passages **highlighted light green** are tied to an **accepted** proposal.
    Click one to jump to that proposal's full record: date, submitter,
    committee, vote, reasoning, and the complete correspondence thread.
  - Passages **highlighted light yellow** are tied to a proposal that is
    **still under review**. Clicking shows its current stage and
    correspondence so far.
- **Proposal Repository** (`/repository`) — every proposal ever filed,
  filterable by status (accepted / under review / declined) and searchable
  by keyword.
- **Declined Archive** (`/repository?status=declined`) — proposals that were
  rejected, each with the committee's stated reason and a "if revisited"
  note, so the next person who raises the same idea doesn't start from zero.
- **Submit New Proposal** (bottom-left panel on the code viewer) — a public
  intake form (title, target code section, submitter, summary, current/
  proposed text, optional file attachment) that creates a new `under_review`
  proposal immediately. It shows up right away in the repository and as a
  yellow "pending" chip beneath its target section on the code page.
- **Ask the code** (bottom-left panel on the code viewer) — a natural-
  language-ish query box, e.g. *"how many changes have been submitted to
  section 3 in the last 5 years"* or *"what were the last three changes made
  to the code"*. Runs entirely offline against the in-memory proposal data
  via a small rule-based parser (`data/query_engine.py`) — no external API
  or key required.

## Project structure

```
app.py                  Flask app + routes
data/mock_data.py        All mock code text + proposal records (edit here to add content)
templates/                Jinja2 HTML templates
static/css/style.css      Styling
static/js/script.js       Small anchor-jump / highlight behavior
render.yaml                Render.com deploy blueprint
requirements.txt           Python dependencies
```

## Run locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open http://localhost:5000

## Deploy to Render

1. Push this folder to a GitHub repository.
2. In Render, choose **New > Blueprint** and point it at the repo —
   `render.yaml` will configure the web service automatically
   (build: `pip install -r requirements.txt`, start: `gunicorn app:app`).
3. Alternatively, choose **New > Web Service**, select the repo, and set:
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`

No environment variables or database are required — everything is served
from `data/mock_data.py` in-memory.

## Extending the concept

- `data/mock_data.py` is intentionally a single, readable file. Each code
  section's body uses inline tokens to mark up highlighted clauses:
  - `[[ACC:P-XXXX-XXX]] ... [[/ACC]]` — light-green, links to an accepted proposal
  - `[[REV:P-XXXX-XXX]] ... [[/REV]]` — light-yellow, links to an under-review proposal
  - Add a matching entry to the `PROPOSALS` dict with a `status` of
    `accepted`, `under_review`, or `declined` and it will automatically
    appear in the repository, search, and (if referenced) the code viewer.
- A real implementation would likely replace `mock_data.py` with a database
  (e.g. Postgres) and an ingestion pipeline that lets committee staff attach
  new correspondence and code diffs as votes happen.
