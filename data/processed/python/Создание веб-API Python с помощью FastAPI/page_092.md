---
source_image: page_092.png
page_number: 92
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.64
tokens: 8437
characters: 1535
timestamp: 2025-12-24T02:18:26.710401
finish_reason: stop
---

В наших маршрутах мы храним пароли в чистом виде без какого-либо шифрования. Это используется только в демонстрационных целях и является неправильной практикой в разработке программного обеспечения в целом. Надлежащие механизмы хранения, такие как шифрование, будут обсуждаться в Главе 6 Подключение к базе данных, где наше приложение переместится из базы данных в приложении в реальную базу данных.

3. Теперь, когда мы определили маршруты для пользовательских операций, давайте зарегистрируем их в main.py и запустим наше приложение. Давайте начнем с импорта наших библиотек и определения пользовательских маршрутов:

```python
from fastapi import FastAPI
from routes.user import user_router

import uvicorn
```

4. Далее создадим экземпляр FastAPI и зарегистрируем маршрут и приложение:

```python
app = FastAPI()

# Register routes

app.include_router(user_router, prefix="/user")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
```

В этом блоке кода мы создали экземпляр FastAPI и зарегистрировали маршрут.

5. Затем мы используем метод uvicorn.run() для запуска нашего приложения на порту 8080 и устанавливаем для перезагрузки значение True. В терминале запустите приложение:

```bash
(venv)$ python main.py
INFO:     Will watch for changes in these directories:
['/Users/youngestdev/Work/Building-Web-APIs-with-FastAPI-and-Python/ch05/planner']
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
INFO:     Started reloader process [6547] using statreload
```