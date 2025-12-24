---
source_image: page_549.png
page_number: 549
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.74
tokens: 7438
characters: 1552
timestamp: 2025-12-24T01:05:27.753602
finish_reason: stop
---

In[6]: fig, ax = plt.subplots(1, 2, figsize=(12, 4),
    sharex=True, sharey=True,
    subplot_kw={'xlim':(-4, 9),
        'ylim':(-0.02, 0.3)})
    fig.subplots_adjust(wspace=0.05)
    for i, offset in enumerate([0.0, 0.6]):
        ax[i].hist(x, bins=bins + offset, normed=True)
        ax[i].plot(x, np.full_like(x, -0.01), '|k',
            markeredgewidth=1)

![Проблема гистограмм: различная интерпретация в зависимости от расположения интервалов](https://i.imgur.com/3Q5z5QG.png)

Рис. 5.141. Проблема гистограмм: различная интерпретация в зависимости от расположения интервалов

Из гистограммы слева очевидно, что мы имеем дело с бимодальным распределением. Справа же мы видим унимодальное распределение с длинным «хвостом». Без вышеприведенного кода вы бы вряд ли предположили, что эти две гистограммы были построены на одних данных. С учетом этого возникает вопрос: как можно доверять интуиции, полученной на основе подобных гистограмм? Что с этим можно сделать?

Небольшое отступление: гистограммы можно рассматривать как «стопки» блоков, в котором для каждой точки набора данных в соответствующий интервал помещается один блок. Посмотрим на это непосредственно (рис. 5.142):

In[7]: fig, ax = plt.subplots()
    bins = np.arange(-3, 8)
    ax.plot(x, np.full_like(x, -0.1), '|k',
        markeredgewidth=1)
    for count, edge in zip(*np.histogram(x, bins)):
        for i in range(count):
            ax.add_patch(plt.Rectangle((edge, i), 1, 1,
                alpha=0.5))
    ax.set_xlim(-4, 8)
    ax.set_ylim(-0.2, 8)

Out[7]: (-0.2, 8)