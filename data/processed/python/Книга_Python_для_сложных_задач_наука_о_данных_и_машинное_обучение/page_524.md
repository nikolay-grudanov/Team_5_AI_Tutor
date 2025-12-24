---
source_image: page_524.png
page_number: 524
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.31
tokens: 7388
characters: 1485
timestamp: 2025-12-24T01:04:44.760607
finish_reason: stop
---

In[8]: from sklearn.datasets import make_moons
    X, y = make_moons(200, noise=.05, random_state=0)

In[9]: labels = KMeans(2, random_state=0).fit_predict(X)
    plt.scatter(X[:, 0], X[:, 1], c=labels,
                s=50, cmap='viridis');

![Рис. 5.116. Неудача метода k-средних в случае нелинейных границ](../images/5_116.png)

Рис. 5.116. Неудача метода k-средних в случае нелинейных границ

Ситуация напоминает обсуждавшееся в разделе «Заглянем глубже: метод опорных векторов» этой главы, где мы использовали ядерное преобразование для проецирования данных в пространство более высокой размерности, в котором возможно линейное разделение. Можно попробовать воспользоваться той же уловкой, чтобы метод k-средних стал распознавать нелинейные границы.

Одна из версий этого ядерного метода k-средних реализована в библиотеке Scikit-Learn в оценивателе SpectralClustering. Она использует граф ближайших соседей для вычисления представления данных более высокой размерности, после чего задает соответствие меток с помощью алгоритма k-средних (рис. 5.117):

In[10]: from sklearn.cluster import SpectralClustering
    model = SpectralClustering(n_clusters=2,
        affinity='nearest_neighbors',
        assign_labels='kmeans')
    labels = model.fit_predict(X)
    plt.scatter(X[:, 0], X[:, 1], c=labels,
                s=50, cmap='viridis');

Как видим, метод k-средних с помощью этого ядерного преобразования способен обнаруживать более сложные нелинейные границы между кластерами.