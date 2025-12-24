---
source_image: page_122.png
page_number: 122
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.04
tokens: 8291
characters: 1929
timestamp: 2025-12-24T07:29:01.034132
finish_reason: stop
---

Доказательство. Положим

\[
\eta_n = c_1 \xi_1 + c_2 \xi_2 + \ldots + c_n \xi_n.
\]

Нетрудно проверить, что

\[
\eta_n - M \eta_n = \sum_{i=1}^n c_i (\xi_i - M \xi_i)
\]

и

\[
(\eta_n - M \eta_n)^2 = \sum_{i,j=1}^n c_i c_j (\xi_i - M \xi_i) (\xi_j - M \xi_j).
\]

Вычисляя математическое ожидание от обеих частей последнего равенства, получим утверждение теоремы.

Правую часть (4.4) можно рассматривать как квадратичную форму от переменных \( c_1, c_2, \ldots, c_n \). Так как при любых \( c_1, c_2, \ldots, c_n \) дисперсия в левой части (4.4) неотрицательна, то квадратичная форма в правой части (4.4) неотрицательно определена. Квадратичная форма неотрицательно определена тогда и только тогда, когда неотрицательны все главные миноры матрицы, составленной из ее коэффициентов. Таким образом, из теоремы 4.1 получили следующее утверждение.

Определитель

\[
\left| \begin{array}{cccc}
\operatorname{cov}(\xi_1, \xi_1) & \operatorname{cov}(\xi_1, \xi_2) & \ldots & \operatorname{cov}(\xi_1, \xi_m) \\
\operatorname{cov}(\xi_2, \xi_1) & \operatorname{cov}(\xi_2, \xi_2) & \ldots & \operatorname{cov}(\xi_2, \xi_m) \\
\ldots & \ldots & \ldots & \ldots \\
\operatorname{cov}(\xi_m, \xi_1) & \operatorname{cov}(\xi_m, \xi_2) & \ldots & \operatorname{cov}(\xi_m, \xi_m)
\end{array} \right| \geq 0 \tag{4.5}
\]

для любых случайных величин \( \xi_1, \xi_2, \ldots, \xi_m; m = 1, 2, \ldots \). При \( m = 2 \) неравенство (4.5) имеет вид

\[
\left| \begin{array}{cc}
D_{\xi_1} & \operatorname{cov}(\xi_1, \xi_2) \\
\operatorname{cov}(\xi_1, \xi_2) & D_{\xi_2}
\end{array} \right| = D_{\xi_1} D_{\xi_2} - \operatorname{cov}^2(\xi_1, \xi_2) \geq 0.
\]

Отсюда

\[
|\operatorname{cov}(\xi_1, \xi_2)| \leq \sqrt{D_{\xi_1} D_{\xi_2}}. \tag{4.6}
\]

В доказательстве формулы (3.5) было попутно получено, что для независимых случайных величин \( \xi_1, \xi_2 \) имеет место равенство

\[
\operatorname{cov}(\xi_1, \xi_2) = 0. \tag{4.7}
\]