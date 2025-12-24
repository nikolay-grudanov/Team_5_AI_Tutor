---
source_image: page_178.png
page_number: 178
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.31
tokens: 8189
characters: 758
timestamp: 2025-12-24T02:20:33.361224
finish_reason: stop
---

Давайте изменим ожидаемый ответ, чтобы подтвердить достоверность нашего теста:

```python
assert response.json()["title"] == "This test should fail"
```

Повторите тест:

```sh
(venv)$ pytest tests/test_routes.py
```

Вот результат:

![Неудачный тест из-за разницы в объектах ответа](../images/ch8_11.png)

Рисунок 8.11 – Неудачный тест из-за разницы в объектах ответа

Тестирование конечной точки DELETE

Наконец, давайте напишем тестовую функцию для конечной точки DELETE:

```python
@pytest.mark.asyncio
async def test_delete_event(default_client: httpx.AsyncClient, mock_event: Event, access_token: str) -> None:
    test_response = {
        "message": "Event deleted successfully."
    }

    headers = {
        "Content-Type": "application/json",
```