---
source_image: page_168.png
page_number: 168
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.40
tokens: 8296
characters: 1102
timestamp: 2025-12-24T02:20:17.296749
finish_reason: stop
---

Перед запуском этого теста давайте кратко закомментируем строку, которая стирает пользовательские данные в conftest.py, поскольку это приведет к сбою аутентифицированных тестов:

```python
# await User.find_all().delete()
```

Со своего терминала запустите сервер MongoDB и запустите тест:

```bash
(venv) $ pytest tests/test_login.py
```

Маршрут регистрации успешно протестирован:

![Успешный тестовый прогон на маршруте регистрации](../images/ch08_03.png)

Рисунок 8.3 – Успешный тестовый прогон на маршруте регистрации

Приступим к написанию теста для маршрута входа. Тем временем вы можете быстро настроить ответ теста, чтобы увидеть, не прошел ли ваш тест или нет!

Тестирование маршрута входа

Ниже теста для маршрута регистрации давайте определим тест для маршрута входа. Мы начнем с определения полезной нагрузки запроса и заголовков, прежде чем инициировать запрос, как в первом тесте:

```python
@pytest.mark.asyncio
async def test_sign_user_in(default_client: httpx.AsyncClient) -> None:
    payload = {
        "username": "testuser@packt.com",
        "password": "testpassword"
    }
```