---
source_image: page_514.png
page_number: 514
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.25
tokens: 7165
characters: 828
timestamp: 2025-12-24T01:04:20.359953
finish_reason: stop
---

min_dist_2 = (thumb_frac * max(proj.max(0) - proj.min(0))) ** 2
shown_images = np.array([2 * proj.max(0)])
for i in range(data.shape[0]):
    dist = np.sum((proj[i] - shown_images) ** 2, 1)
    if np.min(dist) < min_dist_2:
        # Не отображаем слишком близко расположенные точки
        Continue
    shown_images = np.vstack([shown_images, proj[i]])
    imagebox = offsetbox.AnnotationBbox(
        offsetbox.OffsetImage(images[i], cmap=cmap),
        proj[i])
    ax.add_artist(imagebox)

Вызываем эту функцию и видим результат (рис. 5.106):

In[21]: fig, ax = plt.subplots(figsize=(10, 10))
    plot_components(faces.data,
        model=Isomap(n_components=2),
        images=faces.images[:, ::2, ::2])

![Вложение с помощью Isomap данных о лицах](../images/5.106.png)

Рис. 5.106. Вложение с помощью Isomap данных о лицах