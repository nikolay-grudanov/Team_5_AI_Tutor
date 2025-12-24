---
source_image: page_567.png
page_number: 567
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.46
tokens: 7546
characters: 1826
timestamp: 2025-12-24T01:05:48.259411
finish_reason: stop
---

Но сначала воспользуемся простым Гауссовым наивным байесовским классификатором, чтобы было с чем сравнивать:

In[9]: from sklearn.naive_bayes import GaussianNB
    from sklearn.cross_validation import cross_val_score
    cross_val_score(GaussianNB(), X_train, y_train)

Out[9]: array([ 0.9408785 ,  0.8752342 ,  0.93976823])

Как видим, на наших данных даже наивный байесовский алгоритм достигает более чем 90%-ной точности. Попробуем теперь метод опорных векторов с поиском по сетке из нескольких вариантов параметра C:

In[10]: from sklearn.svm import LinearSVC
    from sklearn.grid_search import GridSearchCV
    grid = GridSearchCV(LinearSVC(), {'C': [1.0, 2.0, 4.0, 8.0]})
    grid.fit(X_train, y_train)
    grid.best_score_

Out[10]: 0.98667684407744083

In[11]: grid.best_params_

Out[11]: {'C': 4.0}

Обучим этот оптимальный оцениватель на полном наборе данных:

In[12]: model = grid.best_estimator_
    model.fit(X_train, y_train)

Out[12]: LinearSVC(C=4.0, class_weight=None, dual=True,
    fit_intercept=True, intercept_scaling=1,
    loss='squared_hinge', max_iter=1000,
    multi_class='ovr', penalty='l2',
    random_state=None, tol=0.0001, verbose=0)

5. Выполняем поиск лиц в новом изображении.

Теперь, когда у нас есть модель, возьмем новое изображение и посмотрим, насколько хорошо она в нем себя покажет. Воспользуемся для простоты одним из изображений астронавтов (см. обсуждение этого вопроса в разделе «Предостережения и дальнейшие усовершенствования» этой главы), перемещая по нему скользящее окно и оценивая каждый фрагмент (рис. 5.151):

In[13]: test_image = skimage.data.astronaut()
    test_image = skimage.color.rgb2gray(test_image)
    test_image = skimage.transform.rescale(test_image, 0.5)
    test_image = test_image[:160, 40:180]

    plt.imshow(test_image, cmap='gray')
    plt.axis('off');