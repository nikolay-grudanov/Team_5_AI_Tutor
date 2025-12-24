---
source_image: page_173.png
page_number: 173
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.07
tokens: 8250
characters: 1041
timestamp: 2025-12-24T02:20:23.674345
finish_reason: stop
---

Вот результат:

![Успешный тестовый прогона для извлечения одного события](../images/ch08_07.png)

Рисунок 8.7 – Успешный тестовый прогон для извлечения одного события

Далее напишем тестовую функцию для создания нового события.

Тестирование конечной точки CREATE

Мы начнем с определения функции и получения токена доступа из ранее созданного прибора. Мы создадим полезную нагрузку запроса, которая будет отправлена на сервер, заголовки запроса, которые будут содержать тип контента, а также значение заголовка авторизации. Также будет определен тестовый ответ, после чего инициируется запрос и сравниваются ответы. Добавьте следующий код:

```python
@ pytest.mark.asyncio
async def test_post_event(default_client: httpx.AsyncClient, access_token: str) -> None:
    payload = {
        "title": "FastAPI Book Launch",
        "image": "https://linktomyimage.com/image.png",
        "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
        "tags": [
```