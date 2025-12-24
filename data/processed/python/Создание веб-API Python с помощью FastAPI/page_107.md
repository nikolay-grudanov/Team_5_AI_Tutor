---
source_image: page_107.png
page_number: 107
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.11
tokens: 8149
characters: 700
timestamp: 2025-12-24T02:18:29.908817
finish_reason: stop
---

4. Далее давайте проинструктируем наше приложение создавать базу данных при запуске. Обновите main.py следующим кодом:

```python
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from database.connection import conn

from routes.users import user_router
from routes.events import event_router

import uvicorn

app = FastAPI()

# Register routes

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

@app.on_event("startup")
def on_startup():
    conn()

@app.get("/")
async def home():
    return RedirectResponse(url="/event/")

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
```