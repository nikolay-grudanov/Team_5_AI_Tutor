---
source_image: page_543.png
page_number: 543
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.98
tokens: 7391
characters: 1493
timestamp: 2025-12-24T01:05:18.367468
finish_reason: stop
---

criterion, BIC, см.: https://ru.wikipedia.org/wiki/Информационный_критерий). Оцениватель GMM библиотеки Scikit-Learn включает встроенные методы для вычисления этих критериев, что сильно упрощает указанный подход.

Посмотрим на критерии AIC и BIC как функции от количества компонент GMM для нашего набора данных moon (рис. 5.136):

![Визуализация AIC и BIC с целью выбора количества компонент GMM](https://i.imgur.com/3Q5z5QG.png)

Рис. 5.136. Визуализация AIC и BIC с целью выбора количества компонент GMM

In[17]: n_components = np.arange(1, 21)
    models = [GMM(n, covariance_type='full', random_state=0).fit(Xmoon)
              for n in n_components]

    plt.plot(n_components, [m.bic(Xmoon) for m in models], label='BIC')
    plt.plot(n_components, [m.aic(Xmoon) for m in models], label='AIC')
    plt.legend(loc='best')
    plt.xlabel('n_components');

Оптимальное количество кластеров — то, которое минимизирует AIC или BIC, в зависимости от требуемой аппроксимации. Согласно AIC, наших 16 компонент, вероятно, слишком много, лучше взять 8–12. Как это обычно бывает в подобных задачах, критерий BIC говорит в пользу более простой модели.

Обратите внимание на важный момент: подобный метод выбора числа компонент представляет собой меру успешности работы GMM как оценивателя плотности распределения, а не как алгоритма кластеризации. Я советовал бы вам рассматривать GMM в основном как оцениватель плотности и использовать его для кластеризации только заведомо простых наборов данных.