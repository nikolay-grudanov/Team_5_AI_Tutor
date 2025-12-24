---
source_image: page_228.png
page_number: 228
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.35
tokens: 6257
characters: 1840
timestamp: 2025-12-24T08:13:36.951641
finish_reason: stop
---

(стрелки, направленные вверх, соответствуют отображению \( A \), а стрелки, направленные вниз, соответствуют отображению \( B \)).

При \( n > 2 \) рассмотрим ограничения \( A_L, B_L : L \to K \) отображений \( A \) и \( B \). Согласно лемме пара отображений \( A_L, B_L \) неразложима. При этом \( \dim L = n - m - 2 = t \) и \( \dim K = t + 1 \), где \( t < n \). По предположению индукции пара \( A_L, B_L \) эквивалентна паре

\[
\begin{pmatrix} I_t \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ I_t \end{pmatrix}.
\]

В частности, \( \ker A_L = \ker B_L = 0 \), а значит, \( t = n - 2 \). По предположению индукции можно построить базисы \( e_1, \ldots, e_{n-2} \) и \( \varepsilon_1, \ldots, \varepsilon_{n-1} \) в пространствах \( L \) и \( K \), а с их помощью можно построить требуемые базисы \( e_0, e_1, \ldots, e_{n-2}, e_{n-1} \) и \( \varepsilon_0, \varepsilon_1, \ldots, \varepsilon_{n-1}, \varepsilon_n \):

\[
\begin{array}{cccccc}
\varepsilon_0 & \in & A(B^{-1}(K)) \\
B^{-1}(K) \ni e_0 & \xrightarrow{} & \varepsilon_1 & \in & K \\
L \ni e_1 & \xrightarrow{} & \cdots & \cdots & \cdots & \cdots \\
L \ni e_{n-2} & \xrightarrow{} & \varepsilon_{n-1} & \in & K \\
A^{-1}(K) \ni e_{n-1} & \xrightarrow{} & \varepsilon_n & \in & B(A^{-1}(K)).
\end{array}
\]

(3) \( l \geqslant 2 \). В этом случае пара отображений \( A, B \) разложима. Доказательство проведём индукцией по \( n \).

При \( n = 1 \) выделяются прямые слагаемые \( V \to \operatorname{Im} A + \operatorname{Im} B \) и \( 0 \to (\operatorname{Im} A + \operatorname{Im} B)^{\perp} \neq 0 \).

При \( n > 1 \) рассмотрим ограничения \( A_L, B_L : L \to K \) отображений \( A \) и \( B \). Так как \( \dim L = n - m - 2l = t < n \) и \( \dim K = t + l \), то по предположению индукции пара \( A_L, B_L \) разложима. Но тогда согласно лемме разложима и пара \( A, B \).