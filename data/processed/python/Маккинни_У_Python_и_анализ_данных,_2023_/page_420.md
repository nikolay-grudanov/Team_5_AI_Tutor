---
source_image: page_420.png
page_number: 420
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.42
tokens: 7527
characters: 1556
timestamp: 2025-12-24T02:51:50.336431
finish_reason: stop
---

13  hc      3440 non-null   float64
14  cy      2919 non-null   object
15  ll      2919 non-null   object
16  _heartbeat_  120 non-null   float64
17  kw      93 non-null     object
dtypes: float64(4), object(14)
memory usage: 500.8+ KB

In [30]: frame["tz"].head()
Out[30]:
0    America/New_York
1    America/Denver
2    America/New_York
3    America/Sao_Paulo
4    America/New_York
Name: tz, dtype: object

На выходе по запросу frame мы видим сводное представление, которое показывается для больших объектов DataFrame. Затем можно воспользоваться методом value_counts объекта Series:

In [31]: tz_counts = frame["tz"].value_counts()

In [32]: tz_counts.head()
Out[32]:
America/New_York    1251
521
America/Chicago     400
America/Los_Angeles 382
America/Denver       191
Name: tz, dtype: int64

Эти данные можно визуализировать с помощью библиотеки matplotlib. Графики можно сделать немного приятнее, подставив какое-нибудь значение вместо неизвестных или отсутствующих часовых поясов. Мы заменяем отсутствующие значения методом fillna, а для пустых строк используем индексирование булевым массивом:

In [33]: clean_tz = frame["tz"].fillna("Missing")

In [34]: clean_tz[clean_tz == ""] = "Unknown"

In [35]: tz_counts = clean_tz.value_counts()

In [36]: tz_counts.head()
Out[36]:
America/New_York    1251
Unknown             521
America/Chicago     400
America/Los_Angeles 382
America/Denver       191
Name: tz, dtype: int64

Теперь можно воспользоваться пакетом seaborn для построения горизонтальной столбчатой диаграммы (результат показан на рис. 13.1):