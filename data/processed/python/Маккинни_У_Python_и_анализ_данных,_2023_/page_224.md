---
source_image: page_224.png
page_number: 224
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.38
tokens: 7654
characters: 1829
timestamp: 2025-12-24T02:46:05.284928
finish_reason: stop
---

In [72]: data.index.map(transform)
Out[72]: Index(['OHIO', 'COLO', 'NEW '], dtype='object')

Атрибуту index можно присваивать значение, т. е. модифицировать DataFrame на месте:

In [73]: data.index = data.index.map(transform)

In [74]: data
Out[74]:
    one   two   three   four
OHIO   0     1      2      3
COLO   4     5      6      7
NEW    8     9     10     11

Если требуется создать преобразованный вариант набора данных, не меняя оригинал, то будет полезен метод rename:

In [75]: data.rename(index=str.title, columns=str.upper)
Out[75]:
    ONE   TWO   THREE   FOUR
Ohio   0     1      2      3
Colo   4     5      6      7
New    8     9     10     11

Интересно, что rename можно использовать в сочетании с похожим на словарь объектом, который предоставляет новые значения для подмножества меток оси:

In [76]: data.rename(index={"OHIO": "INDIANA"},
        ....:         columns={"three": "peekaboo"})
Out[76]:
    one   two   peekaboo   four
INDIANA 0     1         2      3
COLO     4     5         6      7
NEW      8     9         10     11

Метод rename избавляет от необходимости копировать объект DataFrame вручную и присваивать значения его атрибутам index и columns.

Дискретизация и группировка по интервалам
Непрерывные данные часто дискретизируются или как-то иначе раскладываются по интервалам — «ящикам» — для анализа. Предположим, что имеются данные о группе лиц в каком-то исследовании и требуется разложить их по ящикам, соответствующим возрасту — дискретной величине:

In [77]: ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]

Разобьем множество возрастов на интервалы: от 18 до 25, от 26 до 35, от 35 до 60 и наконец от 61 и старше. Для этой цели в pandas есть функция pandas.cut:

In [78]: bins = [18, 25, 35, 60, 100]

In [79]: age_categories = pd.cut(ages, bins)

In [80]: age_categories