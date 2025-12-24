---
source_image: page_722.png
page_number: 722
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.00
tokens: 11603
characters: 1206
timestamp: 2025-12-24T02:07:56.777311
finish_reason: stop
---

i = 0
j = 0
out_bytes = bytearray()

for car in in_bytes:
    i = (i + 1) % 256
    # [2] тасуем sbox
    j = (j + sbox[i]) % 256
    sbox[i], sbox[j] = sbox[j], sbox[i]
    # [3] вычисляем t
    t = (sbox[i] + sbox[j]) % 256
    k = sbox[t]
    car = car ^ k
    out_bytes.append(car)

return out_bytes

def test():
    from time import time
    clear = bytearray(b'1234567890' * 100000)
    t0 = time()
    cipher = arcfour(b'key', clear)
    print('elapsed time: %.2fs' % (time() - t0))
    result = arcfour(b'key', cipher)
    assert result == clear, '%r != %r' % (result, clear)
    print('elapsed time: %.2fs' % (time() - t0))
    print('OK')

if __name__ == '__main__':
    test()

В примере A.9 алгоритм хэширования SHA-256 применяется к массивам случайных байтов. Используется модуль hashlib из стандартной библиотеки, который, в свою очередь, основан на библиотеке OpenSSL, написанной на C.

Пример A.9. sha_futures.py: пример futures.ProcessPoolExecutor

import sys
import time
import hashlib

from concurrent import futures
from random import randrange

JOBS = 12
SIZE = 2**20
STATUS = '{} workers, elapsed time: {:.2f}s'

def sha(size):
    data = bytearray(ranrange(256) for i in range(size))