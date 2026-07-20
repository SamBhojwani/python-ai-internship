from fastapi import FastAPI
from app.routes import assistant

app = FastAPI(title="Enterprise AI Knowledge Assistant", version="1.0.0")

app.include_router(assistant.router)


@app.get("/")
def root():
    return {"message": "Enterprise AI Knowledge Assistant is running"}