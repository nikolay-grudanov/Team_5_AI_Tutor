---
source_image: page_126.png
page_number: 126
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.83
tokens: 8310
characters: 1324
timestamp: 2025-12-24T02:19:12.662806
finish_reason: stop
---

В этом блоке кода мы проверяем, существует ли такой пользователь с переданным адресом электронной почты, прежде чем добавлять его в базу данных. Давайте добавим маршрут для входа пользователей:

```python
@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with email does not exist."
        )
    if user_exist.password == user.password:
        return {
            "message": "User signed in successfully."
        }
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid details passed."
    )
```

В этом определенном маршруте мы сначала проверяем, существует ли пользователь, прежде чем проверять действительность его учетных данных. Используемый здесь метод аутентификации является базовым и не рекомендуется в производственной среде. Мы рассмотрим правильные процедуры аутентификации в следующей главе.

Теперь, когда мы реализовали маршруты, давайте запустим экземпляр MongoDB, а также наше приложение. Создайте папку для размещения нашей базы данных MongoDB и запустите экземпляр MongoDB:

```bash
(venv)$ mkdir store
(venv)$ mongod --dbpath store
```