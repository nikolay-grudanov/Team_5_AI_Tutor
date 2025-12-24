---
source_image: page_421.png
page_number: 421
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.75
tokens: 7466
characters: 1281
timestamp: 2025-12-24T02:51:47.632663
finish_reason: stop
---

In [38]: import seaborn as sns

In [39]: subset = tz_counts.head()

In [40]: sns.barplot(y=subset.index, x=subset.to_numpy())

![Bar chart showing the first 10 time zones from the 1.usa.gov dataset](https://i.imgur.com/5zJvJvG.png)

Рис. 13.1. Первые 10 часовых поясов из набора данных 1.usa.gov

Поле a содержит информацию о браузере, устройстве или приложении, выполнившем сокращение URL:

In [41]: frame["a"][1]
Out[41]: 'GoogleMaps/RochesterNY'

In [42]: frame["a"][50]
Out[42]: 'Mozilla/5.0 (Windows NT 5.1; rv:10.0.2) Gecko/20100101 Firefox/10.0.2'

In [43]: frame["a"][51][:50] # long line
Out[43]: 'Mozilla/5.0 (Linux; U; Android 2.2.2; en-us; LG-P9'

Выделение всей интересной информации из таких строк «пользовательских агентов» поначалу может показаться пугающей задачей. Одна из возможных стратегий — вырезать из строки первую лексему (грубо описывающую возможности браузера) и представить поведение пользователя в другом разрезе:

In [44]: results = pd.Series([x.split()[0] for x in frame["a"].dropna()])

In [45]: results.head(5)
Out[45]:
0    Mozilla/5.0
1    GoogleMaps/RochesterNY
2    Mozilla/4.0
3    Mozilla/5.0
4    Mozilla/5.0
dtype: object

In [46]: results.value_counts().head(8)
Out[46]:
Mozilla/5.0    2594
Mozilla/4.0    601
GoogleMaps/RochesterNY    121