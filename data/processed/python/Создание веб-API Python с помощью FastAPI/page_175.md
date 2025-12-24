---
source_image: page_175.png
page_number: 175
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.56
tokens: 8183
characters: 731
timestamp: 2025-12-24T02:20:23.123766
finish_reason: stop
---

Результат выглядит так:

![Успешный тестовый запуск запроса POST](../images/ch08-fig8-8.png)

Рисунок 8.8 – Успешный тестовый запуск запроса POST

Давайте напишем тест для проверки количества событий, хранящихся в базе данных (в нашем случае 2). Добавьте следующее:

```python
@pytest.mark.asyncio
async def test_get_events_count(default_client: httpx.AsyncClient) -> None:
    response = await default_client.get("/event/")

    events = response.json()

    assert response.status_code == 200
    assert len(events) == 2
```

В предыдущем блоке кода мы сохранили ответ JSON в переменной events, длина которой используется для нашего тестового сравнения. Давайте перезапустим тестовый модуль:

(venv) $ pytest tests/test_routes.py