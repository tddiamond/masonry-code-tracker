#!/bin/bash
cd "$(dirname "$0")"
echo "Setting up the app — the first time this may take a minute..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
( sleep 2 && open http://localhost:5050 2>/dev/null || xdg-open http://localhost:5050 2>/dev/null ) &
python app.py
