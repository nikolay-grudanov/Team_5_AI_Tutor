---
source_image: page_593.png
page_number: 593
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 50.93
tokens: 11837
characters: 2269
timestamp: 2025-12-24T02:02:31.425202
finish_reason: stop
---

Разработка серверов с помощью пакета asyncio

Займемся теперь скриптом tcp_charfinder.py, который обрабатывает запросы. Поскольку сказать по поводу этого кода мне предстоит немало, я разбил его на две части, показанные в примерах 18.14 и 18.15.

Пример 18.14. tcp_charfinder.py: простой TCP-сервер с применением функции asyncio.start_server; код этого модуля продолжается в примере 18.15

import sys
import asyncio

from charfinder import UnicodeNameIndex ①

CRLF = b'\r\n'
PROMPT = b'?> '

index = UnicodeNameIndex() ②

@asyncio.coroutine
def handle_queries(reader, writer): ③
    while True: ④
        writer.write(PROMPT)  # не может быть yield from! ⑤
        yield from writer.drain()  # должно быть yield from! ⑥
        data = yield from reader.readline() ⑦
        try:
            query = data.decode().strip()
        except UnicodeDecodeError: ⑧
            query = '\x00'
        client = writer.get_extra_info('peername') ⑨
        print('Received from {}: {!r}'.format(client, query)) ⑩
        if query:
            if ord(query[:1]) < 32: ⑪
                break
            lines = list(index.find_description_strs(query)) ⑫
            if lines:
                writer.writelines(line.encode() + CRLF for line in lines) ⑬
                writer.write(index.status(query, len(lines)).encode() + CRLF) ⑭
            yield from writer.drain() ⑮
            print('Sent {} results'.format(len(lines))) ⑯
        print('Close the client socket') ⑰
        writer.close() ⑱

① Класс UnicodeNameIndex отвечает за построение индекса имен и предоставляет методы запросов к нему.
② Конструктор UnicodeNameIndex читает индекс из файла charfinder_index.pickle, если таковой существует, в противном случае строит индекс, поэтому ответ на первый запрос может занять на несколько секунд больше времени⁸.
⁸ Леонардо Рохаэль отметил, что конструирование UnicodeNameIndex можно было бы поручить отдельному потоку, вызвав метод loop.run_with_executor() из функции main в примере 18.15, тогда сервер был бы готов принимать запросы сразу после построения индекса. Это правда, но поскольку запросы к индексу — единственное, что делает данное приложение, то игра не стоит свеч. Впрочем, реализация совета Леонардо была бы интересным упражнением. Займитесь этим, если хотите.