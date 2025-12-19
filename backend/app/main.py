from fastapi import FastAPI
from app.middleware.traffic_capture import TrafficCaptureMiddleware

app = FastAPI(title="APIScope")
app.add_middleware(TrafficCaptureMiddleware)

@app.get("/")
def root():
    return {"message": "APIScope API running"}

@app.get("/health")
def health():
    return {"status": "ok"}
