---
source_image: page_166.png
page_number: 166
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.45
tokens: 8429
characters: 1620
timestamp: 2025-12-24T02:20:23.241404
finish_reason: stop
---

Имея это в виду, давайте создадим новый экземпляр базы данных из класса Settings:

```python
async def init_db():
    test_settings = Settings()
    test_settings.DATABASE_URL =
    "mongodb://localhost:27017/testdb"

    await test_settings.initialize_database()
```

В предыдущем блоке кода мы определили новый DATABASE_URL, а также вызвали функцию инициализации, определенную в главе 6 «Подключение к базе данных». Сейчас мы используем новую базу данных testdb.

Наконец, давайте определим клиентскую фикстуру по умолчанию, которая возвращает экземпляр нашего приложения, работающего асинхронно через httpx:

```python
@ pytest.fixture(scope="session")
async def default_client():
    await init_db()
    async with httpx.AsyncClient(app=app,
        base_url="http://app") as client:
        yield client
        # Clean up resources
        await Event.find_all().delete()
        await User.find_all().delete()
```

В предыдущем блоке кода сначала инициализируется база данных, а приложение запускается как AsyncClient, который остается активным до конца тестового сеанса. В конце сеанса тестирования коллекция событий и пользователей стирается, чтобы убедиться, что база данных пуста перед каждым запуском теста.

В этом разделе вы познакомились с шагами, связанными с настройкой вашей тестовой среды. В следующем разделе вы познакомитесь с процессом написания тестов для каждой конечной точки, созданной в приложении.

Написание тестов для конечных точек REST API

Когда все готово, давайте создадим модуль test_login.py, в котором мы будем тестировать маршруты аутентификации:

(venv)$ touch tests/test_login.py