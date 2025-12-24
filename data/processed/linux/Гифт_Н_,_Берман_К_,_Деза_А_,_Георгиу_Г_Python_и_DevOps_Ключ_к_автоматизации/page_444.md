---
source_image: page_444.png
page_number: 444
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.41
tokens: 7244
characters: 1039
timestamp: 2025-12-24T03:12:23.982223
finish_reason: stop
---

предсказании новых данных. Для этого вычисляем RMSE (root mean squared error — среднеквадратическая ошибка) предсказанных и контрольных данных.

In[18]:

from sklearn.metrics import mean_squared_error
from math import sqrt

# RMSE — среднеквадратическая ошибка
rms = sqrt(mean_squared_error(y_predicted, y_test))
rms

Out[18]:
10.282608230082417

График соотношения предсказанного и истинного роста. Теперь построим график соотношения предсказанного и истинного роста (рис. 14.3), чтобы выяснить, насколько хороши предсказания модели.

In[19]:

import matplotlib.pyplot as plt
_, ax = plt.subplots()

ax.scatter(x = range(0, y_test.size), y=y_test, c = 'blue', label = 'Actual', alpha = 0.5)
ax.scatter(x = range(0, y_predicted.size), y=y_predicted, c = 'red', label = 'Predicted', alpha = 0.5)

plt.title('Actual Height vs Predicted Height')
plt.xlabel('Weight')
plt.ylabel('Height')
plt.legend()
plt.show()

![Scatter plot of Actual Height vs Predicted Height](../images/14_3.png)

Рис. 14.3. Соотношение предсказанного и истинного роста