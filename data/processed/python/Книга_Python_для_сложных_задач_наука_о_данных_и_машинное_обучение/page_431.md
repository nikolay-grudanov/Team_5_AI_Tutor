---
source_image: page_431.png
page_number: 431
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.24
tokens: 7171
characters: 762
timestamp: 2025-12-24T01:02:13.804530
finish_reason: stop
---

In[10]: %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([4, 2, 1, 3, 7])
plt.scatter(x, y);

![Данные, которые нельзя хорошо описать с помощью прямой линии](../images/fig_5_35.png)

Рис. 5.35. Данные, которые нельзя хорошо описать с помощью прямой линии

Тем не менее мы можем подобрать разделяющую прямую для этих данных с помощью функции LinearRegression и получить оптимальный результат (рис. 5.36):

In[11]: from sklearn.linear_model import LinearRegression
X = x[:, np.newaxis]
model = LinearRegression().fit(X, y)
yfit = model.predict(X)
plt.scatter(x, y)
plt.plot(x, yfit);

![Неудачная прямоугольная аппроксимация](../images/fig_5_36.png)

Рис. 5.36. Неудачная прямоугольная аппроксимация