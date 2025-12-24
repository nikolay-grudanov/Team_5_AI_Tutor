---
source_image: page_721.png
page_number: 721
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.70
tokens: 11675
characters: 1598
timestamp: 2025-12-24T02:08:03.418934
finish_reason: stop
---

Глава 17: примеры, относящиеся к криптографии

return size

def main(workers=None):
    if workers:
        workers = int(workers)
    t0 = time.time()
    with futures.ProcessPoolExecutor(workers) as executor:
        actual_workers = executor._max_workers
        to_do = []
        for i in range(JOBS, 0, -1):
            size = SIZE + int(SIZE / JOBS * (i - JOBS/2))
            job = executor.submit(arcfour_test, size, KEY)
            to_do.append(job)

        for future in futures.as_completed(to_do):
            res = future.result()
            print('%.1f KB'.format(res/2**10))

        print(STATUS.format(actual_workers, time.time() - t0))

    if __name__ == '__main__':
        if len(sys.argv) == 2:
            workers = int(sys.argv[1])
        else:
            workers = None
    main(workers)

В примере A.8 реализован алгоритм шифрования RC4 на чистом Python.

Пример A.8. arcfour.py: код совместим с алгоритмом RC4

"""совместим с алгоритмом RC4"""

def arcfour(key, in_bytes, loops=20):

    kbox = bytearray(256) # create key box
    for i, car in enumerate(key): # copy key and vector
        kbox[i] = car
    j = len(key)
    for i in range(j, 256): # repeat until full
        kbox[i] = kbox[i-j]

    # [1] инициализируем sbox
    sbox = bytearray(range(256))

    # повторяем цикл перемешивания sbox, как рекомендовано в CipherSaber-2
    # http://ciphersaber.gurus.com/faq.html#cs2
    j = 0
    for k in range(loops):
        for i in range(256):
            j = (j + sbox[i] + kbox[i]) % 256
            sbox[i], sbox[j] = sbox[j], sbox[i]

    # главный цикл