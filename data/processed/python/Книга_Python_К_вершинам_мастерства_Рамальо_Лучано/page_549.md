---
source_image: page_549.png
page_number: 549
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.96
tokens: 11823
characters: 1938
timestamp: 2025-12-24T02:00:21.913130
finish_reason: stop
---

Загрузка с индикацией хода выполнения и обработкой ошибок

в файле 17-futures/countries/README.rst (http://bit.ly/1Jlsg2L)
в репозитории кода на GitHub (https://github.com/fluentpython/example-code).

По умолчанию каждый flags2-скрипт загружает флаги 20 стран с самым большим населением с локального сервера (http://localhost:8001/flags), открывая определенное количество соединений по умолчанию, для каждого скрипта свое. В примере 17.9 показан результат прогона скрипта flags2_sequential.py, когда все параметры заданы по умолчанию.

Пример 17.9. Прогон flags2_sequential.py с параметрами по умолчанию: сервер LOCAL, флаги 20 самых густонаселенных стран, 1 соединение

$ python3 flags2_sequential.py
LOCAL site: http://localhost:8001/flags
Searching for 20 flags: from BD to VN
1 concurrent connection will be used.
----------------------
20 flags downloaded.
Elapsed time: 0.10s

Задать набор загружаемых флагов можно несколькими способами. В примере 17.10 показано, как загрузить с сервера DELAY флаги всех стран, коды которых начинаются с букв А, В, С,

$ python3 flags2_threadpool.py -s DELAY a b c
DELAY site: http://localhost:8002/flags
Searching for 78 flags: from AA to CZ
30 concurrent connections will be used.
----------------------
43 flags downloaded.
35 not found.
Elapsed time: 1.72s

Независимо от способа задания кодов стран количество загружаемых флагов можно ограничить с помощью параметра -1/--limit. В примере 17.11 показано, как выполнить ровно 100 запросов с помощью комбинации параметра -a, запрашивающего все флаги, и параметра -1 100.

Пример 17.11. Прогон flags2_asyncio.py с загрузкой 100 флагов (-al 100) с сервера ERROR, 100 одновременных соединений (-m 100)

$ python3 flags2_asyncio.py -s ERROR -al 100 -m 100
ERROR site: http://localhost:8003/flags
Searching for 100 flags: from AD to LK
100 concurrent connections will be used.
----------------------
73 flags downloaded.
27 errors.
Elapsed time: 0.64s