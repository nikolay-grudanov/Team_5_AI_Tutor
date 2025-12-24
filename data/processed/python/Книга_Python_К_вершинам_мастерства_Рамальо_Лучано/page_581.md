---
source_image: page_581.png
page_number: 581
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.28
tokens: 11786
characters: 2140
timestamp: 2025-12-24T02:01:48.617764
finish_reason: stop
---

Улучшение скрипта загрузки на основе asyncio

def download_one(cc, base_url, semaphore, verbose):
    try:
        with (yield from semaphore):  # 4
            image = yield from get_flag(base_url, cc)  # 5
    except web.HTTPNotFound:  # 6
        status = HTTPStatus.not_found
        msg = 'not found'
    except Exception as exc:
        raise FetchError(cc) from exc  # 7
    else:
        save_flag(image, cc.lower() + '.gif')  # 8
        status = HTTPStatus.ok
        msg = 'OK'

    if verbose and msg:
        print(cc, msg)

    return Result(status, cc)

1 Это исключение служит для обертывания исключений сети и протокола HTTP с целью добавления к ним поля country_code, включаемого в сообщение об ошибке.
2 get_flag либо возвращает байты загруженного изображения, либо возбуждает исключение web.HTTPNotFound при получении HTTP-ответа с кодом 404, либо возбуждает исключение aiohttp.HttpProcessingError для всех остальных кодов состояния HTTP.
3 Аргумент semaphore — объект класса asyncio.Semaphore (http://bit.ly/1f6Csp8), механизма синхронизации, ограничивающего количество одновременных запросов.
4 semaphore используется в качестве контекстного менеджера в выражении yield from, чтобы не блокировать систему в целом: когда счетчик семафора достигает максимально разрешенного значения, блокируется только эта сопрограмма.
5 При выходе из этого предложения with счетчик семафора уменьшается, что приводит к разблокировке объекта-сопрограммы, стоящего в очереди к тому же семафору.
6 Если флаг не был найден, просто устанавливаем соответствующее состояние для Result. Любая другая ошибка приводит к исключению FetchError, в котором хранится код страны и исходное исключение, для этого используется конструкция raise X from Y, описанная в документе «PEP 3134 — Exception Chaining and Embedded Tracebacks» (https://www.python.org/dev/peps/pep-3134/).
7 Эта функция записывает изображение флага на диск.

Из примера 18.7 видно, что код функций get_flag и download_one существенно изменился по сравнению с последовательной версией, т. к. теперь они стали сопрограммами, в которых для асинхронных вызовов используется yield from.