---
source_image: page_334.png
page_number: 334
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.79
tokens: 7224
characters: 883
timestamp: 2025-12-24T00:59:49.092703
finish_reason: stop
---

ggplot

В языке программирования R пакет ggplot — очень популярное средство визуализации. Стиль ggplot библиотеки Matplotlib подражает стилям по умолчанию из этого пакета (рис. 4.87):

In[13]: with plt.style.context('ggplot'):
    hist_and_lines()

![Стиль ggplot](../images/fig_4_87.png)

Рис. 4.87. Стиль ggplot

Стиль «байесовские методы для хакеров»

Существует замечательная онлайн-книга «Вероятностное программирование и байесовские методы для хакеров» (Probabilistic Programming and Bayesian Methods for Hackers, http://bit.ly/2fDJsKC). Она содержит рисунки, созданные с помощью библиотеки Matplotlib, и использует в книге для создания единообразного и приятного внешне стиля набор параметров rc. Этот стиль воспроизведен в таблице стилей bmh (рис. 4.88):

In[14]: with plt.style.context('bmh'):
    hist_and_lines()

![Стиль bmh](../images/fig_4_88.png)

Рис. 4.88. Стиль bmh