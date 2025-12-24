---
source_image: page_465.png
page_number: 465
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.66
tokens: 7423
characters: 1575
timestamp: 2025-12-24T01:03:15.394546
finish_reason: stop
---

Если вы работаете с этим блокнотом в интерактивном режиме, можете воспользоваться интерактивными виджетами оболочки IPython для интерактивного просмотра этой возможности модели SVM (рис. 5.58):

In[10]: from ipywidgets import interact, fixed
    interact(plot_svm, N=[10, 200], ax=fixed(None));

![Первый кадр интерактивной визуализации SVM](https://github.com/jakevdp/PythonDataScienceHandbook/raw/master/notebooks/figures/ch05/fig-5-58.png)

Рис. 5.58. Первый кадр интерактивной визуализации SVM (см. полную версию в онлайн-приложении (https://github.com/jakevdp/PythonDataScienceHandbook))

Выходим за границы линейности: SVM-ядро

Возможности метода SVM особенно расширяются при его комбинации с ядрами (kernels). Мы уже сталкивались с ними ранее, в регрессии по комбинации базисных функций из раздела «Заглянем глубже: линейная регрессия» данной главы. Там мы занимались проекцией данных в пространство с большей размерностью, определяемое полиномиальными и Гауссовыми базисными функциями, и благодаря этому имели возможность аппроксимировать нелинейные зависимости с помощью линейного классификатора.

В SVM-моделях можно использовать один из вариантов той же идеи. Чтобы понять, почему здесь необходимы ядра, рассмотрим следующие данные, которые не допускают линейное разделение (рис. 5.59):

In[11]: from sklearn.datasets.samples_generator import make_circles
    X, y = make_circles(100, factor=.1, noise=.1)
    clf = SVC(kernel='linear').fit(X, y)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
    plot_svc_decision_function(clf, plot_support=False);