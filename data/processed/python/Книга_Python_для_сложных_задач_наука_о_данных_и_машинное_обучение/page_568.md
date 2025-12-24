---
source_image: page_568.png
page_number: 568
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.10
tokens: 7349
characters: 1336
timestamp: 2025-12-24T01:05:46.776998
finish_reason: stop
---

Рис. 5.151. Изображение, в котором мы попытаемся найти лицо

Далее создадим окно, которое будет перемещаться по фрагментам этого изображения с вычислением HOG-признаков для каждого фрагмента:

In[14]: def sliding_window(img, patch_size=positive_patches[0].shape,
                        istep=2, jstep=2, scale=1.0):
    Ni, Nj = (int(scale * s) for s in patch_size)
    for i in range(0, img.shape[0] - Ni, istep):
        for j in range(0, img.shape[1] - Ni, jstep):
            patch = img[i:i + Ni, j:j + Nj]
            if scale != 1:
                patch = transform.resize(patch, patch_size)
            yield (i, j), patch

indices, patches = zip(*sliding_window(test_image))
patches_hog = np.array([feature.hog(patch) for patch in patches])
patches_hog.shape

Out[14]: (1911, 1215)

Наконец, возьмем эти фрагменты, для которых вычислены признаки HOG, и воспользуемся нашей моделью, чтобы определить, содержат ли какие-то из них лица:

In[15]: labels = model.predict(patches_hog)
        labels.sum()
Out[15]: 33.0

Таким образом, среди 2000 фрагментов найдено 33 лица. Воспользуемся имеющейся о фрагментах информацией, чтобы определить, где в нашем контрольном изображении они располагаются, нарисовав их границы в виде прямоугольников (рис. 5.152):

In[16]: fig, ax = plt.subplots()
        ax.imshow(test_image, cmap='gray')