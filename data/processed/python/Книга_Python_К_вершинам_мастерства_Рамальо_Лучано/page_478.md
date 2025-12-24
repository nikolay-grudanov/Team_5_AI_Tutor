---
source_image: page_478.png
page_number: 478
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.75
tokens: 11742
characters: 1897
timestamp: 2025-12-24T01:57:02.565678
finish_reason: stop
---

self.original_write = sys.stdout.write ②
sys.stdout.write = self.reverse_write ③
return 'JABBERWOCKY' ④

def reverse_write(self, text): ⑤
    self.original_write(text[::-1])

def __exit__(self, exc_type, exc_value, traceback): ⑥
    import sys ⑦
    sys.stdout.write = self.original_write ⑧
    if exc_type is ZeroDivisionError: ⑨
        print('Пожалуйста, НЕ НАДО делить на нуль!') ⑩
    return True ⑪

1 Python вызывает __enter__ с одним лишь аргументом self.
2 Текущий метод sys.stdout.write сохраняется в атрибуте экземпляра для последующего использования.
3 Подменяем метод sys.stdout.write своим собственным.
4 Возвращаем строку 'JABBERWOCKY', просто чтобы поместить что-то в переменную what.
5 Наш метод sys.stdout.write инвертирует переданный аргумент text и вызывает сохраненную реализацию.
6 Python вызывает метод __exit__ с аргументами None, None, None, если не было ошибок; если же имело место исключение, то в аргументах передаются данные об исключении, описанные ниже.
7 Повторный импорт модулей обходится дешево, потому что Python их кэширует.
8 Восстанавливаем исходный метод sys.stdout.write.
9 Если исключение было и его тип — ZeroDivisionError, печатаем сообщение...
10 ... и возвращаем true, уведомляя интерпретатор о том, что исключение обработано.
11 Если метод __exit__ возвращает None или вообще что-нибудь, кроме true, то исключение, возникшее внутри блока with, распространяется дальше.

Реальные приложения, перехватывающие стандартный вывод, обычно хотят временно подменить sys.stdout похожим на файл объектом, а затем восстановить исходное состояние. Именно это делает контекстный менеджер contextlib.redirect_stdout (http://bit.ly/1MM7Sw6): просто передайте ему похожий на файл объект, который подменит sys.stdout.

Интерпретатор вызывает метод __enter__ без аргументов — если не считать неявного аргумента self. А методу __exit__ передаются следующие три аргумента: