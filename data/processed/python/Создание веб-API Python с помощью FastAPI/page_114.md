---
source_image: page_114.png
page_number: 114
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.66
tokens: 8295
characters: 1158
timestamp: 2025-12-24T02:18:53.031516
finish_reason: stop
---

session.commit()

return {
    "message": "Event deleted successfully"
}

raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Event with supplied ID does not exist"
)

В этом блоке кода функция проверяет, существует ли событие, идентификатор которого был предоставлен, а затем удаляет его из базы данных. После выполнения операции возвращается сообщение об успешном выполнении и выдается исключение, если событие не существует. Удалим событие из базы:

(venv)$ curl -X 'DELETE' \
'http://0.0.0.0:8080/event/delete/1' \
-H 'accept: application/json'

Запрос возвращает успешный ответ:

{
    "message": "Event deleted successfully"
}

Теперь, если мы получим список событий, мы получим пустой массив для ответа:

(venv)$ curl -X 'GET' \
'http://0.0.0.0:8080/event/' \
-H 'accept: application/json'
[]

Мы успешно внедрили базу данных SQL в наше приложение с помощью SQLModel, а также реализовали CRUD операции. Давайте зафиксируем изменения, внесенные в приложение, прежде чем научиться реализовывать CRUD операции в MongoDB:

(venv)$ git add .
(venv)$ git commit -m "[Feature] Incorporate a SQL database and implement CRUD operations"