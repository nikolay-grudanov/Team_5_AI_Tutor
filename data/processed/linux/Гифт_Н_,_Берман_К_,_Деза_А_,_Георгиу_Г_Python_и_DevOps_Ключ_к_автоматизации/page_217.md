---
source_image: page_217.png
page_number: 217
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.49
tokens: 7398
characters: 1840
timestamp: 2025-12-24T03:06:23.896598
finish_reason: stop
---

...
# HELP process_cpu_seconds_total Total user and system CPU time in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 0.27
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 6.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1024.0

Большинство предназначенных для промышленной эксплуатации веб-серверов, таких как Nginx и Apache, могут генерировать исчерпывающие метрики времени отклика и ожидания. Например, для добавления подобного типа данных в приложение Flask отлично подойдет промежуточное ПО, в котором фиксируются все запросы. Приложения обычно выполняют в запросах и другие интересные вещи, так что добавим еще две конечные точки — одну со счетчиком, а другую с таймером. Эти конечные точки будут генерировать метрики, в дальнейшем обрабатываемые библиотекой prometheus_client и выдаваемые при запросе к конечной точке /metrics/ по HTTP.

Добавление счетчика к нашему маленькому приложению требует нескольких небольших изменений. Создайте новую конечную точку:

@app.route('/')
def index():
    return '<h1>Development Prometheus-backed Flask App</h1>'

Теперь опишем объект Counter. Добавьте название счетчика (requests), короткое его описание (Application Request Count) и по крайней мере одну удобную метку (например, endpoint), которая поможет определить источник этого счетчика:

from prometheus_client import Counter

REQUESTS = Counter(
    'requests', 'Application Request Count',
    ['endpoint']
)

@app.route('/')
def index():
    REQUESTS.labels(endpoint='/').inc()
    return '<h1>Development Prometheus-backed Flask App</h1>'

После описания счетчика REQUESTS включите его в функцию index(), перезапустите приложение и выполните несколько запросов. При выполнении запросов