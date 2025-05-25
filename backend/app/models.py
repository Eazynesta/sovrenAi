# backend/app/models.py
from pydantic import BaseModel

class Question(BaseModel):
    question: str
