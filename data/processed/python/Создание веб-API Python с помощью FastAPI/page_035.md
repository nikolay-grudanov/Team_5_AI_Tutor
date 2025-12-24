---
source_image: page_035.png
page_number: 35
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.32
tokens: 8294
characters: 1083
timestamp: 2025-12-24T02:16:41.645350
finish_reason: stop
---

Включите todo_router в приложение FastAPI, используя метод include_router из экземпляра FastAPI:

```python
from fastapi import FastAPI
from todo import todo_router

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Hello World"
    }

app.include_router(todo_router)
```

Когда все на месте, запустите приложение с вашего терминала:

(venv)$ uvicorn api:app --port 8000 --reload

Предыдущая команда запускает наше приложение и дает нам журнал процессов нашего приложения в реальном времени:

(venv) → todos git:(main) ✗ uvicorn api:app --port 8000 --reload
INFO: Will watch for changes in these directories: ['/Users/youngestdev/Work/Building-Web-APIs-with-FastAPI-and-Python/ch02/todos']
INFO: uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO: Started reloader process [4732] using statreload
INFO: Started server process [4734]
INFO: Waiting for application startup.
INFO: Application startup complete.

Следующий шаг — протестировать приложение, отправив запрос GET с помощью curl:

(venv)$ curl http://0.0.0.0:8080/