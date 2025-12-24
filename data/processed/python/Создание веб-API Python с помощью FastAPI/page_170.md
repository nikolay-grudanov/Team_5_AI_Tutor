---
source_image: page_170.png
page_number: 170
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.48
tokens: 8220
characters: 803
timestamp: 2025-12-24T02:20:16.796789
finish_reason: stop
---

Давайте изменим имя пользователя для входа на неправильное, чтобы подтвердить, что тест не пройден:

```python
payload = {
    "username": "wronguser@packt.com",
    "password": "testpassword"
}
```

![Неудачный тест из-за неправильной полезной нагрузки запроса](../images/ch8_05.png)

Рисунок 8.5 – Неудачный тест из-за неправильной полезной нагрузки запроса

Мы успешно написали тесты для маршрутов регистрации и входа. Перейдем к тестированию CRUD-маршрутов для API планировщика событий.

Тестирование конечных точек CRUD

Мы начнем с создания нового модуля с именем test_routes.py:

```bash
(venv) $ touch test_routes.py
```

Во вновь созданный модуль добавьте следующий код:

```python
import httpx
import pytest

from auth.jwt_handler import create_access_token
from models.events import Event
```