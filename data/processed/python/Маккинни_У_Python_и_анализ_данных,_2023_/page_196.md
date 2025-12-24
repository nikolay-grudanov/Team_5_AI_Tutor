---
source_image: page_196.png
page_number: 196
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.43
tokens: 7545
characters: 1359
timestamp: 2025-12-24T02:45:14.582528
finish_reason: stop
---

L   346.0
O   343.0
Q   340.0
M   338.0
J   337.0
F   335.0
K   334.0
H   330.0
dtype: float64

У объекта TextParser имеется также метод get_chunk, который позволяет читать куски произвольного размера.

Вывод данных в текстовом формате
Данные можно экспортитьровать в формате с разделителями. Рассмотрим одну из приведенных выше операций чтения CSV-файла:

In [48]: data = pd.read_csv("examples/ex5.csv")

In [49]: data
Out[49]:
    something   a   b   c   d   message
0      one     1   2  3.0   4      NaN
1     two     5   6   NaN   8   world
2   three     9  10 11.0  12      foo

С помощью метода to_csv объекта DataFrame мы можем вывести данные в файл через запятую:

In [50]: data.to_csv("examples/out.csv")

In [51]: !cat examples/out.csv
,something,a,b,c,d,message
0,one,1,2,3.0,4,
1,two,5,6,,8,world
2,three,9,10,11.0,12,foo

Конечно, допустимы и другие разделители (при выводе в sys.stdout результат отправляется на стандартный вывод, обычно на экран):

In [52]: import sys

In [53]: data.to_csv(sys.stdout, sep="|")
|something|a|b|c|d|message
0|one|1|2|3.0|4|
1|two|5|6|8|world
2|three|9|10|11.0|12|foo

Отсутствующие значения представлены пустыми строками. Но можно указать какой-нибудь другой маркер:

In [54]: data.to_csv(sys.stdout, na_rep="NULL")
,something,a,b,c,d,message
0,one,1,2,3.0,4,NULL
1,two,5,6,NULL,8,world
2,three,9,10,11.0,12,foo