---
source_image: page_226.png
page_number: 226
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.14
tokens: 6167
characters: 1166
timestamp: 2025-12-24T10:07:09.758119
finish_reason: stop
---

-e, --request-rate NUMBER Target number of requests per seconds. Infinite by default
-m, --method STRING HTTP method to use.
-d, --data STRING Data to send along with PUT or POST request.
-r, --request-generator STRING Path to module that exports getRequest function
-i, --report-interval NUMBER Frequency in seconds to report statistics. Default is 10.
-q, --quiet Supress display of progress count info.
-h, --help Show usage info

Типичное использование этой утилиты выглядит примерно так:

% nl.js -c 10 -n 1000 http://yhoo.it/XUdX3p

Данная команда запросит Yahoo.com 1000 раз по 10 запросов за один раз. Вот полученные мною результаты:

% nl.js -c 10 -n 1000 http://yahoo.com
http.createClient is deprecated. Use `http.request` instead.
Completed 910 requests
Completed 1000 requests
Server: yahoo.com:80
HTTP Method: GET
Document Path: /
Concurrency Level: 10
Number of requests: 1000
Body bytes transferred: 207549
Elapsed time (s): 11.19
Requests per second: 89.37
Mean time per request (ms): 111.23
Time per request standard deviation: 147.69
Percentages of requests served within a certain time (ms)
Min: 86
Avg: 111.2
50%: 94
95%: 113
99%: 1516
Max: 1638