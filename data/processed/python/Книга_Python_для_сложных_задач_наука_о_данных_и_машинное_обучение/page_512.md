---
source_image: page_512.png
page_number: 512
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.02
tokens: 7371
characters: 1411
timestamp: 2025-12-24T01:04:28.819508
finish_reason: stop
---

главных компонент» этой главы. Следующая команда позволяет скачать данные и кэшировать их в вашем домашнем каталоге для дальнейшего использования:

In[16]: from sklearn.datasets import fetch_lfw_people
    faces = fetch_lfw_people(min_faces_per_person=30)
    faces.data.shape

Out[16]: (2370, 2914)

Итак, у нас имеется 2370 изображений, каждое размером 2914 пикселов. Другими словами, изображения можно считать точками данных в 2914-мерном пространстве!

Быстро визуализируем несколько изображений, чтобы посмотреть, с чем мы имеем дело (рис. 5.104):

In[17]: fig, ax = plt.subplots(4, 8, subplot_kw=dict(xticks=[], yticks=[]))
    for i, axi in enumerate(ax.flat):
        axi.imshow(faces.images[i], cmap='gray')

![Примеры исходных лиц](../images/5.104.png)

Рис. 5.104. Примеры исходных лиц

Не помешает нарисовать низкоразмерное вложение 2914-мерных данных, чтобы ознакомиться с основными зависимостями между изображениями. Удобно также начать с вычисления РСА и изучения полученной доли объяснимой дисперсии. Это даст нам представление о том, сколько линейных признаков необходимо для описания этих данных (рис. 5.105):

In[18]: from sklearn.decomposition import RandomizedPCA
    model = RandomizedPCA(100).fit(faces.data)
    plt.plot(np.cumsum(model.explained_variance_ratio_))
    plt.xlabel('n components')      # Количество компонент
    plt.ylabel('cumulative variance'); # Интегральная дисперсия