import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import Base
from src import models, schemas, crud

# In-memory SQLite для тестов
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)

# --- Тесты ---

def test_create_question(db):
    question_data = schemas.QuestionCreate(text="What is FastAPI?")
    question = crud.create_question(db, question_data)
    assert question.text == "What is FastAPI?"
    assert question.id is not None

def test_get_question(db):
    question_data = schemas.QuestionCreate(text="What is SQLAlchemy?")
    created = crud.create_question(db, question_data)
    fetched = crud.get_question(db, created.id)
    assert fetched.id == created.id
    assert fetched.text == "What is SQLAlchemy?"

def test_get_all_questions(db):
    crud.create_question(db, schemas.QuestionCreate(text="Q1"))
    crud.create_question(db, schemas.QuestionCreate(text="Q2"))
    questions = crud.get_all_questions(db)
    assert len(questions) == 2

def test_delete_question(db):
    question = crud.create_question(db, schemas.QuestionCreate(text="To be deleted"))
    deleted = crud.delete_question(db, question.id)
    assert deleted.id == question.id
    assert crud.get_question(db, question.id) is None

def test_create_answer(db):
    question = crud.create_question(db, schemas.QuestionCreate(text="Q?"))
    answer_data = schemas.AnswerCreate(user_id="user123", text="A!")
    answer = crud.create_answer(db, question.id, answer_data)
    assert answer.text == "A!"
    assert answer.question_id == question.id

def test_get_answer(db):
    question = crud.create_question(db, schemas.QuestionCreate(text="Q?"))
    answer_data = schemas.AnswerCreate(user_id="user123", text="A!")
    created = crud.create_answer(db, question.id, answer_data)
    fetched = crud.get_answer(db, created.id)
    assert fetched.id == created.id
    assert fetched.text == "A!"

def test_delete_answer(db):
    question = crud.create_question(db, schemas.QuestionCreate(text="Q?"))
    answer_data = schemas.AnswerCreate(user_id="user123", text="A!")
    answer = crud.create_answer(db, question.id, answer_data)
    deleted = crud.delete_answer(db, answer.id)
    assert deleted.id == answer.id
    assert crud.get_answer(db, answer.id) is None