---
source_image: page_324.png
page_number: 324
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.03
tokens: 7338
characters: 1360
timestamp: 2025-12-24T00:59:37.468620
finish_reason: stop
---

изображения лиц людей, — пример, часто используемый в задачах машинного обучения с учителем (более подробную информацию вы можете найти в разделе «Заглянем глубже: метод опорных векторов» главы 5):

In[6]: fig, ax = plt.subplots(5, 5, figsize=(5, 5))
    fig.subplots_adjust(hspace=0, wspace=0)

    # Получаем данные по лицам людей из библиотеки scikit-learn
    from sklearn.datasets import fetch_olivetti_faces
    faces = fetch_olivetti_faces().images

    for i in range(5):
        for j in range(5):
            ax[i, j].xaxis.set_major_locator(plt.NullLocator())
            ax[i, j].yaxis.set_major_locator(plt.NullLocator())
            ax[i, j].imshow(faces[10 * i + j], cmap="bone")

![Скрываем деления на графиках с изображениями](../images/4.75.png)

Рис. 4.75. Скрываем деления на графиках с изображениями

Обратите внимание, что у каждого изображения — отдельная система координат и мы сделали локаторы пустыми, поскольку значения делений (в данном случае количество пикселов) не несут никакой относящейся к делу информации.

Уменьшение или увеличение количества делений

Распространенная проблема с настройками по умолчанию — то, что метки на маленьких субграфиках могут оказаться расположенными слишком близко друг к другу. Это заметно на сетке графиков, показанной на рис. 4.76:

In[7]: fig, ax = plt.subplots(4, 4, sharex=True, sharey=True)