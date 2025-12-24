---
source_image: page_398.png
page_number: 398
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.76
tokens: 5652
characters: 2402
timestamp: 2025-12-24T07:14:54.842171
finish_reason: stop
---

1075. Для треугольной матрицы вида

\[
A = \begin{pmatrix}
\lambda_0 & a_{12} & a_{13} & \ldots & a_{1n} \\
0 & \lambda_0 & a_{23} & \ldots & a_{2n} \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & \ldots & \lambda_0
\end{pmatrix},
\]

где \(a_{i,i+1} \neq 0\ (i = 1, 2, \ldots, n-1)\), будет \(d = 1\). Для диагональной матрицы порядка \(n\), в которой \(p\) элементов главной диагонали равны \(\lambda_0\), будет \(d = p\).

1076. Указание. Перемножить равенства

\[
|A^{-1} - \lambda E| = (-\lambda)^n |A^{-1}| \cdot |A - \frac{1}{\lambda} E|.
\]

1077. Указание. Перемножить равенства

\[
|A - \lambda E| = (\lambda_1 - \lambda)(\lambda_2 - \lambda) \ldots (\lambda_n - \lambda),
\]
\[
|A + \lambda E| = (\lambda_1 + \lambda)(\lambda_2 + \lambda) \ldots (\lambda_n + \lambda)
\]

и заменить \(\lambda^2\) на \(\lambda\).

1078. Указание. Равенство \(|A - \lambda E| = (\lambda_1 - \lambda)(\lambda_2 - \lambda) \ldots (\lambda_n - \lambda)\) перемножить со всеми равенствами, полученными из него заменой \(\lambda\) на \(\lambda \varepsilon_1, \lambda \varepsilon_2, \ldots, \lambda \varepsilon_{p-1}\), где \(\varepsilon_k = \cos \frac{2\pi k}{p} + i \sin \frac{2\pi k}{p}\ (k = 1, 2, \ldots, p-1)\) и в полученном равенстве заменить \(\lambda^p\) на \(\lambda\).

1079. Решение. Пусть \(f(\lambda) = a_0 \prod_{j=1}^s (\lambda - \mu_j)\), кроме того, \(\varphi(\lambda) = \prod_{i=1}^n (\lambda_i - \lambda)\). Полагая \(\lambda = A\) в \(f(\lambda)\), получим: \(f(A) = a_0 \prod_{j=1}^s (A - \mu_j E)\). Переходя от матриц к определителям, находим

\[
|f(A)| = a_0^n \prod_{j=1}^s |A - \mu_j E| = a_0^n \prod_{j=1}^s \varphi(\mu_j) = a_0^n \prod_{j=1}^s \prod_{i=1}^n (\lambda_i - \mu_j) =
\]
\[
= \prod_{i=1}^n \left[ a_0 \prod_{j=1}^s (\lambda_i - \mu_j) \right] = \prod_{i=1}^n f(\lambda_i).
\]

С другой стороны, \(|f(A)| = a_0^n \prod_{j=1}^s \varphi(\mu_j) = R(f, \varphi)\).

1080. Указание. Применить равенство предыдущей задачи к многочлену \(g(x) = f(x) - \lambda\), где \(\lambda\) — произвольное число.

1081. Указание. Применить равенство \(|f(A)| = \frac{|g(A)|}{|h(A)|}\) и использовать задачи 1079 и 1080.

1082. Указание. Если хотя бы одна из матриц \(A, B\) невырождена, то утверждение вытекает из подобия матриц \(AB\) и \(BA\) (см. задачу 1047). В общем случае можно применить задачи 920 и 1070. Для матриц над полем с бесконечным (или достаточно большим) числом