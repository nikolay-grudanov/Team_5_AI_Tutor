---
source_image: page_595.png
page_number: 595
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 53.75
tokens: 11817
characters: 2149
timestamp: 2025-12-24T02:02:38.780527
finish_reason: stop
---

Разработка серверов с помощью пакета asyncio

В примере 18.15 показана функция main для модуля, начатого в примере 18.14.

Пример 18.15. tcp_charfinder.py (продолжение примера 18.14): функция main инициализирует и завершает цикл обработки событий и TCP-сервер

def main(address='127.0.0.1', port=2323):
    port = int(port)
    loop = asyncio.get_event_loop()
    server_coro = asyncio.start_server(handle_queries, address, port, loop=loop)
    server = loop.run_until_complete(server_coro)

    host = server.sockets[0].getsockname()
    print('Serving on {}. Hit CTRL-C to stop.'.format(host))
    try:
        loop.run_forever()
    except KeyboardInterrupt: # нажата CTRL+C
        pass

    print('Server shutting down.')
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

if __name__ == '__main__':
    main(*sys.argv[1:])

1 Функцию main можно вызывать без аргументов.
2 По завершении объект-сопрограмма, полученный от asyncio.start_server, возвращает экземпляр asyncio.Server, TCP-сервера.
3 Управляя сопрограммой server_coro, получаем объект server.
4 Получаем адрес и порт первого сокета сервера и ...
5 ... выводим его на консоль. Это первое, что скрипт печатает на консоли сервера.
6 Исполняем цикл обработки событий; здесь функция main блокируется до тех пор, пока на консоли сервера не будет нажата клавиша CTRL-C.
7 Закрываем сервер.
8 Метод server.wait_closed() возвращает будущий объект; дадим ему возможность выполнить свою работу с помощью метода loop.run_until_complete.
9 Завершаем цикл обработки событий.
10 Это краткий способ выразить обработку необходимых аргументов командной строки: разворачиваем sys.argv[1:] и передаем результат функции main, в которой заданы также значения аргументов по умолчанию.

Отметим, что метод run_until_complete принимает либо сопрограмму (результат start_server), либо объект Future (результат server.wait_closed). Если в качестве аргумента передана сопрограмма, то она обертывается объектом Task.

Разобраться в потоке управления в скрипте tcp_charfinder.py будет проще, если внимательно приглядеться к сообщениям, печатаемым на консоли (см. пример 18.16).