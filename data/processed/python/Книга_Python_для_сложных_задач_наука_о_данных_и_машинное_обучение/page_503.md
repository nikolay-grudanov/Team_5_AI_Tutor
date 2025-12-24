---
source_image: page_503.png
page_number: 503
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.40
tokens: 7333
characters: 1334
timestamp: 2025-12-24T01:04:13.129738
finish_reason: stop
---

In[4]:
    def rotate(X, angle):
        theta = np.deg2rad(angle)
        R = [[np.cos(theta), np.sin(theta)],
             [-np.sin(theta), np.cos(theta)]]
        return np.dot(X, R)

    X2 = rotate(X, 20) + 5
    plt.scatter(X2[:, 0], X2[:, 1], **colorize)
    plt.axis('equal');

![Набор данных после вращения](https://i.imgur.com/3Q5z5QG.png)

Рис. 5.95. Набор данных после вращения

Это говорит о том, что значения \( x \) и \( y \) не обязательно важны для внутренних зависимостей данных. Существенно в таком случае расстояние между каждой из точек и всеми остальными точками набора данных. Для представления его часто используют так называемую матрицу расстояний: при \( N \) точках создается такой массив размера \( N \times N \), что его элемент \( (i, j) \) содержит расстояние между точками \( i \) и \( j \). Воспользуемся эффективной функцией pairwise_distances из библиотеки Scikit-Learn, чтобы выполнить этот расчет для наших исходных данных:

In[5]: from sklearn.metrics import pairwise_distances
    D = pairwise_distances(X)
    D.shape

Out[5]: (1000, 1000)

Как я и обещал, при наших \( N = 1000 \) точках мы получили матрицу размером \( 1000 \times 1000 \), которую можно визуализировать так, как показано на рис. 5.96:

In[6]: plt.imshow(D, zorder=2, cmap='Blues', interpolation='nearest')
    plt.colorbar();