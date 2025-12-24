---
source_image: page_303.png
page_number: 303
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.18
tokens: 7539
characters: 1901
timestamp: 2025-12-24T00:59:15.482876
finish_reason: stop
---

Карта цветов jet, использовавшаяся по умолчанию в библиотеке Matplotlib до версии 2.0, представляет собой пример качественной карты цветов. Ее выбор в качестве карты цветов по умолчанию был весьма неудачен, поскольку качественные карты цветов плохо подходят для отражения количественных данных: обычно они не отражают равномерного роста яркости при продвижении по шкале.

Продемонстрировать это можно путем преобразования шкалы цветов jet в черно-белое представление (рис. 4.51):

In[5]:
from matplotlib.colors import LinearSegmentedColormap

def grayscale_cmap(cmap):
    """Возвращает версию в оттенках серого заданной карты цветов"""
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))

    # Преобразуем RGBA в воспринимаемую глазом светимость серого цвета
    # ср. http://alienryderflex.com/hsp.html
    RGB_weight = [0.299, 0.587, 0.114]
    luminance = np.sqrt(np.dot(colors[:, :3] ** 2, RGB_weight))
    colors[:, :3] = luminance[:, np.newaxis]

    return LinearSegmentedColormap.from_list(cmap.name + "_gray", colors, cmap.N)

def view_colormap(cmap):
    """Рисует карту цветов в эквивалентных оттенках серого"""
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))

    cmap = grayscale_cmap(cmap)
    grayscale = cmap(np.arange(cmap.N))
    fig, ax = plt.subplots(2, figsize=(6, 2),
                           subplot_kw=dict(xticks=[], yticks=[]))
    ax[0].imshow([colors], extent=[0, 10, 0, 1])
    ax[1].imshow([grayscale], extent=[0, 10, 0, 1])

In[6]: view_colormap('jet')

![Карта цветов jet и ее неравномерная шкала светимости](https://i.imgur.com/3Q5z5QG.png)

Рис. 4.51. Карта цветов jet и ее неравномерная шкала светимости

Отметим яркие полосы в ахроматическом изображении. Даже в полном цвете эта неравномерная яркость означает, что определенные части диапазона цветов будут притягивать внимание, что потенциально приведет к акцентированию