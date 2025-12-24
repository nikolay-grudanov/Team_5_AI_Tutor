---
source_image: page_236.png
page_number: 236
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.85
tokens: 7786
characters: 2644
timestamp: 2025-12-24T03:07:17.432605
finish_reason: stop
---

И хотя Kibana — это инструментальная панель, а стек ELK не основан на Python, эти сервисы настолько хорошо интегрированы, что демонстрируют, что такое по-настоящему хорошая архитектура платформы. После первого запуска Kibana начнет искать запущенный на машине экземпляр Elasticsearch, просматривая вывод записей журналов. Таково поведение по умолчанию ее плагина Elasticsearch без каких-либо дополнительных настроек. Все прозрачно, из сообщений понятно, что плагин был инициализирован и смог получить доступ к Elasticsearch:

{
    "type": "log",
    "@timestamp": "2019-08-09T12:34:43Z",
    "tags": ["status", "plugin:elasticsearch@7.3.0", "info"],
    "pid": 7885,
    "state": "yellow",
    "message": "Status changed from uninitialized to yellow",
    "prevState": "uninitialized",
    "prevMsg": "uninitialized"
}

{
    "type": "log",
    "@timestamp": "2019-08-09T12:34:45Z",
    "tags": ["status", "plugin:elasticsearch@7.3.0", "info"],
    "pid": 7885,
    "state": "green",
    "message": "Status changed from yellow to green - Ready",
    "prevState": "yellow",
    "prevMsg": "Waiting for Elasticsearch"
}

Если поменять настройки, указав неправильный порт, из журналов становится совершенно ясно, что ничего само по себе не работает:

{
    "type": "log",
    "@timestamp": "2019-08-09T12:59:27Z",
    "tags": ["error", "elasticsearch", "data"],
    "pid": 8022,
    "message": "Request error, retrying
      GET http://localhost:9199/_xpack => connect ECONNREFUSED 127.0.0.1:9199"
}

{
    "type": "log",
    "@timestamp": "2019-08-09T12:59:27Z",
    "tags": ["warning", "elasticsearch", "data"],
    "pid": 8022,
    "message": "Unable to revive connection: http://localhost:9199/"
}

После запуска Kibana вместе с Elasticsearch (на правильном порте!), Filebeat и Logstash вы увидите полнофункциональную инструментальную панель и множество возможных опций (рис. 7.1).

Выполните запрос к локальному экземпляру Nginx, чтобы в журнале появились новые записи, и запустите обработку данных. В этом примере мы задействуем утилиту Apache Benchmarking (ab), но вы можете использовать просто браузер или сделать запрос напрямую с помощью curl:

$ ab -c 8 -n 50 http://localhost/
This is ApacheBench, Version 2.3 <$Revision: 1430300 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done

Не настраивая далее Kibana, перейдите на URL/порт по умолчанию, на котором она работает, — http://localhost:5601/. Представление по умолчанию предлагает множество дополнительных опций. В разделе discover вы увидите