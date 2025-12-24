---
source_image: page_366.png
page_number: 366
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 10.34
tokens: 7137
characters: 692
timestamp: 2025-12-24T01:00:28.263482
finish_reason: stop
---

In[17]: with sns.axes_style('white'):
    sns.jointplot("total_bill", "tip", data=tips, kind='hex')

![Пример графика факторов со сравнением распределений при различных дискретных факторах](../images/ch4_121.png)

Рис. 4.121. Пример графика факторов со сравнением распределений при различных дискретных факторах

In[18]: sns.jointplot("total_bill", "tip", data=tips, kind='reg');

![График совместного распределения](../images/ch4_122.png)

Рис. 4.122. График совместного распределения

График совместного распределения позволяет даже выполнять автоматическую ядерную оценку плотности распределения и регрессию (рис. 4.123):

In[18]: sns.jointplot("total_bill", "tip", data=tips, kind='reg');