from fastapi import FastAPI
from app.routes import ai

app = FastAPI(title="AI-Powered API", version="1.0.0")

app.include_router(ai.router)


@app.get("/")
def root():
    return {"message": "AI-Powered API is running"}