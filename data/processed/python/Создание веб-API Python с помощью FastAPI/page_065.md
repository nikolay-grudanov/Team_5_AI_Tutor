---
source_image: page_065.png
page_number: 65
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.08
tokens: 8225
characters: 840
timestamp: 2025-12-24T02:17:33.681074
finish_reason: stop
---

detail="Todo with supplied ID doesn't exist",

Теперь давайте повторим попытку получения несуществующей задачи, чтобы убедиться, что возвращается правильный код ответа:

![Отображается правильный код ответа 404](https://i.imgur.com/3Q5z5QG.png)

Рисунок 3.2 – Отображается правильный код ответа 404

Наконец, мы можем объявить код состояния HTTP для переопределения кода состояния по умолчанию для успешных операций, добавив аргумент status_code в функцию декоратора:

@todo_router.post("/todo", status_code=201)
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "message": "Todo added successfully."
    }

В этом разделе мы узнали, как возвращать правильные коды ответов клиентам, а также переопределять код состояния по умолчанию. Также важно отметить, что код состояния успешный по умолчанию — 200.