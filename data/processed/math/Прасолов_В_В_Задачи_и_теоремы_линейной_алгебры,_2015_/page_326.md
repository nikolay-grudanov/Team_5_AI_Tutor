---
source_image: page_326.png
page_number: 326
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.69
tokens: 6394
characters: 1988
timestamp: 2025-12-24T08:16:17.753337
finish_reason: stop
---

Поэтому \( \Lambda^n(A + \lambda^2 M) = n! \sum_{k=0}^n \lambda^{2k} P_k e_1 \wedge \ldots \wedge e_{2n} \), а значит,

\[
\operatorname{Pf}(A + \lambda^2 M) = \sum_{k=0}^n \lambda^{2k} P_k.
\]

Задачи

31.1. Пусть \( \operatorname{Pf}(A) = a_{pq} C_{pq} + f \), где многочлен \( f \) не зависит от \( a_{pq} \); \( A_{pq} \) — матрица, полученная из \( A \) вычёркиванием строк и столбцов с номерами \( p \) и \( q \). Докажите, что \( C_{pq} = (-1)^{p+q+1} \operatorname{Pf}(A_{pq}) \).

31.2. Пусть \( X \) — матрица порядка \( 2n \), строками которой являются координаты векторов \( x_1, \ldots, x_{2n} \); \( g_{ij} = \{x_i, x_j\} \), где величина \( \{a, b\} \) для векторов \( a = (a_1, \ldots a_{2n}) \) и \( b = (b_1, \ldots, b_{2n}) \) равна

\[
\sum_{k=1}^n (a_{2k-1} b_{2k} - a_{2k} b_{2k-1}).
\]

Докажите, что \( \det X = \operatorname{Pf}(G) \), где \( G = \|g_{ij}\|_1^{2n} \).

§ 32. Разложимые тензоры

32.1. Разложимый тензор определяет подпространство

Кососимметрический тензор \( \omega \in \Lambda^k(V) \) называют разложимым, если его можно представить в виде \( \omega = x_1 \wedge \ldots \wedge x_k \), где \( x_i \in V \).

Симметрический тензор \( T \in S^k(V) \) называют разложимым, если его можно представить в виде \( T = S(x_1 \otimes \ldots \otimes x_k) \), где \( x_i \in V \).

Теорема 32.1.1. Если \( x_1 \wedge \ldots \wedge x_k = y_1 \wedge \ldots \wedge y_k \neq 0 \), то \( \langle x_1, \ldots, x_k \rangle = \langle y_1, \ldots, y_k \rangle \).

Доказательство. Предположим, например, что \( y_1 \notin \langle x_1, \ldots, x_k \rangle \). Тогда векторы \( e_1 = x_1, \ldots, e_k = x_k \) и \( e_{k+1} = y_1 \) можно дополнить до базиса. Разложив векторы \( y_1, \ldots, y_k \) по этому базису, получим равенство

\[
e_1 \wedge \ldots \wedge e_k = e_{k+1} \wedge \left( \sum a_{i_2 \ldots i_k} e_{i_2} \wedge \ldots \wedge e_{i_k} \right).
\]

Это равенство противоречит линейной независимости векторов \( e_{i_1} \wedge \ldots \wedge e_{i_k} \).