---
source_image: page_234.png
page_number: 234
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.09
tokens: 11673
characters: 1618
timestamp: 2025-12-24T01:45:34.222679
finish_reason: stop
---

def decorate(func):
    def clocked(*_args):
        t0 = time.time()
        _result = func(*_args)
        elapsed = time.time() - t0
        name = func.__name__
        args = ', '.join(repr(arg) for arg in _args)
        result = repr(_result)
        print(fmt.format(**locals()))
        return _result
    return clocked

return decorate

if __name__ == '__main__':
    @clock()
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(.123)

1 Теперь clock — наша фабрика параметризованных декораторов.
2 decorate — это собственно декоратор.
3 clocked обертывает декорированную функцию.
4 _result — результат, возвращенный декорированной функцией.
5 В _args хранятся фактические аргументы clocked, тогда как args — отображаемая строка.
6 result — строковое представление _result, предназначенное для отображения.
7 Использование **locals() позволяет ссылаться в fmt на любую локальную переменную clocked.
8 clocked заменяет декорированную функцию, поэтому должна возвращать то, что вернула бы эта функция в отсутствие декоратора.
9 decorate возвращает clocked.
10 clock возвращает decorate.
11 В этом тесте clock() вызывается без аргументов, поэтому декоратор будет использовать форматную строку по умолчанию.

При выполнении программы из примера 7.25 печатается следующее:

$ python3 clockdeco_param.py
[0.12412500s] snooze(0.123) -> None
[0.12411904s] snooze(0.123) -> None
[0.12410498s] snooze(0.123) -> None

Для демонстрации новой функциональности в примерах 7.26 и 7.27 показаны еще два модуля, в которых используется clockdeco_param, а также результаты их выполнения.