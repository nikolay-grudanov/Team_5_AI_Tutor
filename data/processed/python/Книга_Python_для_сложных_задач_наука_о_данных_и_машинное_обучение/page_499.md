---
source_image: page_499.png
page_number: 499
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.90
tokens: 7313
characters: 1086
timestamp: 2025-12-24T01:04:03.895175
finish_reason: stop
---

Рис. 5.92. Интегральная объяснимая дисперсия для набора данных LFW

Мы видим, что эти 150 компонент отвечают за более чем 90% дисперсии. Это дает нам уверенность в том, что при использовании 150 компонент мы сможем восстановить большую часть существенных характеристик данных. Ради уточнения сравним входные изображения с восстановленными из этих 150 компонент (рис. 5.93):

In[21]: # Вычисляем компоненты и проекции лиц
pca = RandomizedPCA(150).fit(faces.data)
components = pca.transform(faces.data)
projected = pca.inverse_transform(components)

In[22]: # Рисуем результаты
fig, ax = plt.subplots(2, 10, figsize=(10, 2.5),
    subplot_kw={'xticks':[], 'yticks':[]},
    gridspec_kw=dict(hspace=0.1, wspace=0.1))
for i in range(10):
    ax[0, i].imshow(faces.data[i].reshape(62, 47), cmap='binary_r')
    ax[1, i].imshow(projected[i].reshape(62, 47), cmap='binary_r')
ax[0, 0].set_ylabel('full-dim\ninput')
# Полноразмерные входные данные
ax[1, 0].set_ylabel('150-dim\nreconstruction');
# 150-мерная реконструкция

Рис. 5.93. 150-мерная реконструкция данных из LFW с помощью метода PCA