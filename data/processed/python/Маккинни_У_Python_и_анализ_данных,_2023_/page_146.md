---
source_image: page_146.png
page_number: 146
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.86
tokens: 7566
characters: 1504
timestamp: 2025-12-24T02:43:52.043493
finish_reason: stop
---

Возможность доступа к столбцам как к атрибутам (например, frame2.year) и автозавершение имен столбцов по нажатии Tab предоставляются в IPython для удобства.

Синтаксис frame2[column] работает для любого имени столбца, а frame2.column — только когда имя столбца — допустимое имя переменной Python, не конфликтующее с именами методов DataFrame. Например, если имя столбца содержит пробелы или еще какие-то специальные символы, отличные от знака подчеркивания, то употреблять его в качестве имени атрибута после точки нельзя.

Отметим, что возвращенный объект Series имеет тот же индекс, что и DataFrame, а его атрибут name установлен соответствующим образом.

Строки также можно извлечь по позиции или по имени с помощью специальных атрибутов iloc и loc (подробнее об этом см. в разделе «Выборка из DataFrame с помощью loc и iloc» ниже):

In [59]: frame2.loc[1]
Out[59]:
year    2001
state   Ohio
pop     1.7
debt    NaN
Name: 1, dtype: object

In [60]: frame2.iloc[2]
Out[60]:
year    2002
state   Ohio
pop     3.6
debt    NaN
Name: 2, dtype: object

Столбцы можно модифицировать путем присваивания. Например, пустому столбцу debt можно было бы присвоить скалярное значение или массив значений:

In [61]: frame2["debt"] = 16.5

In [62]: frame2
Out[62]:

   year  state  pop  debt
0  2000  Ohio   1.5  16.5
1  2001  Ohio   1.7  16.5
2  2002  Ohio   3.6  16.5
3  2001  Nevada  2.4  16.5
4  2002  Nevada  2.9  16.5
5  2003  Nevada  3.2  16.5

In [63]: frame2["debt"] = np.arange(6.)

In [64]: frame2
Out[64]: