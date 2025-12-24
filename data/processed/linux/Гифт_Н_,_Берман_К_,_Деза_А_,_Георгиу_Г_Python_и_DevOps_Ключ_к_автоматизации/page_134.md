---
source_image: page_134.png
page_number: 134
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.80
tokens: 7447
characters: 1919
timestamp: 2025-12-24T03:04:17.043323
finish_reason: stop
---

async def scenario_one(session):
    async with session.get("http://localhost:5000") as resp:
        assert resp.status == 200

Сохраните этот код в виде файла load_test.py, создайте маленькое приложение Flask для обработки запросов GET и POST по основному URL и сохраните его в виде файла small.py:

from flask import Flask, redirect, request

app = Flask('basic app')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect('https://www.google.com/search?q=%s' % request.args['q'])
    else:
        return '<h1>GET request from Flask!</h1>'

Запустите приложение Flask с помощью команды FLASK_APP=small.py flask run, а затем запустите molotov, передав ему созданный ранее файл load_test.py:

$ molotov -v -r 100 load_test.py
**** Molotov v1.6. Happy breaking! ****
Preparing 1 worker...
OK
SUCCESSES: 100 | FAILURES: 0 WORKERS: 0
*** Bye ***

В результате в одном процессе-исполнителе будет выполнено 100 запросов к локальному экземпляру Flask. Подлинные возможности этой утилиты раскрываются при большем объеме выполняемых в каждом запросе действий. В ней применяются подходы, аналогичные модульному тестированию, в частности, созданию тестовой среды и ее использованию с последующей очисткой ресурсов, и даже код, способный реагировать на определенные события. А поскольку наше маленькое приложение Flask может обрабатывать запросы POST, перенаправляемые на поиск Google, добавим еще один вариант поведения в файл load_test.py_. На этот раз пусть 100 % запросов будут типа POST:

@molotov.scenario(100)
async def scenario_post(session):
    resp = await session.post("http://localhost:5000", params={'q': 'devops'})
    redirect_status = resp.history[0].status
    error = "unexpected redirect status: %s" % redirect_status
    assert redirect_status == 301, error

Запустим этот новый вариант для выполнения одного-единственного запроса и увидим следующее: