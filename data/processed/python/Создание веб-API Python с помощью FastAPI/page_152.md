---
source_image: page_152.png
page_number: 152
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.11
tokens: 8415
characters: 1371
timestamp: 2025-12-24T02:19:58.102498
finish_reason: stop
---

Это поле позволит нам ограничить операции, выполняемые с событием, только пользователем.

Далее давайте изменим маршрут POST, чтобы обновить поле creator при создании нового события в routes/events.py:

```python
@event_router.post("/new")
async def create_event(body: Event, user: str = Depends(authenticate)) -> dict:
    body.creator = user
    await event_database.save(body)
    return {
        "message": "Event created successfully"
    }
```

В предыдущем блоке кода мы обновили маршрут POST, чтобы добавить адрес электронной почты текущего пользователя в качестве создателя события. Если вы создаете новое мероприятие, оно сохраняется вместе с адресом электронной почты создателя:

```bash
$ curl -X 'POST' \
'http://0.0.0.0:8080/event/new' \
-H 'accept: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXV CJ9.eyJlc2VyIjoicmVhZGVyQHBhY2t0LmNvbSIsImV4cGlyZXMiOjE2NTA4MzI 5NjQuMTU3MjQ4fQ.RxR1TYMx91JtVMNzYcT7718xXWX7skTCfWbnJxyf6fU' \
-H 'Content-Type: application/json' \
-d '{
    "title": "FastAPI Book Launch",
    "image": "https://linktomyimage.com/image.png",
    "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
    "tags": [
        "python",
        "fastapi",
        "book",
        "launch"
    ],
    "location": "Google Meet"
}'
```