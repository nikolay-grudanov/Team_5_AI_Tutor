---
source_image: page_526.png
page_number: 526
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.77
tokens: 7411
characters: 1498
timestamp: 2025-12-24T01:04:53.154959
finish_reason: stop
---

первый шаг извлечения смысла нового набора данных, для которого отсутствует какая-либо априорная информации о метках.

Начнем с загрузки цифр, а затем перейдем к поиску кластеров с помощью алгоритма KMeans. Напомним, что набор данных по цифрам состоит из 1797 выборок с 64 признаками, где каждый из признаков представляет собой яркость одного пикселя в изображении размером 8 × 8:

In[11]: from sklearn.datasets import load_digits
    digits = load_digits()
    digits.data.shape

Out[11]: (1797, 64)

Кластеризация выполняется так же, как и ранее:

In[12]: kmeans = KMeans(n_clusters=10, random_state=0)
    clusters = kmeans.fit_predict(digits.data)
    kmeans.cluster_centers_.shape

Out[12]: (10, 64)

В результате мы получили десять кластеров в 64-мерном пространстве. Обратите внимание, что и центры кластеров представляют собой 64-мерные точки, а значит, их можно интерпретировать как «типичные» цифры в кластере. Посмотрим, что представляют собой эти центры кластеров (рис. 5.118):

In[13]: fig, ax = plt.subplots(2, 5, figsize=(8, 3))
    centers = kmeans.cluster_centers_.reshape(10, 8, 8)
    for axi, center in zip(ax.flat, centers):
        axi.set(xticks=[], yticks=[])
        axi.imshow(center, interpolation='nearest', cmap=plt.cm.binary)

![Центры кластеров](https://i.imgur.com/3Q5z5QG.png)

Рис. 5.118. Центры кластеров

Как видим, алгоритм KMeans даже без меток способен определить кластеры, чьи центры представляют собой легко узнаваемые цифры, возможно, за исключением 1 и 8.