---
source_image: page_326.png
page_number: 326
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.17
tokens: 7394
characters: 1307
timestamp: 2025-12-24T00:59:42.741400
finish_reason: stop
---

подходил для широкого спектра ситуаций, оно работает неплохо, но иногда требуется нечто большее. Рассмотрим показанный на рис. 4.78 график синуса и косинуса:

In[9]: # Строим графики синуса и косинуса
    fig, ax = plt.subplots()
    x = np.linspace(0, 3 * np.pi, 1000)
    ax.plot(x, np.sin(x), lw=3, label='Sine')
    ax.plot(x, np.cos(x), lw=3, label='Cosine')

    # Настраиваем сетку, легенду и задаем пределы осей координат
    ax.grid(True)
    ax.legend(frameon=False)
    ax.axis('equal')
    ax.set_xlim(0, 3 * np.pi);

![График по умолчанию с целочисленными делениями](https://i.imgur.com/1234567.png)

Рис. 4.78. График по умолчанию с целочисленными делениями

Хотелось бы внести несколько изменений. Во-первых, для такого рода данных лучше располагать деления и линии сетки по кратным числу \( \pi \) точках. Сделать это можно путем задания локатора MultipleLocator, располагающего деления в точках, кратных переданному ему числу. В дополнение добавим промежуточные деления в точках, кратных \( \pi / 4 \) (рис. 4.79):

In[10]: ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
        ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 4))
        fig

![Деления в точках, кратных \( \pi / 2 \)](https://i.imgur.com/7654321.png)

Рис. 4.79. Деления в точках, кратных \( \pi / 2 \)