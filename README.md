
# Проект микросервисов на FastAPI

## Обзор
Данный проект содержит два микросервиса на базе FastAPI:
1. **TODO-сервис**: Реализует CRUD-операции для управления задачами.
2. **Сервис сокращения URL**: Позволяет создавать короткие ссылки для URL.

### Docker образы:

- [litwein/shorturl_service](https://hub.docker.com/r/litwein/shorturl_service)
- [litwein/todo_service](https://hub.docker.com/r/litwein/todo_service)

Оба сервиса используют SQLite для хранения данных и упакованы в Docker-контейнеры. Проект поддерживает локальное развертывание, а также развертывание через Docker.

## Быстрый старт
### Локальное развертывание
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/NickLitwinow/MS_Final_Microservices
   cd MS_Final_Microservices
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

### Развертывание через Docker Compose
Из корневой папки:
   ```bash
   docker-compose up -d --build
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

### Примеры shorturl
Все эндпоинты:
<img width="1416" alt="Screenshot 2024-12-26 at 08 24 17" src="https://github.com/user-attachments/assets/bf7286b7-f777-4b02-a2f8-2d4369fa26b3" />

Работа сокращения ссылки:
<img width="1366" alt="Screenshot 2024-12-26 at 08 24 03" src="https://github.com/user-attachments/assets/bef8eb86-6653-4334-820c-7228e90ac9f5" />

Получение полной ссылки по сокращенной:
<img width="1373" alt="Screenshot 2024-12-26 at 08 24 41" src="https://github.com/user-attachments/assets/ab114cd6-569a-4db6-aaa3-04dfac7782ec" />

Вводим значение сокращенной ссылки для редиректа:
<img width="337" alt="Screenshot 2024-12-26 at 08 25 03" src="https://github.com/user-attachments/assets/a174e189-ed00-4c04-9a80-cc799881f698" />

Пересылаемся на полную ссылку:
<img width="1440" alt="Screenshot 2024-12-26 at 08 25 17" src="https://github.com/user-attachments/assets/ce1b68d3-15b1-4812-b54c-702bc733bdf9" />


### Примеры todo
Все эндпоинты:
<img width="1413" alt="Screenshot 2024-12-26 at 08 20 58" src="https://github.com/user-attachments/assets/7b7c7a65-b6b0-4156-bbb3-eede5b82672d" />

Добавляем задачу 1:
<img width="1358" alt="Screenshot 2024-12-26 at 08 21 39" src="https://github.com/user-attachments/assets/70d31b29-ad07-4e6f-942e-dee82fe9ab04" />

Добавляем задачу 2:
<img width="1373" alt="Screenshot 2024-12-26 at 08 22 13" src="https://github.com/user-attachments/assets/10ca2f77-b9d4-4006-adb9-fdcf8c7acdee" />

Смотрим свои планы на ближайшее будущее:
<img width="1370" alt="Screenshot 2024-12-26 at 08 22 28" src="https://github.com/user-attachments/assets/8f007966-f756-427a-97cc-5fad4b2b6436" />

Понимаем что какие-то цели надо скорректировать:
<img width="1370" alt="Screenshot 2024-12-26 at 08 23 13" src="https://github.com/user-attachments/assets/7ebd95d7-eb20-426d-a21f-3c8ebdb38905" />

А какие-то удаляем тк они несбыточны:
<img width="1367" alt="Screenshot 2024-12-26 at 08 23 34" src="https://github.com/user-attachments/assets/f418876a-af5b-4fec-83e4-98887ecb5ecb" />
