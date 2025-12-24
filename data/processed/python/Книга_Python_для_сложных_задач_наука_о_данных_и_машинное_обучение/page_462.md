---
source_image: page_462.png
page_number: 462
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.84
tokens: 7549
characters: 1937
timestamp: 2025-12-24T01:03:18.633675
finish_reason: stop
---

for m, b, d in [(1, 0.65, 0.33), (0.5, 1.6, 0.55), (-0.2, 2.9, 0.2)]:
    yfit = m * xfit + b    plt.plot(xfit, yfit, '-k')
    plt.fill_between(xfit, yfit - d, yfit + d, edgecolor='none',
                     color='#AAAAAA', alpha=0.4)

plt.xlim(-1, 3.5);

В методе опорных векторов в качестве оптимальной модели выбирается линия, максимизирующая этот отступ. Метод опорных векторов — пример оценивателя с максимальным отступом (maximum margin estimator).

Аппроксимация методом опорных векторов

Взглянем на реальную аппроксимацию этих данных: воспользуемся классификатором на основе метода опорных векторов для обучения SVM-модели на них. Пока мы будем использовать линейное ядро и зададим очень большое значение параметра C (что это значит, мы расскажем далее):

In[5]: from sklearn.svm import SVC # "Классификатор на основе метода опорных векторов"
    model = SVC(kernel='linear', C=1E10)
    model.fit(X, y)

Out[5]: SVC(C=10000000000.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape=None, degree=3, gamma='auto',
    kernel='linear',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

Для лучшей визуализации происходящего создадим простую и удобную функцию для построения графика границ решений метода SVM (рис. 5.56):

In[6]:
    def plot_svc_decision_function(model, ax=None, plot_support=True):
        """Строим график решающей функции для двумерной SVC"""
        if ax is None:
            ax = plt.gca()
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()

        # Создаем координатную сетку для оценки модели
        x = np.linspace(xlim[0], xlim[1], 30)
        y = np.linspace(ylim[0], ylim[1], 30)
        Y, X = np.meshgrid(y, x)
        xy = np.vstack([X.ravel(), Y.ravel()]).T
        P = model.decision_function(xy).reshape(X.shape)

        # Рисуем границы принятия решений и отступы
        ax.contour(X, Y, P, colors='k',