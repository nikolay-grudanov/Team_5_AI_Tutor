---
source_image: page_179.png
page_number: 179
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.12
tokens: 5504
characters: 1530
timestamp: 2025-12-24T07:30:20.997615
finish_reason: stop
---

§ 2] ОЦЕНКА НЕИЗВЕСТНЫХ ПАРАМЕТРОВ

если \( \theta \) — одномерный параметр. Если \( \theta = (\theta_1, \ldots, \theta_s) \), то оценки параметров \( \theta_1, \ldots, \theta_s \) удовлетворяют системе уравнений
\[
\frac{\partial \ln L}{\partial \theta_k} = 0, \quad k = 1, 2, \ldots, s.
\]

Пример 3. Пусть величины \( x_k, \ k = 1, 2, \ldots, n \), имеют нормальное распределение. Неизвестными параметрами являются \( a = Mx_k, \ b = \sigma^2 = Dx_k \). Найдем их оценки наибольшего правдоподобия. По формуле (2.3)
\[
L = L(x_1, \ldots, x_n; a, b) = \left( \frac{1}{\sqrt{2 \pi b}} \right)^n \exp \left( - \sum_{k=1}^n \frac{(x_k - a)^2}{2b} \right)
\]
и
\[
\ln L = - \frac{n}{2} (\ln 2 \pi + \ln b) - \frac{1}{2b} \sum_{k=1}^n (x_k - a)^2.
\]
Отсюда для оценок \( a^* \) и \( b^* \) получим систему
\[
\begin{cases}
\frac{\partial \ln L}{\partial a} = \frac{1}{b^*} \sum_{k=1}^n (x_k - a^*) = 0, \\
\frac{\partial \ln L}{\partial b} = - \frac{n}{2b^*} + \frac{1}{2(b^*)^2} \sum_{k=1}^n (x_k - a^*)^2 = 0.
\end{cases}
\]
Из первого уравнения \( a^* = \frac{1}{n} \sum_{k=1}^n x_k = \overline{x} \). Подставляя это значение во второе уравнение, найдем
\[
b^* = \frac{1}{n} \sum_{k=1}^n (x_k - \overline{x})^2.
\]
Оценка \( a^* \) рассматривалась в примере 1. Можно показать (см. задача 17 гл. 5), что \( Mb^* = \frac{n-1}{n} b \). Оценка \( \frac{n}{n-1} b^* \) является несмещенной и состоятельной (см. задачу 2 этой главы).

Пример 4. Найдем оценку наибольшего правдоподобия для вероятности \( p \) успеха в схеме Бернулли. По