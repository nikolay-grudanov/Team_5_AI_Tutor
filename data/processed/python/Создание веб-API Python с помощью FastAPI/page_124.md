---
source_image: page_124.png
page_number: 124
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.13
tokens: 8255
characters: 1191
timestamp: 2025-12-24T02:19:06.753052
finish_reason: stop
---

```python
raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Event with supplied ID does not exist"
)
return event

В маршрутах GET мы вызываем методы, которые мы определили ранее в модуле базы данных. Давайте обновим POST маршруты:

@event_router.post("/new")
async def create_event(body: Event) -> dict:
    await event_database.save(body)
    return {
        "message": "Event created successfully"
    }

Давайте создадим маршрут UPDATE:

@event_router.put("/{id}", response_model=Event)
async def update_event(id: PydanticObjectId, body: EventUpdate) -> Event:
    updated_event = await event_database.update(id, body)
    if not updated_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return updated_event

Наконец, давайте обновим маршрут DELETE:

@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId) -> dict:
    event = await event_database.delete(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
```