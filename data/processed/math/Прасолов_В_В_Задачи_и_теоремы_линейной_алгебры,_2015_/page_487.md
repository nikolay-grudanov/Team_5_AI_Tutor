---
source_image: page_487.png
page_number: 487
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.73
tokens: 6337
characters: 1817
timestamp: 2025-12-24T08:20:48.196278
finish_reason: stop
---

Уравнение \( \dot{A} = -[A, B] \) эквивалентно системе уравнений

\[
\dot{a}_{ij} = a_{ij}(b_i - b_j),
\]

причём \( a_{ij} \neq 0 \) лишь при \( j = i + 1 - p \). В итоге получаем систему уравнений

\[
\dot{a}_i = a_i \left( \sum_{k=1}^{p-1} a_{i+k} - \sum_{k=1}^{p-1} a_{i+1-p+k} \right) = a_i \left( \sum_{k=1}^{p-1} a_{i+k} - \sum_{k=1}^{p-1} a_{i-k} \right).
\]

Таким образом, уравнение (1) имеет первые интегралы

\[
I_m = \operatorname{tr}(A + \lambda M)^{mp}.
\]

§ 55. Матрицы с предписанными собственными значениями

55.1. Фиксированная диагональ

Теорема 55.1.1. Для любого многочлена \( f(x) = x^n + c_1 x^{n-1} + \ldots + c_n \) и любых чисел \( a_1, \ldots, a_{n-1} \) существует матрица порядка \( n \) с характеристическим многочленом \( f \) и элементами \( a_1, \ldots, a_n \) на диагонали (последний диагональный элемент \( a_n \) задаётся соотношением \( a_1 + \ldots + a_n = -c_1 \)).

Доказательство [Fa2]. Многочлены

\[
u_0 = 1, \quad u_1 = x - a_1, \quad \ldots, \quad u_n = (x - a_1) \ldots (x - a_n)
\]

образуют базис в пространстве многочленов степени не более \( n \), поэтому \( f = u_n + \lambda_1 u_{n-1} + \ldots + \lambda_n u_0 \). Приравнивая коэффициенты при \( x^{n-1} \) в левой и правой части, получаем \( c_1 = -(a_1 + \ldots + a_n) + \lambda_1 \), т. е. \( \lambda_1 = c_1 + (a_1 + \ldots + a_n) = 0 \). Пусть

\[
A = \begin{pmatrix}
a_1 & 1 & 0 & \ldots & 0 & 0 \\
0 & a_2 & 1 & \ldots & 0 & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & \ldots & a_{n-1} & 1 \\
-\lambda_n & -\lambda_{n-1} & -\lambda_{n-2} & \ldots & -\lambda_2 & a_n
\end{pmatrix}.
\]

Разложив определитель матрицы \( xI - A \) по последней строке, получим \( |xI - A| = \lambda_n + \lambda_{n-1} u_1 + \ldots + \lambda_2 u_{n-2} + u_n = f \), т. е. \( A \) — искомая матрица. □