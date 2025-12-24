---
source_image: page_428.png
page_number: 428
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.85
tokens: 6615
characters: 2206
timestamp: 2025-12-24T08:19:18.824543
finish_reason: stop
---

43.4. При \( n = 1 \) утверждение верно. Ясно также, что если утверждение верно для \( n \), то

\[
\operatorname{ad}_A^{n+1}(B) = \sum_{i=0}^n (-1)^{n-i} \binom{n}{i} A^{i+1} B A^{n-i} - \sum_{i=0}^n (-1)^{n-i} \binom{n}{i} A^i B A^{n-i+1} =
\]
\[
= \sum_{i=1}^{n+1} (-1)^{n-i+1} \binom{n}{i-1} A^i B A^{n-i+1} + \sum_{i=0}^n (-1)^{n-i+1} \binom{n}{i} A^i B A^{n-i+1} =
\]
\[
= \sum_{i=0}^{n+1} (-1)^{n+1-i} \binom{n+1}{i} A^i B A^{n+1-i}.
\]

43.5. Пусть \( A^k = 0 \) и \( n = 2k - 1 \). Согласно задаче 43.4
\[
\operatorname{ad}_A^n(B) = \sum_{i=0}^n (-1)^i \binom{n}{i} A^i B A^{n-i}.
\]
Одно из чисел \( i \) и \( n - i \) не меньше \( k \), поэтому \( A^i B A^{n-i} = 0 \). Следовательно, \( \operatorname{ad}_A^n(B) = 0 \).

43.6. Отображение \( D = \operatorname{ad}_A : M_{n,n} \to M_{n,n} \) является дифференцированием. Нужно доказать, что если \( D^2 B = 0 \), то \( D^n(B^n) = n! (DB)^n \). Для \( n = 1 \) утверждение очевидно. Предположим, что утверждение верно для некоторого \( n \). Тогда
\[
D^{n+1}(B^n) = D[D^n(B^n)] = n! D[(DB)^n] = n! \sum_{i=0}^{n-1} (DB)^i (D^2 B)(DB)^{n-1-i} = 0.
\]
Ясно, что
\[
D^{n+1}(B^{n+1}) = D^{n+1}(B \cdot B^n) = \sum_{i=0}^{n+1} \binom{n+1}{i} (D^i B)(D^{n+1-i}(B^n)).
\]
А так как \( D^i B = 0 \) при \( i \geq 2 \), то
\[
D^{n+1}(B^{n+1}) = B \cdot D^{n+1}(B^n) + (n+1)(DB)(D^n(B^n)) =
= (n+1)(DB)(D^n(B^n)) = (n+1)! (DB)^{n+1}.
\]

43.7. Докажем сначала требуемое утверждение при \( n = 1 \). При \( m = 1 \) утверждение очевидно. Ясно также, что если утверждение верно для некоторого \( m \), то \([A^{m+1}, B] = A(A^m B - B A^m) + (AB - BA)A^m = mA[A, B]A^{m-1} + [A, B]A^m = (m+1)[A, B]A^m\).
Пусть теперь \( m > n > 0 \). Домножив равенство \([A^n, B] = n[A, B]A^{n-1}\) справа на \(mA^{m-n}\), получим \(m[A^n, B]A^{m-n} = mn[A, B]A^{m-1} = n[A^m, B]\).

43.8. Оператору \( \operatorname{ad}_A \) в пространстве \( \operatorname{Hom}(V, V) \) соответствует оператор \( L = I \otimes A - A^T \otimes I \) в пространстве \( V^* \otimes V \) (см. п. 29.8). Если оператор \( A \) диагонален в базисе \( e_1, \ldots, e_n \), то оператор \( L \) диагонален в базисе \( e_i^* \otimes e_j \). Поэтому \( \operatorname{Ker} L^n = \operatorname{Ker} L \).