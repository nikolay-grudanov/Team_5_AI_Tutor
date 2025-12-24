---
source_image: page_117.png
page_number: 117
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.08
tokens: 8303
characters: 1235
timestamp: 2025-12-24T02:18:58.859552
finish_reason: stop
---

• .delete(): Этот метод отвечает за удаление записи документа из базы данных, например:

event = await Event.get("74478287284ff")
await event.delete()

Теперь, когда мы узнали, как работают методы, содержащиеся в библиотеке Beanie, давайте инициализируем базу данных в нашем приложении планировщика событий, определим наши документы и реализуем CRUD операции.

Инициализация базы данных

Давайте посмотрим на шаги, чтобы сделать это:

1. В папке базы данных создайте модуль connection.py:

(venv)$ touch connection.py

Pydantic позволяет нам читать переменные среды, создавая дочерний класс родительского класса BaseSettings. При создании веб-API стандартной практикой является хранение переменных конфигурации в файле среды.

2. В connection.py, добавьте следующее:

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(
            database=client.get_default_database(),
            document_models=[]
        )

class Config:
    env_file = ".env"