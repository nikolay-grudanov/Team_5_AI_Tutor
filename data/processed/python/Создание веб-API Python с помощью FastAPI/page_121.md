---
source_image: page_121.png
page_number: 121
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.36
tokens: 8293
characters: 1176
timestamp: 2025-12-24T02:19:03.011561
finish_reason: stop
---

Теперь, когда мы успешно добавили блоки кода для инициализации базы данных, давайте приступим к реализации методов для CRUD операций.

**CRUD операции**

В connection.py, создайте новый класс Database, который принимает модель в качестве аргумента во время инициализации:

```python
from pydantic import BaseSettings, BaseModel
from typing import Any, List, Optional

class Database:
    def __init__(self, model):
        self.model = model
```

Модель, передаваемая во время инициализации, представляет собой класс модели документа Event или User.

**Создать**

Давайте создадим метод в классе Database, чтобы добавить запись в коллекцию базы данных:

```python
async def save(self, document) -> None:
    await document.create()
    return
```

В этом блоке кода мы определили метод save для получения документа, который будет экземпляром документа, переданного в экземпляр Database в момент создания экземпляра.

**Читать**

Давайте создадим методы для извлечения записи базы данных или всех записей, присутствующих в коллекции базы данных.:

```python
async def get(self, id: PydanticObjectId) -> Any:
    doc = await self.model.get(id)
    if doc:
        return doc
```