---
source_image: page_210.png
page_number: 210
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.46
tokens: 7615
characters: 2193
timestamp: 2025-12-24T00:56:47.978526
finish_reason: stop
---

Теперь же я предложил бы углубиться в эти несколько строк кода и выполнить их пошагово, чтобы убедиться, что вы действительно понимаете, какой вклад в результат они вносят. Это в чем-то непростой пример, но благодаря хорошему пониманию элементов кода у вас появятся средства для исследования ваших собственных данных.

Сводные таблицы

Мы уже видели возможности по исследованию отношений в наборе данных, предоставляемые абстракцией GroupBy. Сводная таблица (pivot table) — схожая операция, часто встречающаяся в электронных таблицах и других программах, работающих с табличными данными. Сводная таблица получает на входе простые данные в виде столбцов и группирует записи в двумерную таблицу, обеспечивающую многомерное представление данных. Различие между сводными таблицами и операцией GroupBy иногда неочевидно. Лично мне помогает представлять сводные таблицы как многомерную версию агрегирующей функции GroupBy. То есть вы выполняете операцию «разбить, применить, объединить», но как разбиение, так и объединение происходят не на одномерном индексе, а на двумерной координатной сетке.

Данные для примеров работы со сводными таблицами

Для примеров из этого раздела мы воспользуемся базой данных пассажиров парохода «Титаник», доступной через библиотеку Seaborn (см. раздел «Визуализация с помощью библиотеки Seaborn» главы 4):

In[1]: import numpy as np
       import pandas as pd
       import seaborn as sns
       titanic = sns.load_dataset('titanic')

In[2]: titanic.head()

Out[2]:
   survived  pclass    sex  age  sibsp  parch     fare embarked class  who adult_male deck embark_town alive alone
0         0       3  male  22.0     1      0   7.2500        S  Third   man        True  NaN  Southampton  no  False
1         1       1 female  38.0     1      0  71.2833        C  First  woman      False    C  Cherbourg  yes  False
2         1       3 female  26.0     0      0   7.9250        S  Third  woman      False  NaN  Southampton  yes  True
3         1       1 female  35.0     1      0  53.1000        S  First  woman      False    C  Cherbourg  yes  False
4         0       3  male  35.0     0      0   8.0500        S  Third   man        True  NaN  Southampton  no  False