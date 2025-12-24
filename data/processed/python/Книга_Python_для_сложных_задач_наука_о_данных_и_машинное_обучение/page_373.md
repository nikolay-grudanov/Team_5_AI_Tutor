---
source_image: page_373.png
page_number: 373
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.08
tokens: 7144
characters: 749
timestamp: 2025-12-24T01:00:49.204146
finish_reason: stop
---

в частности, метки на оси X перекрываются. Однако, поскольку результат — простой график Matplotlib, можно воспользоваться методами из раздела «Пользовательские настройки делений на осях координат» данной главы для настройки подобных вещей.

![Зависимости между величинами в «марафонском» наборе данных](https://i.imgur.com/3Q5z5QG.png)

Рис. 4.128. Зависимости между величинами в «марафонском» наборе данных

Кроме того, представляет интерес различие между мужчинами и женщинами. Рассмотрим гистограмму коэффициентов распределения сил для этих двух групп (рис. 4.129):

In[33]: sns.kdeplot(data.split_frac[data.gender=='M'], label='men', shade=True)
sns.kdeplot(data.split_frac[data.gender=='W'], label='women', shade=True)
plt.xlabel('split_frac');