---
source_image: page_410.png
page_number: 410
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.77
tokens: 6677
characters: 2858
timestamp: 2025-12-24T08:18:53.902430
finish_reason: stop
---

и \( B \) индуцируют операторы \( A_1 \) и \( B_1 \) в пространстве \( V_1 = V / \langle v \rangle \), причём \( \operatorname{rk} [A_1, B_1] \leq 1 \). Следовательно, операторы \( A_1 \) и \( B_1 \) имеют общий собственный вектор в пространстве \( V_1 \) и т. д. Кроме того, можно считать, что \( \operatorname{Ker} A \neq 0 \) (иначе вместо оператора \( A \) можно взять оператор \( A - \lambda I \)).

Доказательство проведём индукцией по \( n = \dim V \). Если \( n = 1 \), то утверждение очевидно. Пусть \( C = [A, B] \). При доказательстве шага индукции рассмотрим два случая.

1. \( \operatorname{Ker} A \subset \operatorname{Ker} C \). В этом случае \( B(\operatorname{Ker} A) \subset \operatorname{Ker} A \), так как если \( Ax = 0 \), то \( Cx = 0 \) и \( ABx = BAx + Cx = 0 \). Следовательно, можно рассмотреть ограничение оператора \( B \) на \( \operatorname{Ker} A \neq 0 \) и выбрать в \( \operatorname{Ker} A \) собственный вектор \( v \) оператора \( B \); вектор \( v \) при этом будет также и собственным вектором оператора \( A \).

2. \( \operatorname{Ker} A \not\subset \operatorname{Ker} C \), т. е. \( Ax = 0 \) и \( Cx \neq 0 \) для некоторого вектора \( x \). Так как \( \operatorname{rk} C = 1 \), то \( \operatorname{Im} C = \langle y \rangle \), где \( y = Cx \). Кроме того,
\[
y = Cx = ABx - BAx = ABx \in \operatorname{Im} A.
\]
Следовательно, \( B(\operatorname{Im} A) \subset \operatorname{Im} A \). В самом деле, \( BAz = ABz - Cz \), где \( ABz \in \operatorname{Im} A \) и \( Cz \in \operatorname{Im} C \subset \operatorname{Im} A \). По предположению \( \operatorname{Ker} A \neq 0 \), поэтому \( \dim \operatorname{Im} A < n \). Пусть \( A' \) и \( B' \) — ограничения операторов \( A \) и \( B \) на \( \operatorname{Im} A \). Тогда \( \operatorname{rk} [A', B'] \leq 1 \), а значит, согласно предположению индукции у операторов \( A' \) и \( B' \) есть общий собственный вектор. □

Задачи

43.1. Пусть \( A = \operatorname{diag}(1, 2, \ldots, n) \), \( J = N + \lambda I \) — жорданова клетка порядка \( n \) и \( B = NA \). Докажите, что \( \operatorname{ad}_J^2 A = \operatorname{ad}_J^2 B = 0 \).

43.2. Докажите, что \( \operatorname{tr}([A, B]C) = \operatorname{tr}(A[B, C]) \).

43.3. Докажите, что если \( C = [A_1, B_1] + \ldots + [A_n, B_n] \) и матрица \( C \) коммутирует с матрицами \( A_1, \ldots, A_n \), то матрица \( C \) нильпотентна.

43.4. Докажите, что \( \operatorname{ad}_A^n(B) = \sum_{i=0}^n (-1)^{n-i} \binom{n}{i} A^i B A^{n-i} \).

43.5. Докажите, что если оператор \( A \) нильпотентен, то оператор \( \operatorname{ad}_A \) тоже нильпотентен.

43.6 [Kl1]. Докажите, что если \( \operatorname{ad}_A^2(B) = 0 \), то \( \operatorname{ad}_A^n(B^n) = n! (\operatorname{ad}_A(B))^n \).

43.7. Докажите, что если \( [A, [A, B]] = 0 \) и \( m \geq n > 0 \), то \( n[A^m, B] = m[A^n, B]A^{m-n} \).