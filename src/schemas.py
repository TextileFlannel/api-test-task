from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, constr, ConfigDict


class AnswerBase(BaseModel):
    user_id: str
    text: constr(min_length=1)


class AnswerCreate(AnswerBase):
    pass


class Answer(BaseModel):
    id: int
    question_id: int
    user_id: str
    text: constr(min_length=1)
    created_at: datetime

    class Config:
        model_config = ConfigDict(from_attributes=True)


class QuestionBase(BaseModel):
    text: constr(min_length=1)


class QuestionCreate(QuestionBase):
    pass


class Question(BaseModel):
    id: int
    text: constr(min_length=1)
    created_at: datetime
    answers: Optional[List[Answer]] = []

