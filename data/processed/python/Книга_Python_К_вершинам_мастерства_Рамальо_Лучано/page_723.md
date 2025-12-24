---
source_image: page_723.png
page_number: 723
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.63
tokens: 11532
characters: 1283
timestamp: 2025-12-24T02:07:52.950457
finish_reason: stop
---

Глава 17: примеры HTTP-клиентов из серии flags2

algo = hashlib.new('sha256')
algo.update(data)
return algo.hexdigest()

def main(workers=None):
    if workers:
        workers = int(workers)
    t0 = time.time()

    with futures.ProcessPoolExecutor(workers) as executor:
        actual_workers = executor._max_workers
        to_do = (executor.submit(sha, SIZE) for i in range(JOBS))
        for future in futures.as_completed(to_do):
            res = future.result()
            print(res)

    print(STATUS.format(actual_workers, time.time() - t0))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        workers = int(sys.argv[1])
    else:
        workers = None
    main(workers)

Глава 17: примеры HTTP-клиентов из серии flags2

Во всех примерах flags2-скриптов из раздела «Загрузка с индикацией хода выполнения и обработкой ошибок» главы 17 используются функции из модуля flags2_common.py (пример А.10).

Пример А.10. flags2_common.py

"""Служебные функции для второй серии примеров загрузки флагов.
"""

import os
import time
import sys
import string
import argparse
from collections import namedtuple
from enum import Enum

Result = namedtuple('Result', 'status data')

HTTPStatus = Enum('Status', 'ok not_found error')

POP20_CC = ('CN IN US ID BR PK NG BD RU JP'