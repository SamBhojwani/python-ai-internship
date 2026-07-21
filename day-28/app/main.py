from fastapi import FastAPI
from app.routes import assistant, documents, auth_routes
from app.database import engine, Base
from app.models import User

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Enterprise AI Knowledge Assistant", version="2.0.0")

app.include_router(auth_routes.router)
app.include_router(assistant.router)
app.include_router(documents.router)


@app.get("/")
def root():
    return {"message": "Enterprise AI Knowledge Assistant is running"}