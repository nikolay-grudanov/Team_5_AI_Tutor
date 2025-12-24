---
source_image: page_144.png
page_number: 144
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.49
tokens: 7374
characters: 892
timestamp: 2025-12-24T02:43:41.334879
finish_reason: stop
---

ключей в data (который зависит от того, в каком порядке ключи вставлялись в словарь):

In [50]: frame
Out[50]:
    state   year   pop
0   Ohio   2000   1.5
1   Ohio   2001   1.7
2   Ohio   2002   3.6
3   Nevada 2001   2.4
4   Nevada 2002   2.9
5   Nevada 2003   3.2

В Jupyter-блокноте объекты DataFrame отображаются в виде HTML-таблицы, более удобной для браузера. Пример см. на рис. 5.1.

![HTML-таблица DataFrame](https://i.imgur.com/3Q5z5QG.png)

Рис. 5.1. Вид объектов pandas DataFrame в Jupyter

Для больших объектов DataFrame метод head отбирает только первые пять строк:

In [51]: frame.head()
Out[51]:
    state   year   pop
0   Ohio   2000   1.5
1   Ohio   2001   1.7
2   Ohio   2002   3.6
3   Nevada 2001   2.4
4   Nevada 2002   2.9

Аналогично tail возвращает последние пять строк:

In [52]: frame.tail()
Out[52]:
    state   year   pop
1   Ohio   2001   1.7
2   Ohio   2002   3.6