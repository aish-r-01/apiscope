from fastapi import FastAPI
from app.middleware.traffic_capture import TrafficCaptureMiddleware
from app.storage.redis_client import redis_client

app = FastAPI(title="APIScope")
app.add_middleware(TrafficCaptureMiddleware)

@app.get("/")
def root():
    return {"message": "APIScope API running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/debug/features/{api_key}")
def debug_features(api_key: str):
    base = f"api:{api_key}"
    return {
        "requests_per_min": redis_client.get(f"{base}:count"),
        "unique_endpoints": redis_client.scard(f"{base}:endpoints"),
        "unique_ips": redis_client.scard(f"{base}:ips"),
    }
