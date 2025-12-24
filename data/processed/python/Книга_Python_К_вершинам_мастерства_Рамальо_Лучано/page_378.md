---
source_image: page_378.png
page_number: 378
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 11.00
tokens: 11524
characters: 1019
timestamp: 2025-12-24T01:51:37.326101
finish_reason: stop
---

Множественное наследование и порядок разрешения методов

Любой язык с множественным наследованием должен как-то разрешать конфликты имен в случае, когда в не связанных между собой родительских классах имеются методы с одним и тем же именем. Эта «проблема ромбовидного наследования» иллюстрируется на рис. 12.1 и в примере 12.4.

![UML-диаграмма классов и порядок разрешения методов](https://i.imgur.com/3Q5z5QG.png)

Рис. 12.1. Слева: UML-диаграмма классов, иллюстрирующая «проблему ромбовидного наследования». Справа: пунктирными стрелками показан порядок разрешения методов (method resolution order – MRO) в Python для примера 12.4

Пример 12.4. diamond.py: классы A, B, C и D образуют граф, показанный на рис. 12.1

class A:
    def ping(self):
        print('ping:', self)

class B(A):
    def pong(self):
        print('pong:', self)

class C(A):
    def pong(self):
        print('PONG:', self)

class D(B, C):

    def ping(self):
        super().ping()
        print('post-ping:', self)

    def pingpong(self):