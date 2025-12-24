---
source_image: page_095.png
page_number: 95
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.40
tokens: 8268
characters: 1133
timestamp: 2025-12-24T02:18:20.734552
finish_reason: stop
---

Маршруты событий

После создания пользовательских маршрутов следующим шагом будет реализация маршрутов для событийных операций. Давайте посмотрим на шаги:

1. Начните с импорта зависимостей и определения маршрутизатора событий:

```python
from fastapi import APIRouter, Body, HTTPException, status
from models.events import Event
from typing import List

event_router = APIRouter(
    tags=["Events"]
)

events = []
```

2. Следующим шагом является определение маршрута для получения всех событий и события, соответствующего предоставленному идентификатору в базе данных:

```python
@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    return events

@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )
```

Во втором маршруте мы вызываем исключение HTTP_404_NOT_FOUND, когда событие с предоставленным идентификатором не существует.