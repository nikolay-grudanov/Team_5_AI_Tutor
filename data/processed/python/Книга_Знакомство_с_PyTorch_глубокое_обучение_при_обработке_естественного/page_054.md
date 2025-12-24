---
source_image: page_054.png
page_number: 54
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.91
tokens: 7337
characters: 1271
timestamp: 2025-12-24T02:22:27.529423
finish_reason: stop
---

и сигма-функция, — сжимающая функция, но отображающая вещественные значения из \((-\infty, +\infty)\) в диапазоне \([-1, +1]\).

Пример 3.3. Функция активации th

import torch
import matplotlib.pyplot as plt

x = torch.range(-5., 5., 0.1)
y = torch.tanh(x)
plt.plot(x.numpy(), y.numpy())
plt.show()

![График функции активации tanh](https://i.imgur.com/3Q5z5QG.png)

ReLU

ReLU (произносится «рей-лу») расшифровывается как выпрямленный линейный блок (rectified linear unit). Вероятно, это важнейшая из функций активации. На самом деле можно даже сказать, что многие из последних новшеств глубокого обучения были бы невозможны без ReLU. Для столь фундаментальной концепции она появилась удивительно недавно. И форма ее также очень проста:

\[
f(x) = \max(0, x).
\]

Таким образом, все, что делает блок ReLU, — обнуляет отрицательные значения, как показано в примере 3.4.

Пример 3.4. ReLU-активация

import torch
import matplotlib.pyplot as plt

relu = torch.nn.ReLU()
x = torch.range(-5., 5., 0.1)
y = relu(x)

plt.plot(x.numpy(), y.numpy())
plt.show()

![График функции активации ReLU](https://i.imgur.com/3Q5z5QG.png)

Эффект обрезания ReLU, помогающий справиться с проблемой исчезающего градиента, может сам стать проблемой, когда с течением времени некоторые выходные