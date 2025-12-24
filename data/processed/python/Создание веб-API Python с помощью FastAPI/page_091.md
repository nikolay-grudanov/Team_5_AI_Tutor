---
source_image: page_091.png
page_number: 91
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.71
tokens: 8284
characters: 1270
timestamp: 2025-12-24T02:18:13.746402
finish_reason: stop
---

status_code=status.HTTP_409_CONFLICT,
detail="User with supplied username exists"
)
users[data.email] = data
return {
    "message": "User successfully registered!"
}

В маршруте регистрации, определенном ранее, мы используем базу данных в приложении. (Мы познакомимся с базой данных в Главе 6 «Подключение к базе данных».)

Маршрут проверяет, существует ли пользователь с похожим адресом электронной почты в базе данных перед добавлением нового.

2. Давайте реализуем маршрут входа:

@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    if users[user.email] not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
            detail="User does not exist"
        )
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
            detail="Wrong credentials passed"
        )

    return {
        "message": "User signed in successfully"
    }

В этом маршруте первым делом проверяется, существует ли такой пользователь в базе данных, и, если такой пользователь не существует, возникает исключение. Если пользователь существует, приложение проверяет, совпадают ли пароли, прежде чем вернуть успешное сообщение или исключение.