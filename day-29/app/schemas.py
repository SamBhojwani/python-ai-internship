from pydantic import BaseModel, field_validator
from typing import List, Optional
from datetime import datetime


class AskRequest(BaseModel):
    question: str

    @field_validator("question")
    @classmethod
    def question_must_not_be_empty(cls, value):
        if not value or not value.strip():
            raise ValueError("Question cannot be empty")
        return value


class Source(BaseModel):
    document: str
    score: float


class AskResponse(BaseModel):
    answer: str
    sources: List[Source]


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
    category: str
    score: float


class SearchResponse(BaseModel):
    query: str
    results: List[SearchResult]


class CategoriesResponse(BaseModel):
    categories: List[str]


class DocumentInfo(BaseModel):
    id: str
    filename: str
    category: str


class DocumentsResponse(BaseModel):
    documents: List[DocumentInfo]
    total: int


class UserRegister(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class ConversationEntry(BaseModel):
    id: int
    question: str
    answer: str
    timestamp: datetime

    class Config:
        from_attributes = True


class HistoryResponse(BaseModel):
    history: List[ConversationEntry]


class FeedbackRequest(BaseModel):
    question_id: int
    rating: int
    comment: Optional[str] = None

    @field_validator("rating")
    @classmethod
    def rating_must_be_valid(cls, value):
        if value < 1 or value > 5:
            raise ValueError("Rating must be between 1 and 5")
        return value


class FeedbackResponse(BaseModel):
    success: bool
    feedback_id: int


class AnalyticsResponse(BaseModel):
    total_requests: int
    average_response_time_ms: float
    top_category: Optional[str]
    average_rating: Optional[float]