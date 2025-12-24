---
source_image: page_048.png
page_number: 48
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.82
tokens: 8199
characters: 717
timestamp: 2025-12-24T02:17:07.521879
finish_reason: stop
---

ReDoc

Документация ReDoc дает более подробное и прямое представление о моделях, маршрутах и API. Вы можете получить к нему доступ, добавив /redoc к адресу приложения. В веб-браузере перейдите по адресу http://127.0.0.1:8000/redoc:

![Портал документации на базе ReDoc](../images/2.3.png)

Рисунок 2.3 – Портал документации на базе ReDoc

Чтобы правильно сгенерировать JSON схему, вы можете указать примеры того, как пользователь будет заполнять данные в модели. Пример задается путем встраивания класса Config в класс модели. Давайте добавим пример схемы в нашу модель Todo:

```python
class Todo(BaseModel):
    id: int
    item: str

class Config:
    Schema_extra = {
        "Example": {
            "id": 1,
```