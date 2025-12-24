---
source_image: page_125.png
page_number: 125
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.37
tokens: 8194
characters: 974
timestamp: 2025-12-24T02:19:03.211076
finish_reason: stop
---

return {
    "message": "Event deleted successfully."
}

Теперь, когда мы реализовали CRUD операции для наших маршрутов событий, давайте реализуем маршруты для регистрации пользователя и входа пользователя.

routes/users.py

Начнем с обновления импорта и создания экземпляра базы данных:

from fastapi import APIRouter, HTTPException, status
from database.connection import Database

from models.users import User, UserSignIn

user_router = APIRouter(
    tags=["User"],
)

user_database = Database(User)

Затем обновите маршрут POST для подписи новых пользователей:

@user_router.post("/signup")
async def sign_user_up(user: User) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with email provided exists already."
        )
    await user_database.save(user)
    return {
        "message": "User created successfully"
    }