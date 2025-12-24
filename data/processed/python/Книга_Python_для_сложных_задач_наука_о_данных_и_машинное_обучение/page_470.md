---
source_image: page_470.png
page_number: 470
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.36
tokens: 7578
characters: 2094
timestamp: 2025-12-24T01:03:30.427748
finish_reason: stop
---

fig.subplots_adjust(left=0.0625, right=0.95, wspace=0.1)

for axi, C in zip(ax, [10.0, 0.1]):
    model = SVC(kernel='linear', C=C).fit(X, y)
    axi.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
    plot_svc_decision_function(model, axi)
    axi.scatter(model.support_vectors_[:, 0],
                model.support_vectors_[:, 1],
                s=300, lw=1, facecolors='none');
    axi.set_title('C = {0:.1f}'.format(C), size=14)

Оптимальное значение параметра C зависит от конкретного набора данных. Его следует настраивать с помощью перекрестной проверки или какой-либо аналогичной процедуры (дальнейшую информацию см. в разделе «Гиперпараметры и проверка модели» данной главы).

Пример: распознавание лиц

В качестве примера работы метода опорных векторов рассмотрим задачу распознавания лиц. Мы воспользуемся набором данных Labeled Faces in the Wild¹ (LFW), состоящим из нескольких тысяч упорядоченных фотографий различных общественных деятелей. В библиотеку Scikit-Learn встроена утилита для загрузки этого набора данных:

In[18]: from sklearn.datasets import fetch_lfw_people
    faces = fetch_lfw_people(min_faces_per_person=60)
    print(faces.target_names)
    print(faces.images.shape)

['Ariel Sharon' 'Colin Powell' 'Donald Rumsfeld' 'George W Bush'
 'Gerhard Schroeder' 'Hugo Chavez' 'Junichiro Koizumi' 'Tony Blair']
(1348, 62, 47)

Выведем на рисунок несколько из этих лиц, чтобы увидеть, с чем мы будем иметь дело (рис. 5.64):

In[19]: fig, ax = plt.subplots(3, 5)
    for i, axi in enumerate(ax.flat):
        axi.imshow(faces.images[i], cmap='bone')
        axi.set(xticks=[], yticks=[],
            xlabel=faces.target_names[faces.target[i]])

Каждое изображение содержит 62 × 47, то есть примерно 3000 пикселов. Мы можем рассматривать каждый пиксель как признак, но эффективнее использовать какой-либо препроцессор для извлечения более осмысленных признаков. В данном случае мы воспользуемся методом главных компонент (см. раздел «Заглянем глубже: метод главных компонент» данной главы) для извлечения 150 базовых компонент,

¹ См.: http://vis-www.cs.umass.edu/lfw/