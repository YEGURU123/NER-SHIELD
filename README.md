# NER SHIELD

This package keeps the supplied NER SHIELD webpage as the base and adds a separate backend-connected AI Prediction System.

## Included
- Original NER SHIELD interface and existing features retained from the supplied HTML
- Login/register/guest UI
- Dashboard, alerts and awareness videos
- Map/location functionality already present in the supplied page
- SOS interface and browser audio behavior already present in the supplied page
- Profile and settings
- Separate AI Prediction System connected to Python
- Google integration support via the existing map-oriented webpage and optional Google Maps API key configuration

## Run in VS Code (Windows)
Open the `NER_SHIELD` folder, then:

    python -m venv .venv
    .\.venv\Scripts\python.exe -m pip install -r requirements.txt
    .\.venv\Scripts\python.exe run.py

Open:

    http://127.0.0.1:8000

## Google connection
If you want to use a Google Maps JavaScript API key, copy `.env.example` to `.env`, add your own key, and configure the map script in the frontend. API keys are not included in this ZIP.
