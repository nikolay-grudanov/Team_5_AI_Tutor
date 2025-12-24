---
source_image: page_315.png
page_number: 315
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.64
tokens: 7370
characters: 1421
timestamp: 2025-12-24T00:59:30.253854
finish_reason: stop
---

import matplotlib as mpl
plt.style.use('seaborn-whitegrid')
import numpy as np
import pandas as pd

Пример: влияние выходных дней на рождение детей в США

Вернемся к данным, с которыми мы работали ранее в разделе «Пример: данные о рождаемости» главы 3, где мы сгенерировали график среднего количества рождений детей в зависимости от дня календарного года. Эти данные можно скачать по адресу https://raw.githubusercontent.com/jakevdp/data-CDCbirths/master/births.csv.

Начнем с той же процедуры очистки данных, которую мы использовали ранее, и построим график результатов (рис. 4.67):

In[2]:
births = pd.read_csv('births.csv')

quartiles = np.percentile(births['births'], [25, 50, 75])
mu, sig = quartiles[1], 0.74 * (quartiles[2] - quartiles[0])
births = births.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')

births['day'] = births['day'].astype(int)

births.index = pd.to_datetime(10000 * births.year +
    100 * births.month +
    births.day, format='%Y%m%d')
births_by_date = births.pivot_table('births',
    [births.index.month, births.index.day])
births_by_date.index = [pd.datetime(2012, month, day)
    for (month, day) in births_by_date.index]

In[3]: fig, ax = plt.subplots(figsize=(12, 4))
    births_by_date.plot(ax=ax);

![Среднее ежедневное количество новорожденных в зависимости от даты](../images/fig_4_67.png)

Рис. 4.67. Среднее ежедневное количество новорожденных в зависимости от даты