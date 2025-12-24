---
source_image: page_133.png
page_number: 133
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.28
tokens: 7525
characters: 2022
timestamp: 2025-12-24T03:04:20.382681
finish_reason: stop
---

Подобная информация и способ ее представления умопомрачительны. С одного взгляда можно понять, отказывает ли находящийся в промышленной эксплуатации сервер в соединениях (по полю Failed requests) и каковы средние показатели. В данном случае использовались запросы типа GET, но утилита ab позволяет задействовать и другие HTTP-«глаголы», например POST, и даже выполнять HEAD-запросы. Подобные утилиты следует применять осмотрительно, ведь с их помощью легко можно нагрузить сервер сильнее допустимого. Далее приведены более реалистичные показатели используемого в действительности HTTP-сервиса:

...
Benchmarking prod1.ceph.internal (be patient)

Server Software:        nginx
Server Hostname:         prod1.ceph.internal
Server Port:             443
SSL/TLS Protocol:        TLSv1.2,ECDHE-RSA-AES256-GCM-SHA384,2048,256
Server Temp Key:        ECDH P-256 256 bits
TLS Server Name:        prod1.ceph.internal

Complete requests:      200
Failed requests:        0
Total transferred:     212600 bytes
HTML transferred:       175000 bytes
Requests per second:   83.94 [#/sec] (mean)
Time per request:      1191.324 [ms] (mean)
Time per request:      11.913 [ms] (mean, across all concurrent requests)
Transfer rate:         87.14 [Kbytes/sec] received
...

Теперь показатели совсем другие, ab обращается к сервису с подключенным SSL, поэтому выводит информацию о доступных протоколах. 83 запроса в секунду представляется не слишком хорошими характеристиками, но речь идет о сервере API, генерирующем JSON, одномоментная нагрузка которого (наподобие только что сгенерированной) обычно не слишком высока.

Нагрузочное тестирование с помощью molotov

Проект Molotov (https://molotov.readthedocs.io) — интересное решение в сфере нагрузочного тестирования. Часть его возможностей аналогична возможностям Apache Benchmark, но это проект на языке Python, благодаря чему вы можете писать сценарии на Python и использовать модуль asyncio.

Вот так выглядит простейший пример применения molotov:

import molotov

@molotov.scenario(100)