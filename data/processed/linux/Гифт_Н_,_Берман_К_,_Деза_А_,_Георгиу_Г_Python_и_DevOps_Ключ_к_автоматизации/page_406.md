---
source_image: page_406.png
page_number: 406
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.04
tokens: 7350
characters: 1537
timestamp: 2025-12-24T03:11:35.448978
finish_reason: stop
---

Content root path: python-simple-http-endpoint
Now listening on: http://0.0.0.0:7071
Application started. Press Ctrl+C to shut down.
[8/24/19 12:21:35 AM] INFO: Successfully opened gRPC channel to 127.0.0.1:53952
Http Functions:
    currentTime: [GET,POST] http://localhost:7071/api/currentTime

Проверьте ее работу с другого терминала:

$ curl http://127.0.0.1:7071/api/currentTime?name=joe
Hello joe!%

Модифицируйте HTTP-обработчик в файле currentTime/init.py, включив в его ответ текущее время:

import datetime

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
    else:
        name = req_body.get('name')

    current_time = datetime.datetime.now().time()
    if name:
        return func.HttpResponse(f"Hello {name}, the current time is {current_time}!")
    else:
        return func.HttpResponse(
            "Please pass a name on the query string or in the request body",
            status_code=400
        )

Проверьте работу обновленной функции с помощью curl:

$ curl http://127.0.0.1:7071/api/currentTime?name=joe
Hello joe, the current time is 17:26:54.256060!%

Установите CLI Azure с помощью системы управления пакетами pip:

$ pip install azure.cli

Создайте в интерактивном режиме с помощью утилиты az командной строки Azure Resource Group, Storage Account и Function App. Этот режим позволяет