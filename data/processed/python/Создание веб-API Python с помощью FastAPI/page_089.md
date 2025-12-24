---
source_image: page_089.png
page_number: 89
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.62
tokens: 8166
characters: 789
timestamp: 2025-12-24T02:18:05.368659
finish_reason: stop
---

6. Далее мы создадим новую модель, NewUser, которая наследуется от модели User; эта новая модель будет использоваться в качестве типа данных при регистрации нового пользователя. Модель User будет использоваться в качестве модели ответа, когда мы не хотим взаимодействовать с паролем, уменьшая объем работы, которую необходимо выполнить.

7. Наконец, давайте реализуем модель для входа пользователей в:

```python
class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": fastapi@packt.com,
                "password": "strong!!!",
                "events": []
            }
        }
```

Теперь, когда мы успешно реализовали наши модели, давайте реализуем маршруты в следующем разделе.