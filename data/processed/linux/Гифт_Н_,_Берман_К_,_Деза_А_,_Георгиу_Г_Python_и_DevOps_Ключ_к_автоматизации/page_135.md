---
source_image: page_135.png
page_number: 135
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.54
tokens: 7858
characters: 2205
timestamp: 2025-12-24T03:04:32.809306
finish_reason: stop
---

$ molotov -v -r 1 --processes 1 load_test.py
**** Molotov v1.6. Happy breaking! ****
Preparing 1 worker...
OK
AssertionError('unexpected redirect status: 302',)
    File ".venv/lib/python3.6/site-packages/molotov/worker.py", line 206, in step
        **scenario['kw'])
    File "load_test.py", line 12, in scenario_two
        assert redirect_status == 301, error
SUCCESSES: 0 | FAILURES: 1
*** Bye ***

Единственного запроса (флаг -r 1) оказалось достаточно для того, чтобы все завершилось неудачей. Необходимо модифицировать оператор контроля для проверки состояния 302 вместо 301. После этого поменяйте соотношение запросов POST на 80, чтобы в приложение Flask отправлялись и другие запросы (GET). В результате файл должен выглядеть следующим образом:

import molotov

@molotov.scenario()
async def scenario_one(session):
    async with session.get("http://localhost:5000/") as resp:
        assert resp.status == 200

@molotov.scenario(80)
async def scenario_two(session):
    resp = await session.post("http://localhost:5000", params={'q': 'devops'})
    redirect_status = resp.history[0].status
    error = "unexpected redirect status: %s" % redirect_status
    assert redirect_status == 302, error

Запустите load_test.py для выполнения десяти запросов, два с помощью метода GET, а остальные — с помощью POST:

127.0.0.1 - - [04/Sep/2019 12:10:54] "POST /?q=devops HTTP/1.1" 302 -
127.0.0.1 - - [04/Sep/2019 12:10:56] "POST /?q=devops HTTP/1.1" 302 -
127.0.0.1 - - [04/Sep/2019 12:10:57] "POST /?q=devops HTTP/1.1" 302 -
127.0.0.1 - - [04/Sep/2019 12:10:58] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [04/Sep/2019 12:10:58] "POST /?q=devops HTTP/1.1" 302 -
127.0.0.1 - - [04/Sep/2019 12:10:59] "POST /?q=devops HTTP/1.1" 302 -
127.0.0.1 - - [04/Sep/2019 12:11:00] "POST /?q=devops HTTP/1.1" 302 -
127.0.0.1 - - [04/Sep/2019 12:11:01] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [04/Sep/2019 12:11:01] "POST /?q=devops HTTP/1.1" 302 -
127.0.0.1 - - [04/Sep/2019 12:11:02] "POST /?q=devops HTTP/1.1" 302 -

Как видите, возможности molotov можно легко расширять с помощью чистого Python-кода и приспосабливать к прочим, более сложным потребностям. Эти примеры — лишь малая толика того, на что способна эта утилита.