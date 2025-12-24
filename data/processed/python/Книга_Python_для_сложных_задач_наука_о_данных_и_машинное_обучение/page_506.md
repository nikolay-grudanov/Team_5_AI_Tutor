---
source_image: page_506.png
page_number: 506
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 11.99
tokens: 7101
characters: 580
timestamp: 2025-12-24T01:04:03.747400
finish_reason: stop
---

Рис. 5.98. Данные, линейно вложенные в трехмерное пространство

Можно теперь передать эти данные оценивателю MDS для вычисления матрицы расстояний и последующего определения оптимального двумерного вложения для нее. В результате мы получаем восстановленное представление исходных данных (рис. 5.99):

In[11]: model = MDS(n_components=2, random_state=1)
    out3 = model.fit_transform(X3)
    plt.scatter(out3[:, 0], out3[:, 1], **colorize)
    plt.axis('equal');

Рис. 5.99. MDS-вложение трехмерных данных позволяет восстановить исходные данные с точностью до вращения и отражения