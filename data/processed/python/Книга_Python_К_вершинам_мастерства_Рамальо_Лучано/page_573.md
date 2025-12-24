---
source_image: page_573.png
page_number: 573
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.82
tokens: 11736
characters: 1887
timestamp: 2025-12-24T02:01:28.315152
finish_reason: stop
---

Загрузка с применением asyncio и aiohttp

from flags import BASE_URL, save_flag, show, main

@asyncio.coroutine
def get_flag(cc):
    url = '{}/{}{}.gif'.format(BASE_URL, cc=cc.lower())
    resp = yield from aiohttp.request('GET', url)
    image = yield from resp.read()
    return image

@asyncio.coroutine
def download_one(cc):
    image = yield from get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in sorted(cc_list)]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()
    return len(res)

if __name__ == '__main__':
    main(download_many)

1 Модуль aiohttp необходимо устанавливать, он не входит в стандартную библиотеку.
2 Повторно используем функции из модуля flags (пример 17.2).
3 Сопрограммы следует снабжать декоратором @asyncio.coroutine.
4 Блокирующие операции реализованы в виде сопрограмм, а наш код делегирует им работу с помощью yield from, поэтому они работают асинхронно.
5 Чтение содержимого ответов — отдельная асинхронная операция.
6 download_one должна быть сопрограммой, потому что в ней используется yield from.
7 Единственное отличие от последовательной реализации download_one — слова yield from в этой строчке; все остальное ничуть не изменилось.
8 Получаем ссылку на внутреннюю реализацию цикла обработки событий.
9 Строим список объектов-генераторов, вызывая функцию download_one по одному разу для каждого загружаемого флага.
10 Несмотря на свое имя, wait — неблокирующая функция. Это сопрограмма, которая завершается, когда завершатся все переданные ей сопрограммы (таково поведение wait по умолчанию, см. объяснение после примера).
11 Выполняем цикл обработки событий, пока сопрограмма wait_coro не завершится; в этом месте скрипт блокируется на все время работы цикла