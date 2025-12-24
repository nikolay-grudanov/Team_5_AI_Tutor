---
source_image: page_552.png
page_number: 552
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.26
tokens: 11680
characters: 1839
timestamp: 2025-12-24T02:00:22.257890
finish_reason: stop
---

6 Относящиеся к HTTP исключения, возбужденные функцией get_flag и не обработанные в download_one, обрабатываются здесь.
7 Прочие относящиеся к сети исключения обрабатываются здесь. Все остальные исключения аварийно завершают скрипт, потому что в функции flags2_common.main, из которой вызывается download_many, нет блока try/except.
8 Если исключение не вышло за пределы download_one, то из именованного кортежа HTTPStatus, возвращенного этой функцией, извлекается значение status.
9 Если произошла ошибка, устанавливаем соответствующее значение status.
10 Увеличиваем счетчик, используя значение из перечисления HTTPStatus в качестве ключа.
11 При работе в режиме подробной информации отображаем сообщение об ошибке для текущего кода страны, если таковое имеется.
12 Возвращаем counter, чтобы функция main могла вывести финальный отчет.

Теперь рассмотрим переработанный пример с пулом потоков, flags2_threadpool.py.

Использование futures.as_completed

Чтобы включить индикатор хода выполнения и обработку ошибок, мы используем в скрипте flags2_threadpool.py класс futures.ThreadPoolExecutor совместно с уже встречавшейся функцией futures.as_completed. В примере 17.14 приведен полный код flags2_threadpool.py. Заново реализована только функция download_many; все остальные функции заимствованы из модулей flags2_common и flags2_sequential.

Пример 17.14. flags2_threadpool.py: полный исходный код

import collections
from concurrent import futures
import requests
import tqdm

from flags2_common import main, HTTPStatus
from flags2_sequential import download_one

DEFAULT_CONCUR_REQ = 30
MAX_CONCUR_REQ = 1000

def download_many(cc_list, base_url, verbose, concur_req):
    counter = collections.Counter()
    with futures.ThreadPoolExecutor(max_workers=concur_req) as executor:
        to_do_map = {}
        for cc in sorted(cc_list):