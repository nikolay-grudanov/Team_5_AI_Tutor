---
source_image: page_177.png
page_number: 177
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.66
tokens: 8206
characters: 810
timestamp: 2025-12-24T02:20:30.550283
finish_reason: stop
---

url = f"/event/{str(mock_event.id)}"

response = await default_client.put(url,
json=test_payload, headers=headers)

assert response.status_code == 200
assert response.json()["title"] == test_payload["title"]

В предыдущем блоке кода мы изменяем событие, хранящееся в базе данных, извлекая ID из фикстуры mock_event. Затем мы определяем полезную нагрузку запроса и заголовки. В переменной response инициируется запрос и сравнивается полученный ответ. Давайте подтвердим, что тест работает правильно:

(venv)$ pytest tests/test_routes.py

Вот результат:

![Успешный запуск запроса UPDATE](../images/ch08_10.png)

Рисунок 8.10 – Успешный запуск запроса UPDATE

Совет
Приспособление mock_event пригодится, поскольку ID документов MongoDB уникально генерируется каждый раз, когда документ добавляется в базу данных.