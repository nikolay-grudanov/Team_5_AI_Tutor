---
source_image: page_505.png
page_number: 505
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.97
tokens: 7262
characters: 1079
timestamp: 2025-12-24T01:04:12.640927
finish_reason: stop
---

Рис. 5.97. MDS-вложение, вычисленное на основе попарных расстояний между точками

MDS как обучение на базе многообразий

Полезность этого метода становится еще очевиднее, если учесть, что матрицы расстояний можно вычислить для данных любой размерности. Так, например, вместо вращения данных в двумерном пространстве можно спроектировать их в трехмерное пространство с помощью следующей функции (по существу, это трехмерное обобщение матрицы вращения, с которой мы имели дело ранее):

In[9]:
    def random_projection(X, dimension=3, rseed=42):
        assert dimension >= X.shape[1]
        rng = np.random.RandomState(rseed)
        C = rng.randn(dimension, dimension)
        e, V = np.linalg.eigh(np.dot(C, C.T))
        return np.dot(X, V[:X.shape[1]])

    X3 = random_projection(X, 3)
    X3.shape

Out[9]: (1000, 3)

Визуализируем эти точки, чтобы понять, с чем имеем дело (рис. 5.98):

In[10]: from mpl_toolkits import mplot3d
    ax = plt.axes(projection='3d')
    ax.scatter3D(X3[:, 0], X3[:, 1], X3[:, 2],
                **colorize)
    ax.view_init(azim=70, elev=50)