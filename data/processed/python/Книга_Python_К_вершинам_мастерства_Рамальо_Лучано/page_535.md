---
source_image: page_535.png
page_number: 535
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.48
tokens: 11729
characters: 1938
timestamp: 2025-12-24T01:59:39.843383
finish_reason: stop
---

Пример: три способа загрузки из веба

Пример 17.3. flags_threadpool.py: многопоточный скрипт загрузки с применением класса futures.ThreadPoolExecutor

from concurrent import futures

from flags import save_flag, get_flag, show, main

MAX_WORKERS = 20

def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))

    return len(list(res))

if __name__ == '__main__':
    main(download_many)

1 Используем некоторые функции из модуля flags (пример 17.2).
2 Максимальное число потоков в объекте ThreadPoolExecutor.
3 Функция, загружающая одно изображение, ее будет исполнять каждый поток.
4 Устанавливаем количество рабочих потоков: используем минимум из наибольшего допустимого числа потоков (MAX_WORKERS) и фактического числа подлежащих обработке элементов, чтобы не создавать лишних потоков.
5 Создаем экземпляр ThreadPoolExecutor с таким числом рабочих потоков; метод executor.__exit__ вызовет executor.shutdown(wait=True), который блокирует выполнение программы до завершения всех потоков.
6 Метод map похож на встроенную функцию map с тем исключением, что функция download_one параллельно вызывается из нескольких потоков; он возвращает генератор, который можно обойти для получения значений, возвращенных каждой функцией.
7 Возвращаем количество полученных результатов. Если функция в каком-то потоке возбудила исключение, то оно возникнет в этом месте, когда неявный вызов next() попытается получить соответствующее значение от итератора.
8 Вызываем функцию main из модуля flags, передавая ей усовершенствованную версию download_many.

Отметим, что функция download_one из примера 17.3, по сути дела, является телом цикла for в функции download_many из примера 17.2. Это типичный рефак-