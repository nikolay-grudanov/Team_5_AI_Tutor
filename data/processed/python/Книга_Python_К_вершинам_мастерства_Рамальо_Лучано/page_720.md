---
source_image: page_720.png
page_number: 720
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 61.91
tokens: 11819
characters: 1923
timestamp: 2025-12-24T02:08:17.565896
finish_reason: stop
---

taxi: 2    Event(time=40, proc=2, action='drop off passenger')
taxi: 2    Event(time=44, proc=2, action='pick up passenger')
taxi: 1    Event(time=55, proc=1, action='pick up passenger')
taxi: 1    Event(time=59, proc=1, action='drop off passenger')
taxi: 0    Event(time=65, proc=0, action='drop off passenger')
taxi: 1    Event(time=65, proc=1, action='pick up passenger')
taxi: 2    Event(time=65, proc=2, action='drop off passenger')
taxi: 2    Event(time=72, proc=2, action='pick up passenger')
taxi: 0    Event(time=76, proc=0, action='going home')
taxi: 1    Event(time=80, proc=1, action='drop off passenger')
taxi: 1    Event(time=88, proc=1, action='pick up passenger')
taxi: 2    Event(time=95, proc=2, action='drop off passenger')
taxi: 2    Event(time=97, proc=2, action='pick up passenger')
taxi: 2    Event(time=98, proc=2, action='drop off passenger')
taxi: 1    Event(time=106, proc=1, action='drop off passenger')
taxi: 2    Event(time=109, proc=2, action='going home')
taxi: 1    Event(time=110, proc=1, action='going home')
*** end of events ***
# END TAXI_SAMPLE_RUN

Глава 17: примеры, относящиеся к криптографии

Эти скрипты использовались при демонстрации применения futures.ProcessPoolExecutor для запуска счетных задач.

Код в примере A.7 шифрует и дешифрирует массивы случайных байтов с помощью алгоритма RC4. Для его работы необходим модуль arcfour.py (пример A.8).

Пример A.7. arcfour_futures.py: пример futures.ProcessPoolExecutor

import sys
import time
from concurrent import futures
from random import randrange
from arcfour import arcfour

JOBS = 12
SIZE = 2**18

KEY = b"'Twas brillig, and the slithy toves\nDid gyre"
STATUS = '{} workers, elapsed time: {:.2f}s'

def arcfour_test(size, key):
    in_text = bytearray(ranrange(256) for i in range(size))
    cypher_text = arcfour(key, in_text)
    out_text = arcfour(key, cypher_text)
    assert in_text == out_text, 'Failed arcfour_test'