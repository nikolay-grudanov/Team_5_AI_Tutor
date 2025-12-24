---
source_image: page_538.png
page_number: 538
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.89
tokens: 7353
characters: 1234
timestamp: 2025-12-24T01:05:10.700978
finish_reason: stop
---

# Рисуем эллипс
for nsig in range(1, 4):
    ax.add_patch(Ellipse(position, nsig * width, nsig * height,
        angle, **kwargs))

def plot_gmm(gmm, X, label=True, ax=None):
    ax = ax or plt.gca()
    labels = gmm.fit(X).predict(X)
    if label:
        ax.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis', zorder=2)
    else:
        ax.scatter(X[:, 0], X[:, 1], s=40, zorder=2)
    ax.axis('equal')
    w_factor = 0.2 / gmm.weights_.max()
    for pos, covar, w in zip(gmm.means_, gmm.covars_, gmm.weights_):
        draw_ellipse(pos, covar, alpha=w * w_factor)

После этого можем посмотреть, какие результаты выдает четырехкомпонентный метод GMM на наших данных (рис. 5.129):

In[11]: gmm = GMM(n_components=4, random_state=42)
    plot_gmm(gmm, X)

![Четырехкомпонентный метод GMM в случае круглых кластеров](https://i.imgur.com/3Q5z5QG.png)

Рис. 5.129. Четырехкомпонентный метод GMM в случае круглых кластеров

Аналогично можно воспользоваться подходом GMM для «растянутого» набора данных. С учетом полной ковариации модель будет подходить даже для очень продолговатых, вытянутых в длину кластеров (рис. 5.130):

In[12]: gmm = GMM(n_components=4, covariance_type='full', random_state=42)
    plot_gmm(gmm, X_stretched)