---
source_image: page_030.png
page_number: 30
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.75
tokens: 7387
characters: 1462
timestamp: 2025-12-24T03:01:46.576930
finish_reason: stop
---

Установка и запуск Python

Чтобы опробовать в работе код из этой главы, вам понадобятся Python версии 3.7 или более поздней¹ и доступ к командной оболочке. В macOS X, Windows и большинстве дистрибутивов Linux для доступа к командной оболочке достаточно открыть терминал. Чтобы узнать используемую версию Python, откройте командную оболочку и наберите команду python --version:

$ python --version
Python 3.8.0

Скачать установочные пакеты Python можно непосредственно с сайта Python.org (https://www.python.org/downloads). Можно также воспользоваться системой управления пакетами, например Apt, RPM, MacPorts, Homebrew, Chocolatey и др.

Командная оболочка Python

Простейший способ работы с Python — воспользоваться встроенным интерактивным интерпретатором. Просто набрав в командной оболочке python, вы сможете интерактивно выполнять операторы Python. Для выхода из командной оболочки наберите exit():

$ python
Python 3.8.0 (default, Sep 23 2018, 09:47:03)
[Clang 9.0.0 (clang-900.0.38)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 1 + 2
3
>>> exit()

Сценарии Python

Код Python выполняется из файла с расширением .py:

# Мой первый сценарий Python
print('Hello world!')

Сохраните этот код в файле hello.py. Для вызова этого сценария наберите в командной оболочке python с последующим именем файла:

$ python hello.py
Hello world!

¹ По состоянию на сентябрь 2021 г. текущая стабильная версия — 3.9.7. — Примеч. пер.