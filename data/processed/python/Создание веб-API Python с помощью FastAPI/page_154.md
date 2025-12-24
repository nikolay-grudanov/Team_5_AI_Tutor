---
source_image: page_154.png
page_number: 154
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.82
tokens: 8364
characters: 1180
timestamp: 2025-12-24T02:19:58.536925
finish_reason: stop
---

user: str = Depends(authenticate)) -> Event:
    event = await event_database.get(id)
    if event.creator != user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Operation not allowed"
        )

В предыдущем блоке кода функция маршрута проверяет, может ли текущий пользователь редактировать событие, прежде чем продолжить, в противном случае она вызывает исключение неверного запроса HTTP 400.
Вот пример использования другого пользователя:

$ curl -X 'PUT' \
'http://0.0.0.0:8080/event/6265a83fc823a3c912830074' \
-H 'accept: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlc2VyIjoiZmFzdGFwaUBwYWNrdC5jb20iLCJleHBpcmVzIjoxNjUwODMzOTc2LjI2NzgzMX0.MMRT6pwEDBVHTU5C1a6MV8j9wCfWhqbza9NBpZz08xE' \
-H 'Content-Type: application/json' \
-d '{
    "title": "FastAPI Book Launch"
}'

Вот ответ:

{
    "detail": "Operation not allowed"
}

Наконец, давайте обновим маршрут DELETE:

@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId, user: str = Depends(authenticate)):
    event = await event_database.get(id)
    if event.creator != user:
        raise HTTPException(