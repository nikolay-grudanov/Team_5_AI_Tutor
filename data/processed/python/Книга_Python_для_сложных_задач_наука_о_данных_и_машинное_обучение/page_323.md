---
source_image: page_323.png
page_number: 323
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.43
tokens: 7367
characters: 1409
timestamp: 2025-12-24T00:59:37.801914
finish_reason: stop
---

In[4]: print(ax.xaxis.get_major_formatter())
    print(ax.xaxis.get_minor_formatter())

<matplotlib.ticker.LogFormatterMathText object at 0x107512780>
<matplotlib.ticker.NullFormatter object at 0x10752dc18>

Мы видим, что расположение меток как основных, так и промежуточных делений задает локатор LogLocator (что логично для логарифмического графика). Метки промежуточных делений форматируются форматером NullFormatter (это означает, что метки отображаться не будут).

Продемонстрируем несколько примеров настройки этих локаторов и форматеров для различных графиков.

Прячем деления и/или метки

Наиболее частая операция с делениями/метками — скрывание делений или меток с помощью классов plt.NullLocator() и plt.NullFormatter(), как показано на рис. 4.74:

In[5]: ax = plt.axes()
    ax.plot(np.random.rand(50))

    ax.yaxis.set_major_locator(plt.NullLocator())
    ax.xaxis.set_major_formatter(plt.NullFormatter())

![График со скрытыми метками делений (ось X) и скрытыми делениями (ось Y)](https://example.com/image.png)

Рис. 4.74. График со скрытыми метками делений (ось X) и скрытыми делениями (ось Y)

Обратите внимание, что мы убрали метки (но оставили деления/линии координатной сетки) с оси X, и убрали деления (а следовательно, и метки) с оси Y. Отсутствие делений может быть полезно во многих случаях, например, если нужно отобразить сетку изображений. Например, рассмотрим рис. 4.75, содержащий