---
source_image: page_483.png
page_number: 483
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.62
tokens: 6483
characters: 2238
timestamp: 2025-12-24T08:20:41.413766
finish_reason: stop
---

53.3. Докажите, что для любой унитарной матрицы \( U \) существует такая эрмитова матрица \( H \), что \( U = e^{iH} \).

53.4. а) Докажите, что если вещественная матрица \( X \) кососимметрична, то матрица \( e^X \) ортогональна.
    б) Докажите, что любую ортогональную матрицу \( U \) с определителем 1 можно представить в виде \( e^X \), где \( X \) — вещественная кососимметрическая матрица.

53.5. а) Пусть \( A \) — вещественная матрица. Докажите, что \( \det e^A = 1 \) тогда и только тогда, когда \( \operatorname{tr} A = 0 \).
    б) Пусть \( B \) — вещественная матрица и \( \det B = 1 \). Всегда ли найдётся такая вещественная матрица \( A \), что \( B = e^A \)?

53.6. а) Докажите, что \( (\det A)' = \operatorname{tr}(\dot{A} \operatorname{adj} A^T) = (\det A) \operatorname{tr}(\dot{A} A^{-1}) \).
    б) Пусть \( A \) — матрица порядка \( n \). Докажите, что \( \operatorname{tr}(A(\operatorname{adj} A^T))' = (n-1) \operatorname{tr}(\dot{A} \operatorname{adj} A^T) \).

53.7. Докажите, что если матрица \( A \) нильпотентна, то матрица \( e^A \) унипотентна. Верно ли обратное?

53.8. Докажите, что
\[
e^{tX_1} e^{tX_2} \ldots e^{tX_n} = \exp \left\{ t \bullet X_i + \frac{t^2}{2} \sum_{i<j} [X_i, X_j] \right\} + O(t^3).
\]

53.9. Пусть \( \partial_i = \partial / \partial x_i \). Докажите, что
\[
\begin{vmatrix}
1 & 1 & \ldots & 1 \\
\partial_1 & \partial_2 & \ldots & \partial_n \\
\cdots & \cdots & \cdots & \cdots \\
\partial_1^{n-1} & \partial_2^{n-1} & \ldots & \partial_n^{n-1}
\end{vmatrix}
\begin{vmatrix}
1 & 1 & \ldots & 1 \\
x_1 & x_2 & \ldots & x_n \\
\cdots & \cdots & \cdots & \cdots \\
x_1^{n-1} & x_2^{n-1} & \ldots & x_n^{n-1}
\end{vmatrix} = 1! \cdot 2! \ldots n!.
\]

53.10 [Ai]. Рассмотрим отображение \( F : M_{n,n} \to M_{n,n} \). Пусть \( \Omega F(X) = \| \omega_{ij}(X) \|_1^n \), где \( \omega_{ij}(X) = \frac{\partial}{\partial x_{ji}} \operatorname{tr} F(X) \). Докажите, что если \( F(X) = X^m \), где \( m \) — целое число, то \( \Omega F(X) = m X^{m-1} \).

§ 54. Пары Лакса и интегрируемые системы

54.1. Уравнение Лакса

Рассмотрим систему дифференциальных уравнений \( \dot{x}(t) = f(x, t) \), где \( x = (x_1, \ldots, x_n) \). Функцию \( F(x_1, \ldots, x_n) \), отличную от константы,