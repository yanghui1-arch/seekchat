from pydantic import BaseModel, Field


class Chat(BaseModel):
    content: str = Field(...)