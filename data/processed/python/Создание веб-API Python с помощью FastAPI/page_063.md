---
source_image: page_063.png
page_number: 63
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.26
tokens: 8335
characters: 1187
timestamp: 2025-12-24T02:17:29.942790
finish_reason: stop
---

Класс HTTPException принимает три аргумента:

• status_code: Код состояния, который будет возвращен для этого сбоя

• detail: Сопроводительное сообщение для отправки клиенту

• headers: Необязательный параметр для ответов, требующих заголовков

В наших определениях пути маршрута задачи мы возвращаем сообщение, когда задача не может быть найдена. Мы будем обновлять его, чтобы вызывать HTTPException. HTTPException позволяет нам вернуть адекватный код ответа на ошибку.

В нашем текущем приложении получение несуществующей задачи возвращает код статуса ответа 200 вместо кода статуса ответа 404 на http://127.0.0.1:8000/docs:

![Запрос возвращает ответ 200 вместо ответа 404](../images/ch3-fig3-1.png)

Рисунок 3.1 – Запрос возвращает ответ 200 вместо ответа 404

Обновляя маршруты для использования класса HTTPException, мы можем возвращать соответствующие детали в нашем ответе. В todo.py, обновите маршруты для получения, обновления и удаления списка дел:

from fastapi import APIRouter, Path, HTTPException, status
..
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict:
    for todo in todo_list: