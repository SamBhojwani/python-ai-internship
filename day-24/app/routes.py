from fastapi import APIRouter, HTTPException
from app.schemas import SearchRequest, SearchResponse
from app.search_service import perform_search

router = APIRouter()


@router.post("/search", response_model=SearchResponse)
def search(request: SearchRequest):
    try:
        results = perform_search(request.query, top=request.top, min_score=request.min_score)
        return SearchResponse(query=request.query, results=results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {e}")