---
source_image: page_125.png
page_number: 125
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.08
tokens: 7611
characters: 1232
timestamp: 2025-12-24T02:43:11.665131
finish_reason: stop
---

In [172]: z = np.sqrt(xs ** 2 + ys ** 2)

In [173]: z
Out[173]:
array([[7.0711, 7.064 , 7.0569, ..., 7.0499, 7.0569, 7.064 ],
       [7.064 , 7.0569, 7.0499, ..., 7.0428, 7.0499, 7.0569],
       [7.0569, 7.0499, 7.0428, ..., 7.0357, 7.0428, 7.0499],
       ...,
       [7.0499, 7.0428, 7.0357, ..., 7.0286, 7.0357, 7.0428],
       [7.0569, 7.0499, 7.0428, ..., 7.0357, 7.0428, 7.0499],
       [7.064 , 7.0569, 7.0499, ..., 7.0428, 7.0499, 7.0569]])

Предвосхищая главу 9, я воспользуюсь библиотекой matplotlib для визуализации двумерного массива:

In [174]: import matplotlib.pyplot as plt

In [175]: plt.imshow(z, cmap=plt.cm.gray, extent=[-5, 5, -5, 5])
Out[175]: <matplotlib.image.AxesImage at 0x7f624ae73b20>

In [176]: plt.colorbar()
Out[176]: <matplotlib.colorbar.Colorbar at 0x7f6253e43ee0>

In [177]: plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
Out[177]: Text(0.5, 1.0, 'Image plot of $\\sqrt{x^2 + y^2}$ for a grid of values'

На рис. 4.3 показан результат применения функции imshow из библиотеки matplotlib для создания изображения по двумерному массиву значений функции.

![График функции двух переменных на сетке](https://i.imgur.com/3Q5z5QG.png)

Рис. 4.3. График функции двух переменных на сетке