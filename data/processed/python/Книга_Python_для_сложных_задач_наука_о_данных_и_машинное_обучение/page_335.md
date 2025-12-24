---
source_image: page_335.png
page_number: 335
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.47
tokens: 7177
characters: 789
timestamp: 2025-12-24T00:59:53.991288
finish_reason: stop
---

Темный фон

Для используемых в презентациях рисунков часто удобнее темный, а не светлый фон. Эту возможность предоставляет стиль dark_background (рис. 4.89):

In[15]: with plt.style.context('dark_background'):
    hist_and_lines()

![Стиль dark_background](../images/fig_4_89.png)

Рис. 4.89. Стиль dark_background

Оттенки серого

Иногда приходится готовить для печатного издания черно-белые рисунки. Для этого может пригодиться стиль grayscale, продемонстрированный на рис. 4.90:

In[16]: with plt.style.context('grayscale'):
    hist_and_lines()

![Стиль grayscale](../images/fig_4_90.png)

Рис. 4.90. Стиль grayscale

Стиль Seaborn

В библиотеке Matplotlib есть также стили, источником вдохновения для которых послужила библиотека Seaborn (обсуждаемая подробнее в разделе «Визуализация