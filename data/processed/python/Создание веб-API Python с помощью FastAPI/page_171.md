---
source_image: page_171.png
page_number: 171
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.91
tokens: 8409
characters: 1659
timestamp: 2025-12-24T02:20:35.680227
finish_reason: stop
---

В предыдущем блоке кода мы импортировали обычные зависимости. Мы также импортировали функцию create_access_token (user) и модель Event. Поскольку некоторые из маршрутов защищены, мы будем генерировать токен доступа самостоятельно. Давайте создадим новую фикстуру, которая при вызове возвращает токен доступа. Приспособление имеет область модуля, что означает, что оно запускается только один раз — при выполнении тестового модуля — и не вызывается при каждом вызове функции. Добавьте следующий код:

```python
@ pytest.fixture(scope="module")
async def access_token() -> str:
    return create_access_token("testuser@packt.com")
```

Давайте создадим новый прибор, который добавляет событие в базу данных. Это действие выполняется для запуска предварительных тестов перед тестированием конечных точек CRUD. Добавьте следующий код:

```python
@ pytest.fixture(scope="module")
async def mock_event() -> Event:
    new_event = Event(
        creator="testuser@packt.com",
        title="FastAPI Book Launch",
        image="https://linktomyimage.com/image.png",
        description="We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
        tags=["python", "fastapi", "book", "launch"],
        location="Google Meet"
    )

    await Event.insert_one(new_event)

    yield new_event
```

Тестирование конечных точек READ

Далее давайте напишем тестовую функцию, которая проверяет GET-метод HTTP на маршруте /event:

```python
@ pytest.mark.asyncio
async def test_get_events(default_client: httpx.AsyncClient, mock_event: Event) -> None:
    response = await default_client.get("/event/")
```