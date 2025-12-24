---
source_image: page_218.png
page_number: 218
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.40
tokens: 7399
characters: 1753
timestamp: 2025-12-24T03:06:23.953032
finish_reason: stop
---

к конечной точке /metrics/ в выводимой информации будут отражены выполненные нами действия:

...
# HELP requests_total Application Request Count
# TYPE requests_total counter
requests_total{endpoint="/"} 3.0
# TYPE requests_created gauge
requests_created{endpoint="/"} 1.562512871203272e+09

Теперь добавьте объект Histogram для захвата более подробной информации о конечной точке, которая иногда отвечает с некоторым запозданием. Код моделирует эту ситуацию посредством приостановки выполнения на случайно выбранный промежуток времени. Как и в функции index, необходима новая конечная точка, в которой бы использовался объект Histogram:

from prometheus_client import Histogram

TIMER = Histogram(
    'slow', 'Slow Requests',
    ['endpoint']
)

В моделируемой нами ресурсоемкой операции задействуется функция, отслеживающая время ее начала и окончания, а затем передающая эту информацию в объект Histogram:

import time
import random

@app.route('/database/')
def database():
    with TIMER.labels('/database').time():
        # Моделируем время отклика базы данных
        sleep(random.uniform(1, 3))
    return '<h1>Completed expensive database operation</h1>'

Нам нужны еще два модуля, time и random, для вычисления передаваемого в гистограмму значения времени и моделирования производимой в базе данных ресурсоемкой операции. Запустите приложение еще раз, обратитесь к конечной точке /database/ — и увидите, как при опросе конечной точки /metrics/ начнут генерироваться данные. При этом должны появиться несколько записей, соответствующих измерению длительностей выполнения смоделированной операции:

# HELP slow Slow Requests
# TYPE slow histogram
slow_bucket{endpoint="/database",le="0.005"} 0.0
slow_bucket{endpoint="/database",le="0.01"} 0.0