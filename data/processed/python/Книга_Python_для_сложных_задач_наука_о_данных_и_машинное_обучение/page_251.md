---
source_image: page_251.png
page_number: 251
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 13.31
tokens: 7121
characters: 609
timestamp: 2025-12-24T00:57:39.145051
finish_reason: stop
---

Работа с временными рядами

![График среднего почасового количества велосипедов](../images/3_15.png)

Рис. 3.15. Среднее почасовое количество велосипедов

Нас могут также интересовать изменения ситуации по дням недели. Это можно выяснить с помощью операции groupby (рис. 3.16):

In[44]: by_weekday = data.groupby(data.index.dayofweek).mean()
    by_weekday.index = ['Mon', 'Tues', 'Wed', 'Thurs',
                         'Fri', 'Sat', 'Sun']
    by_weekday.plot(style=[':', '--', '-']);

![График среднего количества велосипедов по дням](../images/3_16.png)

Рис. 3.16. Среднее количество велосипедов по дням