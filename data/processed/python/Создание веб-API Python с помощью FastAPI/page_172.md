---
source_image: page_172.png
page_number: 172
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.86
tokens: 8319
characters: 1133
timestamp: 2025-12-24T02:20:31.021615
finish_reason: stop
---

assert response.status_code == 200
assert response.json()[0]["_id"] == str(mock_event.id)

В предыдущем блоке кода мы тестируем путь маршрута события, чтобы проверить, присутствует ли событие, добавленное в базу данных в фикстуре mock_event.
Давайте запустим тест:

(venv) $ pytest tests/test_routes.py

Вот результат:

![Успешный тестовый запуск](../images/ch08/fig8-6.png)

Рисунок 8.6 – Успешный тестовый запуск

Далее давайте напишем тестовую функцию для конечной точки /event/{id}:

@pytest.mark.asyncio
async def test_get_event(default_client: httpx.AsyncClient, mock_event: Event) -> None:
    url = f"/event/{str(mock_event.id)}"
    response = await default_client.get(url)

    assert response.status_code == 200
    assert response.json()["creator"] == mock_event.creator
    assert response.json()["_id"] == str(mock_event.id)

В предыдущем блоке кода мы тестируем конечную точку, которая извлекает одно событие. Переданный идентификатор события извлекается из фикстуры mock_event, а результат запроса сравнивается с данными, хранящимися в фикстуре mock_event.
Давайте запустим тест:

(venv) $ pytest tests/test_routes.py