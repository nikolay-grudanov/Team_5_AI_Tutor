---
source_image: page_281.png
page_number: 281
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.85
tokens: 6553
characters: 2729
timestamp: 2025-12-24T08:15:13.183074
finish_reason: stop
---

Доказательство. Равенства \( A^*x = 0 \) и \( Ax = 0 \) эквивалентны, так как \( (A^*x, A^*x) = (x, AA^*x) = (x, A^*Ax) = (Ax, Ax) \).

Равенство \( A^*x = 0 \) означает, что \( (x, Ay) = (A^*x, y) = 0 \) для всех \( y \), т. е. \( x \in (\operatorname{Im} A)^{\perp} \). Поэтому \( \operatorname{Im} A = (\operatorname{Ker} A^*)^{\perp} \) и \( \operatorname{Im} A^* = (\operatorname{Ker} A)^{\perp} \). А так как \( \operatorname{Ker} A = \operatorname{Ker} A^* \), то \( \operatorname{Im} A = \operatorname{Im} A^* \).

Следствие. Если \( A \) — нормальный оператор, то \( V = \operatorname{Ker} A \oplus (\operatorname{Ker} A)^{\perp} = \operatorname{Ker} A \oplus \operatorname{Im} A \).

25.2. Собственные векторы нормального оператора

Теорема 25.2.1. Оператор \( A \) нормален тогда и только тогда, когда любой собственный вектор оператора \( A \) является собственным вектором оператора \( A^* \).

Доказательство. Легко проверить, что если оператор \( A \) нормален, то оператор \( A - \lambda I \) тоже нормален, а значит, \( \operatorname{Ker}(A - \lambda I) = \operatorname{Ker}(A^* - \overline{\lambda} I) \), т. е. любой собственный вектор оператора \( A \) является собственным вектором оператора \( A^* \).

Предположим теперь, что любой собственный вектор оператора \( A \) является собственным вектором оператора \( A^* \). Докажем, что если \( Ax = \lambda x \), то \( A(\langle x \rangle^{\perp}) \subset \langle x \rangle^{\perp} \). В самом деле, если \( y \in \langle x \rangle^{\perp} \), то \( (x, Ay) = (A^*x, y) = (\mu x, y) = \mu(x, y) = 0 \). Возьмём произвольный собственный вектор \( e_1 \) оператора \( A \). Оператор \( A \) можно ограничить на пространство \( \langle e_1 \rangle^{\perp} \). В этом пространстве возьмём произвольный собственный вектор \( e_2 \) оператора \( A \) и т. д. В итоге получим ортонормированный собственный базис оператора \( A \), поэтому \( A \) — нормальный оператор.

25.3. Полиномиальное выражение \( A^* \) через \( A \)

Теорема 25.3.1. Если \( A \) — нормальная матрица, то \( A^* \) полиномиально выражается через \( A \).

Доказательство. Пусть \( A = U \Lambda U^* \), где \( \Lambda = \operatorname{diag}(\lambda_1, \ldots, \lambda_n) \) и \( U \) — унитарная матрица. Тогда
\[
A^* = U \Lambda^* U^*,
\]
где \( \Lambda^* = \operatorname{diag}(\overline{\lambda}_1, \ldots, \overline{\lambda}_n) \). Построим интерполяционный многочлен \( p \), для которого \( p(\lambda_i) = \overline{\lambda}_i \) при \( i = 1, \ldots, n \). Тогда
\[
p(\Lambda) = \operatorname{diag}(p(\lambda_1), \ldots, p(\lambda_n)) = \operatorname{diag}(\overline{\lambda}_1, \ldots, \overline{\lambda}_n) = \Lambda^*.
\]
Поэтому \( p(A) = Up(\Lambda)U^* = U \Lambda^* U^* = A^* \).