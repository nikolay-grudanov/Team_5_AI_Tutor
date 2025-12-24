---
source_image: page_544.png
page_number: 544
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.49
tokens: 7529
characters: 1965
timestamp: 2025-12-24T01:05:25.698133
finish_reason: stop
---

Пример: использование метода GMM для генерации новых данных

Мы увидели простой пример применения метода GMM в качестве порождающей модели данных с целью создания новых выборок на основе соответствующего исходным данным распределения. В этом разделе мы продолжим воплощение этой идеи и сгенерируем новые рукописные цифры на основе корпуса стандартных цифр, который мы использовали ранее.

Для начала загрузим набор данных по цифрам с помощью инструментов библиотеки Scikit-Learn:

In[18]: from sklearn.datasets import load_digits
    digits = load_digits()
    digits.data.shape

Out[18]: (1797, 64)

Далее выведем на рисунок первые 100 из них, чтобы вспомнить, с чем мы имеем дело (рис. 5.137):
In[19]: def plot_digits(data):
        fig, ax = plt.subplots(10, 10, figsize=(8, 8),
            subplot_kw=dict(xticks=[], yticks=[]))
        fig.subplots_adjust(hspace=0.05, wspace=0.05)
        for i, axi in enumerate(ax.flat):
            im = axi.imshow(data[i].reshape(8, 8), cmap='binary')
            im.set_clim(0, 16)
    plot_digits(digits.data)

Наш набор данных состоит почти из 1800 цифр в 64 измерениях. Построим на их основе GMM, чтобы сгенерировать еще. У смесей Гауссовых распределений могут быть проблемы со сходимостью в пространстве столь высокой размерности, поэтому начнем с применения обратимого алгоритма для понижения размерности данных. Воспользуемся для этой цели простым алгоритмом PCA с сохранением 99 % дисперсии в проекции данных:

In[20]: from sklearn.decomposition import PCA
    pca = PCA(0.99, whiten=True)
    data = pca.fit_transform(digits.data)
    data.shape

Out[20]: (1797, 41)

Результат оказался 41-мерным, то есть размерность была снижена почти на 1/3 практически без потерь информации. Воспользуемся для этих спроцированных данных критерием AIC для определения необходимого количества компонент GMM (рис. 5.138):

In[21]: n_components = np.arange(50, 210, 10)
    models = [GMM(n, covariance_type='full', random_state=0)