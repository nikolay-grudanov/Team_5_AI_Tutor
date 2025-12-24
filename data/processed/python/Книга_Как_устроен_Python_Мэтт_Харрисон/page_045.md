---
source_image: page_045.png
page_number: 45
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.15
tokens: 7249
characters: 1060
timestamp: 2025-12-24T02:35:11.375266
finish_reason: stop
---

Несколько примеров имен переменных — как хороших, так и плохих:

>>> good = 4
>>> bAd = 5 # плохо - верхний регистр
>>> a_longer_variable = 6

# Не рекомендуется
>>> badLongerVariable = 7

# Плохо - начинается с цифры
>>> 3rd_bad_variable = 8
    File "<stdin>", line 1
        3rd_bad_variable = 8
            ^
SyntaxError: invalid syntax

# Плохо - ключевое слово
>>> for = 4
    File "<stdin>", line 1
        for = 4
            ^
SyntaxError: invalid syntax

# Плохо - встроенная функция
>>> compile = 5

СОВЕТ
Правила и соглашения назначения имен в Python перечислены в документе «PEP 8 — Style Guide for Python Code»¹. Сокращение PEP означает «Python Enhancement Proposal», то есть «Предложение по улучшению Python» — так называется процесс документирования функции, усовершенствования или передовой практики для Python. Документы PEP доступны на сайте Python.

ПРИМЕЧАНИЕ
Хотя Python не разрешает использовать ключевые слова в качестве имен переменных, встроенные имена могут использоваться как переменные.

¹ https://www.python.org/dev/peps/pep-0008/