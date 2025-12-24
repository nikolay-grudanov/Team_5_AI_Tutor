---
source_image: page_123.png
page_number: 123
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.85
tokens: 8303
characters: 1268
timestamp: 2025-12-24T02:19:12.455864
finish_reason: stop
---

Удалить

Наконец, давайте создадим метод для удаления записи из базы данных:

```python
async def delete(self, id: PydanticObjectId) -> bool:
    doc = await self.get(id)
    if not doc:
        return False
    await doc.delete()
    return True
```

В этом блоке кода метод проверяет, существует ли такая запись, прежде чем приступить к ее удалению из базы данных.

Теперь, когда мы заполнили наш файл базы данных нужными методами, необходимыми для выполнения CRUD операций, давайте также обновим маршруты.

routes/events.py

Начнем с обновления импорта и создания экземпляра database:

```python
from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status
from database.connection import Database

from models.events import Event
from typing import List
event_database = Database(Event)
```

Имея импорт и экземпляр базы данных, давайте обновим все маршруты. Начните с обновления маршрутов GET:

```python
@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    events = await event_database.get_all()
    return events

@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: PydanticObjectId) -> Event:
    event = await event_database.get(id)
    if not event:
```