---
source_image: page_107.png
page_number: 107
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.65
tokens: 7498
characters: 1899
timestamp: 2025-12-24T00:54:19.668148
finish_reason: stop
---

Массив булевых значений в библиотеке NumPy можно рассматривать как строку битов, где \(1 = \text{True}\) и \(0 = \text{False}\), а результат применения операторов \& и | аналогичен вышеприведенному:

In[37]: A = np.array([1, 0, 1, 0, 1, 0], dtype=bool)
       B = np.array([1, 1, 1, 0, 1, 1], dtype=bool)
       A | B

Out[37]: array([ True,  True,  True, False,  True,  True], dtype=bool)

Использование же ключевого слова or для этих массивов приведет к вычислению истинности или ложности всего объекта массива — не определенного формально значения:

In[38]: A or B

---------------------------------------------------------------------------
ValueError                                 Traceback (most recent call last)
<ipython-input-38-5d8e4f2e21c0> in <module>()
----> 1 A or B

ValueError: The truth value of an array with more than one element is...

При создании булева выражения с заданным массивом следует использовать операторы & и |, а не операции and или or:

In[39]: x = np.arange(10)
       (x > 4) & (x < 8)

Out[39]: array([False, False, ..., True, True, False, False], dtype=bool)

Попытка же вычислить истинность или ложность всего массива приведет к уже наблюдавшейся нами выше ошибке ValueError:

In[40]: (x > 4) and (x < 8)

---------------------------------------------------------------------------
ValueError                                 Traceback (most recent call last)
<ipython-input-40-3d24f1ffd63d> in <module>()
----> 1 (x > 4) and (x < 8)

ValueError: The truth value of an array with more than one element is...

Итак, запомните: операции and и or вычисляют единое булево значение для всего объекта, в то время как операторы & и | вычисляют много булевых значений для содержимого (отдельных битов или байтов) объекта. Второй из этих вариантов практически всегда будет именно той операцией, которая будет вам нужна при работе с булевыми массивами библиотеки NumPy.