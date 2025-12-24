---
source_image: page_155.png
page_number: 155
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.04
tokens: 8466
characters: 1086
timestamp: 2025-12-24T02:20:08.029378
finish_reason: stop
---

В предыдущем блоке кода мы указываем функции маршрута сначала проверить, является ли текущий пользователь создателем, в противном случае вызвать исключение. Давайте рассмотрим пример, когда другой пользователь пытается удалить событие другого пользователя:

```bash
$ curl -X 'DELETE' \
'http://0.0.0.0:8080/event/6265a83fc823a3c912830074' \
-H 'accept: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXV CJ9.eyJ1c2VyIjoiZmFzdGFwaUBwYWNrdC5jb20iLCJleHBpcmVzIjoxNjUwOD MzOTc2LjI2NzgzMX0.MMRT6pwEDBVHTU5ClA6MV8j9wCfWhqbza9NBpZz08xE'
```

Ненайденное событие возвращается в качестве ответа:

```json
{
    "detail": "Event not found"
}
```

Однако владелец может удалить событие:

```bash
$ curl -X 'DELETE' \
'http://0.0.0.0:8080/event/6265a83fc823a3c912830074' \
-H 'accept: application/json' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVC J9.eyJ1c2VyIjoicmVhZGVyQHBhY2t0LmNvbSIIsImV4cGlyZXMiOjE2NTA4MzQz OTUuMDkzMDI3fQ.IKYHWQ2YO3rQc-KR8kyfoy_54MsEVE75WbRqoVbdow0'
```

Вот ответ:

```json
{
    "message": "Event deleted successfully."
}
```