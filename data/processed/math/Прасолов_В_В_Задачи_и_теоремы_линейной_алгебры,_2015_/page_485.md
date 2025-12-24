---
source_image: page_485.png
page_number: 485
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.88
tokens: 6449
characters: 1902
timestamp: 2025-12-24T08:20:43.215902
finish_reason: stop
---

где \( U = \exp(x_1 - x_2) + \ldots + \exp(x_{n-1} - x_n) \). Эту систему уравнений можно переписать в виде уравнения Лакса с

\[
L = \begin{pmatrix}
b_1 & a_1 & 0 & \ldots & \ldots & 0 \\
a_1 & b_2 & a_2 & \ldots & \ldots & 0 \\
0 & a_2 & b_3 & \ldots & \ldots & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & \ldots & b_{n-1} & a_{n-1} \\
0 & 0 & 0 & \ldots & a_{n-1} & b_n
\end{pmatrix}
\]

и

\[
A = \begin{pmatrix}
0 & a_1 & 0 & \ldots & \ldots & 0 \\
-a_1 & 0 & a_2 & \ldots & \ldots & 0 \\
0 & -a_2 & 0 & \ldots & \ldots & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & \ldots & 0 & a_{n-1} \\
0 & 0 & 0 & \ldots & -a_{n-1} & 0
\end{pmatrix},
\]

где \( 2a_k = \exp\left(\frac{1}{2}(x_k - x_{k+1})\right) \) и \( 2b_k = -\dot{x}_k \). В самом деле, уравнение \( \dot{L} = [A, L] \) эквивалентно системе уравнений

\[
\begin{aligned}
&\dot{b}_1 = 2a_1^2, \quad \dot{b}_2 = 2(a_2^2 - a_1^2), \quad \ldots, \quad \dot{b}_n = -2a_{n-1}^2, \\
&\dot{a}_1 = a_1(b_2 - b_1), \quad \ldots, \quad \dot{a}_{n-1} = a_{n-1}(b_n - b_{n-1}).
\end{aligned}
\]

Из уравнения

\[
\dot{a}_k = a_k(b_{k+1} - b_k) = a_k \frac{\dot{x}_k - \dot{x}_{k+1}}{2}
\]

следует, что

\[
\ln a_k = \frac{1}{2}(x_k - x_{k+1}) + c_k, \quad \text{т. е.} \quad a_k = d_k \exp \frac{1}{2}(x_k - x_{k+1}).
\]

Поэтому уравнение \( \dot{b}_k = 2(a_k^2 - a_{k-1}^2) \) эквивалентно уравнению

\[
-\frac{\ddot{x}_k}{2} = 2(d_k^2 \exp(x_k - x_{k+1}) - d_{k-1}^2 \exp(x_{k-1} - x_k)).
\]

Если \( d_1 = \ldots = d_{h-1} = \frac{1}{2} \), то получаем требуемые уравнения.

54.3. Уравнения движения твёрдого тела

Движение многомерного твёрдого тела с матрицей инерции \( J \) описывается уравнением

\[
\dot{M} = [M, \omega],
\]

где \( \omega \) — кососимметрическая матрица, \( M = J \omega + \omega J \); матрицу \( J \) можно при этом считать диагональной. Уравнение (1) уже записано в