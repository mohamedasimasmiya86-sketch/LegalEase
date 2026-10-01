from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="LegalEase",
    description="AI-Powered Legal Document Generator",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "LegalEase API is running",
        "status": "success"
    }