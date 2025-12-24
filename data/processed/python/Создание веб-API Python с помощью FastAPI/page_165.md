---
source_image: page_165.png
page_number: 165
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.49
tokens: 8358
characters: 1333
timestamp: 2025-12-24T02:20:16.928227
finish_reason: stop
---

Далее мы создадим файл конфигурации с именем pytest.ini. Добавьте в него следующий код:

[pytest]
asyncio_mode = True

Файл конфигурации читается при запуске pytest. Это автоматически заставляет pytest запускать все тесты в асинхронном режиме.

Имея файл конфигурации, давайте создадим тестовый модуль conftest.py, который будет отвечать за создание экземпляра нашего приложения, необходимого для тестовых файлов. В папке с тестами создайте модуль conftest:

(venv)$ touch tests/conftest.py

Мы начнем с импорта необходимых зависимостей в conftest.py:

import asyncio
import httpx
import pytest

from main import app
from database.connection import Settings
from models.events import Event
from models.users import User

В предыдущем блоке кода мы импортировали модули asyncio, httpx и pytest. Модуль asyncio будет использоваться для создания активного сеанса цикла, чтобы тесты выполнялись в одном потоке, чтобы избежать конфликтов. Тест httpx будет действовать как асинхронный клиент для выполнения CRUD операций HTTP. Библиотека pytest необходима для определения фикстур.

Мы также импортировали приложение-экземпляр нашего приложения, а также модели и класс Settings. Давайте определим фикстуру сеанса цикла:

@ pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()