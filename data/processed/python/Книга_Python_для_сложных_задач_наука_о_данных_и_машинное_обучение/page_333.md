---
source_image: page_333.png
page_number: 333
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.15
tokens: 7223
characters: 857
timestamp: 2025-12-24T00:59:49.030988
finish_reason: stop
---

Стиль по умолчанию

Стиль по умолчанию — тот, который мы видели до сих пор во всей книге. Начнем с него. Во-первых, восстановим нашу конфигурацию среды к имевшимся в блокноте значениям по умолчанию:

In[10]: # Восстанавливаем rcParams
    plt.rcParams.update(IPython_default);

Теперь посмотрим, как выглядят наши графики (рис. 4.85):

In[11]: hist_and_lines()

![Графики по умолчанию](../images/fig_4_85.png)

Рис. 4.85. Стиль библиотеки Matplotlib по умолчанию

Стиль FiveThirtyEight

Стиль FiveThirtyEight подражает оформлению популярного сайта FiveThirtyEight (http://fivethirtyeight.com/). Как вы можете видеть на рис. 4.86, он включает жирные шрифты, толстые линии и прозрачные оси координат.

In[12]: with plt.style.context('fivethirtyeight'):
    hist_and_lines()

![Графики FiveThirtyEight](../images/fig_4_86.png)

Рис. 4.86. Стиль FiveThirtyEight