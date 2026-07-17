from pydantic import BaseModel, field_validator
from typing import List


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
    question: str
    answer: str
    documents_used: List[str]
    sources: List[Source]
    retrieved_count: int