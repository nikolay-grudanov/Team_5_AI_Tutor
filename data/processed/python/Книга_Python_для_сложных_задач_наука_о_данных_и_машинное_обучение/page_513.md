---
source_image: page_513.png
page_number: 513
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.39
tokens: 7283
characters: 1217
timestamp: 2025-12-24T01:04:25.333331
finish_reason: stop
---

Как видим, для сохранения 90% дисперсии необходимо почти 100 компонент. Это значит, что данные, по своей сути, имеют чрезвычайно высокую размерность и их невозможно описать линейно с помощью всего нескольких компонент.

![Интегральная дисперсия, полученная из проекции методом РСА](../images/5.105.png)

Рис. 5.105. Интегральная дисперсия, полученная из проекции методом РСА

В подобном случае могут оказаться полезны нелинейные вложения на базе многообразий, такие как LLE и Isomap. Рассчитать вложение Isomap для этих лиц можно аналогичным вышеприведенному образом:

In[19]: from sklearn.manifold import Isomap
model = Isomap(n_components=2)
proj = model.fit_transform(faces.data)
proj.shape

Out[19]: (2370, 2)

Результат представляет собой двумерную проекцию всех исходных изображений. Чтобы лучше представить, что говорит нам эта проекция, опишем функцию, выводящую миниатюры изображений в местах проекций:

In[20]: from matplotlib import offsetbox

    def plot_components(data, model, images=None, ax=None,
                        thumb_frac=0.05, cmap='gray'):
        ax = ax or plt.gca()

        proj = model.fit_transform(data)
        ax.plot(proj[:, 0], proj[:, 1], '.k')

        if images is not None: