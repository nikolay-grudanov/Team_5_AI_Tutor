---
source_image: page_598.png
page_number: 598
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.24
tokens: 11699
characters: 1803
timestamp: 2025-12-24T02:02:31.425096
finish_reason: stop
---

port = int(port)
loop = asyncio.get_event_loop()
host = loop.run_until_complete(init(loop, address, port)) ⑦
print('Serving on {}. Hit CTRL-C to stop.'.format(host))
try:
    loop.run_forever() ⑧
except KeyboardInterrupt: # нажата CTRL+C
    pass
print('Server shutting down.')
loop.close() ⑨

if __name__ == '__main__':
    main(*sys.argv[1:])

① Сопрограмма init отдает сервер, который будет обрабатывать запросы в цикле обработки событий.
② Класс aiohttp.web.Application представляет веб-приложение...
③ ... в котором маршруты сопоставляют функции-обработчики образцам URL-адресов; в данном случае запрос GET / маршрутизируется функции home (см. пример 18.18).
④ Метод app.make_handler возвращает объект типа aiohttp.web.RequestHandler, который обрабатывает HTTP-запросы в соответствии с маршрутами, заданными в объекте app.
⑤ Метод create_server создает сервер, использующий в качестве обработчика протокола объект handler, и связывает его с адресом address и портом port.
⑥ Возвращаем адрес и порт первого сокета сервера.
⑦ Вызываем init для запуска сервера и получения его адреса и порта.
⑧ Исполняем цикл обработки событий; main блокируется, пока управление остается у цикла.
⑨ Закрываем цикл обработки событий.

В плане знакомства с asyncio API интересно сравнить инициализацию серверов в примерах 18.17 и 18.15.

Создание и планирование TCP-сервера производилось в следующих двух строчках функции main:

server_coro = asyncio.start_server(handle_queries, address, port,
    loop=loop)
server = loop.run_until_complete(server_coro)

А HTTP-сервер создается в функции init:

server = yield from loop.create_server(handler,
    address, port)

Но init сама является сопрограммой, поэтому активируется она в функции main следующим образом:

host = loop.run_until_complete(init(loop, address, port))