---
source_image: page_189.png
page_number: 189
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.31
tokens: 4888
characters: 637
timestamp: 2025-12-24T07:30:17.920253
finish_reason: stop
---

Задачи к главе 10

где ошибки измерения \( \delta_i \) независимы, нормально распределены, \( m\delta_i = 0, D\delta_i = \sigma^2 \). Функция правдоподобия

\[
L(y_1, ..., y_n; x_1, ..., x_n; \alpha, \beta, \sigma^2) = (2\pi \sigma^2)^{-\frac{n}{2}} e^{-\frac{1}{2} Q},
\]

где \( Q = \frac{1}{\sigma^2} \sum_{i=1}^n (y_i - \alpha - \beta x_i)^2 \). Минимизируя \( Q \), найти оценки наибольшего правдоподобия параметров \( \alpha, \beta, \sigma^2 \) в предположении, что \( \sum_{i=1}^n x_i = 0 \). (Если условие \( \sum x_i = 0 \) не выполнено, то можно перейти к новым переменным \( x'_i = x_i - \left( \sum_{i=1}^n x_i \right)/n \).)