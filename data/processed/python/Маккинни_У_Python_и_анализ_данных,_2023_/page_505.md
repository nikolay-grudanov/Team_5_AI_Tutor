---
source_image: page_505.png
page_number: 505
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.84
tokens: 7634
characters: 2104
timestamp: 2025-12-24T02:54:19.388075
finish_reason: stop
---

В.5. СРЕДСТВА РАЗРАБОТКИ ПРОГРАММ

IPython не только является удобной средой для интерактивных вычислений и исследования данных, но и прекрасно оснащен для разработки программ. В приложениях для анализа данных прежде всего важно, чтобы код был правильным. К счастью, в IPython встроен отлично интегрированный и улучшенный отладчик Python pdb. Кроме того, код должен быть быстрым. Для этого в IPython имеются удобные встроенные средства хронометража и профилирования. Ниже я расскажу об этих инструментах подробнее.

Интерактивный отладчик
Отладчик IPython дополняет pdb завершением по нажатии клавиши Tab, подсветкой синтаксиса и контекстом для каждой строки трассировки исключения. Отлаживать программу лучше всего немедленно после возникновения ошибки. Команда %debug, выполненная сразу после исключения, вызывает «посмертный» отладчик и переходит в то место стека вызовов, где было возбуждено исключение:

In [2]: run examples/ipython_bug.py
---------------------------------------------------------------------------
AssertionError                                 Traceback (most recent call last)
/home/wesm/code/pydata-book/examples/ipython_bug.py in <module>()
    13     throws_an_exception()
    14
--> 15 calling_things()

/home/wesm/code/pydata-book/examples/ipython_bug.py in calling_things()
    11 def calling_things():
    12     works_fine()
--> 13     throws_an_exception()
    14
    15 calling_things()

/home/wesm/code/pydata-book/examples/ipython_bug.py in throws_an_exception()
     7     a = 5
     8     b = 6
---> 9     assert(a + b == 10)
    10
    11 def calling_things():

AssertionError:

In [3]: %debug
> /home/wesm/code/pydata-book/examples/ipython_bug.py(9)throws_an_exception()
    8     b = 6
---> 9     assert(a + b == 10)
    10
ipdb>

Находясь в отладчике, можно выполнять произвольный Python-код и просматривать все объекты и данные (которые интерпретатор «сохранил живыми») в каждом кадре стека. По умолчанию отладчик оказывается на самом нижнем уровне — там, где произошла ошибка. Клавиши u (вверх) и d (вниз) позволяют переходить с одного уровня стека на другой: