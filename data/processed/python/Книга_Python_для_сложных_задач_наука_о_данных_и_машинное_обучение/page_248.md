---
source_image: page_248.png
page_number: 248
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 5.98
tokens: 6987
characters: 220
timestamp: 2025-12-24T00:57:29.065634
finish_reason: stop
---

In[40]: weekly = data.resample('W').sum()
weekly.plot(style=[':', '--', '-'])
plt.ylabel('Weekly bicycle count'); # Количество велосипедов еженедельно

Рис.

![График количества велосипедов по часам](../images/ch3_2.png)