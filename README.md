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
