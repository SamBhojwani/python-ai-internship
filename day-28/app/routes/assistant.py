from fastapi import APIRouter, HTTPException, Query, Depends
from typing import Optional
from app.schemas import (
    AskRequest, AskResponse, SearchRequest, SearchResponse,
    CategoriesResponse, DocumentsResponse
)
from app.services.assistant_service import (
    ask_assistant, search_documents, list_categories, list_documents
)
from app.dependencies import get_current_user
from app.models import User

router = APIRouter(prefix="/assistant", tags=["Assistant"])


@router.post("/ask", response_model=AskResponse)
def ask(request: AskRequest, category: Optional[str] = Query(default=None), current_user: User = Depends(get_current_user)):
    try:
        result = ask_assistant(request.question, top_n=3, category=category)
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