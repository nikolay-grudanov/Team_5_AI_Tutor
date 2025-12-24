---
source_image: page_225.png
page_number: 225
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.17
tokens: 6565
characters: 2391
timestamp: 2025-12-24T08:13:38.772367
finish_reason: stop
---

Ясно, что

\[
\dim A^{-1}(K)_N + \dim (\mathrm{Ker}\,A)_N = \dim A^{-1}(K) - \dim L =
= (n - l - b) - (n - a - b - 2l + r) = l + a - r.
\]

Аналогично \( \dim B^{-1}(K)_N + \dim (\mathrm{Ker}\,B)_N = l + b - r \).

Покажем, что сумма подпространств \( L \oplus (\mathrm{Ker}\,A)_N \oplus A^{-1}(K)_N \) и \( (\mathrm{Ker}\,B)_N \oplus B^{-1}(K)_N \) прямая. Предположим, что вектор \( x \) лежит в первом из этих подпространств. Тогда \( Ax \in A(L) + K \subset K \). А если вектор \( x \) лежит во втором из этих подпространств, то \( Bx \in K \). Таким образом, \( x \in A^{-1}(K) \cap B^{-1}(K) = L \). Остаётся заметить, что \( ((\mathrm{Ker}\,B)_N \oplus B^{-1}(K)_N) \cap L = 0 \).

Выберем в пространстве \( V \) подпространство \( X \) так, что

\[
V = L \oplus (\mathrm{Ker}\,A)_N \oplus A^{-1}(K)_N \oplus (\mathrm{Ker}\,B)_N \oplus B^{-1}(K)_N \oplus X.
\]

При этом \( \dim X = n - (n - a - b - 2l + r) - (l + a - r) - (l + b - r) = r \).
Рассмотрим подпространство \( Y = AX + BX \subset W \). Ясно, что \( \dim Y \leq 2r \).
Учитывая, что \( AL \subset K, A(\mathrm{Ker}\,A)_N = 0, A(A^{-1}(K)_N) \subset K \) и т. д., получаем, что пространство \( W = \mathrm{Im}\,A + \mathrm{Im}\,B \) можно представить в виде

\[
K + B(\mathrm{Ker}\,A)_N + B(A^{-1}(K)_N) + A(\mathrm{Ker}\,B)_N + A(B^{-1}(K)_N) + Y.
\]

Сумма размерностей слагаемых при этом не превосходит

\[
(n - l - a - b) + (l + a - r) + (l + b - r) + 2r = n + l = \dim W.
\]

Это означает, что рассматриваемая сумма подпространств прямая и, кроме того, ограничения отображения \( A \) на \( (\mathrm{Ker}\,B)_N \) и \( B^{-1}(K)_N \) обратимы, ограничения отображение \( B \) на \( (\mathrm{Ker}\,A)_N \) и \( A^{-1}(K)_N \) обратимы и \( \dim Y = 2r \).

Отображения \( A \) и \( B \) переводят

\[
L \oplus A^{-1}(K)_N \oplus B^{-1}(K)_N
\]

в

\[
K \oplus B(A^{-1}(K)_N) \oplus A(B^{-1}(K)_N),
\]

\( (\mathrm{Ker}\,A)_N \) в \( B(\mathrm{Ker}\,A)_N \), \( (\mathrm{Ker}\,B)_N \) в \( A(\mathrm{Ker}\,B)_N \), \( X \) в \( Y \). Неразложимая пара отображений получается лишь в том случае, когда пространства \( V \) и \( W \) сводятся к одному из этих четырёх слагаемых.

Легко проверить, что неразложимые отображения

\[
(\mathrm{Ker}\,A)_N \to B(\mathrm{Ker}\,A)_N,\quad (\mathrm{Ker}\,B)_N \to A(\mathrm{Ker}\,B)_N,\quad X \to Y
\]

имеют вид \( (0, I_1) \), \( (I_1, 0) \), \( (P_1^T, Q_1^T) \) соответственно.