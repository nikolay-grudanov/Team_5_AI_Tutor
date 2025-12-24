---
source_image: page_039.png
page_number: 39
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.16
tokens: 7677
characters: 2260
timestamp: 2025-12-24T02:41:01.507925
finish_reason: stop
---

Некоторые базовые понятия Python, например классы и объектно-ориентированное программирование, в этой главе не рассматриваются, хотя их полезно включить в арсенал средств для анализа данных. Для желающих углубить свои знания я рекомендую дополнить эту главу официальным пособием по Python (https://docs.python.org/3/) и, возможно, одной из многих замечательных книг по программированию на Python вообще. Начать можно, например, с таких книг:
○ Python Cookbook, Third Edition, by David Beazley and Brian K. Jones (O’Reilly);
○ Fluent Python by Luciano Ramalho (O’Reilly)¹;
○ Effective Python by Brett Slatkin (Pearson)².

2.1. ИНТЕРПРЕТАТОР PYTHON

Python – интерпретируемый язык. Интерpreterator Python исполняет программу по одному предложению за раз. Стандартный интерактивный интерpreterator Python запускается из командной строки командой python:

$ python
Python 3.10.4 | packaged by conda-forge | (main, Mar 24 2022, 17:38:57)
[GCC 10.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 5
>>> print(a)
5
Строка >>> – это приглашение к вводу выражения. Для выхода из интерpreterатора Python нужно либо ввести команду exit(), либо нажать Ctrl-D (только в Linux и macOS).
Для выполнения Python-программы нужно просто набрать команду python, указав в качестве первого аргумента имя файла с расширением .py. Допустим, вы создали файл hello_world.py с таким содержимым:

print("Hello world")

Чтобы выполнить его, достаточно ввести следующую команду (файл hello_world.py должен находиться в текущем каталоге):

$ python hello_world.py
Hello world

Многие программисты выполняют свой код на Python именно таким образом, но в мире научных приложений и анализа данных принято использовать IPython, улучшенный и дополненный интерpreterator Python, или веб-блокноты Jupyter, первоначально разработанные как часть проекта IPython. Введение в IPython и Jupyter будет дано в этой главе, а углубленное описание возможностей IPython – в приложении 3. С помощью команды %run IPython исполняет код в указанном файле в том же процессе, что позволяет интерактивно изучать результаты по завершении выполнения.

¹ Лусиану Рамальо. Python. К вершинам мастерства. 2-е изд. ДМК Пресс, 2022.
² Бретт Слаткин. Секреты Python. Вильямс, 2017.