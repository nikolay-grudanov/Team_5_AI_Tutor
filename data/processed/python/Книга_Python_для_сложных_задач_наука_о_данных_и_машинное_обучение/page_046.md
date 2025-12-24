---
source_image: page_046.png
page_number: 46
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.66
tokens: 7333
characters: 1152
timestamp: 2025-12-24T00:52:31.667192
finish_reason: stop
---

Traceback (most recent call last):

    File "<ipython-input-4-b2e110f6fc8f>", line 1, in <module>
      func2(1)

    File "<ipython-input-1-d849e34d61fb>", line 7, in func2
      return func1(a, b)

    File "<ipython-input-1-d849e34d61fb>", line 2, in func1
      return a / b

ZeroDivisionError: division by zero

Режим Verbose добавляет еще некоторую информацию, включая аргументы для всех вызываемых функций:

In[5]: %xmode Verbose

Exception reporting mode: Verbose

In[6]: func2(1)
------------------------------------------------------------
ZeroDivisionError                                 Traceback (most recent call last)
<ipython-input-6-b2e110f6fc8f> in <module>()
----> 1 func2(1)
      global func2 = <function func2 at 0x103729320>

<ipython-input-1-d849e34d61fb> in func2(x=1)
      5     a = x
      6     b = x - 1
----> 7     return func1(a, b)
      global func1 = <function func1 at 0x1037294d0>
      a = 1
      b = 0

<ipython-input-1-d849e34d61fb> in func1(a=1, b=0)
      1 def func1(a, b):
----> 2     return a / b
      a = 1
      b = 0
      3
      4 def func2(x):
      5     a = x
ZeroDivisionError: division by zero