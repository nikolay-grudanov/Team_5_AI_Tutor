---
source_image: page_131.png
page_number: 131
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.38
tokens: 7264
characters: 1248
timestamp: 2025-12-24T02:37:21.121992
finish_reason: stop
---

является пакетом, то каталог plot/ должен находиться в одном из каталогов из sys.path:

    >>> import plot
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    ImportError: No module named plot
    >>> sys.path.append('/home/test/a')
    >>> import plot
    >>> plot.histogram()

Также можно включить этот каталог в PYTHONPATH из командной строки, используемой для запуска Python.

Еще раз подчеркнем, что обычно задавать вручную sys.path или PYTHONPATH не нужно. В нормальной ситуации вы устанавливаете библиотеки, а программа установки размещает их в правильном каталоге.

СОВЕТ

Если вы хотите узнать местонахождение библиотеки в файловой системе, проверьте атрибут __file__:

    >>> import json
    >>> json.__file__
    '/usr/lib/python3.6/json/__init__.py'

Этот способ работает только с библиотеками, реализованными на Python. Модуль sys не реализован на Python, поэтому эта попытка завершается неудачей:

    >>> import sys
    >>> sys.__file__
    Traceback (most recent call last):
        ...
    AttributeError: module 'sys' has no attribute '__file__'

25.6. Итоги

В этой главе рассматриваются модули и пакеты. Модуль представляет собой файл Python. Пакет представляет собой каталог, в котором при-