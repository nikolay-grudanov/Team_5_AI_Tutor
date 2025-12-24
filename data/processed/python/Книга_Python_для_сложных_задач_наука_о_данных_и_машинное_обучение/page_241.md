---
source_image: page_241.png
page_number: 241
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.26
tokens: 7123
characters: 655
timestamp: 2025-12-24T00:57:23.046352
finish_reason: stop
---

разница между ними заключается в том, что resample() выполняет агрегирование данных, а asfreq() — выборку данных.

Рассмотрим, что возвращают эти два метода для данных по ценам закрытия Google при понижающей дискретизации данных. Здесь мы выполняем передискретизацию данных на конец финансового года (рис. 3.6).

![График изменения цен акций Google с течением времени](../images/fig_3_5.png)

**Рис. 3.5.** График изменения цен акций Google с течением времени

![Передискретизация цен акций Google](../images/fig_3_6.png)

**Рис. 3.6.** Передискретизация цен акций Google

In[29]: goog.plot(alpha=0.5, style='-')
goog.resample('BA').mean().plot(style=':')