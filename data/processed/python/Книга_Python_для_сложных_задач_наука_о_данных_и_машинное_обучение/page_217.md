---
source_image: page_217.png
page_number: 217
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 6.81
tokens: 7050
characters: 493
timestamp: 2025-12-24T00:56:39.197999
finish_reason: stop
---

С помощью этого можно построить график дней рождения в зависимости от дня недели за несколько десятилетий (рис. 3.3):

In[19]:
import matplotlib.pyplot as plt
import matplotlib as mpl

births.pivot_table('births', index='dayofweek',
                   columns='decade', aggfunc='mean').plot()
plt.gca().set_xticklabels(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
plt.ylabel('mean births by day'); # среднее количество новорожденных в день

День недели

Среднее количество новорожденн