---
source_image: page_045.png
page_number: 45
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.62
tokens: 7390
characters: 1482
timestamp: 2025-12-24T00:52:37.437416
finish_reason: stop
---

возможность управлять количеством выводимой при генерации исключения информации. Рассмотрим следующий код:

In[1]: def func1(a, b):
        return a / b
    def func2(x):
        a = x
        b = x - 1
        return func1(a, b)

In[2]: func2(1)
---------------------------------------------------------------------------
ZeroDivisionError                       Traceback (most recent call last)
<ipython-input-2-b2e110f6fc8f^gt; in <module>()
----> 1 func2(1)

<ipython-input-1-d849e34d61fb> in func2(x)
      5     a = x
      6     b = x - 1
----> 7     return func1(a, b)

<ipython-input-1-d849e34d61fb> in func1(a, b)
      1 def func1(a, b):
----> 2     return a / b
      3
      4 def func2(x):
      5     a = x

ZeroDivisionError: division by zero

Вызов функции func2 приводит к ошибке, и чтение выведенной трассы позволяет нам в точности понять, что произошло. По умолчанию эта трасса включает несколько строк, описывающих контекст каждого из приведших к ошибке шагов. С помощью «магической» функции %xmode (сокращение от exception mode — режим отображения исключений) мы можем управлять тем, какая информация будет выведена.

Функция %xmode принимает на входе один аргумент, режим, для которого есть три значения: Plain (Простой), Context (По контексту) и Verbose (Расширенный). Режим по умолчанию — Context, вывод при котором показан выше. Режим Plain дает более сжатый вывод и меньше информации:

In[3]: %xmode Plain

Exception reporting mode: Plain

In[4]: func2(1)