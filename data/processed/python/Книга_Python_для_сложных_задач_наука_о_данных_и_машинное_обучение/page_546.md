---
source_image: page_546.png
page_number: 546
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.45
tokens: 7235
characters: 927
timestamp: 2025-12-24T01:05:13.826687
finish_reason: stop
---

Похоже, что AIC минимизируют примерно 110 компонент; этой моделью мы и воспользуемся. Обучим этот алгоритм на наших данных и убедимся, что он сошелся:

In[22]: gmm = GMM(110, covariance_type='full', random_state=0)
    gmm.fit(data)
    print(gmm.converged_)

True

Теперь можно сгенерировать 100 новых точек в этом 41-мерном пространстве, используя GMM как порождающую модель:

In[23]: data_new = gmm.sample(100, random_state=0)
    data_new.shape

Out[23]: (100, 41)

Наконец, можно воспользоваться обратным преобразованием объекта РСА для формирования новых цифр (рис. 5.139):

In[24]: digits_new = pca.inverse_transform(data_new)
    plot_digits(digits_new)

![«Новые» цифры, полученные случайным образом из модели оценивателя GMM](../images/5.139.png)

Рис. 5.139. «Новые» цифры, полученные случайным образом из модели оценивателя GMM

Результаты по большей части выглядят как вполне правдоподобные цифры из набора данных!