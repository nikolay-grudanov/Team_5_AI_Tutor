---
source_image: page_497.png
page_number: 497
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.99
tokens: 7427
characters: 1677
timestamp: 2025-12-24T01:04:05.042728
finish_reason: stop
---

В данном случае 50% дисперсии соответствует 12 главным компонентам. Вычислим эти компоненты, после чего воспользуемся обратным преобразованием для восстановления отфильтрованных цифр (рис. 5.90):

In[16]: components = pca.transform(noisy)
        filtered = pca.inverse_transform(components)
        plot_digits(filtered)

![Цифры с устраненным с помощью метода РСА шумом](../images/5.90.png)

Рис. 5.90. Цифры с устраненным с помощью метода РСА шумом

Эти возможности по сохранению сигнала/фильтрации шума делают метод РСА очень удобной процедурой выбора признаков, например, вместо обучения классификатора на чрезвычайно многомерных данных можно обучить его на низкоразмерном представлении, что автоматически приведет к фильтрации случайного шума во входных данных.

Пример: метод Eigenfaces

Ранее мы рассмотрели пример использования проекции РСА в качестве процедуры выбора признаков для распознавания лиц с помощью метода опорных векторов (см. раздел «Заглянем глубже: метод опорных векторов» данной главы). Теперь мы вернемся к этому примеру и рассмотрим его подробнее. Напоминаю, что мы используем набор данных Labeled Faces in the Wild (LFW), доступный через библиотеку Scikit-Learn:

In[17]: from sklearn.datasets import fetch_lfw_people
        faces = fetch_lfw_people(min_faces_per_person=60)
        print(faces.target_names)
        print(faces.images.shape)

['Ariel Sharon' 'Colin Powell' 'Donald Rumsfeld' 'George W Bush'
 'Gerhard Schroeder' 'Hugo Chavez' 'Junichiro Koizumi' 'Tony Blair']
(1348, 62, 47)

Выясним, какие главные оси координат охватывают этот набор данных. Поскольку набор данных велик, воспользуемся классом RandomizedPCA — содержащийся в нем