---
source_image: page_259.png
page_number: 259
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.34
tokens: 7581
characters: 1755
timestamp: 2025-12-24T02:47:07.226859
finish_reason: stop
---

a    2    3    4    5
b    2    9   10   11

In [29]: frame.swaplevel(0, 1).sort_index(level=0)
Out[29]:
state      Ohio      Colorado
color     Green     Red     Green
key2 key1
1         a        0       1       2
          b        6       7       8
2         a        3       4       5
          b        9      10      11

Производительность выборки данных из иерархически индексированных объектов будет гораздо выше, если индекс отсортирован лексикографически, начиная с самого внешнего уровня, т. е. в результате вызова sort_index(level=0) или sort_index().

Сводная статистика по уровню
У многих методов объектов DataFrame и Series, вычисляющих сводные и описательные статистики, имеется параметр level для задания уровня, на котором требуется производить агрегирование по конкретной оси. Рассмотрим тот же объект DataFrame, что и выше; мы можем суммировать по уровню для строк или для столбцов:

In [30]: frame.groupby(level="key2").sum()
Out[30]:
state  Ohio  Colorado
color  Green  Red  Green
key2
1      6      8      10
2     12     14     16

In [31]: frame.groupby(level="color", axis="columns").sum()
Out[31]:
color  Green  Red
key1 key2
a      1      2      1
       2      8      4
b      1     14      7
       2     20     10

Мы гораздо подробнее рассмотрим механизм groupby в главе 10.

Индексирование столбцами DataFrame
Не так уж редко возникает необходимость использовать один или несколько столбцов DataFrame в качестве индекса строк; альтернативно можно переместить индекс строк в столбцы DataFrame. Рассмотрим пример:

In [32]: frame = pd.DataFrame({"a": range(7), "b": range(7, 0, -1),
.....:           "c": ["one", "one", "one", "two", "two",
.....:                "two", "two"],
.....:           "d": [0, 1, 2, 0, 1, 2, 3]})