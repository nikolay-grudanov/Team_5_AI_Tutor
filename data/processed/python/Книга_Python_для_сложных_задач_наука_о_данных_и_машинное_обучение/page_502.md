---
source_image: page_502.png
page_number: 502
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.18
tokens: 7339
characters: 1277
timestamp: 2025-12-24T01:04:07.715900
finish_reason: stop
---

# Открываем этот PNG-файл и берем из него случайные точки
from matplotlib.image import imread
data = imread('hello.png')[::1, :, 0].T
rng = np.random.RandomState(rseed)
X = rng.rand(4 * N, 2)
i, j = (X * data.shape).astype(int).T
mask = (data[i, j] < 1)
X = X[mask]
X[:, 0] *= (data.shape[0] / data.shape[1])
X = X[:N]
return X[np.argsort(X[:, 0])]

Вызываем эту функцию и визуализируем полученные данные (рис. 5.94):

In[3]: X = make_hello(1000)
    colorize = dict(c=X[:, 0], cmap=plt.cm.get_cmap('rainbow', 5))
    plt.scatter(X[:, 0], X[:, 1], **colorize)
    plt.axis('equal');

![Данные для обучения на базе многообразий](hello.png)

Рис. 5.94. Данные для обучения на базе многообразий

Выходные данные двумерны и состоят из точек, формирующих слово HELLO. Эта внешняя форма данных поможет нам отслеживать визуально работу алгоритмов.

Многомерное масштабирование (MDS)

При взгляде на подобные данные становится ясно, что конкретные значения x и y — не самая существенная характеристика этого набора данных: мы можем пропорционально увеличить/сжать или повернуть данные, а надпись HELLO все равно останется четко различимой. Например, при использовании матрицы вращения для вращения данных значения x и y изменятся, но данные, по существу, останутся теми же (рис. 5.95):