---
source_image: page_496.png
page_number: 496
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.03
tokens: 7196
characters: 740
timestamp: 2025-12-24T01:03:52.643801
finish_reason: stop
---

ax.imshow(data[i].reshape(8, 8),
    cmap='binary', interpolation='nearest',
    clim=(0, 16))
plot_digits(digits.data)

![Цифры без шума](../images/5_88.png)
Рис. 5.88. Цифры без шума

Добавим случайный шум для создания зашумленного набора данных и нарисуем уже его (рис. 5.89):

In[14]: np.random.seed(42)
noisy = np.random.normal(digits.data, 4)
plot_digits(noisy)

![Цифры с добавленным Гауссовым случайным шумом](../images/5_89.png)
Рис. 5.89. Цифры с добавленным Гауссовым случайным шумом

Визуально очевидно, что изображения зашумлены и содержат фиктивные пиксели. Обучим алгоритм PCA на этих зашумленных данных, указав, что проекция должна сохранять 50 % дисперсии:

In[15]: pca = PCA(0.50).fit(noisy)
pca.n_components_

Out[15]: 12