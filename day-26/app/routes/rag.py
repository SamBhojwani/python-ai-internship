from fastapi import APIRouter, HTTPException
from app.schemas import AskRequest, AskResponse, ChatRequest, ChatResponse, HistoryResponse
from app.services.rag_service import answer_question, chat_with_context, get_history

router = APIRouter(prefix="/ai", tags=["RAG"])


@router.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):
    try:
        result = answer_question(request.question, top_n=3)
        return AskResponse(
            question=request.question,
            answer=result["answer"],
            documents_used=result["documents_used"],
            sources=result["sources"],
            retrieved_count=result["retrieved_count"]
        )
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        result = chat_with_context(request.session_id, request.message, top_n=3)
        return ChatResponse(
            session_id=request.session_id,
            answer=result["answer"],
            documents_used=result["documents_used"],
            sources=result["sources"],
            retrieved_count=result["retrieved_count"]
        )
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))
    

@router.get("/history", response_model=HistoryResponse)
def history(session_id: str):
    turns = get_history(session_id)
    return HistoryResponse(session_id=session_id, history=turns)