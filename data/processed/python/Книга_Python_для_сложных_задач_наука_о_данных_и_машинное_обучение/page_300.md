---
source_image: page_300.png
page_number: 300
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.53
tokens: 7390
characters: 1553
timestamp: 2025-12-24T00:59:05.056487
finish_reason: stop
---

Отображение нескольких легенд

Иногда при построении графика необходимо добавить на него несколько легенд для одной и той же системы координат. К сожалению, библиотека Matplotlib не сильно упрощает эту задачу: используя стандартный интерфейс legend, можно создавать только одну легенду для всего графика. Если попытаться создать вторую легенду с помощью функций plt.legend() и ax.legend(), она просто перекроет первую. Решить эту проблему можно, создав изначально для легенды новый рисователь (artist), после чего добавить вручную второй рисователь на график с помощью низкоуровневого метода ax.add_artist() (рис. 4.48):

In[10]: fig, ax = plt.subplots()

    lines = []
    styles = ['-', '--', '-.', ':']
    x = np.linspace(0, 10, 1000)

    for i in range(4):
        lines += ax.plot(x, np.sin(x - i * np.pi / 2),
                         styles[i], color='black')
    ax.axis('equal')

    # Задаем линии и метки первой легенды
    ax.legend(lines[:2], ['line A', 'line B'],      # Линия А, линия В
              loc='upper right', frameon=False)

    # Создаем вторую легенду и добавляем рисователь вручную
    from matplotlib.legend import Legend
    leg = Legend(ax, lines[2:], ['line C', 'line D'], # Линия С, линия D
                 loc='lower right', frameon=False)
    ax.add_artist(leg);

![Разделенная на части легенда](../images/fig_4_48.png)

Рис. 4.48. Разделенная на части легенда

Мы мельком рассмотрели низкоуровневые объекты рисования, из которых состоит любой график библиотеки Matplotlib. Если вы заглянете в исходный код метода