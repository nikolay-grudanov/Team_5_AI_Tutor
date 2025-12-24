---
source_image: page_468.png
page_number: 468
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.50
tokens: 7358
characters: 1333
timestamp: 2025-12-24T01:03:18.238498
finish_reason: stop
---

Out[14]: SVC(C=1000000.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

In[15]: plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
    plot_svc_decision_function(clf)
    plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1],
        s=300, lw=1, facecolors='none');
    
![Обучение ядерного SVM на наших данных](https://i.imgur.com/3Q5z5QG.png)

Рис. 5.61. Обучение ядерного SVM на наших данных

С помощью этого ядерного метода опорных векторов мы можем определить подходящую нелинейную границу решений. Такая методика ядерного преобразования часто используется в машинном обучении для превращения быстрых линейных методов в быстрые нелинейные, особенно для моделей, в которых можно воспользоваться kernel trick.

Настройка SVM: размытие отступов

До сих пор наше обсуждение касалось хорошо очищенных наборов данных, в которых существует идеальная граница решений. Но что, если данные в некоторой степени перекрываются?

Например, допустим, мы имеем дело со следующими данными (рис. 5.62):

In[16]: X, y = make_blobs(n_samples=100, centers=2,
    random_state=0, cluster_std=1.2)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn');