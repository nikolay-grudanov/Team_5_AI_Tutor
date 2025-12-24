---
source_image: page_096.png
page_number: 96
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.59
tokens: 8279
characters: 1260
timestamp: 2025-12-24T02:18:24.322579
finish_reason: stop
---

3. Давайте реализуем маршруты для создания события, удаления одного события и удаления всех событий, содержащихся в базе данных:

```python
@event_router.post("/new")
async def create_event(body: Event = Body(...)) -> dict:
    events.append(body)
    return {
        "message": "Event created successfully"
    }

@event_router.delete("/{id}")
async def delete_event(id: int) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return { "message": "Event deleted successfully" }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )
@event_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {
        "message": "Events deleted successfully"
    }
```

Мы успешно реализовали маршруты для событий. Маршрут UPDATE будет реализован в главе 6 «Подключение к базе данных», где мы перенесем наше приложение для использования реальной базы данных.

4. Теперь, когда мы реализовали маршруты, давайте обновим нашу конфигурацию маршрута, чтобы включить маршрут события в main.py:

```python
from fastapi import FastAPI
from routes.user import user_router
from routes.events import event_router
```