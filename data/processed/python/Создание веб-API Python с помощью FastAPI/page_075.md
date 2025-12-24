---
source_image: page_075.png
page_number: 75
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.51
tokens: 8252
characters: 1071
timestamp: 2025-12-24T02:17:43.983665
finish_reason: stop
---

for todo in todo_list:
    if todo.id == todo_id:
        return templates.TemplateResponse(
            "todo.html", {
                "request": request,
                "todo": todo
            })
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
    )

В предыдущем блоке кода мы настроили Jinja для просмотра каталога templates для обслуживания шаблонов, переданных в templates. Метод TemplateResponse().

Метод для добавления задачи также был обновлен, чтобы включить зависимость от переданного ввода. Зависимости будут подробно обсуждаться в Главе 6 «Подключение к базе данных».

3. В model.py, добавьте выделенный код перед классом Config:

from typing import List, Optional

class Todo(BaseModel):
    id: Optional[int]
    item: str

    @classmethod
    def as_form(
        cls,
        item: str = Form(...)
    ):
        return cls(item=item)

Теперь, когда мы обновили наш код API, давайте напишем наши шаблоны. Мы начнем с написания базового шаблона home.html на следующем шаге.