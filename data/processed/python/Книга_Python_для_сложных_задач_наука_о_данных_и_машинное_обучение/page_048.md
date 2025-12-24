---
source_image: page_048.png
page_number: 48
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.40
tokens: 7328
characters: 1078
timestamp: 2025-12-24T00:52:31.654104
finish_reason: stop
---

In[8]: %debug

> <ipython-input-1-d849e34d61fb>(2)func1()
    1 def func1(a, b):
----> 2      return a / b
        3

ipdb> up
> <ipython-input-1-d849e34d61fb>(7)func2()
    5      a = x
    6      b = x - 1
----> 7      return func1(a, b)

ipdb> print(x)
1
ipdb> up
> <ipython-input-6-b2e110f6fc8f>(1)<module>()
----> 1 func2(1)

ipdb> down
> <ipython-input-1-d849e34d61fb>(7)func2()
    5      a = x
    6      b = x - 1
----> 7      return func1(a, b)

ipdb> quit

Это позволяет быстро находить не только что вызвало ошибку, но и какие вызовы функций привели к ней.

Если вам необходимо, чтобы отладчик запускался автоматически при генерации исключения, можно воспользоваться «магической» функцией %pdb для включения такого автоматического поведения:

In[9]: %xmode Plain
    %pdb on
    func2(1)

Exception reporting mode: Plain
Automatic pdb calling has been turned ON

Traceback (most recent call last):

    File "<ipython-input-9-569a67d2d312>", line 3, in <module>
        func2(1)

    File "<ipython-input-1-d849e34d61fb>", line 7, in func2
        return func1(a, b)