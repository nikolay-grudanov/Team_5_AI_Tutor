---
source_image: page_153.png
page_number: 153
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.77
tokens: 8242
characters: 941
timestamp: 2025-12-24T02:19:48.954228
finish_reason: stop
---

Ответ, возвращенный из запроса выше:

```json
{
    "message": "Event created successfully"
}
```

Далее давайте получим список событий, хранящихся в базе данных:

```sh
$ curl -X 'GET' \
'http://0.0.0.0:8080/event/' \
-H 'accept: application/json'
```

Ответ на запрос выше:

```json
[
    {
        "_id": "6265a807e0c8daefb72261ea",
        "creator": "reader@packt.com",
        "title": "FastAPI BookLaunch",
        "image": "https://linktomyimage.com/image.png",
        "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
        "tags": [
            "python",
            "fastapi",
            "book",
            "launch"
        ],
        "location": "Google Meet"
    }
]
```

Далее давайте обновим маршрут UPDATE:

```python
@event_router.put("/{id}", response_model=Event)
async def update_event(id: PydanticObjectId, body: EventUpdate,
```