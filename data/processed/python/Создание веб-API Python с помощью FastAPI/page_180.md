---
source_image: page_180.png
page_number: 180
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.90
tokens: 8175
characters: 704
timestamp: 2025-12-24T02:20:31.012175
finish_reason: stop
---

url = f"/event/{str(mock_event.id)}"
response = await default_client.get(url)

assert response.status_code == 200
assert response.json()["creator"] == mock_event.creator
assert response.json()["_id"] == str(mock_event.id)

Ожидаемый ответ — отказ. Давайте попробуем:

(venv) $ pytest tests/test_routes.py

Вот результат:

![Неудачный тестовый ответ](../images/ch8-13.png)

Рисунок 8.13 – Неудачный тестовый ответ

Как видно из предыдущего снимка экрана, элемент больше не может быть найден в базе данных. Теперь, когда вы успешно реализовали тесты для аутентификации и маршрутов событий, раскомментируйте код, отвечающий за очистку пользовательских данных из базы данных.:

await User.find_all().delete()