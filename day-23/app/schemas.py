from pydantic import BaseModel, field_validator


class GenerateRequest(BaseModel):
    prompt: str

    @field_validator("prompt")
    @classmethod
    def prompt_must_not_be_empty(cls, value):
        if not value or not value.strip():
            raise ValueError("Prompt cannot be empty")
        return value


class GenerateResponse(BaseModel):
    success: bool
    response: str

class UtilityRequest(BaseModel):
    text: str

    @field_validator("text")
    @classmethod
    def text_must_not_be_empty(cls, value):
        if not value or not value.strip():
            raise ValueError("Text cannot be empty")
        return value

class UtilityResponse(BaseModel):
    success: bool
    response: str

class ChatRequest(BaseModel):
    session_id: str
    message: str

    @field_validator("message")
    @classmethod
    def message_must_not_be_empty(cls, value):
        if not value or not value.strip():
            raise ValueError("Message cannot be empty")
        return value


class ChatResponse(BaseModel):
    success: bool
    response: str
    session_id: str