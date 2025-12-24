---
source_image: page_219.png
page_number: 219
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.30
tokens: 8476
characters: 2224
timestamp: 2025-12-24T07:31:12.948156
finish_reason: stop
---

**Глава 8**

1. \(0,75 \cdot 10^{-m+2}\).
3. Нормальное распределение с параметрами \((0, 1)\).
4. \(\frac{\lambda^m}{m!} e^{-\lambda}\).

**Глава 9**

1. 1/6.
2. а) Нет, если \(p \neq q\) (например, \(P(\eta_3 = 1 / \eta_3 = -1) = 1/2\), \(P(\eta_3 = 1 | \eta_1 = 1, \eta_2 = -1) = 2pq\). б) Да, \(P(\eta_{t+1} = 1 | \eta_t = 1) = p\), \(P(\eta_{t+1} = 1 | \eta_t = -1) = q\). в) Да,
\[
\begin{pmatrix}
q & p & 0 & 0 \\
0 & 0 & q & p \\
q & p & 0 & 0 \\
0 & 0 & q & p
\end{pmatrix}
\]
3. \(\left( \begin{array}{cc} 3/7 & 4/7 \\ 1/11 & 10/11 \end{array} \right)\).

5. \[
\begin{pmatrix}
p_{11}(t) & p_{12}(t) \\
p_{21}(t) & p_{22}(t)
\end{pmatrix}
= \frac{1}{\alpha + \beta}
\begin{pmatrix}
\beta & \alpha \\
\beta & \alpha
\end{pmatrix}
+ \frac{(1-\alpha-\beta)t}{\alpha+\beta}
\begin{pmatrix}
\alpha & -\alpha \\
-\beta & \beta
\end{pmatrix}.
\]

**Глава 10**

3. \(M\alpha^* = a + \frac{b-a}{n+1}\), \(Mb^* = b - \frac{b-a}{n+1}\).
4. Да; \(M\alpha^* = 0\), \(D\alpha^* = 1/n^2\).
5. \(\lambda^* = (x_1 + x_2 + \ldots + x_n)/n\).
6. \(\alpha^* = (y_1 + \ldots + y_n)/n\),
\[
\beta^* = (x_1 y_1 + \ldots + x_n y_n)/(x_1^2 + \ldots + x_n^2), \quad (\sigma^2)^* = \frac{1}{n} \sum_{i=1}^n (y_i - \alpha^* - \beta^* x_i)^2.
\]

**Глава 11**

1. \(\lambda t + \lambda^2 t (t+s)\).
2. \(P(\tau_1 < t) = 1 - e^{-\lambda t}, t > 0\).
4. \(P(\tau_1 < t_1, \tau_2 < t_2) = (1 - e^{-\lambda t_1})(1 - e^{-\lambda t_2}), t_1 > 0, t_2 > 0\).
5. \(\frac{(\lambda t_1)^{k_1}}{k_1!} e^{-\lambda t_1} \times \frac{[\lambda (t_2 - t_1)]^{k_2 - k_1}}{(k_2 - k_1)!} e^{-\lambda (t_2 - t_1)} \frac{[\lambda (T - t_2)]^{k_3 - k_2}}{(k_3 - k_2)!} e^{-\lambda (T - t_2)}\).
6. \(bt\).
7. \(\lambda = (1 - p)/p\).
8. \(D\mu_t = B_t = t\), \(M\mu_t = 1\).

9.
\[
\begin{pmatrix}
p_{11}(t) & p_{12}(t) \\
p_{21}(t) & p_{22}(t)
\end{pmatrix}
= \frac{1}{\alpha + \beta}
\begin{pmatrix}
\beta & \alpha \\
\beta & \alpha
\end{pmatrix}
+ \frac{e^{-(\alpha+\beta)t}}{\alpha+\beta}
\begin{pmatrix}
\alpha & -\alpha \\
-\beta & \beta
\end{pmatrix}.
\]

10.
\[
\begin{cases}
\frac{\partial f_1}{\partial t} = -(\alpha - is) f_1 + \alpha f_2, \\
\frac{\partial f_2}{\partial t} = \beta f_1 - (\beta + is) f_2, \quad f_1(0, s) = f_2(0, s) = 1.
\end{cases}
\]