from fastapi import APIRouter, HTTPException
from app.schemas import GenerateRequest, GenerateResponse
from app.services.ai_service import generate_text

router = APIRouter(prefix="/ai", tags=["AI"])


@router.post("/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest):
    try:
        result = generate_text(request.prompt)
        return GenerateResponse(success=True, response=result)
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))