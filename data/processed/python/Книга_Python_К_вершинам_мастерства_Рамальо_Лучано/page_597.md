---
source_image: page_597.png
page_number: 597
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.29
tokens: 11642
characters: 1389
timestamp: 2025-12-24T02:02:22.019087
finish_reason: stop
---

Разработка серверов с помощью пакета asyncio

показан простой веб-интерфейс сервера, где выведены результаты поиска смайлика «cat face» (кошачья мордочка).

![Окно браузера с результатами поиска символов по строке «cat face»](https://i.imgur.com/3Q5z5QG.png)

Рис. 18.3. В окне браузера отображаются результаты поиска символов по строке «cat face», возвращенные сервером http_charfinder.py

В одних браузерах символы Unicode отображаются лучше, в других хуже.
Рис. 18.3 скопирован из браузера Firefox на платформе Mac OS X, и точно такой же результат дал Safari. Но последние версии Chrome и Opera на той же машине не показали смайликов с кошачьими мордочками. Результаты других запросов (например, по слову «chess») выглядели прекрасно, так что эта проблема, вероятно, связана со шрифтами, которыми Chrome и Opera пользуются в OS X.

Начнем с анализа самой интересной, последней, части скрипта http_charfinder.py, где находится цикл обработки событий и производится инициализация и закрытие HTTP-сервера.

Пример 18.17. http_charfinder.py: функции main и init

@asyncio.coroutine
def init(loop, address, port): ①
    app = web.Application(loop=loop) ②
    app.router.add_route('GET', '/', home) ③
    handler = app.make_handler() ④
    server = yield from loop.create_server(handler, address, port) ⑤
    return server.sockets[0].getsockname() ⑥

def main(address="127.0.0.1", port=8888):