---
source_image: page_320.png
page_number: 320
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.94
tokens: 6546
characters: 2443
timestamp: 2025-12-24T08:16:13.772923
finish_reason: stop
---

в вектор

\[
(-1)^{\sigma}(-1)^{\tau}
\begin{vmatrix}
a_{\alpha_{p+1}, j_1} & \cdots & a_{\alpha_{p+1}, j_{n-p}} \\
\cdots & \cdots & \cdots \\
a_{\alpha_n, j_1} & \cdots & a_{\alpha_n, j_{n-p}}
\end{vmatrix}
e_{j_1} \wedge \ldots \wedge e_{j_{n-p}},
\]

где набор \( j_1, \ldots, j_{n-p} \) и перестановка \( \sigma \) строятся по набору \( i_1, \ldots, i_p \), как описано выше. Ясно, что \( (-1)^{\sigma}(-1)^{\tau} = (-1)^{\rho} \), где \( \rho = (\alpha_1, \ldots, \alpha_n) \). Таким образом, вектор \( Ae_{\alpha_1} \wedge \ldots \wedge Ae_{\alpha_p} \) переходит в вектор

\[
(-1)^{\rho} Ae_{\alpha_{p+1}} \wedge \ldots \wedge Ae_{\alpha_n},
\]

т. е. отображение *, которое задаётся базисом \( e_1, \ldots, e_n \), совпадает с отображением *, которое задаётся базисом \( Ae_1, \ldots, Ae_n \).

Отображение Ходжа является изометрией относительно скалярного произведения в \( \Lambda^{n-1}(\mathbb{R}^n) \), заданного формулой

\[
(v_1 \wedge \ldots \wedge v_{n-1}, w_1 \wedge \ldots \wedge w_{n-1}) = |(v_i, w_j)|_1^{n-1},
\]

т. е. если \( *(v_1 \wedge \ldots \wedge v_{n-1}) = v_n \) и \( *(w_1 \wedge \ldots \wedge w_{n-1}) = w_n \), то имеет место равенство

\[
(v_n, w_n) = |(v_i, w_j)|_1^{n-1}.
\]

Действительно, это равенство очевидно в случае, когда \( v_n \) и \( w_n \) — векторы из канонического базиса. Кроме того, обе части этого равенства — полилинейные функции от \( v_1, \ldots, v_{n-1} \) и от \( w_1, \ldots, w_{n-1} \).

30.7. Векторное произведение

Отображение Ходжа в \( \mathbb{R}^3 \) тесно связано с векторным произведением, а именно,

\[
v \times w = *(v \wedge w).
\]

Действительно, обе части этого равенства линейны по \( v \) и \( w \), поэтому его достаточно проверить для базисных векторов. Остаётся заметить, что \( *(e_1 \wedge e_2) = e_3, *(e_1 \wedge e_3) = -e_2 \) и \( *(e_2 \wedge e_3) = e_1 \).

Аналогичным образом для векторов \( v_1, \ldots, v_{n-1} \in \mathbb{R}^{n-1} \) можно определить их векторное произведение следующим образом:

\[
v_1 \times v_2 \times \ldots \times v_{n-1} = *(v_1 \wedge v_2 \wedge \ldots \wedge v_{n-1}).
\]

Эквивалентное определение векторного произведения таково. Фиксируем векторы \( v_1, \ldots, v_{n-1} \in \mathbb{R}^n \) и рассмотрим функцию \( \varphi : \mathbb{R}^n \to \mathbb{R} \), заданную формулой \( \varphi(u) = \det(v_1, \ldots, v_{n-1}, u) \) — определитель матрицы, столбцами которой служат координаты векторов \( v_1, \ldots, v_{n-1}, u \).