---
source_image: page_088.png
page_number: 88
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.04
tokens: 8283
characters: 1167
timestamp: 2025-12-24T02:18:11.678075
finish_reason: stop
---

Наша модель событий в первом блоке кода содержит пять полей:

▪ Название события
▪ Ссылка на баннер изображения события
▪ Описание события
▪ Теги событий для группировки
▪ Место проведения

Во втором блоке кода мы определяем пример данных события. Это направлено на то, чтобы направлять нас при создании нового события из нашего API.

4. Теперь, когда мы определили нашу модель событий, давайте определим модель User:

```python
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event

class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]]
```

Наша модель пользователя, определенная ранее, содержит следующие поля:

▪ Электронная почта пользователя
▪ Пароль пользователя
▪ Список событий, созданный пользователем, который по умолчанию пуст

5. Теперь, когда мы определили нашу модель User, давайте создадим пример, показывающий, как хранятся и устанавливаются пользовательские данные:

```python
class Config:
    schema_extra = {
        "example": {
            "email": fastapi@packt.com,
            "username": "strong!!!",
            "events": [],
        }
    }
```