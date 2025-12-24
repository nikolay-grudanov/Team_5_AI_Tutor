---
source_image: page_139.png
page_number: 139
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.65
tokens: 8200
characters: 745
timestamp: 2025-12-24T02:19:23.931155
finish_reason: stop
---

"password": "exemplary"
}
'

Мы получаем успешный ответ на запрос выше:

{
    "message": "User created successfully"
}

Теперь, когда мы создали пользователя, давайте проверим, что пароль, отправленный в базу данных, был хеширован. Для этого мы создадим интерактивный сеанс MongoDB, который позволит нам запускать команды из базы данных.

В новом окне терминала выполните следующие команды:

$ mongo --port 27017

Запускается интерактивный сеанс MongoDB:

![Интерактивный сеанс MongoDB](../images/chapter7/fig7_2.png)

Рисунок 7.2 – Интерактивный сеанс MongoDB

При работающем интерактивном сеансе выполните серию команд, чтобы переключиться на базу данных планировщика и получить все пользовательские записи:

> use planner
> db.users.find({})