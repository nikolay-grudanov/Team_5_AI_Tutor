---
source_image: page_176.png
page_number: 176
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.35
tokens: 8182
characters: 764
timestamp: 2025-12-24T02:20:23.184448
finish_reason: stop
---

Вот результат:

![Успешный тестовый прогон для подтверждения количества событий](./images/8.9.png)

Рисунок 8.9 – Успешный тестовый прогон для подтверждения количества событий

Мы успешно протестировали конечные точки GET /event и /event/{id} и конечную точку POST /event/new, соответственно. Давайте проверим конечные точки UPDATE и DELETE для /event/new дальше.

Тестирование конечной точки UPDATE

Начнем с конечной точки UPDATE:

```python
@ pytest.mark.asyncio
async def test_update_event(default_client: httpx.AsyncClient, mock_event: Event, access_token: str) -> None:
    test_payload = {
        "title": "Updated FastAPI event"
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
```