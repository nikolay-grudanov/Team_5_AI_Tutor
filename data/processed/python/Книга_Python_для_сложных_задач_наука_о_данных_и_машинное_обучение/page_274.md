---
source_image: page_274.png
page_number: 274
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.40
tokens: 7187
characters: 736
timestamp: 2025-12-24T00:58:20.662272
finish_reason: stop
---

способ настройки пределов осей координат — методы plt.xlim() и plt.ylim() (рис. 4.12):

In[9]: plt.plot(x, np.sin(x))

    plt.xlim(-1, 11)
    plt.ylim(-1.5, 1.5);

![Пример задания пределов осей координат](../images/fig_4_12.png)

Рис. 4.12. Пример задания пределов осей координат

Если вам нужно, чтобы оси отображались зеркально, можно указать аргументы в обратном порядке (рис. 4.13):

In[10]: plt.plot(x, np.sin(x))

    plt.xlim(10, 0)
    plt.ylim(1.2, -1.2);

![Пример зеркального отображения оси Y](../images/fig_4_13.png)

Рис. 4.13. Пример зеркального отображения оси Y

Удобный метод для этих действий — plt.axis() (не перепутайте метод plt.axis() с методом plt.axes()!). Метод plt.axis() предоставляет возможность задавать