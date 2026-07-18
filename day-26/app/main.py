from fastapi import FastAPI
from app.routes import rag

app = FastAPI(title="RAG Assistant API", version="1.0.0")

app.include_router(rag.router)


@app.get("/")
def root():
    return {"message": "RAG Assistant API is running"}