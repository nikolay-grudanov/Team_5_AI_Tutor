---
source_image: page_322.png
page_number: 322
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.72
tokens: 5686
characters: 2331
timestamp: 2025-12-24T07:12:58.591329
finish_reason: stop
---

функцию от p-векторов \( \varphi^1, \varphi^2, \ldots, \varphi^p \) сопряженного пространства \( V_n^* \), заданную равенством

\[
F(\varphi^1, \varphi^2, \ldots, \varphi^p) = \begin{vmatrix}
\varphi^1(x_1) & \varphi^2(x_1) & \ldots & \varphi^p(x_1) \\
\varphi^1(x_2) & \varphi^2(x_2) & \ldots & \varphi^p(x_2) \\
\ldots & \ldots & \ldots & \ldots \\
\varphi^1(x_p) & \varphi^2(x_p) & \ldots & \varphi^p(x_p)
\end{vmatrix}.
\]

**1913.** Выяснить, как изменяются координаты тензора типа \((p, q)\) при переходе от базиса \(e_1, \ldots, e_n\) к базису \(e'_1, \ldots, e'_n\), полученному из предыдущего путем данной подстановки \(\pi(i) = k_i\) (\(i = 1, 2, \ldots, n\)); это значит, что \(e'_i = e_{\pi(i)}\) (\(i = 1, 2, \ldots, n\)).

**1914.** Найти координаты в данном базисе \(e_1, \ldots, e_n\) тензора типа \((n, n)\), заданного равенством

\[
F(x_1, \ldots, x_n; \quad \varphi^1, \ldots, \varphi^n) = \begin{vmatrix}
\varphi^1(x_1) & \varphi^2(x_1) & \ldots & \varphi^n(x_1) \\
\varphi^1(x_2) & \varphi^2(x_2) & \ldots & \varphi^n(x_2) \\
\ldots & \ldots & \ldots & \ldots \\
\varphi^1(x_n) & \varphi^2(x_n) & \ldots & \varphi^n(x_n)
\end{vmatrix}.
\]

**1915.** Пусть \( F(x_1, \ldots, x_n; \quad \varphi^1, \ldots, \varphi^n) \) — полилинейная функция, кососимметрическая как по аргументам \(x_1, \ldots, x_n\), так и по аргументам \(\varphi^1, \ldots, \varphi^n\). Доказать, что ее значения через координаты в данном базисе выражаются формулой

\[
F(x_1, \ldots, x_n, \quad \varphi^1, \ldots, \varphi^n) = \det(x) \det(\varphi) \cdot F(e_1, \ldots, e_n; \quad e^1, \ldots, e^n),
\]

где \(e^i\) — базис, сопряженный базису \(e_i\), \(\det(x)\) — определитель из координат векторов \(x_1, \ldots, x_n\) в базисе \(e_1, \ldots, e_n\) и \(\det(\varphi)\) — определитель из координат векторов \(\varphi^1, \ldots, \varphi^n\) в базисе \(e^1, \ldots, e^n\).

**1916.** Пусть дан тензор типа \((p, q)\) в виде полилинейной функции \(F(x_1, \ldots, x_p; \quad \varphi^1, \ldots, \varphi^q)\). Его сверткой по номерам \(k \leq p,\ l \leq q\) называется сумма

\[
\sum_{i=1}^n F(x_1, \ldots, x_{k-1}, e_i, x_{k+1}, \ldots, x_p; \quad \varphi^1, \ldots, \varphi^{l-1}, e^l, \varphi^{l+1}, \ldots, \varphi^1).
\]

Показать, что свертка не зависит от базиса и является тензором типа \((p-1, q-1)\). Предполагается, что \(p, q > 0\).