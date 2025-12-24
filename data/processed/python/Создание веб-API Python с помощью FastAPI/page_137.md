---
source_image: page_137.png
page_number: 137
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.73
tokens: 8301
characters: 1326
timestamp: 2025-12-24T02:19:28.667251
finish_reason: stop
---

deprecated="auto")

class HashPassword:
    def create_hash(self, password: str):
        return pwd_context.hash(password)

    def verify_hash(self, plain_password: str, hashed_password: str):
        return pwd_context.verify(plain_password, hashed_password)

В предыдущем блоке кода мы начинаем с импорта CryptContext, который использует схему bcrypt для хеширования переданных ему строк. Контекст хранится в переменной контекста pwd_context, что дает нам доступ к методам, необходимым для выполнения нашей задачи.

Затем определяется класс HashPassword, который содержит два метода: create_hash и verify_hash:

• Метод create_hash принимает строку и возвращает хешированное значение.
• verify_hash берет простой пароль и хешированный пароль и сравнивает их. Функция возвращает логическое значение, указывающее, совпадают ли переданные значения или нет.

Теперь, когда мы создали класс для обработки хеширования паролей, давайте обновим маршрут регистрации, чтобы хешировать пароль пользователя перед его сохранением в базе данных:

routes/users.py

from auth.hash_password import HashPassword
from database.connection import Database

user_database = Database(User)
hash_password = HashPassword()

@user_router.post("/signup")
async def sign_user_up(user: User) -> dict:
    user_exist = await User.find_one(User.email ==