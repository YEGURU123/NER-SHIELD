def clamp(x, lo, hi):
    return max(lo, min(hi, float(x)))

def normalize(x, lo, hi):
    return (clamp(x, lo, hi) - lo) / (hi - lo) if hi != lo else 0.0

def fuse(raw):
    return {
        "rainfall": normalize(raw.get("rainfall_mm", 0), 0, 200),
        "soil": normalize(raw.get("soil_moisture", 0), 0, 100),
        "slope": normalize(raw.get("slope_degree", 0), 0, 60),
        "road": normalize(raw.get("road_condition", 0.7), 0, 1),
        "history": normalize(raw.get("historical_disruptions", 0), 0, 10),
    }
