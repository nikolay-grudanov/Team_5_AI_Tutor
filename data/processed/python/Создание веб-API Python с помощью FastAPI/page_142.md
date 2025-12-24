---
source_image: page_142.png
page_number: 142
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.46
tokens: 8264
characters: 1234
timestamp: 2025-12-24T02:19:32.284455
finish_reason: stop
---

Срок действия устанавливается равным часу с момента создания. Затем полезная нагрузка передается методу encode(), который принимает три параметра:

• Payload: Словарь, содержащий значения для кодирования.
• Key: Ключ, используемый для подписи полезной нагрузки.
• Algorithm: Алгоритм, используемый для подписи полезной нагрузки. По умолчанию и наиболее распространенным является алгоритм HS256.

Далее давайте создадим функцию для проверки подлинности токена, отправленного в наше приложение:

```python
def verify_access_token(token: str) -> dict:
    try:
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])

        expire = data.get("expires")

        if expire is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No access token supplied"
            )
        if datetime.utcnow() > datetime.utcfromtimestamp(expire):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Token expired!"
            )
        return data

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid token"
        )
```