---
source_image: page_224.png
page_number: 224
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.81
tokens: 11822
characters: 2064
timestamp: 2025-12-24T01:45:07.989989
finish_reason: stop
---

result = func(*args, **kwargs)
elapsed = time.time() - t0
name = func.__name__
arg_lst = []
if args:
    arg_lst.append(', '.join(repr(arg) for arg in args))
if kwargs:
    pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
    arg_lst.append(', '.join(pairs))
arg_str = ', '.join(arg_lst)
print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
return result
return clocked

Декоратор functools.wraps — лишь один из нескольких готовых декораторов в стандартной библиотеке. В следующем разделе мы рассмотрим два наиболее впечатляющих декоратора в модуле functools: lru_cache и singledispatch.

Декораторы в стандартной библиотеке
В Python есть три встроенные функции, предназначенные для декорирования методов: property, classmethod и staticmethod. Функцию property мы обсудим в разделе «Использование свойств для контроля атрибутов» на стр. 633, а остальные — в разделе «Декораторы classmethod и staticmethod» на стр. 281.

Еще один часто встречающийся декоратор — functools.wraps, вспомогательное средство для построения корректных декораторов, которым мы воспользовались в примере 7.17. Два самых интересных декоратора в стандартной библиотеке — lru_cache и совсем новый singledispatch (добавлен в версии Python 3.4). Оба определены в модуле functools. Их мы далее и рассмотрим.

Кэширование с помощью functools.lru_cache
Декоратор functools.lru_cache очень полезен на практике. Он реализует «запоминание» (memoization): прием оптимизации, смысл которого заключается в сохранении результатов предыдущих дорогостоящих вызовов функции, что позволяет избежать повторного вычисления с теми же аргументами, что и раньше. Акроним LRU расшифровывается как «Least Recently Used» (последний использованный); это означает, что рост кэша ограничивается путем вытеснения тех элементов, к которым давно не было обращений.

Продемонстрируем применение lru_cache на примере медленной рекурсивной функции вычисления n-ого числа Фибоначчи.

Пример 7.18. Очень накладный рекурсивный способ вычисления n-ого числа Фибоначчи
from clockdeco import clock
@clock