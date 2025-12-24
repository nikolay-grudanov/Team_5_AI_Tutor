---
source_image: page_038.png
page_number: 38
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.67
tokens: 8313
characters: 1190
timestamp: 2025-12-24T02:16:54.389221
finish_reason: stop
---

В примере запроса POST отправленные данные были в следующем формате:

```json
{
    "id": id,
    "item": item
}
```

Однако пустой словарь также мог быть отправлен без возврата какой-либо ошибки. Пользователь может отправить запрос с телом, отличным от показанного ранее. Создание модели с требуемой структурой тела запроса и присвоение ее в качестве типа телу запроса гарантирует, что будут переданы только те поля данных, которые присутствуют в модели.

Например, чтобы в предыдущем примере поля содержались только в теле запроса, создайте новый файл model.py и добавьте в него приведенный ниже код:

```python
from Pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str
```

В предыдущем блоке кода мы создали модель Pydantic, которая принимает только два поля:

• id — целочисленное число
• item — строка

Давайте продолжим и используем модель в маршруте POST. В api.py, импортируйте модель:

```python
from model import Todo
```

Затем замените тип переменной тела запроса с dict на Todo:

```python
todo_list = []

@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}
```