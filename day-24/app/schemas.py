from pydantic import BaseModel, field_validator
from typing import List


class SearchRequest(BaseModel):
    query: str

    @field_validator("query")
    @classmethod
    def query_must_not_be_empty(cls, value):
        if not value or not value.strip():
            raise ValueError("Query cannot be empty")
        return value


class SearchResult(BaseModel):
    document: str
    score: float


class SearchResponse(BaseModel):
    query: str
    results: List[SearchResult]