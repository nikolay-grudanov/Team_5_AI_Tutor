---
source_image: page_119.png
page_number: 119
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.22
tokens: 8185
characters: 931
timestamp: 2025-12-24T02:18:53.184431
finish_reason: stop
---

class Settings:
    name = "events"

4. Давайте создадим модель Pydantic для операций UPDATE:

class EventUpdate(BaseModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }

5. В model/users.py, замените содержимое модуля следующим:

from typing import Optional, List
from beanie import Document, Link

from pydantic import BaseModel, EmailStr

from models.events import Event