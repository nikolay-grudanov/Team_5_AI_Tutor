---
source_image: page_529.png
page_number: 529
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.80
tokens: 7358
characters: 1245
timestamp: 2025-12-24T01:04:53.348307
finish_reason: stop
---

In[18]: # Обратите внимание: для работы этого кода
    # должен быть установлен пакет pillow
    from sklearn.datasets import load_sample_image
    china = load_sample_image("china.jpg")
    ax = plt.axes(xticks=[], yticks=[])
    ax.imshow(china);

![Исходное изображение](https://i.imgur.com/3Q5z5QG.png)

Рис. 5.120. Исходное изображение

Само изображение хранится в трехмерном массиве размера (высота, ширина, RGB), содержащем вклад в цвет по красному/синему/зеленому каналам в виде целочисленных значений от 0 до 255:

In[19]: china.shape

Out[19]: (427, 640, 3)

Этот набор пикселов можно рассматривать как облако точек в трехмерном цветовом пространстве. Изменим форму данных на [n_samples × n_features] и масштабируем шкалу цветов так, чтобы они располагались между 0 и 1:

In[20]: data = china / 255.0 # используем шкалу 0...1
    data = data.reshape(427 * 640, 3)
    data.shape

Out[20]: (273280, 3)

Визуализируем эти пиксели в данном цветовом пространстве, используя подмножество из 10 000 пикселов для быстроты работы (рис. 5.121):

In[21]:
    def plot_pixels(data, title, colors=None, N=10000):
        if colors is None:
            colors = data

        # Выбираем случайное подмножество
        rng = np.random.RandomState(0)