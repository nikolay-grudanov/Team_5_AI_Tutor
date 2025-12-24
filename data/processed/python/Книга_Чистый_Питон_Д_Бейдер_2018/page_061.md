---
source_image: page_061.png
page_number: 61
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.60
tokens: 7375
characters: 1529
timestamp: 2025-12-24T02:28:44.517198
finish_reason: stop
---

2.5. Шокирующая правда о форматировании строковых значений

>>> def greet(name, question):
...     return ("Привет, " + name + "! Как " +
                question + "?")

На практике реализация слегка быстрее, чем эта, потому что в ней в качестве оптимизации используется код операции BUILD_STRING¹. Но функционально они одинаковы:

>>> import dis
>>> dis.dis(greet)
   2 LOAD_CONST           1 ('Привет, ')
   2 LOAD_FAST            0 (name)
   4 FORMAT_VALUE         0
   6 LOAD_CONST           2 ("! Как ")
   8 LOAD_FAST            1 (question)
  10 FORMAT_VALUE         0
  12 LOAD_CONST           3 ('?')
  14 BUILD_STRING         5
  16 RETURN_VALUE

Строковые литералы также поддерживают существующий синтаксис форматных строк метода str.format(). Это позволяет решать те же самые задачи форматирования, которые мы обсудили в предыдущих двух разделах:

>>> f"Эй, {name}! Вот ошибка {errno:#x}!"
"Эй, Боб! Вот ошибка 0xbadc0ffee!"

Новые форматированные строковые литералы Python аналогичны шаблонным литералам JavaScript, добавленным в ES2015. Убежден, что они являются довольно приятным дополнением к языку, и я уже начал их использовать в своей повседневной работе с Python 3. Подробнее о форматированных строковых литералах вы можете узнать из официальной документации Python².

¹ См. Python 3. Спорный вопрос в трекере ошибок № 27078: https://bugs.python.org/issue27078
² См. документацию Python «Форматированные строковые литералы»: https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals