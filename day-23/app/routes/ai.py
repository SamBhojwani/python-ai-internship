from fastapi import APIRouter, HTTPException
from app.schemas import GenerateRequest, GenerateResponse, UtilityRequest, UtilityResponse
from app.services.ai_service import generate_text, run_prompt_template

router = APIRouter(prefix="/ai", tags=["AI"])


@router.post("/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest):
    try:
        result = generate_text(request.prompt)
        return GenerateResponse(success=True, response=result)
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))


@router.post("/summarize", response_model=UtilityResponse)
def summarize(request: UtilityRequest):
    try:
        result = run_prompt_template("summarize.txt", request.text)
        return UtilityResponse(success=True, response=result)
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))


@router.post("/translate", response_model=UtilityResponse)
def translate(request: UtilityRequest):
    try:
        result = run_prompt_template("translate.txt", request.text)
        return UtilityResponse(success=True, response=result)
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))


@router.post("/email", response_model=UtilityResponse)
def email(request: UtilityRequest):
    try:
        result = run_prompt_template("email.txt", request.text)
        return UtilityResponse(success=True, response=result)
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))


@router.post("/explain-code", response_model=UtilityResponse)
def explain_code(request: UtilityRequest):
    try:
        result = run_prompt_template("explain_code.txt", request.text)
        return UtilityResponse(success=True, response=result)
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))