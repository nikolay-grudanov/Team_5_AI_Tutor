---
source_image: page_053.png
page_number: 53
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 10.42
tokens: 5240
characters: 534
timestamp: 2025-12-24T07:39:05.719870
finish_reason: stop
---

7. Примеры

На языке R.
x <- seq(0, 1, 0.01) # Значения независимой переменной
# с шагом 0,01.
plot(x, 1-10*x^2*(1-x)^2, type="l",
    col="blue", lty=1, pch=2, lwd=2,
    main="Функция мощности критерия", xlab="p", ylab="w(p)")

![Функция мощности критерия](../images/fig_7_1.png)

На языке Python.
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 1, 1000)
plt.plot(x, 1-10*x**2*(1-x)**2)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel("p")
plt.ylabel("w(p)")
plt.title(u"Функция мощности критерия")