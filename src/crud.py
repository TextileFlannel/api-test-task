from sqlalchemy.orm import Session
from sqlalchemy.future import select
from src import models, schemas


def get_all_questions(db: Session):
    result = db.execute(select(models.Question))
    return result.scalars().all()


def create_question(db: Session, question: schemas.QuestionCreate):
    db_question = models.Question(text=question.text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


def get_question(db: Session, question_id: int):
    result = db.execute(
        select(models.Question).where(models.Question.id == question_id)
    )
    return result.scalars().first()


def delete_question(db: Session, question_id: int):
    question = get_question(db, question_id)
    if question is None:
        return None
    db.delete(question)
    db.commit()
    return question


def create_answer(db: Session, question_id: int, answer: schemas.AnswerCreate):
    db_answer = models.Answer(
        question_id=question_id,
        user_id=answer.user_id,
        text=answer.text
    )
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer


def get_answer(db: Session, answer_id: int):
    result = db.execute(
        select(models.Answer).where(models.Answer.id == answer_id)
    )
    return result.scalars().first()


def delete_answer(db: Session, answer_id: int):
    answer = get_answer(db, answer_id)
    if answer is None:
        return None
    db.delete(answer)
    db.commit()
    return answer
