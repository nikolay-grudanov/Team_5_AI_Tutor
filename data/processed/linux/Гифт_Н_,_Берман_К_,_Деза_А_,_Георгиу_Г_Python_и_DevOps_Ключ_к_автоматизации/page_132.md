---
source_image: page_132.png
page_number: 132
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.91
tokens: 7507
characters: 1788
timestamp: 2025-12-24T03:04:19.958017
finish_reason: stop
---

Оценка быстродействия HTTP с помощью Apache Benchmark (ab)

Мы просто обожаем нагружать серверы, с которыми работаем, заданиями, чтобы убедиться в правильной обработке ими нагрузки, особенно перед их переводом в промышленную эксплуатацию. Иногда мы даже пытаемся искусственно вызвать какое-нибудь редкое состояние гонки, возможное при высокой нагрузке. Утилита Apache Benchmark (ab в командной строке) — одна из тех крошечных утилит, которым требуется всего несколько флагов, чтобы добиться нужных результатов.

Следующая команда выполняет по 100 запросов, всего 10 000, к локальной машине, на которой запущен Nginx:

$ ab -c 100 -n 10000 http://localhost/

Подобный тест — довольно жестоко по отношению к реальной системе, но речь идет всего лишь о локальном сервере, а запросы представляют собой просто HTTP GET. ab выводит очень подробный отчет, который выглядит следующим образом (мы немного сократили его):

Benchmarking localhost (be patient)
...
Completed 10000 requests
Finished 10000 requests

Server Software:        nginx/1.15.9
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        612 bytes

Concurrency Level:      100
Time taken for tests:   0.624 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      8540000 bytes
HTML transferred:       6120000 bytes
Requests per second:    16015.37 [#/sec] (mean)
Time per request:       6.244 [ms] (mean)
Time per request:       0.062 [ms] (mean, across all concurrent requests)
Transfer rate:          13356.57 [Kbytes/sec] received

Connection Times (ms)
    min  mean[+/-sd] median   max
Connect:     0    3   0.6     3     5
Processing:  0    4   0.8     3     8
Waiting:     0    3   0.8     3     6
Total:       0    6   1.0     6     9