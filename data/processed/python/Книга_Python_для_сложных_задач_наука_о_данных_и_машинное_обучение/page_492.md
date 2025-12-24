---
source_image: page_492.png
page_number: 492
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.22
tokens: 7284
characters: 1114
timestamp: 2025-12-24T01:03:51.701410
finish_reason: stop
---

Начнем с загрузки данных:

In[9]: from sklearn.datasets import load_digits
    digits = load_digits()
    digits.data.shape

Out[9]:
(1797, 64)

Напоминаем, что данные состоят из изображений 8 × 8 пикселов, то есть 64-мерны. Чтобы понять зависимости между этими точками, воспользуемся методом РСА для проекции их в пространство более подходящей размерности, допустим, 2:

In[10]: pca = PCA(2)  # Проекция из 64-мерного в двумерное пространство
    projected = pca.fit_transform(digits.data)
    print(digits.data.shape)
    print(projected.shape)

(1797, 64)
(1797, 2)

Теперь можно построить график двух главных компонент каждой точки, чтобы получить больше информации о наших данных (рис. 5.84):

In[11]: plt.scatter(projected[:, 0], projected[:, 1],
    c=digits.target, edgecolor='none', alpha=0.5,
    cmap=plt.cm.get_cmap('spectral', 10))
    plt.xlabel('component 1') # Компонента 1
    plt.ylabel('component 2') # Компонента 2
    plt.colorbar();

![Пример применения метода РСА к данным по рукописным цифрам](https://i.imgur.com/3Q5z5QG.png)

Рис. 5.84. Применение метода РСА к данным по рукописным цифрам