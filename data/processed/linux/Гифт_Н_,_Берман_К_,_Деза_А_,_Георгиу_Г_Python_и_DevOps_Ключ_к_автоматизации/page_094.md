---
source_image: page_094.png
page_number: 94
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.04
tokens: 7384
characters: 1606
timestamp: 2025-12-24T03:03:25.720375
finish_reason: stop
---

Узнать порядок байтов в вашей архитектуре можно с помощью атрибута sys.byteorder:

In [1]: import sys

In [2]: sys.byteorder
Out[2]: 'little'

Размер объектов Python можно узнать с помощью функции sys.getsizeof. При ограниченном объеме памяти она может оказаться очень полезной:

In [3]: sys.getsizeof(1)
Out[3]: 28

Если ваш код должен вести себя по-разному в зависимости от операционной системы, можно воспользоваться sys.platform для проверки:

In [5]: sys.platform
Out[5]: 'darwin'

Еще чаще встречается ситуация, когда необходимо задействовать возможности языка или модули, доступные только в определенных версиях Python. Управлять поведением в зависимости от текущего интерпретатора Python можно с помощью sys.version_info. В следующем примере выводятся различные сообщения для Python 3.7, Python версий выше 3, но ниже 3.7 и Python версий ниже 3:

if sys.version_info.major < 3:
    print("You need to update your Python version")
elif sys.version_info.minor < 7:
    print("You are not running the latest version of Python")
else:
    print("All is good.")

Мы обсудим применение модуля sys подробнее далее в этой главе, когда будем писать утилиты командной строки.

Взаимодействие с операционной системой с помощью модуля os

Вы уже видели, как в главе 2 модуль os использовался для работы с файловой системой. У него также есть множество разнообразных атрибутов и функций для работы с операционной системой. В примере 3.1 приведены некоторые из них.

Пример 3.1. Примеры возможностей модуля os
In [1]: import os

In [2]: os.getcwd() ①
Out[2]: '/Users/kbehrman/Google-Drive/projects/python-devops'