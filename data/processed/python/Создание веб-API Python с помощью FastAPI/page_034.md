---
source_image: page_034.png
page_number: 34
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.81
tokens: 8369
characters: 1493
timestamp: 2025-12-24T02:16:42.042265
finish_reason: stop
---

Далее мы создадим временную базу данных в приложении, а также два маршрута для добавления и извлечения задач:

```python
todo_list = []

@todo_router.post("/todo")
async def add_todo(todo: dict) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}

@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {"todos": todo_list}
```

В предыдущем блоке кода мы создали два маршрута для наших операций с задачами. Первый маршрут добавляет задачу в список задач с помощью метода POST, а второй маршрут извлекает все элементы задачи из списка задач с помощью метода GET.

Мы завершили операции пути для маршрута todo. Следующим шагом является передача приложения в производство, чтобы мы могли протестировать определенные операции пути.

Класс APIRouter работает так же, как и класс FastAPI. Однако uvicorn не может использовать экземпляр APIRouter для обслуживания приложения, в отличие от FastAPIs.
Маршруты, определенные с помощью класса APIRouter, добавляются в экземпляр fastapi для обеспечения их видимости.

Чтобы обеспечить видимость маршрутов todo, мы включим обработчик операций пути todo_router в основной экземпляр FastAPI с помощью метода include_router().

include_router()
Метод include_router(router, ...) отвечает за добавление маршрутов, определенных с помощью класса APIRouter, в экземпляр основного приложения, чтобы сделать маршруты видимыми.

В api.py, import todo_router из todo.py:

```python
from todo import todo_router
```