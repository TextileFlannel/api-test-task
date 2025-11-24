from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List

from src import schemas
from src.database import get_db
from src import crud

router = APIRouter()


@router.get("/questions/", response_model=List[schemas.Question])
def read_questions(db: Session = Depends(get_db)):
    questions = crud.get_all_questions(db)
    return questions


@router.post("/questions/", response_model=schemas.Question, status_code=status.HTTP_201_CREATED)
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    db_question = crud.create_question(db, question)
    return db_question


@router.get("/questions/{question_id}", response_model=schemas.Question)
def read_question(question_id: int, db: Session = Depends(get_db)):
    question = crud.get_question(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question


@router.delete("/questions/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_question(question_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_question(db, question_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Question not found")
    return


@router.post("/questions/{question_id}/answers/", response_model=schemas.Answer, status_code=status.HTTP_201_CREATED)
def create_answer(question_id: int, answer: schemas.AnswerCreate, db: Session = Depends(get_db)):
    question = crud.get_question(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    db_answer = crud.create_answer(db, question_id, answer)
    return db_answer


@router.get("/answers/{answer_id}", response_model=schemas.Answer)
def read_answer(answer_id: int, db: Session = Depends(get_db)):
    answer = crud.get_answer(db, answer_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    return answer


@router.delete("/answers/{answer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_answer(answer_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_answer(db, answer_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Answer not found")
    return
