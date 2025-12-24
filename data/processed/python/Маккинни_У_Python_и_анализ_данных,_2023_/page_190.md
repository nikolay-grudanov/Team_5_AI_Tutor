---
source_image: page_190.png
page_number: 190
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.53
tokens: 7619
characters: 1539
timestamp: 2025-12-24T02:45:04.013226
finish_reason: stop
---

6.1. Чтение и запись данных в текстовом формате

In [15]: pd.read_csv("examples/ex2.csv", names=["a", "b", "c", "d", "message"])
Out[15]:
    a   b   c   d message
0   1   2   3   4   hello
1   5   6   7   8   world
2   9  10  11  12   foo

Допустим, мы хотим, чтобы столбец message стал индексом возвращаемого объекта DataFrame. Этого можно добиться, задав аргумент index_col, в котором указать, что индексом будет столбец с номером 4 или с именем 'message':

In [16]: names = ["a", "b", "c", "d", "message"]

In [17]: pd.read_csv("examples/ex2.csv", names=names, index_col="message")
Out[17]:
      a   b   c   d
message
hello   1   2   3   4
world   5   6   7   8
foo     9  10  11  12

Если вы хотите сформировать иерархический индекс из нескольких столбцов (см. раздел 8.1), то просто передайте список их номеров или имен:

In [18]: !cat examples/csv_mindex.csv
key1,key2,value1,value2
one,a,1,2
one,b,3,4
one,c,5,6
one,d,7,8
two,a,9,10
two,b,11,12
two,c,13,14
two,d,15,16

In [19]: parsed = pd.read_csv("examples/csv_mindex.csv",
....:                 index_col=["key1", "key2"])

In [20]: parsed
Out[20]:
      value1 value2
key1 key2
one  a      1      2
     b      3      4
     c      5      6
     d      7      8
two  a      9     10
     b     11     12
     c     13     14
     d     15     16

Иногда в таблице нет фиксированного разделителя, а для разделения полей используются пробелы или еще какой-то символ. Рассмотрим такой текстовый файл:

In [21]: !cat examples/ex3.txt
A    B    C
aaa -0.264438 -1.026059 -0.619500