---
source_image: page_471.png
page_number: 471
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.30
tokens: 7253
characters: 1275
timestamp: 2025-12-24T01:03:15.794768
finish_reason: stop
---

которые мы передадим нашему классификатору на основе метода опорных векторов. Упростим эту задачу, объединив препроцессор и классификатор в единый конвейер:

In[20]: from sklearn.svm import SVC
        from sklearn.decomposition import RandomizedPCA
        from sklearn.pipeline import make_pipeline

        pca = RandomizedPCA(n_components=150, whiten=True, random_state=42)
        svc = SVC(kernel='rbf', class_weight='balanced')
        model = make_pipeline(pca, svc)

![Примеры из набора данных Labeled Faces in the Wild](https://i.imgur.com/3Q5z5QG.png)

Рис. 5.64. Примеры из набора данных Labeled Faces in the Wild

Для контроля результатов работы нашего классификатора разобьем данные на обучающую и контрольную последовательности:

In[21]: from sklearn.cross_validation import train_test_split
        Xtrain, Xtest, ytrain, ytest = train_test_split(faces.data,
                                                      faces.target,
                                                      random_state=42)

Наконец, воспользуемся поиском по сетке с перекрестной проверкой для анализа сочетаний параметров. Подберем значения параметров C (управляющего размытием отступов) и gamma (управляющего размером ядра радиальной базисной функции) и определим оптимальную модель: