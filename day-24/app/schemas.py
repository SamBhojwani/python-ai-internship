from pydantic import BaseModel, field_validator
from typing import List, Optional


class SearchRequest(BaseModel):
    query: str
    top: Optional[int] = 1
    min_score: Optional[float] = 0.0

    @field_validator("query")
    @classmethod
    def query_must_not_be_empty(cls, value):
        if not value or not value.strip():
            raise ValueError("Query cannot be empty")
        return value

    @field_validator("top")
    @classmethod
    def top_must_be_positive(cls, value):
        if value is not None and value < 1:
            raise ValueError("top must be at least 1")
        return value


class SearchResult(BaseModel):
    document: str
    score: float
    metadata: dict


class SearchResponse(BaseModel):
    query: str
    results: List[SearchResult]