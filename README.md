
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
![Screenshot 2024-12-26 at 08.07.48.png](..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fkk%2F2t7q31r53hz60_94_r8w7sh00000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_SFrNGS%2FScreenshot%202024-12-26%20at%2008.07.48.png)
Работа сокращения ссылки:
![Screenshot 2024-12-26 at 08.07.09.png](..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fkk%2F2t7q31r53hz60_94_r8w7sh00000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_GyKyJZ%2FScreenshot%202024-12-26%20at%2008.07.09.png)
Получение полной ссылки по сокращенной:
![Screenshot 2024-12-26 at 08.07.31.png](..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fkk%2F2t7q31r53hz60_94_r8w7sh00000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_nGC9oS%2FScreenshot%202024-12-26%20at%2008.07.31.png)
Вводим значение сокращенной ссылки для редиректа:
![Screenshot 2024-12-26 at 08.08.07.png](..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fkk%2F2t7q31r53hz60_94_r8w7sh00000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_rp2MUO%2FScreenshot%202024-12-26%20at%2008.08.07.png)
Пересылаемся на полную ссылку:
![Screenshot 2024-12-26 at 08.08.16.png](..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fkk%2F2t7q31r53hz60_94_r8w7sh00000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_mZYJ2D%2FScreenshot%202024-12-26%20at%2008.08.16.png)

### Примеры todo
Все эндпоинты:
![Screenshot 2024-12-26 at 08.10.14.png](..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fkk%2F2t7q31r53hz60_94_r8w7sh00000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_1JSUE6%2FScreenshot%202024-12-26%20at%2008.10.14.png)
Добавляем задачу 1:
![Screenshot 2024-12-26 at 08.11.09.png](..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fkk%2F2t7q31r53hz60_94_r8w7sh00000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_NYgldd%2FScreenshot%202024-12-26%20at%2008.11.09.png)
Добавляем задачу 2:
![Screenshot 2024-12-26 at 08.12.07.png](..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fkk%2F2t7q31r53hz60_94_r8w7sh00000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_BqNzxo%2FScreenshot%202024-12-26%20at%2008.12.07.png)
Смотрим свои планы на ближайшее будущее:
![Screenshot 2024-12-26 at 08.12.44.png](..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fkk%2F2t7q31r53hz60_94_r8w7sh00000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_TFVNaX%2FScreenshot%202024-12-26%20at%2008.12.44.png)
Понимаем что какие-то цели надо скорректировать:
![Screenshot 2024-12-26 at 08.13.59.png](..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fkk%2F2t7q31r53hz60_94_r8w7sh00000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_vUgNMw%2FScreenshot%202024-12-26%20at%2008.13.59.png)
А какие-то удаляем тк они несбыточны:
![Screenshot 2024-12-26 at 08.14.38.png](..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fkk%2F2t7q31r53hz60_94_r8w7sh00000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_okURX4%2FScreenshot%202024-12-26%20at%2008.14.38.png)