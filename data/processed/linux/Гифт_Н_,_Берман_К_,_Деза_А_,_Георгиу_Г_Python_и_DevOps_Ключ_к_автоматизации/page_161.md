---
source_image: page_161.png
page_number: 161
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.30
tokens: 7405
characters: 1817
timestamp: 2025-12-24T03:05:02.403535
finish_reason: stop
---

мых для генерации пакета файлов. Описание пакета для setuptools приводится в файле setup.py, расположенном в каталоге верхнего уровня. В нашем примере проекта этот файл выглядит следующим образом:

from setuptools import setup, find_packages

setup(
    name="hello-world",
    version="0.0.1",
    author="Example Author",
    author_email="stopspamer@ukr.net",
    url="example.com",
    description="A hello-world example package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

Файл setup.py импортирует из модуля две вспомогательные функции: setup и find_packages. Именно для функции setup необходимо подробное описание пакета. Функция find_packages представляет собой утилиту для автоматического обнаружения местоположения файлов Python. Кроме того, этот файл импортирует classifiers, описывающие некоторые аспекты пакета, в частности лицензию, поддерживаемые операционные системы и версии Python. Это так называемые trove-классификаторы (trove classifiers), и в каталоге пакетов Python (https://pypi.org/classifiers) есть подробное описание всех доступных классификаторов. При загрузке в PyPI публикуются подробные описания пакетов.

Достаточно добавить всего один этот файл, чтобы сгенерировать пакет, в данном случае пакет дистрибутива исходного кода (source distribution package). Из-за отсутствия файла README при выполнении команд выводится предупреждение. Чтобы предотвратить это, добавьте пустой файл README в каталог верхнего уровня с помощью команды touch README.

Содержимое каталога проекта должно выглядеть следующим образом:

hello-world
│   hello_world
│   │   __init__.py
│   │   main.py
│   ├── README
│   └── setup.py

1 directory, 2 files