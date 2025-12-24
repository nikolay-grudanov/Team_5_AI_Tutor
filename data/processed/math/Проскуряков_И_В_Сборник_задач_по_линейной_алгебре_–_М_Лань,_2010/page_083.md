---
source_image: page_083.png
page_number: 83
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.63
tokens: 5586
characters: 2104
timestamp: 2025-12-24T07:07:19.692077
finish_reason: stop
---

*517. Показать, что определитель

\[
\begin{vmatrix}
1 & \cos \varphi_3 & \cos \varphi_2 \\
\cos \varphi_3 & 1 & \cos \varphi_1 \\
\cos \varphi_2 & \cos \varphi_1 & 1
\end{vmatrix}
\]

равен нулю, если \( \varphi_1 + \varphi_2 + \varphi_3 = 0 \).

*518. Пусть \( l_1, l_2, l_3 \) и \( m_1, m_2, m_3 \) — косинусы углов двух лучей с ортогональными осями координат и \( \varphi \) — угол между этими лучами. Доказать, что \( \sin^2 \varphi = (l_1 m_2 - l_2 m_1)^2 + (l_2 m_3 - l_3 m_2)^2 + (l_3 m_1 - l_1 m_3)^2 \).

519. Пусть \( \alpha_1, \beta_1, \gamma_1; \alpha_2, \beta_2, \gamma_2; \alpha_3, \beta_3, \gamma_3 \) — углы трех лучей \( L_1, L_2, L_3 \) с ортогональными осями координат, и пусть углы этих лучей между собой будут \( \varphi_1 = \angle(L_2, L_3), \varphi_2 = \angle(L_3, L_1), \varphi_3 = \angle(L_1, L_2) \). Доказать, что

\[
\begin{vmatrix}
\cos \alpha_1 & \cos \beta_1 & \cos \gamma_1 \\
\cos \alpha_2 & \cos \beta_2 & \cos \gamma_2 \\
\cos \alpha_3 & \cos \beta_3 & \cos \gamma_3
\end{vmatrix}^2 =
= 1 - \cos^2 \varphi_1 - \cos^2 \varphi_2 - \cos^2 \varphi_3 + 2 \cos \varphi_1 \cos \varphi_2 \cos \varphi_3.
\]

*520. Пусть \( (x_1, y_1), (x_2, y_2), (x_3, y_3) \) будут прямоугольные координаты точек \( M_1, M_2, M_3 \) на плоскости. Показать, что определитель

\[
\begin{vmatrix}
x_1 & y_1 & 1 \\
x_2 & y_2 & 1 \\
x_3 & y_3 & 1
\end{vmatrix}
\]

не изменится при повороте осей координат и переносе начала. Пользуясь этим, выяснить его геометрический смысл.

*521. Пусть \( (x_1, y_1) \) и \( x_2, y_2 \) — прямоугольные координаты двух точек \( M_1 \) и \( M_2 \) на плоскости. Выяснив геометрический смысл определителя \( \begin{vmatrix} x_1 & y_1 \\ x_2 & y_2 \end{vmatrix} \), узнать, меняется ли он при повороте осей и при переносе начала координат?

*522. Вычислив произведение определителей

\[
\begin{vmatrix}
x_1 & y_1 & R \\
x_2 & y_2 & R \\
x_3 & y_3 & R
\end{vmatrix}
\cdot
\begin{vmatrix}
-x_1 & -y_1 & R \\
-x_2 & -y_2 & R \\
-x_3 & -y_3 & R
\end{vmatrix},
\]

получить выражение радиуса описанного круга через стороны \( a, b, c \) и площадь \( S \) треугольника.