---
source_image: page_110.png
page_number: 110
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.93
tokens: 8230
characters: 1017
timestamp: 2025-12-24T02:18:38.383899
finish_reason: stop
---

"tags": [
    "python",
    "fastapi",
    "book",
    "launch"
],
    "location": "Google Meet"
}

Возвращается успешный ответ:

{
    "message": "Event created successfully"
}

Если операцию выполнить не удалось, библиотека выдаст исключение.

Чтение событий

Давайте обновим маршрут GET, который извлекает список событий для извлечения данных из базы данных:

@event_router.get("/", response_model=List[Event])
async def retrieve_all_events(session=Depends(get_session)) -> List[Event]:
    statement = select(Event)
    events = session.exec(statement).all()
    return events

Аналогичным образом, маршрут для отображения данных события при получении по его идентификатору также обновляется:

@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"