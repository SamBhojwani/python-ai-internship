from fastapi import APIRouter, HTTPException, Query, Depends
from typing import Optional
from sqlalchemy.orm import Session
from app.schemas import (
    AskRequest, AskResponse, SearchRequest, SearchResponse,
    CategoriesResponse, DocumentsResponse, HistoryResponse,
    FeedbackRequest, FeedbackResponse, AnalyticsResponse
)
from app.services.assistant_service import (
    ask_assistant, search_documents, list_categories, list_documents,
    get_user_history, submit_feedback, get_analytics
)
from app.dependencies import get_current_user
from app.database import get_db
from app.models import User

router = APIRouter(prefix="/assistant", tags=["Assistant"])


@router.post("/ask", response_model=AskResponse)
def ask(
    request: AskRequest,
    category: Optional[str] = Query(default=None),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        result = ask_assistant(request.question, top_n=3, category=category, db=db, user_id=current_user.id, username=current_user.username)
        return AskResponse(answer=result["answer"], sources=result["sources"])
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))


@router.post("/search", response_model=SearchResponse)
def search(request: SearchRequest, category: Optional[str] = Query(default=None), current_user: User = Depends(get_current_user)):
    try:
        results = search_documents(request.query, top_n=5, category=category)
        return SearchResponse(query=request.query, results=results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {e}")


@router.get("/categories", response_model=CategoriesResponse)
def categories():
    return CategoriesResponse(categories=list_categories())


@router.get("/documents", response_model=DocumentsResponse)
def documents():
    docs = list_documents()
    return DocumentsResponse(documents=docs, total=len(docs))


@router.get("/history", response_model=HistoryResponse)
def history(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    conversations = get_user_history(db, current_user.id)
    return HistoryResponse(history=conversations)


@router.post("/feedback", response_model=FeedbackResponse)
def feedback(request: FeedbackRequest, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        feedback_id = submit_feedback(
            db, current_user.id, request.question_id, request.rating, request.comment
        )
        return FeedbackResponse(success=True, feedback_id=feedback_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    

@router.get("/analytics", response_model=AnalyticsResponse)
def analytics(db: Session = Depends(get_db)):
    result = get_analytics(db)
    return AnalyticsResponse(**result)