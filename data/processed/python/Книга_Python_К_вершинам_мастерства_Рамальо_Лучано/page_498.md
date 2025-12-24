---
source_image: page_498.png
page_number: 498
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.78
tokens: 11672
characters: 1802
timestamp: 2025-12-24T01:57:54.210749
finish_reason: stop
---

generator.close()

Выражение yield, в котором генератор приостановлен, возбуждает исключение GeneratorExit. Если генератор не обработает это исключение или возбудит исключение StopIteration — обычно в результате выполнения до конца — вызывающая сторона не получит никакой ошибки. Получив исключение GeneratorExit, генератор не должен отдавать значение, иначе возникнет исключение RuntimeError. Если генератор возбудит любое другое исключение, то оно распространится в контекст вызывающей стороны.

Официальная документация по методам объекта-генератора находится в разделе 6.2.9.1 «Методы генератора-итератора» справочного руководства по языку Python (https://docs.python.org/3/reference/expressions.html#generator-iterator-methods).

Посмотрим, как управлять сопрограммой с помощью методов close и throw. В следующих примерах будет использована функция demo_exc_handling из примера 16.8.

Пример 16.8. coro_exc_demo.py: тестовый код для изучения обработки исключений в сопрограммах

class DemoException(Exception):
    """An exception type for the demonstration."""

def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException: ①
            print('*** DemoException handled. Continuing...')
        else: ②
            print('-> coroutine received: {!r}'.format(x))
        raise RuntimeError('This line should never run.') ③

① Специальная обработка DemoException.
② Если исключения не было, вывести полученное значение.
③ Эта строка никогда не выполняется.

Последняя строка в примере 16.8 недостижима, потому что из бесконечного цикла можно выйти только в результате необработанного исключения, а это приводит к немедленному завершению сопрограммы.

Нормальная работа функции demo_exc_handling показана в примере 16.9.