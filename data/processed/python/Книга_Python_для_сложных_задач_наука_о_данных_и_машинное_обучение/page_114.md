---
source_image: page_114.png
page_number: 114
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.08
tokens: 7225
characters: 980
timestamp: 2025-12-24T00:54:19.471419
finish_reason: stop
---

необходимо быстро выяснить, как они распределяются по массиву интервалов. Это можно сделать с помощью метода at() универсальных функций следующим образом:

In[23]: np.random.seed(42)
    x = np.random.randn(100)

    # Рассчитываем гистограмму вручную
    bins = np.linspace(-5, 5, 20)
    counts = np.zeros_like(bins)

    # Ищем подходящий интервал для каждого x
    i = np.searchsorted(bins, x)

    # Добавляем 1 к каждому из интервалов
    np.add.at(counts, i, 1)

Полученные числа отражают количество точек в каждом из интервалов, другими словами, гистограмму (рис. 2.9):

In[24]: # Визуализируем результаты
    plt.plot(bins, counts, linestyle='steps');

![Вычисленная вручную гистограмма](https://i.imgur.com/3Q5z5QG.png)

Рис. 2.9. Вычисленная вручную гистограмма

Получать каждый раз гистограмму таким образом нет необходимости. Библиотека Matplotlib предоставляет процедуру plt.hist(), которая делает то же самое одной строкой кода:

plt.hist(x, bins, histtype='step');