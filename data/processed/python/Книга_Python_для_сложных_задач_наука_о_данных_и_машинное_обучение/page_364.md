---
source_image: page_364.png
page_number: 364
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.27
tokens: 7271
characters: 972
timestamp: 2025-12-24T01:00:28.262374
finish_reason: stop
---

2        4.7      3.2      1.3      0.2   setosa
3        4.6      3.1      1.5      0.2   setosa
4        5.0      3.6      1.4      0.2   setosa

Визуализация многомерных зависимостей между выборками сводится к вызову функции sns.pairplot (рис. 4.119):

In[13]: sns.pairplot(iris, hue='species', size=2.5);

![График пар, демонстрирующий зависимости между четырьмя переменными](../images/4.119.png)

Рис. 4.119. График пар, демонстрирующий зависимости между четырьмя переменными

Фасетные гистограммы

Иногда оптимальный способ представления данных — гистограммы подмножеств. Функция FacetGrid библиотеки Seaborn делает эту задачу элементарной. Рассмотрим данные, отображающие суммы, которые персонал ресторана получает в качестве чаевых, в зависимости от данных различных индикаторов (рис. 4.120):

In[14]: tips = sns.load_dataset('tips')
    tips.head()
Out[14]:    total_bill  tip  sex  smoker  day  time  size
    0         16.99  1.01  Female   No   Sun  Dinner   2