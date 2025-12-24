---
source_image: page_307.png
page_number: 307
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.08
tokens: 7366
characters: 958
timestamp: 2025-12-24T02:48:23.153967
finish_reason: stop
---

Рис. 9.18. Распределение по количеству гостей в группе за каждый день недели

Как видим, в выходные количество гостей в одной группе увеличивается.
Если перед построением графика данные необходимо как-то агрегировать, то пакет seaborn может существенно упростить жизнь (установите пакет командой install seaborn). Посмотрим, как с помощью seaborn посчитать процент чаевых в зависимости от дня (результат показан на рис. 9.19):

In [87]: import seaborn as sns

In [88]: tips["tip_pct"] = tips["tip"] / (tips["total_bill"] - tips["tip"])

In [89]: tips.head()
Out[89]:
   total_bill   tip smoker  day    time  size  tip_pct
0      16.99  1.01     No  Sun  Dinner    2  0.063204
1      10.34  1.66     No  Sun  Dinner    3  0.191244
2      21.01  3.50     No  Sun  Dinner    3  0.199886
3      23.68  3.31     No  Sun  Dinner    2  0.162494
4      24.59  3.61     No  Sun  Dinner    4  0.172069

In [90]: sns.barplot(x="tip_pct", y="day", data=tips, orient="h")