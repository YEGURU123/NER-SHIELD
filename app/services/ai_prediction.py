from app.services.data_fusion import fuse

def predict(raw):
    f = fuse(raw)
    score = (
        0.35*f["rainfall"] + 0.25*f["soil"] + 0.20*f["slope"]
        + 0.12*f["history"] + 0.08*(1-f["road"])
    )
    score = max(0.0, min(1.0, score))
    if score < 0.34: level = "LOW"
    elif score < 0.67: level = "MODERATE"
    elif score < 0.85: level = "HIGH"
    else: level = "CRITICAL"
    confidence = round(75 + abs(score-0.5)*30, 1)
    return {
        "risk_level": level,
        "risk_probability": round(score, 4),
        "risk_percent": round(score*100, 1),
        "confidence": min(99.0, confidence),
        "features": f,
        "summary": f"Conditions indicate {level.lower()} landslide risk."
    }
