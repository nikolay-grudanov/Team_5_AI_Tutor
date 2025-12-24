---
source_image: page_145.png
page_number: 145
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.61
tokens: 7536
characters: 1201
timestamp: 2025-12-24T02:43:51.603010
finish_reason: stop
---

3  Nevada  2001  2.4
4  Nevada  2002  2.9
5  Nevada  2003  3.2

Если задать последовательность столбцов, то столбцы DataFrame расположатся строго в указанном порядке:

In [53]: pd.DataFrame(data, columns=["year", "state", "pop"])
Out[53]:
   year  state  pop
0  2000   Ohio  1.5
1  2001   Ohio  1.7
2  2002   Ohio  3.6
3  2001  Nevada  2.4
4  2002  Nevada  2.9
5  2003  Nevada  3.2

Если запросить столбец, которого нет в data, то он будет заполнен значениями NaN:

In [54]: frame2 = pd.DataFrame(data, columns=["year", "state", "pop", "debt"])

In [55]: frame2
Out[55]:
   year  state  pop  debt
0  2000   Ohio  1.5    NaN
1  2001   Ohio  1.7    NaN
2  2002   Ohio  3.6    NaN
3  2001  Nevada  2.4    NaN
4  2002  Nevada  2.9    NaN
5  2003  Nevada  3.2    NaN

In [56]: frame2.columns
Out[56]: Index(['year', 'state', 'pop', 'debt'], dtype='object')

Столбец DataFrame можно извлечь как объект Series, воспользовавшись нотацией словарей, или с помощью атрибута:

In [57]: frame2["state"]
Out[57]:
0    Ohio
1    Ohio
2    Ohio
3  Nevada
4  Nevada
5  Nevada
Name: state, dtype: object

In [58]: frame2.year
Out[58]:
0    2000
1    2001
2    2002
3    2001
4    2002
5    2003
Name: year, dtype: int64