---
source_image: page_220.png
page_number: 220
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.78
tokens: 7469
characters: 1215
timestamp: 2025-12-24T02:45:53.756260
finish_reason: stop
---

А метод drop_duplicates возвращает DataFrame, содержащий только строки, которым в массиве, возвращенном методом duplicated, соответствует значение False:

In [52]: data.drop_duplicates()
Out[52]:
   k1  k2
0  one   1
1  two   1
2  one   2
3  two   3
4  one   3
5  two   4

По умолчанию оба метода принимают во внимание все столбцы, но можно указать произвольное подмножество столбцов, которые необходимо исследовать на наличие дубликатов. Допустим, есть еще один столбец значений, и мы хотим отфильтровать строки, которые содержат повторяющиеся значения только в столбце 'k1':

In [53]: data["v1"] = range(7)

In [54]: data
Out[54]:
   k1  k2  v1
0  one   1   0
1  two   1   1
2  one   2   2
3  two   3   3
4  one   3   4
5  two   4   5
6  two   4   6

In [55]: data.drop_duplicates(subset=["k1"])

Out[55]:
   k1  k2  v1
0  one   1   0
1  two   1   1

По умолчанию методы duplicated и drop_duplicates оставляют первую встретившуюся строку с данной комбинацией значений. Но если задать параметр keep="last", то будет оставлена последняя строка:

In [56]: data.drop_duplicates(["k1", "k2"], keep="last")
Out[56]:
   k1  k2  v1
0  one   1   0
1  two   1   1
2  one   2   2
3  two   3   3
4  one   3   4
6  two   4   6