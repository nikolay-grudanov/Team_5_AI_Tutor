---
source_image: page_113.png
page_number: 113
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.45
tokens: 8283
characters: 1087
timestamp: 2025-12-24T02:18:48.434658
finish_reason: stop
---

status_code=status.HTTP_404_NOT_FOUND,
    detail="Event with supplied ID does not exist"
)

В предыдущем блоке кода мы проверяем наличие события, прежде чем приступить к обновлению данных события. После обновления события возвращаются обновленные данные. Обновим существующий заголовок статьи:

(venv)$ curl -X 'PUT' \
'http://0.0.0.0:8080/event/edit/1' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
    "title": "Packt''s FastAPI book launch II"
}'

{
    "id": 1,
    "title": "Packt's FastAPI book launch II",
    "image": "fastapi-book.jpeg",
    "description": "The launch of the FastAPI book will hold on xyz.",
    "tags": ["python", "fastapi"],
    "location": "virtual" }

Теперь, когда мы добавили функцию обновления, давайте быстро добавим операцию удаления в следующем разделе.

Удаление событий

В events.py, обновите маршрут delete определенный ранее:

@event_router.delete("/delete/{id}")
async def delete_event(id: int, session=Depends(get_session)) -> dict:
    event = session.get(Events, id)
    if event:
        session.delete(event)