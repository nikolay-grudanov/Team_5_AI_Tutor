---
source_image: page_030.png
page_number: 30
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.87
tokens: 8436
characters: 1543
timestamp: 2025-12-24T02:16:54.389239
finish_reason: stop
---

В предыдущей команде, uvicorn принимает следующие аргументы:

• file:instance: Файл, содержащий экземпляр FastAPI и переменную имени, содержащую экземпляр FastAPI..
• --port PORT: Порт, на котором будет обслуживаться приложение.
• --reload: Необязательный аргумент, включенный для перезапуска приложения при каждом изменении файла.

Команда возвращает следующий вывод:

(venv) → todos uvicorn api:app --port 8080 --reload
INFO:    Will watch for changes in these directories: ['/Users/youngestdev/Documents/todos']
INFO:    Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
INFO:    Started reloader process [3982] using statreload
INFO:    Started server process [3984]
INFO:    Waiting for application startup.
INFO:    Application startup complete.

Следующий шаг — протестировать приложение, отправив запрос GET в API. В новом терминале отправьте запрос GET с помощью curl следующим образом:

$ curl http://0.0.0.0:8080/

Ответ от приложения в консоле будет следующим:

{ "message": "Hello World" }

Резюме

В этой главе мы узнали, как установить инструменты, необходимые для настройки нашей среды разработки. Мы также создали простой API в качестве введения в FastAPI и научились создавать маршрут в процессе.

В следующей главе вы познакомитесь с маршрутизацией в FastAPI. Во-первых, вы познакомитесь с процессом построения моделей для проверки полезной нагрузки запросов и ответов с помощью Pydantic. Затем вы узнаете о параметрах пути и запроса, а также о теле запроса и, наконец, узнаете, как создать приложение CRUD todo.