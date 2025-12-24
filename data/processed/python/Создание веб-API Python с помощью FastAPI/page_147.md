---
source_image: page_147.png
page_number: 147
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.88
tokens: 8396
characters: 1247
timestamp: 2025-12-24T02:19:50.874351
finish_reason: stop
---

Возвращаемый ответ представляет собой токен доступа и тип токена:

```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoicmVhZGVyQHBhY2t0LmNvbSIsImV4cGlyZXMiOjE2NTA4Mjc0MjQuMDg2NDAxfQ.LY4i5EjIzlsKdfMyWKi7XH71LeDuVt3832hNfkQx8C8",
    "token_type": "Bearer"
}
```

Теперь, когда мы убедились, что маршрут работает должным образом, давайте обновим маршруты событий, чтобы разрешать только авторизованным пользователям события CREATE, UPDATE и DELETE.

Обновление маршрутов событий

Теперь, когда у нас есть наша аутентификация, давайте добавим зависимость аутентификации в функции маршрута POST, PUT и DELETE:

```python
from auth.authenticate import authenticate

async def create_event(body: Event, user: str = Depends(authenticate)) -> dict:
    ..

async def update_event(id: PydanticObjectId, body: EventUpdate, user: str = Depends(authenticate)) -> Event:
    ..

async def delete_event(id: PydanticObjectId, user: str = Depends(authenticate)) -> dict:
    ..
```

После внедрения зависимостей веб-сайт интерактивной документации автоматически обновляется для отображения защищенных маршрутов. Если мы войдем в http://0.0.0.0:8080/docs, мы увидим кнопку авторизации в правом верхнем углу и замки на маршрутах событий: