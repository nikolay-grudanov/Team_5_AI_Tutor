---
source_image: page_530.png
page_number: 530
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.86
tokens: 7366
characters: 1329
timestamp: 2025-12-24T01:04:53.393392
finish_reason: stop
---

i = rng.permutation(data.shape[0])[:N]
colors = colors[i]
R, G, B = data[i].T

fig, ax = plt.subplots(1, 2, figsize=(16, 6))
ax[0].scatter(R, G, color=colors, marker='.')
ax[0].set(xlabel='Red', ylabel='Green', xlim=(0, 1), ylim=(0, 1))

ax[1].scatter(R, B, color=colors, marker='.')
ax[1].set(xlabel='Red', ylabel='Blue', xlim=(0, 1), ylim=(0, 1))

fig.suptitle(title, size=20);

In[22]: plot_pixels(data, title='Input color space: 16 million possible colors') # Исходное цветовое пространство: 16 миллионов возможных цветов

![Распределение пикселов в цветовом пространстве RGB](https://i.imgur.com/3Q5z5QG.png)

Рис. 5.121. Распределение пикселов в цветовом пространстве RGB

Теперь уменьшим количество цветов с 16 миллионов до 16 путем кластеризации методом \( k \)-средних на пространстве пикселов. Так как наш набор данных очень велик, воспользуемся мини-пакетным методом \( k \)-средних, который вычисляет результат гораздо быстрее, чем стандартный метод \( k \)-средних путем работы с подмножествами набора данных (рис. 5.122):

In[23]: from sklearn.cluster import MiniBatchKMeans
kmeans = MiniBatchKMeans(16)
kmeans.fit(data)
new_colors = kmeans.cluster_centers_[kmeans.predict(data)]

plot_pixels(data, colors=new_colors,
    title="Reduced color space: 16 colors")
    # Редуцированное цветовое пространство: 16 цветов