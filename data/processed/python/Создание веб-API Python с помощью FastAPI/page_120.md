---
source_image: page_120.png
page_number: 120
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.20
tokens: 8138
characters: 601
timestamp: 2025-12-24T02:18:48.652321
finish_reason: stop
---

6. Теперь, когда мы определили документы, давайте обновим поле document_models в connection.py:

```python
from models.users import User
from models.events import Event

async def initialize_database(self):
    client = AsyncIOMotorClient(self.DATABASE_URL)
    await init_beanie(
        database=client.get_default_database(),
        document_models=[Event, User])
```

7. Наконец, давайте создадим файл среды, .env, и добавим URL-адрес базы данных, чтобы завершить этап инициализации базы данных:

```bash
(venv)$ touch .env
(venv)$ echo DATABASE_URL=mongodb://localhost:27017/
planner >> .env
```