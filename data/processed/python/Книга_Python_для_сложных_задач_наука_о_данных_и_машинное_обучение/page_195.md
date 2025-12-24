---
source_image: page_195.png
page_number: 195
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.50
tokens: 7595
characters: 2019
timestamp: 2025-12-24T00:56:28.092455
finish_reason: stop
---

Похоже, что источник пустых значений по населению — Пуэрто-Рико, до 2000 года. Вероятно, это произошло из-за того, что необходимых данных не было в первоисточнике.

Мы видим, что некоторые из новых значений столбца state тоже пусты, а значит, в ключе объекта abbrevs отсутствовали соответствующие записи! Выясним, для каких территорий отсутствуют соответствующие значения:

In[24]: merged.loc[merged['state'].isnull(), 'state/region'].unique()

Out[24]: array(['PR', 'USA'], dtype=object)

Все понятно: наши данные по населению включают записи для Пуэрто-Рико (PR) и США в целом (USA), отсутствующие в ключе аббревиатуры штатов. Исправим это, вставив соответствующие записи:

In[25]: merged.loc[merged['state/region'] == 'PR', 'state'] = 'Puerto Rico'
        merged.loc[merged['state/region'] == 'USA', 'state'] = 'United States'
        merged.isnull().any()

Out[25]: state/region    False
          ages           False
          year            False
          population      True
          state           False
          dtype: bool

В столбце state больше нет пустых значений. Готово!

Теперь можно слить результат с данными по площади штатов с помощью аналогичной процедуры. После изучения имеющихся результатов становится понятно, что нужно выполнить соединение по столбцу state в обоих объектах:

In[26]: final = pd.merge(merged, areas, on='state', how='left')
        final.head()

Out[26]:   state/region  ages  year  population  state  area (sq. mi)
           0         AL  under18  2012  1117489.0  Alabama  52423.0
           1         AL    total  2012  4817528.0  Alabama  52423.0
           2         AL  under18  2010  1130966.0  Alabama  52423.0
           3         AL    total  2010  4785570.0  Alabama  52423.0
           4         AL  under18  2011  1125763.0  Alabama  52423.0

Выполним снова проверку на пустые значения, чтобы узнать, были ли какие-то несовпадения:

In[27]: final.isnull().any()

Out[27]: state/region    False
          ages           False
          year            False