---
source_image: page_489.png
page_number: 489
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.40
tokens: 7353
characters: 1219
timestamp: 2025-12-24T01:03:51.983363
finish_reason: stop
---

[[ 0.94446029   0.32862557]
 [ 0.32862557 -0.94446029]]

In[5]: print(pca.explained_variance_)

[ 0.75871884   0.01838551]

Чтобы понять смысл этих чисел, визуализируем их в виде векторов над входными данными, используя компоненты для задания направления векторов, а объяснимую дисперсию — в качестве квадратов их длин (рис. 5.81):

In[6]: def draw_vector(v0, v1, ax=None):
    ax = ax or plt.gca()
    arrowprops=dict(arrowstyle='->',
                    linewidth=2,
                    shrinkA=0, shrinkB=0)
    ax.annotate('', v1, v0, arrowprops=arrowprops)

    # Рисуем данные
    plt.scatter(X[:, 0], X[:, 1], alpha=0.2)
    for length, vector in zip(pca.explained_variance_, pca.components_):
        v = vector * 3 * np.sqrt(length)
        draw_vector(pca.mean_, pca.mean_ + v)
    plt.axis('equal');

![Визуализация главных осей данных](https://i.imgur.com/5.81.png)

Рис. 5.81. Визуализация главных осей данных

Эти векторы отражают главные оси координат данных, а показанная на рис. 5.81 длина соответствует «важности» роли данной оси при описании распределения данных, точнее говоря, это мера дисперсии данных при проекции на эту ось. Проекции точек данных на главные оси и есть главные компоненты данных.