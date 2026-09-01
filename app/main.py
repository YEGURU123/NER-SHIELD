from flask import Flask, jsonify, request, send_from_directory
from pathlib import Path
from app.services.ai_prediction import predict

BASE_DIR = Path(__file__).resolve().parent.parent
app = Flask(__name__, static_folder=str(BASE_DIR/"static"))

@app.get("/")
def home():
    return send_from_directory(app.static_folder, "index.html")

@app.get("/api/health")
def health():
    return jsonify({"status":"ok","service":"NER SHIELD"})

@app.post("/api/predict")
def api_predict():
    raw = request.get_json(silent=True) or {}
    try:
        return jsonify(predict(raw))
    except (TypeError, ValueError) as exc:
        return jsonify({"error": str(exc)}), 400
