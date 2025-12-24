---
source_image: page_134.png
page_number: 134
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.34
tokens: 7171
characters: 948
timestamp: 2025-12-24T02:37:15.255879
finish_reason: stop
---

который служит примером программного использования кода.
Модуль ``doctest`` может выполнить эту строку документации и проверить ее правильность по выходным данным.

```python
>>> import io
>>> fin = io.StringIO(
...
    'hello\nworld\n')
>>> fout = io.StringIO()
>>> cat = Catter([fin],
...    show_numbers=True)
>>> cat.run(fout)
>>> print(fout.getvalue())
    1 hello
    2 world

"""
import argparse
import logging
import sys

__version__ = '0.0.1'

logging.basicConfig(
    level=logging.DEBUG)

class Catter(object):
    """
    Класс для конкатенации файлов
    в стандартном выводе

    Строка документации класса,
    выводится командой ``help(cat.Catter)``
    """

    def __init__(self, files,
            show_numbers=False):
        self.files = files
        self.show_numbers = show_numbers

    def run(self, fout):
        # Использовать 6 пробелов для чисел
        # с выравниванием по правому краю
        fmt = '{0:>6} {1}'
```