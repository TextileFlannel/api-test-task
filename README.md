# Тестовое задание API

Backend-приложение на FastAPI для управления вопросами и ответами с базой данных PostgreSQL.

## Запуск с Docker

1. Соберите и запустите контейнеры:

```bash
docker-compose up --build
```

2. Приложение FastAPI будет доступно по адресу `http://localhost:8000`.

3. PostgreSQL база данных будет доступна на порту 5432.

## Endpoints API

### Вопросы

- `GET /questions/` — получить список всех вопросов.
- `POST /questions/` — создать новый вопрос.
- `GET /questions/{question_id}` — получить вопрос по ID с ответами.
- `DELETE /questions/{question_id}` — удалить вопрос вместе с ответами.

### Ответы

- `POST /questions/{question_id}/answers/` — добавить ответ к вопросу.
- `GET /answers/{answer_id}` — получить ответ по ID.
- `DELETE /answers/{answer_id}` — удалить ответ.

## Запуск миграций

Для применения миграций базы данных используется Alembic.

1. Установить Alembic:

```bash
pip install alembic
```

2. Установите переменную окружения `DATABASE_URL` с параметрами подключения к базе данных PostgreSQL. Пример для Linux/Mac:

```bash
export DATABASE_URL="postgresql://user:password@host:port/database"
```

Для Windows PowerShell:

```powershell
$env:DATABASE_URL="postgresql://user:password@host:port/database"
```

3. Запустите миграции командой:

```bash
alembic upgrade head
```

Эта команда применит все доступные миграции к базе данных.

Для создания новых миграций используйте:

```bash
alembic revision --autogenerate -m "описание изменений"
```

## Запуск тестов

Для запуска тестов используется `pytest`.

1. Установить Pytest:

```bash
pip install pytest
```

2. Запустите тесты командой:

```bash
pytest
```

Тесты находятся в папке `tests` и покрывают основные сценарии работы API.
