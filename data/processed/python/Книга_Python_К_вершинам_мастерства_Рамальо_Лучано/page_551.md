---
source_image: page_551.png
page_number: 551
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.27
tokens: 11813
characters: 2304
timestamp: 2025-12-24T02:00:21.927741
finish_reason: stop
---

Загрузка с индикацией хода выполнения и обработкой ошибок

4 Любое другое исключение типа HTTPError возбуждается повторно, прочие исключения просто распространяются в вызывающую программу.
5 Если задан параметр -v/--verbose, то отображается сообщение, содержащее код страны и состояние; именно так мы видим индикатор хода выполнения в режиме вывода подробной информации.
6 Именованный кортеж Result, возвращенный функцией download_one, включает поле status со значением HTTPStatus.not_found или HTTPStatus.ok.

В примере 17.13 приведена последовательная версия функции download_many. Ее код прямоолинеен, но его стоит изучить хотя бы для сравнения с параллельными версиями. Обратите внимание на индикацию хода выполнения, обработку ошибок и подсчет количества загрузок с разным исходом.

Пример 17.13. flags2_sequential.py: последовательная реализация download_many

def download_many(cc_list, base_url, verbose, max_req):
    counter = collections.Counter() ①
    cc_iter = sorted(cc_list) ②
    if not verbose:
        cc_iter = tqdm.tqdm(cc_iter) ③
    for cc in cc_iter: ④
        try:
            res = download_one(cc, base_url, verbose) ⑤
        except requests.exceptions.HTTPError as exc: ⑥
            error_msg = 'HTTP error {res.status_code} - {res.reason}'
            error_msg = error_msg.format(res=exc.response)
        except requests.exceptions.ConnectionError as exc: ⑦
            error_msg = 'Connection error'
        else: ⑧
            error_msg = ''
            status = res.status
            if error_msg:
                status = HTTPStatus.error ⑨
                counter[status] += 1 ⑩
                if verbose and error_msg: ⑪
                    print('*** Error for {}: {}'.format(cc, error_msg))
    return counter ⑫

1 Этот объект Counter подсчитывает количество загрузок с разными исходами: HTTPStatus.ok, HTTPStatus.not_found, HTTPStatus.error.
2 В cc_iter хранится отсортированный по алфавиту список кодов стран, полученных в виде аргументов.
3 Если не задан режим подробной информации, то cc_iter передается функции tqdm, которая возвращает итератор, отдающий элементы из cc_iter и одновременно отображающий анимированный индикатор хода выполнения.
4 В этом цикле for мы обходим cc_iter и ...
5 ... производим загрузку, последовательно обращаясь к download_one.