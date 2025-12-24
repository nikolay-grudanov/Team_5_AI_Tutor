---
source_image: page_331.png
page_number: 331
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.54
tokens: 7258
characters: 1005
timestamp: 2025-12-24T00:59:43.175480
finish_reason: stop
---

In[5]: from matplotlib import cycler
    colors = cycler('color',
        ['#EE6666', '#3388BB', '#9988DD',
         '#EECC55', '#88BB44', '#FFBBBB'])
    plt.rc('axes', facecolor='#E6E6E6', edgecolor='none',
           axisbelow=True, grid=True, prop_cycle=colors)
    plt.rc('grid', color='w', linestyle='solid')
    plt.rc('xtick', direction='out', color='gray')
    plt.rc('ytick', direction='out', color='gray')
    plt.rc('patch', edgecolor='#E6E6E6')
    plt.rc('lines', linewidth=2)

Описав эти настройки, мы можем создать график и посмотреть на них в действии (рис. 4.83):

In[6]: plt.hist(x);

![Пользовательская гистограмма с настройками rc](https://i.imgur.com/1.png)

Рис. 4.83. Пользовательская гистограмма с настройками rc

Посмотрим, как выглядят с этими параметрами rc простые графики (рис. 4.84):

In[7]: for i in range(4):
    plt.plot(np.random.rand(10))

![Линейный график с пользовательскими стилями](https://i.imgur.com/2.png)

Рис. 4.84. Линейный график с пользовательскими стилями