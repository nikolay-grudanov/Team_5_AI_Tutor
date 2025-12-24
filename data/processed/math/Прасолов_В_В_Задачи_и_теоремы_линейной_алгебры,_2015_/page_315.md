---
source_image: page_315.png
page_number: 315
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.32
tokens: 6530
characters: 2465
timestamp: 2025-12-24T08:16:09.204127
finish_reason: stop
---

где \(1 \leq i_1 < \ldots < i_q \leq n\), причём любой такой набор значений соответствует некоторой кососимметрической функции. Поэтому размерность пространства кососимметрических функций равна размерности пространства \(\Lambda^q V^*\), а значит, эти пространства изоморфны.

Построим теперь канонический изоморфизм \(\Lambda^q V^* \to (\Lambda^q V)^*\). Линейное отображение \(V^* \otimes \ldots \otimes V^* \to (V \otimes \ldots \otimes V)^*\), переводящее элемент \((f_1, \ldots, f_q) \in V^* \otimes \ldots \otimes V^*\) в полилинейную функцию

\[
f(v_1, \ldots, v_q) = f_1(v_1) \ldots f_q(v_q),
\]

является каноническим изоморфизмом. Рассмотрим ограничение этого отображения на \(\Lambda^q V^*\). Элемент \(f_1 \wedge \ldots \wedge f_q = A(f_1 \otimes \ldots \otimes f_q) \in \Lambda^q V^*\) переходит в полилинейную функцию

\[
f(v_1, \ldots, v_q) = \frac{1}{q!} \sum_{\sigma} (-1)^{\sigma} f_1(v_{\sigma(1)}) \ldots f_q(v_{\sigma(q)}).
\]

Функция \(f\) кососимметрична, поэтому получаем отображение \(\Lambda^q V^* \to (\Lambda^q V)^*\). Проверим, что это отображение — изоморфизм. Ясно, что

\[
\tilde{f}(A(v_1 \otimes \ldots \otimes v_q)) = \left( \frac{1}{q!} \right)^2 \sum_{\sigma, \tau} (-1)^{\sigma \tau} f_1(v_{\sigma \tau(1)}) \ldots f_q(v_{\sigma \tau(q)}) =
\]
\[
= \frac{1}{q!} \sum_{\sigma} (-1)^{\sigma} f_1(v_{\sigma(1)}) \ldots f_q(v_{\sigma(q)}) = \frac{1}{q!} \begin{vmatrix}
f_1(v_1) & \ldots & f_1(v_q) \\
\cdots & \cdots & \cdots \\
f_q(v_1) & \ldots & f_q(v_q)
\end{vmatrix}.
\]

Пусть \(e_1, \ldots, e_n\) и \(\varepsilon_1, \ldots, \varepsilon_n\) — двойственные базисы пространств \(V\) и \(V^*\). Элементы \(e_{i_1} \wedge \ldots \wedge e_{i_q}\) образуют базис пространства \(\Lambda^q V\); рассмотрим двойственный базис пространства \((\Lambda^q V)^*\). Из доказанного выше равенства следует, что при рассматриваемом отображении элемент \(\varepsilon_{i_1} \wedge \ldots \wedge \varepsilon_{i_q}\) переходит в базисный элемент, двойственный \(q! \, e_{i_1} \wedge \ldots \wedge e_{i_q}\).

Замечание. Попутно доказано равенство

\[
\tilde{f}(A(v_1 \otimes \ldots \otimes v_q)) = \frac{1}{q!} \tilde{f}(v_1 \otimes \ldots \otimes v_q)
\]

для \(f \in \Lambda^q V^*\).

30.4. Свойства внешнего произведения

Теорема 30.4.1. \(T_0^2(V) = \Lambda^2(V) \oplus S^2(V)\).

Доказательство. Для доказательства достаточно заметить, что

\[
a \otimes b = \frac{1}{2}(a \otimes b - b \otimes a) + \frac{1}{2}(a \otimes b + b \otimes a).
\]