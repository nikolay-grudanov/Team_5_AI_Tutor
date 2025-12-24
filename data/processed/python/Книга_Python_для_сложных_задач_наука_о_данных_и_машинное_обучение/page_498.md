---
source_image: page_498.png
page_number: 498
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.91
tokens: 7472
characters: 1753
timestamp: 2025-12-24T01:04:12.866419
finish_reason: stop
---

рандомизированный метод позволяет аппроксимировать первые \( N \) компонент намного быстрее, чем обычный оцениватель PCA, что очень удобно для многомерных данных (в данном случае размерность равна почти 3000). Рассмотрим первые 150 компонент:

In[18]: from sklearn.decomposition import RandomizedPCA
    pca = RandomizedPCA(150)
    pca.fit(faces.data)

Out[18]: RandomizedPCA(copy=True, iterated_power=3, n_components=150,
    random_state=None, whiten=False)

В нашем случае будет интересно визуализировать изображения, соответствующие первым нескольким главным компонентам (эти компоненты формально носят название собственных векторов (eigenvectors), так что подобные изображения часто называют «собственными лицами» (eigenfaces)). Как вы видите из рис. 5.91, они такие же жуткие, как и их название:

In[19]: fig, axes = plt.subplots(3, 8, figsize=(9, 4),
    subplot_kw={'xticks':[], 'yticks':[]},
    gridspec_kw=dict(hspace=0.1, wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(pca.components_[i].reshape(62, 47), cmap='bone')

![Визуализация собственных лиц, полученных из набора данных LFW](../images/5.91.png)

Рис. 5.91. Визуализация собственных лиц, полученных из набора данных LFW

Результат весьма интересен и позволяет ощутить разнообразие изображений: например, вид первых нескольких собственных лиц (считая с левого верхнего угла связан с углом падения света на лицо, а в дальнейшем главные векторы выделяют некоторые черты, например глаза, носы и губы. Посмотрим на интегральную дисперсию этих компонент, чтобы выяснить, какая доля информации сохраняется (рис. 5.92):

In[20]: plt.plot(np.cumsum(pca.explained_variance_ratio_))
    plt.xlabel('number of components')
    plt.ylabel('cumulative explained variance');