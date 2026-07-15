from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routes import ai

app = FastAPI(title="AI-Powered API", version="1.0.0")

app.include_router(ai.router)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"success": False, "detail": "An unexpected server error occurred."}
    )


@app.get("/")
def root():
    return {"message": "AI-Powered API is running"}