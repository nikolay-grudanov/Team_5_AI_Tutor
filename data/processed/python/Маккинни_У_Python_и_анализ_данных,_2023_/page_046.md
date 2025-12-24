---
source_image: page_046.png
page_number: 46
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.38
tokens: 7420
characters: 1575
timestamp: 2025-12-24T02:41:03.603903
finish_reason: stop
---

Интропекция
Если ввести вопросительный знак (?) до или после имени переменной, то будет напечатана общая информация об объекте:

In [1]: b = [1, 2, 3]

In [2]: b?
Type: list
String form: [1, 2, 3]
Length: 3
Docstring:
Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.

In [3]: print?
Docstring:
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file: a file-like object (stream); defaults to the current sys.stdout.
sep: string inserted between values, default a space.
end: string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.
Type: builtin_function_or_method

Это называется интропекцией объекта. Если объект представляет собой функцию или метод экземпляра, то будет показана строка документации, при условии ее существования. Допустим, мы написали такую функцию (этот код можно ввести в IPython or Jupyter):

def add_numbers(a, b):
    """
    Сложить два числа
    Возвращаем
    ------
    the_sum : типа аргументов
    """
    return a + b

Тогда при вводе знака ? мы увидим строку документации:

In [6]: add_numbers?
Signature: add_numbers(a, b)
Docstring:
Сложить два числа
Возвращает
----------
the_sum : типа аргументов
File: <ipython-input-9-6a548a216e27>
Type: function

И последнее применение ? – поиск в пространстве имен IPython по аналогии со стандартной командной строкой UNIX или Windows. Если ввести несколько