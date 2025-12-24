---
source_image: page_147.png
page_number: 147
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.83
tokens: 7555
characters: 1419
timestamp: 2025-12-24T02:43:55.894059
finish_reason: stop
---

Когда столбцу присваивается список или массив, длина значения должна совпадать с длиной DataFrame. Если же присваивается объект Series, то его метки будут точно выровнены с индексом DataFrame, а в «дырки» будут вставлены значения NA:

In [65]: val = pd.Series([-1.2, -1.5, -1.7], index=["two", "four", "five"])

In [66]: frame2["debt"] = val

In [67]: frame2
Out[67]:
   year   state  pop  debt
0  2000    Ohio  1.5   NaN
1  2001    Ohio  1.7   NaN
2  2002    Ohio  3.6   NaN
3  2001  Nevada  2.4   NaN
4  2002  Nevada  2.9   NaN
5  2003  Nevada  3.2   NaN

Присваивание несуществующему столбцу приводит к созданию нового столбца.

Для удаления столбцов служит ключевое слово del, как и в обычном словаре. Для демонстрации работы del я сначала добавлю новый столбец булевых признаков, показывающих, находится ли в столбце state значение "Ohio":

In [68]: frame2["eastern"] = frame2["state"] == "Ohio"

In [69]: frame2
Out[69]:
   year   state  pop  debt  eastern
0  2000    Ohio  1.5   NaN   True
1  2001    Ohio  1.7   NaN   True
2  2002    Ohio  3.6   NaN   True
3  2001  Nevada  2.4   NaN  False
4  2002  Nevada  2.9   NaN  False
5  2003  Nevada  3.2   NaN  False

Новый столбец нельзя создать, пользуясь синтаксисом frame2.eastern.

Затем для удаления этого столбца я воспользуюсь методом del:

In [70]: del frame2["eastern"]

In [71]: frame2.columns
Out[71]: Index(['year', 'state', 'pop', 'debt'], dtype='object')