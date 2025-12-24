---
source_image: page_146.png
page_number: 146
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.42
tokens: 8093
characters: 374
timestamp: 2025-12-24T02:19:25.138460
finish_reason: stop
---

Рисунок 7.5 – Текст запроса для обновленного маршрута входа

Давайте войдем в систему, чтобы убедиться, что маршрут работает правильно

$ curl -X 'POST' \
'http://0.0.0.0:8080/user/signin' \
-H 'accept: application/json' \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d 'grant_type=&username=reader%40packt.com&password=exemplary&scope=&client_id=&client_secret='