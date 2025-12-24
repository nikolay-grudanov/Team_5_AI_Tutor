---
source_image: page_405.png
page_number: 405
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.66
tokens: 7345
characters: 1325
timestamp: 2025-12-24T01:01:39.249356
finish_reason: stop
---

Обучение без учителя: понижение размерности

Хотелось бы визуализировать наши точки в 64-мерном параметрическом пространстве, но эффективно визуализировать точки в пространстве такой высокой размерности непросто. Понизим вместо этого количество измерений до 2, воспользовавшись методом обучения без учителя. Здесь мы будем применять алгоритм обучения на базе многообразий под названием Isomap (см. раздел «Заглянем глубже: обучение на базе многообразий» этой главы) и преобразуем данные в двумерный вид:

In[26]: from sklearn.manifold import Isomap
    iso = Isomap(n_components=2)
    iso.fit(digits.data)
    data_projected = iso.transform(digits.data)
    data_projected.shape

Out[26]: (1797, 2)

Теперь наши данные стали двумерными. Построим график этих данных, чтобы увидеть, можно ли что-то понять из их структуры (рис. 5.19):

In[27]: plt.scatter(data_projected[:, 0], data_projected[:, 1],
    c=digits.target, edgecolor='none', alpha=0.5,
    cmap=plt.cm.get_cmap('spectral', 10))
plt.colorbar(label='digit label', ticks=range(10))
plt.clim(-0.5, 9.5);

![Isomap-вложение набора данных цифр](https://i.imgur.com/3Q5z5QG.png)

Рис. 5.19. Isomap-вложение набора данных цифр

Этот график дает нам представление о разделении различных цифр в 64-мерном пространстве. Например, нули (отображаемые черным цветом) и единицы