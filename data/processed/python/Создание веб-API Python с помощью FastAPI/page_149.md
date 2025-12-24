---
source_image: page_149.png
page_number: 149
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.31
tokens: 8305
characters: 866
timestamp: 2025-12-24T02:19:44.175074
finish_reason: stop
---

Теперь, когда мы успешно вошли в систему, мы можем создать событие:

![Создание нового события](./images/7.8.png)

Рисунок 7.8 – Создать новое событие

Те же операции можно выполнить из командной строки. Во-первых, давайте получим наш токен доступа:

```bash
$ curl -X 'POST' \
    'http://0.0.0.0:8080/user/signin' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'grant_type=&username=reader%40packt.com&password=exemplary&scope=&client_id=&client_secret='
```

Отправленный запрос возвращает токен доступа, который представляет собой строку JWT, и тип токена, который имеет тип Bearer:

```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlc2VyIjoicmVhZGVyQHBhY2t0LmNvbSIsImV4cGlyZXMiOjE2NTA4MjkxODMuNTg3NjAyfQ.MOXjI5GXnyzGNftdlxDGyM119_L11uPq8yCxBHepf04",
    "token_type": "Bearer"
}
```