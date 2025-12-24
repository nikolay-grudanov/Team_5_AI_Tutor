---
source_image: page_143.png
page_number: 143
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.71
tokens: 8389
characters: 1621
timestamp: 2025-12-24T02:19:40.563065
finish_reason: stop
---

В предыдущем блоке кода функция принимает в качестве аргумента строку токена и выполняет несколько проверок в блоке try. Сначала функция проверяет срок действия токена. Если срок действия не указан, значит, токен не был предоставлен. Вторая проверка — валидность токена — генерируется исключение, информирующее пользователя об истечении срока действия токена. Если токен действителен, возвращается декодированная полезная нагрузка.

В блоке except для любой ошибки JWT выдается исключение неверного запроса.

Теперь, когда мы реализовали функции для создания и проверки токенов, отправляемых в приложение, давайте создадим функцию, которая проверяет аутентификацию пользователя и служит зависимостью.

Обработка аутентификации пользователя

Мы успешно внедрили компоненты для хеширования и сравнения паролей, а также компоненты для создания и декодирования JWT. Давайте реализуем функцию зависимости, которая будет внедрена в маршруты событий. Эта функция будет служить единственным источником правды для извлечения пользователя для активного сеанса.

В auth/authenticate.py добавьте следующее:

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from auth.jwt_handler import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/signin")

async def authenticate(token: str = Depends(oauth2_scheme)) -> str:
    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Sign in for access"
        )

    decoded_token = verify_access_token(token)
    return decoded_token["user"]
```