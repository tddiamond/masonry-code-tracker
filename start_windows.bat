@echo off
cd /d "%~dp0"
echo Setting up the app the first time this may take a minute...
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
start "" http://localhost:5050
python app.py
pause
