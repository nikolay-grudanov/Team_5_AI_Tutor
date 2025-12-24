---
source_image: page_151.png
page_number: 151
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.26
tokens: 8280
characters: 1156
timestamp: 2025-12-24T02:19:50.842346
finish_reason: stop
---

"image": "https://linktomyimage.com/image.png",
"description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
"tags": [
    "python",
    "fastapi",
    "book",
    "launch"
],
"location": "Google Meet"
}

Вот ответ:

$ {
    "detail": "Not authenticated"
}

Теперь, когда мы успешно защитили маршруты, давайте обновим защищенные маршруты следующим образом:

• Маршрут POST: добавление созданного события в список событий, принадлежащих пользователю.
• Маршрут UPDATE: измените маршрут, чтобы можно было обновить только событие, созданное пользователем.
• Маршрут DELETE: измените маршрут, чтобы удалить можно было только событие, созданное пользователем.

В предыдущем разделе мы успешно внедрили зависимости аутентификации в наши операции маршрутизации. Чтобы легко идентифицировать события и предотвратить удаление пользователем события другого пользователя, мы обновим класс документа события, а также маршруты.

Обновление класса документа события и маршрутов

Добавьте поле creator в класс документа Event в models/events.py:

class Event(Document):
    creator: Optional[str]