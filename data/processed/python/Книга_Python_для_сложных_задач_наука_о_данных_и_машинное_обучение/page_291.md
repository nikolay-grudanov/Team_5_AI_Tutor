---
source_image: page_291.png
page_number: 291
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.27
tokens: 7238
characters: 962
timestamp: 2025-12-24T00:58:45.969583
finish_reason: stop
---

data = np.random.randn(1000)

In[2]: plt.hist(data);

![Простая гистограмма](../images/4_35.png)

Рис. 4.35. Простая гистограмма

У функции hist() имеется множество параметров для настройки как вычисления, так и отображения. Вот пример гистограммы с детальными пользовательскими настройками (рис. 4.36):

In[3]: plt.hist(data, bins=30, normed=True, alpha=0.5,
    histtype='stepfilled', color='steelblue',
    edgecolor='none');

![Гистограмма с пользовательскими настройками](../images/4_36.png)

Рис. 4.36. Гистограмма с пользовательскими настройками

Docstring функции plt.hist содержит более подробную информацию о других доступных возможностях пользовательской настройки. Сочетание опции histtype='stepfilled' с заданной прозрачностью alpha представляется мне очень удобным для сравнения гистограмм нескольких распределений (рис. 4.37):

In[4]: x1 = np.random.normal(0, 0.8, 1000)
    x2 = np.random.normal(-2, 1, 1000)
    x3 = np.random.normal(3, 2, 1000)