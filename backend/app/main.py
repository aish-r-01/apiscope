from fastapi import FastAPI

app = FastAPI(title="APIScope")

@app.get("/")
def root():
    return {"message": "APIScope API running"}

@app.get("/health")
def health():
    return {"status": "ok"}
