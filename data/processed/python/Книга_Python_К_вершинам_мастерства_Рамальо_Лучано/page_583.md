---
source_image: page_583.png
page_number: 583
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.04
tokens: 11652
characters: 1846
timestamp: 2025-12-24T02:01:39.712263
finish_reason: stop
---

Улучшение скрипта загрузки на основе asyncio

Пример 18.8. flags2_asyncio.py: продолжение скрипта из примера 18.7

@asyncio.coroutine
def downloader_coro(cc_list, base_url, verbose, concur_req):
    counter = collections.Counter()
    semaphore = asyncio.Semaphore(concur_req)
    to_do = [download_one(cc, base_url, semaphore, verbose) for cc in sorted(cc_list)]
    to_do_iter = asyncio.as_completed(to_do)
    if not verbose:
        to_do_iter = tqdm.tqdm(to_do_iter, total=len(cc_list))
    for future in to_do_iter:
        try:
            res = yield from future
        except FetchError as exc:
            country_code = exc.country_code
            try:
                error_msg = exc.__cause__.args[0]
            except IndexError:
                error_msg = exc.__cause__.__class__.__name__
            if verbose and error_msg:
                msg = '*** Error for {}: {}'
                print(msg.format(country_code, error_msg))
            status = HTTPStatus.error
        else:
            status = res.status
        counter[status] += 1
    return counter

def download_many(cc_list, base_url, verbose, concur_req):
    loop = asyncio.get_event_loop()
    coro = downloader_coro(cc_list, base_url, verbose, concur_req)
    counts = loop.run_until_complete(coro)
    loop.close()
    return counts

if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)

1 Сопрограмма получает те же аргументы, что download_many, но вызвать ее из main напрямую нельзя, потому что это сопрограмма, а не обычная функция.
2 Создаем объект asyncio.Semaphore, который разрешает запускать одновременно не более concur_req сопрограмм.
3 Создаем список объектов-сопрограмм, по одному для каждого вызова сопрограммы download_one.
4 Получаем итератор, который будет возвращать будущие объекты по мере их завершения.