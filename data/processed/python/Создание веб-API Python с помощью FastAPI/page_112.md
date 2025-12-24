---
source_image: page_112.png
page_number: 112
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.81
tokens: 8298
characters: 1360
timestamp: 2025-12-24T02:18:48.599810
finish_reason: stop
---

```json
}
{
    "id": 1,
    "title": "FastAPI Book Launch",
    "image": "fastapi-book.jpeg",
    "description": "The launch of the FastAPI book will hold on xyz.",
    "tags": [
        "python",
        "fastapi"
    ],
    "location": "virtual"
}
```

После успешной реализации операций READ давайте добавим функцию редактирования для нашего приложения.

Обновление событий

Давайте добавим маршрут UPDATE в routes/events.py:

```python
@event_router.put("/edit/{id}", response_model=Event)
async def update_event(id: int, new_data: EventUpdate, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        event_data = new_data.dict(exclude_unset=True)
        for key, value in event_data.items():
            setattr(event, key, value)
        session.add(event)
        session.commit()
        session.refresh(event)

        return event
    raise HTTPException(
```

В тело функции добавьте следующий блок кода, чтобы получить существующее событие и обработать изменения события:

```python
    event = session.get(Event, id)
    if event:
        event_data = new_data.dict(exclude_unset=True)
        for key, value in event_data.items():
            setattr(event, key, value)
        session.add(event)
        session.commit()
        session.refresh(event)

        return event
    raise HTTPException(
```