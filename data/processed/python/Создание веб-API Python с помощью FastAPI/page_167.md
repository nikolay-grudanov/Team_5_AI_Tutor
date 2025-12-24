---
source_image: page_167.png
page_number: 167
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.62
tokens: 8286
characters: 1153
timestamp: 2025-12-24T02:20:09.632822
finish_reason: stop
---

В тестовом модуле мы начнем с импорта зависимостей:

```python
import httpx
import pytest
```

**Тестирование маршрута регистрации**

Первая конечная точка, которую мы будем тестировать, — это конечная точка регистрации. Мы добавим декоратор `pytest.mark.asyncio`, который сообщает `pytest` что нужно рассматривать это как асинхронный тест. Давайте определим функцию и полезную нагрузку запроса:

```python
@ pytest.mark.asyncio
async def test_sign_new_user(default_client: httpx.AsyncClient) -> None:
    payload = {
        "email": "testuser@packt.com",
        "password": "testpassword",
    }
```

Определим заголовок запроса и ожидаемый ответ:

```python
headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

test_response = {
    "message": "User created successfully"
}
```

Теперь, когда мы определили ожидаемый ответ на этот запрос, давайте инициируем запрос:

```python
response = await default_client.post("/user/signup", json=payload, headers=headers)
```

Далее мы проверим, был ли запрос успешным, сравнив ответы:

```python
assert response.status_code == 200
assert response.json() == test_response
```