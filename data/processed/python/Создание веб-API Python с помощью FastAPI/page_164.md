---
source_image: page_164.png
page_number: 164
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.15
tokens: 8449
characters: 1773
timestamp: 2025-12-24T02:20:23.380126
finish_reason: stop
---

# Fixture is defined.
@ pytest.fixture
def event() -> EventUpdate:
    return EventUpdate(
        title="FastAPI Book Launch",
        image="https://packt.com/fastapi.png",
        description="We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
        tags=["python", "fastapi", "book", "launch"],
        location="Google Meet"
    )
def test_event_name(event: EventUpdate) -> None:
    assert event.title == "FastAPI Book Launch"

В предыдущем блоке кода мы определили фикстуру, которая возвращает экземпляр pydantic модели EventUpdate. Это приспособление передается в качестве аргумента в функцию test_event_name, что позволяет сделать свойства доступными.

Декоратор фикстуры может дополнительно принимать аргументы. Одним из этих аргументов является область действия — область действия фикстуры сообщает pytest какова продолжительность функции фикстуры.
В этой главе мы будем использовать две области видимости:

• session: Эта область сообщает pytest, что нужно создать экземпляр функции один раз для всего сеанса тестирования.
• module: Эта область инструктирует pytest выполнять добавленную функцию только после выполнения тестового модуля.

Теперь, когда мы знаем, что такое фикстура, давайте настроим нашу тестовую среду в следующем разделе.

Настройка тестовой среды
В предыдущем разделе мы узнали об основах тестирования, а также о том, что такое фикстуры. Теперь мы проверим конечные точки для CRUD операций, а также аутентификацию пользователей. Чтобы протестировать наши асинхронные API, мы будем использовать httpx и установим библиотеку pytest-asyncio, чтобы мы могли протестировать наш асинхронный API.

Установите дополнительные библиотеки:

(venv)$ pip install httpx pytest-asyncio