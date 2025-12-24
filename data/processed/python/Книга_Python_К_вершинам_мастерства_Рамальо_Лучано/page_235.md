---
source_image: page_235.png
page_number: 235
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.62
tokens: 11695
characters: 1360
timestamp: 2025-12-24T01:45:34.880016
finish_reason: stop
---

Параметризованные декораторы

Пример 7.26. clockdeco_param_demo1.py

import time
from clockdeco_param import clock

@clock('{name}: {elapsed}s')
def snooze(seconds):
    time.sleep(seconds)

for i in range(3):
    snooze(.123)

Результат выполнения примера 7.26:

$ python3 clockdeco_param_demo1.py
snooze: 0.12414693832397461s
snooze: 0.1241159439086914s
snooze: 0.12412118911743164s

Пример 7.27. clockdeco_param_demo2.py

import time
from clockdeco_param import clock

@clock('{name}({args}) dt={elapsed:0.3f}s')
def snooze(seconds):
    time.sleep(seconds)

for i in range(3):
    snooze(.123)

Результат выполнения примера 7.27:

$ python3 clockdeco_param_demo2.py
snooze(0.123) dt=0.124s
snooze(0.123) dt=0.124s
snooze(0.123) dt=0.124s

На этом мы завершаем изучение декораторов, поскольку объем книги не позволяет развить эту тему дальше. См. ниже раздел «Дополнительная литература» и в особенности блог Грэхема Дамплтона (Graham Dumpleton) и модуль wrapt, содержащий профессиональные приемы построения декораторов.

Грэхем Дамплтон и Леннарт Регебро — один из рецензентов этой книги — считают, что декораторы лучше писать как классы, реализующие метод __call__, а не как функции (как в примерах из этой главы). Согласен, что для нетривиальных декораторов такой подход разумнее, но функции проще, когда требуется объяснить основную идею этого механизма.