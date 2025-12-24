---
source_image: page_599.png
page_number: 599
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.57
tokens: 11737
characters: 2082
timestamp: 2025-12-24T02:02:40.727770
finish_reason: stop
---

Разработка серверов с помощью пакета asyncio

И asyncio.start_server, и loop.create_server — сопрограммы, возвращающие объекты asyncio.Server. Чтобы запустить сервер и вернуть на него ссылку, каждой из них нужно управлять до завершения. В случае TCP-сервера это делалось путем вызова метода loop.run_until_complete(server_coro), где server_coro — результат, полученный от asyncio.start_server. В примере HTTP-сервера метод create_server активируется в выражении yield from в сопрограмме init, которой функция main управляет в вызове loop.run_until_complete(init(...)).

Все это я говорю, чтобы подчеркнуть важный факт: сопрограмма делает что-то, только если ей управляют, а для управления сопрограммой asyncio.coroutine нужно либо воспользоваться выражением yield from, либо передать ее одной из нескольких функций из пакета asyncio, который принимают сопрограммы или будущие объекты, например run_until_complete.

В примере 18.18 показана функция home, настроенная для обработки корневого URL-адреса (/) в нашем HTTP-сервере.

Пример 1818. http_charfinder.py: функция home

def home(request):
    query = request.GET.get('query', '').strip()  # Получаем строку запроса, из которой удалены начальные и конечные пробелы.
    print('Query: {!r}'.format(query))  # Протоколируем запрос на консоли сервера.
    if query:
        descriptions = list(index.find_descriptions(query))
        res = '\n'.join(ROW_TPL.format(**vars(descr))
            for descr in descriptions)
        msg = index.status(query, len(descriptions))
    else:
        descriptions = []
        res = ''
        msg = 'Enter words describing characters.'

    html = template.format(query=query, result=res, message=msg)
    print('Sending {} results'.format(len(descriptions)))  # Отрисовываем HTML-страницу.
    return web.Response(content_type=CONTENT_TYPE, text=html)  # Протоколируем ответ на консоли сервера.
    Строим и возвращаем объект Response.

Отметим, что функция home — не сопрограмма и не должна ей быть, если в ней нет выражений yield from. В документации по методу add_route из пакета aiohttp