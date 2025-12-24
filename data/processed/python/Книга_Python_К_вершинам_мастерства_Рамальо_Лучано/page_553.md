---
source_image: page_553.png
page_number: 553
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.84
tokens: 11751
characters: 2029
timestamp: 2025-12-24T02:00:33.463028
finish_reason: stop
---

Загрузка с индикацией хода выполнения и обработкой ошибок

future = executor.submit(download_one,
    cc, base_url, verbose) ⑨
to_do_map[future] = cc ⑩
done_iter = futures.as_completed(to_do_map) ⑪
if not verbose:
    done_iter = tqdm.tqdm(done_iter, total=len(cc_list)) ⑫
for future in done_iter: ⑬
    try:
        res = future.result() ⑭
    except requests.exceptions.HTTPError as exc: ⑮
        error_msg = 'HTTP {res.status_code} - {res.reason}'
        error_msg = error_msg.format(res=exc.response)
    except requests.exceptions.ConnectionError as exc:
        error_msg = 'Connection error'
    else:
        error_msg = ''
        status = res.status
    if error_msg:
        status = HTTPStatus.error
        counter[status] += 1
        if verbose and error_msg:
            cc = to_do_map[future] ⑯
            print('*** Error for {}: {}'.format(cc, error_msg))
return counter

if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)

1 Импортируем библиотеку с индикатором хода выполнения.
2 Импортируем одну функцию и одно перечисление из модуля flags2_common.
3 Повторно используем функцию download_one из модуля flags2_sequential (пример 17.12).
4 Если в командной строке не задан параметр -m/--max_req, то принимаем такое максимальное число одновременных запросов, оно и станет размером пула потоков. Фактическое число потоков может быть меньше, если загружается меньше флагов.
5 MAX_CONCUR_REQ — максимальное число одновременных запросов независимо от числа загружаемых флагов и от значения параметра -m/--max_req; это мера предосторожности.
6 Создаем объект executor с параметром max_workers, равным величине concur_req, которую функция main вычисляет как минимум из MAX_CONCUR_REQ, длины списка cc_list, и значения параметра командной строки -m/--max_req. Это позволяет избежать создания большего числа потоков, чем необходимо.
7 Этот словарь отображает каждый экземпляр Future — представляющий одну загрузку — на соответствующий код страны для показа в сообщении об ошибке.