---
source_image: page_362.png
page_number: 362
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 8.96
tokens: 7058
characters: 410
timestamp: 2025-12-24T01:00:20.707330
finish_reason: stop
---

Рис. 4.116. Двумерный график ядерной оценки плотности

Посмотреть на совместное распределение и частные распределения можно, воспользовавшись функцией sns.jointplot. Для этого графика мы зададим стиль с белым фоном (рис. 4.117):

In[10]: with sns.axes_style('white'):
        sns.jointplot("x", "y", data, kind='kde');

Рис. 4.117. График совместного распределения с двумерным графиком ядерной оценки плотности