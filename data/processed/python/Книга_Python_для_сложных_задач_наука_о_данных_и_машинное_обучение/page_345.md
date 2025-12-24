---
source_image: page_345.png
page_number: 345
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.20
tokens: 7313
characters: 1232
timestamp: 2025-12-24T01:00:04.430601
finish_reason: stop
---

In[1]: %matplotlib inline
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.basemap import Basemap

Лишь несколько строк кода отделяет установку и импорт набора инструментов Basemap от построения географических графиков (построение графика на рис. 4.102 требует также наличия пакета PIL в Python 2 или пакета pillow в Python 3):

In[2]: plt.figure(figsize=(8, 8))
    m = Basemap(projection='ortho', resolution=None, lat_0=50, lon_0=-100)
    m.bluemarble(scale=0.5);

![Проекция Земли с помощью метода bluemarble](../images/chapter4/fig4_102.png)

Рис. 4.102. Проекция Земли с помощью метода bluemarble

Смысл передаваемых Basemap атрибутов мы обсудим далее.

Удобнее всего то, что отображаемая на рисунке сфера — не просто изображение, это полнофункциональная система координат Matplotlib, понимающая сферические координаты и позволяющая легко дорисовывать данные на карту! Например, можно взять другую картографическую проекцию, посмотреть на крупный план Северной Америки и нарисовать местоположение Сиэтла. Мы воспользуемся изображением на основе набора данных etopo (отражающим топографические элементы как на поверхности земли, так и находящиеся под океаном) в качестве фона карты (рис. 4.103):