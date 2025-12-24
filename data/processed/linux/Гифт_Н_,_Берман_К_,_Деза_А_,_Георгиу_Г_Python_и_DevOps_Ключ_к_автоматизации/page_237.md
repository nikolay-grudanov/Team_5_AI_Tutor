---
source_image: page_237.png
page_number: 237
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.12
tokens: 7251
characters: 915
timestamp: 2025-12-24T03:06:52.843494
finish_reason: stop
---

Рис. 7.1. Стартовая страница инструментальной панели Kibana

всю структурированную информацию по запросам. Вот пример доступного в Kibana (получающего данные из Elasticsearch) фрагмента в формате JSON, обработанного Logstash:

...
    "input": {
        "type": "log"
    },
    "auth": "-",
    "ident": "-",
    "request": "/",
    "response": "200",
    "@timestamp": "2019-08-08T21:03:46.513Z",
    "verb": "GET",
    "@version": "1",
    "referrer": "\"-\"",
    "httpversion": "1.1",
    "message": "::1 - - [08/Aug/2019:21:03:45 +0000] \"GET / HTTP/1.1\" 200",
    "clientip": "::1",
    "geoip": {},
    "ecs": {
        "version": "1.0.1"
    },
    "host": {
        "os": {
            "codename": "Core",
            "name": "CentOS Linux",
            "version": "7 (Core)",
            "platform": "centos",
            "kernel": "3.10.0-957.1.3.el7.x86_64",
            "family": "redhat"
        },
