---
source_image: page_361.png
page_number: 361
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 11.52
tokens: 7150
characters: 674
timestamp: 2025-12-24T01:00:23.104330
finish_reason: stop
---

In[7]: for col in 'xy':
    sns.kdeplot(data[col], shade=True)

![Использование ядерной оценки плотности для визуализации распределений](../images/4_114.png)

Рис. 4.114. Использование ядерной оценки плотности для визуализации распределений

С помощью функции distplot можно сочетать гистограммы и KDE (рис. 4.115):

In[8]: sns.distplot(data['x'])
    sns.distplot(data['y']);

![Совместный график ядерной оценки плотности и гистограммы](../images/4_115.png)

Рис. 4.115. Совместный график ядерной оценки плотности и гистограммы

Если передать функции kdeplot весь двумерный набор данных, можно получить двумерную визуализацию данных (рис. 4.116):

In[9]: sns.kdeplot(data);