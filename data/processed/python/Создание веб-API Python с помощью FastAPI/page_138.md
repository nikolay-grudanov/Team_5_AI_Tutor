---
source_image: page_138.png
page_number: 138
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.86
tokens: 8296
characters: 1203
timestamp: 2025-12-24T02:19:29.928008
finish_reason: stop
---

```python
user.email)

    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with email provided exists already."
        )
    hashed_password = hash_password.create_hash(
        user.password)
    user.password = hashed_password
    await user_database.save(user)
    return {
        "message": "User created successfully"
    }
```

Теперь, когда мы обновили маршрут регистрации пользователя, чтобы хешировать пароль перед сохранением, давайте создадим нового пользователя для подтверждения. В окне терминала запустите приложение:

(venv)$ python main.py
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
INFO:     Started reloader process [8144] using statreload
INFO:     Started server process [8147]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

В другом окне терминала запустите экземпляр MongoDB:

$ mongod --dbpath database --port 27017

Далее создадим нового пользователя:

$ curl -X 'POST' \
    'http://0.0.0.0:8080/user/signup' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
        "email": "reader@packt.com",
```