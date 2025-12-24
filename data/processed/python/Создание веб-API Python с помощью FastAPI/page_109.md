---
source_image: page_109.png
page_number: 109
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.08
tokens: 8351
characters: 1398
timestamp: 2025-12-24T02:18:53.107367
finish_reason: stop
---

Что такое Depends?
Класс Depends отвечает за выполнение внедрения зависимостей в приложениях FastAPI. Класс Depends принимает источник истинности, такой как функция, в качестве аргумента и передается в качестве аргумента функции в маршруте, требуя, чтобы условие зависимости было выполнено до того, как любая операция может быть выполнена.

2. Далее давайте обновим функцию маршрута POST, отвечающую за создание нового события, create_event():

@event_router.post("/new")
async def create_event(new_event: Event, session=Depends(get_session)) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)

    return {
        "message": "Event created successfully"
    }

В этом блоке кода мы указали, что объект сеанса, необходимый для выполнения транзакций базы данных, зависит от функции get_session(), которую мы создали ранее.

В теле функции данные добавляются в сессию, а затем фиксируются в базе данных, после чего база данных обновляется.

3. Давайте протестируем маршруты для предварительного просмотра изменений:

(venv)$ curl -X 'POST' \
'http://0.0.0.0:8080/event/new' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
    "title": "FastAPI Book Launch",
    "image": "fastapi-book.jpeg",
    "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
