---
source_image: page_531.png
page_number: 531
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.33
tokens: 7343
characters: 1124
timestamp: 2025-12-24T01:04:53.208184
finish_reason: stop
---

Редуцированное цветовое пространство: 16 цветов

![Два графика, показывающие редуцированное цветовое пространство с двумя осами: Красный и Зеленый (слева), Красный и Синий (справа)](https://i.imgur.com/3Q5z5QG.png)

Рис. 5.122. Шестнадцать кластеров в цветовом пространстве RGB

В результате исходные пиксели перекрашиваются в другие цвета: каждый пиксел получает цвет ближайшего центра кластера. Рисуя эти новые цвета в пространстве изображения вместо пространства пикселов, видим эффект от перекрашивания (рис. 5.123).

Первоначальное изображение	16-цветное изображение

![Два изображения: первоначальное (слева) и 16-цветное (справа)](https://i.imgur.com/7K8vJvL.png)

Рис. 5.123. Полноцветное изображение (слева) по сравнению с 16-цветным (справа)

In[24]:
china_recolored = new_colors.reshape(china.shape)

fig, ax = plt.subplots(1, 2, figsize=(16, 6),
    subplot_kw=dict(xticks=[], yticks=[]))
fig.subplots_adjust(wspace=0.05)
ax[0].imshow(china)
ax[0].set_title('Original Image', size=16) # Первоначальное изображение
ax[1].imshow(china_recolored)
ax[1].set_title('16-color Image', size=16); # 16-цветное изображение