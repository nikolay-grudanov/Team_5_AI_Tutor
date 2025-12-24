---
source_image: page_092.png
page_number: 92
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.97
tokens: 7481
characters: 1936
timestamp: 2025-12-24T02:42:13.953246
finish_reason: stop
---

Кстати, float может возбуждать и другие исключения, не только ValueError:

In [229]: float((1, 2))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-229-82f777b0e564> in <module>
----> 1 float((1, 2))
TypeError: float() argument must be a string or a real number, not 'tuple'

Возможно, вы хотите перехватить только исключение ValueError, поскольку TypeError (аргумент был не строкой и не числом) может свидетельствовать об ожидаемой ошибке в программе. Для этого нужно написать после except тип исключения:

def attempt_float(x):
    try:
        return float(x)
    except ValueError:
        return x

В таком случае получим:

In [231]: attempt_float((1, 2))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-231-8b0026e9e6b7> in <module>
----> 1 attempt_float((1, 2))
<ipython-input-230-6209ddec2b5> in attempt_float(x)
      1 def attempt_float(x):
      2     try:
----> 3         return float(x)
      4     except ValueError:
      5         return x
TypeError: float() argument must be a string or a real number, not 'tuple'

Можно перехватывать исключения нескольких типов, для этого достаточно написать кортеж типов (скобки обязательны):

def attempt_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return x

Иногда исключение не нужно перехватывать, но какой-то код должен быть выполнен вне зависимости от того, возникло исключение в блоке try или нет. Для этого служит предложение finally:

f = open(path, mode="w")

try:
    write_to_file(f)
finally:
    f.close()

Здесь объект файла f закрывается в любом случае. Можно также написать код, который исполняется, только если в блоке try не было исключения, для этого используется ключевое слово else: