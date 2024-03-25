# Pydantic은 FastAPI의 입출력 스펙을 정의하고 그 값을 검증하기 위해 사용하는 라이브러리

import datetime

from pydantic import BaseModel, field_validator

from domain.answer.answer_schema import Answer

# Question 스키마
class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answers: list[Answer] = []

    class Config:
        from_attributes = True

class QuestionList(BaseModel):
    total: int = 0
    question_list: list[Question] =[]

class QuestionCreate(BaseModel):
    subject: str
    content: str

    @field_validator('subject','content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v