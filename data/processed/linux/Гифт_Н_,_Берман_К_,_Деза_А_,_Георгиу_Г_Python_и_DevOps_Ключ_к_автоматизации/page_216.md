---
source_image: page_216.png
page_number: 216
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.76
tokens: 7517
characters: 2008
timestamp: 2025-12-24T03:06:30.968767
finish_reason: stop
---

Prometheus отлично подходит для краткосрочных и часто меняющихся временных данных, в то время как Graphite лучше подходит для информации, собранной за большой промежуток времени. Оба предоставляют очень развитой язык запросов, но возможности Prometheus шире.

Отличная утилита для Python для отправки метрик в Prometheus — prometheus_client (https://oreil.ly/t9NtW), а если речь идет о веб-приложении, то этот клиент интегрирован с множеством веб-серверов Python, в частности Twisted, WSGI, Flask и даже Gunicorn. Помимо этого, он может экспортитьвать все данные для выдачи их в заданной конечной точке (вместо использования для этого отдельного экземпляра HTTP-сервера). Чтобы ваше веб-приложение выдавало их в конечной точке /metrics/, добавьте обработчик, вызывающий метод prometheus_client.generate_latest(), который вернет данные в формате, понятном синтаксическому анализатору Prometheus.

Создайте маленькое приложение Flask (сохраните его в виде файла web.py), чтобы самим попробовать, насколько прост в применении generate_latest(), не забыв перед этим установить пакет prometheus_client:

from flask import Response, Flask
import prometheus_client

app = Flask('prometheus-app')

@app.route('/metrics/')
def metrics():
    return Response(
        prometheus_client.generate_latest(),
        mimetype='text/plain; version=0.0.4; charset=utf-8'
    )

Запустите приложение с помощью предназначенного для разработки веб-сервера Flask:

$ FLASK_APP=web.py flask run
* Serving Flask app "web.py"
* Environment: production
  WARNING: This is a development server.
  Use a production WSGI server instead.
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [07/Jul/2019 10:16:20] "GET /metrics HTTP/1.1" 308 -
127.0.0.1 - - [07/Jul/2019 10:16:20] "GET /metrics/ HTTP/1.1" 200 -

Пока приложение работает, откройте веб-браузер и введите URL http://localhost:5000/metrics. При этом будет генерироваться информация, подходящая для сбора Prometheus, хотя ничего особо ценного в ней нет: