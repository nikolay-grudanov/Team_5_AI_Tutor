---
source_image: page_566.png
page_number: 566
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.12
tokens: 11725
characters: 1834
timestamp: 2025-12-24T02:00:58.203263
finish_reason: stop
---

except asyncio.CancelledError:
    break
write(' ' * len(status) + '\x08' * len(status))

@asyncio.coroutine
def slow_function(): ⑤
    # имитируем ожидание завершения длительной операции ввода-вывода
    yield from asyncio.sleep(3) ⑥
    return 42

@asyncio.coroutine
def supervisor(): ⑦
    spinner = asyncio.async(spin('thinking!')) ⑧
    print('spinner object:', spinner) ⑨
    result = yield from slow_function() ⑩
    spinner.cancel() ⑪
    return result

def main():
    loop = asyncio.get_event_loop() ⑫
    result = loop.run_until_complete(supervisor()) ⑬
    loop.close()
    print('Answer:', result)

if __name__ == '__main__':
    main()

1 Сопрограммы, работающие с asyncio, должны быть снабжены декоратором @asyncio.coroutine. Это необязательно, но в высшей степени желательно.
См. объяснение после листинга.
2 Здесь нам не нужен аргумент signal, который в функции spin из примера 18.1 служил для завершения потока.
3 Используем yield from asyncio.sleep(.1), а не просто time.sleep (.1), чтобы спать, не блокируя цикл обработки событий.
4 Если после пробуждения spin возникло исключение asyncio.CancelledError, значит, была запрошена отмена, поэтому выходим из цикла.
5 slow_function — теперь сопрограмма, в которой yield from используется, чтобы цикл обработки событий мог продолжать работу, пока сопрограмма спит, имитируя ввод-вывод.
6 Выражение yield from asyncio.sleep(3) уступает управление главному циклу, который возобновит сопрограмму после указанной в sleep задержки.
7 supervisor — теперь тоже сопрограмма, поэтому она может управлять функцией slow_function с помощью yield from.
8 asyncio.async(...) планирует выполнение сопрограммы spin, оберывая ее объектом Task, который возвращается немедленно
9 Распечатываем объект Task. Результат имеет вид <Task pending coro=<spin() running at spinner_asyncio.py:12>>