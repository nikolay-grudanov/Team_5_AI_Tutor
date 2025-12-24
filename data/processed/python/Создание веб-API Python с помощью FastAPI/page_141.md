---
source_image: page_141.png
page_number: 141
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.49
tokens: 8273
characters: 1070
timestamp: 2025-12-24T02:19:32.299103
finish_reason: stop
---

.env

SECRET_KEY=HI5HL3V3L$3CR3T

После этого добавьте следующий импорт в jwt_handler.py:

import time
from datetime import datetime

from fastapi import HTTPException, status
from jose import jwt, JWTError
from database.database import Settings

В предыдущем блоке кода мы импортировали модули time, класс HTTPException, а также статус из FastAPI. Мы также импортировали библиотеку jose отвечающую за кодирование и декодирование JWT, и класс Settings.

Далее мы создадим экземпляр класса Settings, чтобы мы могли получить переменную SECRET_KEY и создать функцию, отвечающую за создание токена:

settings = Settings()

def create_access_token(user: str) -> str:
    payload = {
        "user": user,
        "expires": time.time() + 3600
    }

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token

В предыдущем блоке кода функция принимает строковый аргумент, который передается в словарь полезной нагрузки. Словарь полезной нагрузки содержит пользователя и время истечения срока действия, которое возвращается при декодировании JWT.