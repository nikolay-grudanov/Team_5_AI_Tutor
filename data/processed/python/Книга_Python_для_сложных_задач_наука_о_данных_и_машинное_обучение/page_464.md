---
source_image: page_464.png
page_number: 464
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.39
tokens: 7427
characters: 1444
timestamp: 2025-12-24T01:03:11.466136
finish_reason: stop
---

отступа, точки не меняют аппроксимацию! Формально дело в том, что эти точки не вносят вклада в используемую для обучения модели функцию потерь, так что их расположение и количество не имеет значения, если они не пересекают отступов.

Это можно увидеть, например, если построить график модели, обученной на первых 60 и первых 120 точках набора данных (рис. 5.57):

In[9]: def plot_svm(N=10, ax=None):
    X, y = make_blobs(n_samples=200, centers=2,
                      random_state=0, cluster_std=0.60)
    X = X[:N]
    y = y[:N]
    model = SVC(kernel='linear', C=1E10)
    model.fit(X, y)

    ax = ax or plt.gca()
    ax.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 6)
    plot_svc_decision_function(model, ax)

fig, ax = plt.subplots(1, 2, figsize=(16, 6))
fig.subplots_adjust(left=0.0625, right=0.95, wspace=0.1)
for axi, N in zip(ax, [60, 120]):
    plot_svm(N, axi)
    axi.set_title('N = {0}'.format(N))

![Влияние новых обучающих точек на модель SVM](https://i.imgur.com/3Q5z5QG.png)

Рис. 5.57. Влияние новых обучающих точек на модель SVM

На левом рисунке мы видим модель и опорные векторы для 60 обучающих точек. На правом рисунке мы удвоили количество обучающих точек, но модель не изменилась: три опорных вектора с левого рисунка остались опорными векторами и справа. Подобная невосприимчивость к тому, как именно ведут себя удаленные точки, — одна из сильных сторон модели SVM.