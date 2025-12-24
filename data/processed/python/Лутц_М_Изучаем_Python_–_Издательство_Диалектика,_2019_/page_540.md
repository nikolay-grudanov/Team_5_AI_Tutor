---
source_image: page_540.png
page_number: 540
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.73
tokens: 7321
characters: 1088
timestamp: 2025-12-24T01:23:59.032788
finish_reason: stop
---

Проверьте свои знания: контрольные вопросы

1. Что выведет следующий код и почему?
   >>> X = 'Spam'
   >>> def func():
   ...     print(X)
   >>> func()

2. Что выведет следующий код и почему?
   >>> X = 'Spam'
   >>> def func():
   ...     X = 'NI!'
   >>> func()
   >>> print(X)

3. Что выведет следующий код и почему?
   >>> X = 'Spam'
   >>> def func():
   ...     X = 'NI'
   ...     print(X)
   >>> func()
   >>> print(X)

4. Что выведет следующий код и почему?
   >>> X = 'Spam'
   >>> def func():
   ...     global X
   ...     X = 'NI'
   >>> func()
   >>> print(X)

5. Что выведет следующий код и почему?
   >>> X = 'Spam'
   >>> def func():
   ...     X = 'NI'
   ...     def nested():
   ...         print(X)
   ...     nested()
   >>> func()
   >>> X

6. Что выведет следующий код в Python 3.x и почему?
   >>> def func():
   ...     X = 'NI'
   ...     def nested():
   ...         nonlocal X
   ...         X = 'Spam'
   ...     nested()
   ...     print(X)
   >>> func()

7. Назовите три или большее количество способов сохранения информации о состоянии в функции Python.