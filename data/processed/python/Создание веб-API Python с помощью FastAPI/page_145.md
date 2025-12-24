---
source_image: page_145.png
page_number: 145
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.76
tokens: 8250
characters: 1075
timestamp: 2025-12-24T02:19:35.367243
finish_reason: stop
---

user.username)
    ..
    if hash_password.verify_hash(user.password, user_exist.password):
        access_token = create_access_token(
            user_exist.email)
        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }

В предыдущем блоке кода мы внедрили класс OAuth2PasswordRequestForm в качестве зависимости для этой функции, гарантируя строгое соблюдение спецификации OAuth. В теле функции мы сравниваем пароль и возвращаем токен доступа и тип токена. Прежде чем протестировать обновленный маршрут, давайте создадим модель ответа для маршрута входа в models/users.py, чтобы заменить класс модели UserSignIn, который больше не используется:

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

Обновите импорт и модель ответа для маршрута входа:

from models.users import User, TokenResponse

@user_router.post("/signin", response_model=TokenResponse)

Давайте посетим интерактивные документы, чтобы убедиться, что тело запроса соответствует спецификациям OAuth2 по адресу http://0.0.0.0:8080/docs: