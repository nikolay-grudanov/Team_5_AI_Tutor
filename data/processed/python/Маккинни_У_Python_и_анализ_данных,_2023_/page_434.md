---
source_image: page_434.png
page_number: 434
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.49
tokens: 7547
characters: 1402
timestamp: 2025-12-24T02:52:09.967613
finish_reason: stop
---

13.3. Имена, которые давали детям в США за период с 1880 по 2010 год

In [106]: !head -n 10 datasets/babynames/yob1880.txt
Mary,F,7065
Anna,F,2604
Emma,F,2003
Elizabeth,F,1939
Minnie,F,1746
Margaret,F,1578
Ida,F,1472
Alice,F,1414
Bertha,F,1320
Sarah,F,1288

Поскольку поля разделены запятыми, файл можно загрузить в объект DataFrame методом pandas.read_csv:

In [107]: names1880 = pd.read_csv("datasets/babynames/yob1880.txt",
.....:                names=["name", "sex", "births"])

In [108]: names1880
Out[108]:
      name   sex  births
0     Mary    F     7065
1     Anna    F     2604
2     Emma    F     2003
3  Elizabeth    F     1939
4    Minnie    F     1746
...   ...   ...     ...
1995  Woodie   M       5
1996  Worthy   M       5
1997  Wright   M       5
1998   York    M       5
1999 Zachariah   M       5
[2000 rows x 3 columns]

В эти файлы включены только имена, которыми были названы не менее 5 младенцев в году, поэтому для простоты сумму значений в столбце sex можно считать общим числом родившихся в данном году младенцев:

In [109]: names1880.groupby("sex")[["births"]].sum()
Out[109]:
sex
F    90993
M   110493
Name: births, dtype: int64

Поскольку в каждом файле находятся данные только за один год, то первое, что нужно сделать, — собрать все данные в единый объект DataFrame и добавить поле year. Это легко сделать методом pandas.concat. Выполните следующий код в ячейке Jupyter: