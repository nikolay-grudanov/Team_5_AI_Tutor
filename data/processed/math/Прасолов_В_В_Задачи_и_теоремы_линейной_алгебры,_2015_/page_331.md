---
source_image: page_331.png
page_number: 331
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.16
tokens: 6540
characters: 2493
timestamp: 2025-12-24T08:16:37.631888
finish_reason: stop
---

32.3. Альтернатива соотношениям Плюккера

Соотношения Плюккера — это система уравнений степени 2, задающая множество разложимых тензоров в \( \Lambda^m V \). То же самое множество можно задать системой уравнений степени \( m \). Делается это следующим образом.

Для \( \alpha_1, \ldots, \alpha_m \in V^* \) можно рассмотреть линейные отображения \( c_j : \Lambda^m V \to V, j = 1, \ldots, m \), и \( c : \Lambda^m V \to \mathbb{R} \), которые задаются следующими формулами:

\[
c_j(v_1 \wedge \ldots \wedge v_m) = \begin{vmatrix}
\alpha_1(v_1) & \ldots & \alpha_{j-1}(v_1) & v_1 & \alpha_{j+1}(v_1) & \ldots & \alpha_m(v_1) \\
\cdots & \cdots & \cdots & \cdots & \cdots & \cdots & \cdots \\
\alpha_1(v_m) & \ldots & \alpha_{j-1}(v_m) & v_m & \alpha_{j+1}(v_m) & \ldots & \alpha_m(v_m)
\end{vmatrix},
\]

\[
c(v_1 \wedge \ldots \wedge v_m) = \begin{vmatrix}
\alpha_1(v_1) & \ldots & \alpha_m(v_1) \\
\cdots & \cdots & \cdots \\
\alpha_1(v_m) & \ldots & \alpha_m(v_m)
\end{vmatrix}.
\]

Здесь выражение для \( c_j \) нужно понимать как формальное разложение определителя по \( j \)-му столбцу, т. е. \( c_j(v_1 \wedge \ldots \wedge v_m) \) — это линейная комбинация векторов \( v_1, \ldots, v_m \) с соответствующими коэффициентами.

Теорема 32.3.1 [Ro1]. Кососимметрический тензор \( \omega \in \Lambda^m V \) разложим тогда и только тогда, когда для любых \( \alpha_1, \ldots, \alpha_m \in V^* \) имеет место равенство

\[
c_1(\omega) \wedge \ldots \wedge c_m(\omega) = (c(\omega))^{m-1} \omega,
\]

где \( c_1, \ldots, c_m \) и \( c \) определены по \( \alpha_1, \ldots, \alpha_m \), как указано выше.

Доказательство. Если равенство (1) имеет место для всех \( \alpha_1, \ldots, \alpha_m \), то для данного \( \omega \neq 0 \) мы сразу получаем явное разложение, поскольку \( \alpha_1, \ldots, \alpha_m \) можно выбрать так, что \( c(\omega) = 1 \).

Предположим теперь, что \( \omega = v_1 \wedge \ldots \wedge v_m \). Равенство (1) можно доказать разными способами.

Первый способ. Пусть \( a_{ij} = \alpha_i(v_j) \) и \( M_{ij} \) — определитель матрицы, полученной из матрицы \( A = \| a_{ij} \|_1^m \) вычёркиванием \( i \)-й строки и \( j \)-го столбца. Тогда \( c_1(\omega) \wedge \ldots \wedge c_m(\omega) = w_1 \wedge \ldots \wedge w_m \), где

\[
w_j = \sum_{k=1}^m (-1)^{k+j} M_{kj} v_j.
\]

Поэтому

\[
c_1(\omega) \wedge \ldots \wedge c_m(\omega) = \sum_{(i_1, \ldots, i_m) \in S_m} (-1)^{(i_1, \ldots, i_m)} M_{1i_1} \cdot \ldots \cdot M_{mi_m} v_1 \wedge \ldots \wedge v_m.
\]