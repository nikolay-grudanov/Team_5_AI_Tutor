---
source_image: page_534.png
page_number: 534
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.06
tokens: 7256
characters: 931
timestamp: 2025-12-24T01:04:53.321352
finish_reason: stop
---

for i, center in enumerate(centers)]
    for c, r in zip(centers, radii):
        ax.add_patch(plt.Circle(c, r, fc='#CCCCCC', lw=3, alpha=0.5, zorder=1))

In[5]: kmeans = KMeans(n_clusters=4, random_state=0)
    plot_kmeans(kmeans, X)

![Круглые кластеры, подразумеваемые моделью k-средних](https://i.imgur.com/1234567.png)

Рис. 5.125. Круглые кластеры, подразумеваемые моделью k-средних

Немаловажный нюанс, касающийся метода \( k \)-средних, состоит в том, что эти модели кластеров обязательно должны иметь форму окружностей: метод \( k \)-средних не умеет работать с овальными или эллипсовидными кластерами. Так, например, если несколько преобразовать те же данные, присвоенные метки окажутся перепутаны (рис. 5.126).

![Неудовлетворительная работа метода k-средних в случае кластеров некруглой формы](https://i.imgur.com/8901234.png)

Рис. 5.126. Неудовлетворительная работа метода k-средних в случае кластеров некруглой формы