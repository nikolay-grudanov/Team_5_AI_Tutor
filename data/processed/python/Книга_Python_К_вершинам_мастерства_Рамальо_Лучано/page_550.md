---
source_image: page_550.png
page_number: 550
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.98
tokens: 11711
characters: 1941
timestamp: 2025-12-24T02:00:08.049885
finish_reason: stop
---

Так выглядит пользовательский интерфейс flags2-примеров. Теперь познакомимся с их реализацией.

Обработка ошибок во flags2-примерах

Общая стратегия обработки ошибок HTTP заключается в том, что ошибки 404 (Не найдено) обрабатываются функцией, отвечающей за загрузку одного файла (download_one), а все остальные исключения распространяются наружу и обрабатываются функцией download_many.

И на этот раз начнем с рассмотрения последовательного кода, за выполнением которого легко проследить; многие функции из него будут использоваться и в многопоточном скрипте. В примере 17.2 показаны функции, которые собственно и выполняют загрузку в скриптах flags2_sequential.py и flags2_threadpool.py.

Пример 17.12. flags2_sequential.py: базовые функции, отвечающие за загрузку, обе используются также в скрипте flags2_threadpool.py

def get_flag(base_url, cc):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    resp = requests.get(url)
    if resp.status_code != 200:
        resp.raise_for_status()
    return resp.content

def download_one(cc, base_url, verbose=False):
    try:
        image = get_flag(base_url, cc)
    except requests.exceptions.HTTPError as exc:
        res = exc.response
        if res.status_code == 404:
            status = HTTPStatus.not_found
            msg = 'not found'
        else:
            raise
    else:
        save_flag(image, cc.lower() + '.gif')
        status = HTTPStatus.ok
        msg = 'OK'

    if verbose:
        print(cc, msg)

    return Result(status, cc)

1 Функция get_flag не обрабатывает ошибки, она вызывает метод requests.Response.raise_for_status для любого кода HTTP, кроме 200.
2 Функция download_one перехватывает исключение requests.exceptions.HTTPError, чтобы обработать ошибку с кодом 404 и только ее...
3 ... установив локальное состояние HTTPStatus.not_found; HTTPStatus — это перечисление Enum, импортированное из модуля flags2_common (пример A.10 в приложении А).