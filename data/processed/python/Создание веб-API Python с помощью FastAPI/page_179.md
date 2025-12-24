---
source_image: page_179.png
page_number: 179
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.24
tokens: 8181
characters: 713
timestamp: 2025-12-24T02:20:33.361201
finish_reason: stop
---

"Authorization": f"Bearer {access_token}"

}
url = f"/event/{mock_event.id}"

response = await default_client.delete(url, headers=headers)

assert response.status_code == 200
assert response.json() == test_response

Как и в предыдущих тестах, определяется ожидаемый ответ теста, а также заголовки. Маршрут DELETE задействован, и ответ сравнивается. Давайте запустим тест:

(venv)$ pytest tests/test_routes.py

Вот результат:

![Успешный тест УДАЛИТЬ](../images/ch08_12.png)

Рисунок 8.12 – Успешный тест УДАЛИТЬ

Чтобы убедиться, что документ действительно был удален, добавим финальную проверку:

@ pytest.mark.asyncio
async def test_get_event_again(default_client: httpx.AsyncClient, mock_event: Event) -> None: