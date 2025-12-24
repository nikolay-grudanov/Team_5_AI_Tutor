---
source_image: page_711.png
page_number: 711
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.20
tokens: 11739
characters: 1803
timestamp: 2025-12-24T02:07:28.327951
finish_reason: stop
---

Глава 14: скрипт преобразования базы данных isis2json.py

sys.exit(1)

fmt = 'Selected Vector2d type: {.__name__}.{.__name__}'
print(fmt.format(module, module.Vector2d))

mem_init = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print('Creating {:,} Vector2d instances'.format(NUM_VECTORS))

vectors = [module.Vector2d(3.0, 4.0) for i in range(NUM_VECTORS)]

mem_final = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

print('Initial RAM usage: {:14,}'.format(mem_init))
print('Final RAM usage: {:14,}'.format(mem_final))

Глава 14: скрипт преобразования базы данных isis2json.py

В примере А.5 приведен скрипт isis2json.py, обсуждавшийся в разделе «Пример: генераторы в утилите преобразования базы данных» главы 14. В нем используется генераторная функция для ленивого преобразования баз данных CDS/ISIS в формат JSON с целью последующей загрузки в CouchDB или MongoDB.

Отметим, что этот скрипт написан на Python 2 и рассчитан на запуск под управлением CPython или Jython версий от 2.5 до 2.7, но не версии Python 3. При работе под управлением CPython он умеет читать только iso-файлы, а в случае Jython — также mst-файлы — благодаря библиотеке Bruma, которую можно скачать с GitHub по адресу https://github.com/fluentpython/isis2json. Рабочая документация находится в том же репозитории.

Пример А.5. isis2json.py: зависимости и документация доступны в репозитории fluentpython/isis2json на GitHub (https://github.com/fluentpython/isis2json)

# этот скрипт работает с Python или Jython (версии >=2.5 и <3)

import sys
import argparse
from uuid import uuid4
import os

try:
    import json
except ImportError:
    if os.name == 'java': # running Jython
        from com.xhaus.jyson import JysonCodec as json
    else:
        import simplejson as json

SKIP_INACTIVE = True
DEFAULT_QTY = 2**31