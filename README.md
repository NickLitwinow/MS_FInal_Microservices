
# Проект микросервисов на FastAPI

## Обзор
Данный проект содержит два микросервиса на базе FastAPI:
1. **TODO-сервис**: Реализует CRUD-операции для управления задачами.
2. **Сервис сокращения URL**: Позволяет создавать короткие ссылки для URL.

Оба сервиса используют SQLite для хранения данных и упакованы в Docker-контейнеры. Проект поддерживает локальное развертывание, а также развертывание через Docker.

## Требования
- Python 3.8 или выше
- Docker и Docker Compose
- Git

## Быстрый старт
### Локальное развертывание
1. Клонируйте репозиторий:
   ```bash
   git clone <ссылка_на_репозиторий>
   cd <название_репозитория>
   ```
2. Перейдите в папку с нужным сервисом (`todo/` или `shorturl/`) и установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Запустите сервис:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

### Развертывание через Docker
1. Соберите образы для сервисов:
   ```bash
   docker build -t todo-service:latest ./todo
   docker build -t shorturl-service:latest ./shorturl
   ```
2. Запустите контейнеры:
   ```bash
   docker run -d -p 8000:80 -v todo_data:/app/data todo-service:latest
   docker run -d -p 8001:80 -v shorturl_data:/app/data shorturl-service:latest
   ```

## Использование
### TODO-сервис
- **POST /items**: Создание задачи.
- **GET /items**: Получение списка задач.
- **GET /items/{item_id}**: Получение задачи по ID.
- **PUT /items/{item_id}**: Обновление задачи по ID.
- **DELETE /items/{item_id}**: Удаление задачи.

### Сервис сокращения URL
- **POST /shorten**: Создание короткой ссылки.
- **GET /{short_id}**: Перенаправление на полный URL.
- **GET /stats/{short_id}**: Получение информации о короткой ссылке.
