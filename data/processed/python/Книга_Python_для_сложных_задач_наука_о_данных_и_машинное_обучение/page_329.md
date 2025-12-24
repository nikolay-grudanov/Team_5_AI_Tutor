---
source_image: page_329.png
page_number: 329
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.52
tokens: 7349
characters: 1304
timestamp: 2025-12-24T00:59:49.186464
finish_reason: stop
---

Здесь мы рассмотрим некоторые параметры конфигурации среды (rc) библиотеки Matplotlib и новую возможность — таблицы стилей (stylesheets), содержащие не-плохие наборы конфигураций по умолчанию.

Выполнение пользовательских настроек графиков вручную

Ранее в этой главе мы видели, что можно менять отдельные настройки графиков, получая в итоге нечто более приятное глазу, чем настройки по умолчанию. Эти настройки можно выполнять и для каждого графика отдельно. Например, вот довольно скучная гистограмма по умолчанию (рис. 4.81):

In[1]: import matplotlib.pyplot as plt
    plt.style.use('classic')
    import numpy as np
    %matplotlib inline

In[2]: x = np.random.randn(1000)
    plt.hist(x);

![Гистограмма в стиле библиотеки Matplotlib по умолчанию](../images/fig_4_81.png)

Рис. 4.81. Гистограмма в стиле библиотеки Matplotlib по умолчанию

Мы можем настроить ее вид вручную, превратив эту гистограмму в намного более приятный глазу график, показанный на рис. 4.82:

In[3]: # Используем серый фон
    ax = plt.axes(axisbg='#E6E6E6')
    ax.set_axisbelow(True)

    # Рисуем сплошные белые линии сетки
    plt.grid(color='w', linestyle='solid')

    # Скрываем основные линии осей координат
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Скрываем деления сверху и справа