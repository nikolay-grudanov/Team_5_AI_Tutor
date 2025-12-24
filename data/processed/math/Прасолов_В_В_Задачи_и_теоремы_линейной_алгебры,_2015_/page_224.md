---
source_image: page_224.png
page_number: 224
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.55
tokens: 6528
characters: 2412
timestamp: 2025-12-24T08:13:36.940168
finish_reason: stop
---

Несложно показать, что пара линейных отображений \( P_k, Q_k : V^{k+1} \to W^k \) неразложима.

**Теорема 14.6.1 (Кронекер).** *Любая неразложимая пара линейных отображений \( A, B : V \to W \) над полем \( \mathbb{C} \) эквивалентна одной из следующих пар:*
1) \( (I_k, J_k(\lambda)),\ k \geqslant 1; \)
2) \( (J_k(\lambda), I_k),\ k \geqslant 1; \)
3) \( (P_k, Q_k),\ k \geqslant 0; \)
4) \( (P_k^T, Q_k^T),\ k \geqslant 0. \)

**Доказательство [Bu].** Перейдя при необходимости к транспонированным матрицам (т. е. к отображениям двойственных пространств), будем считать, что \( \dim V \leqslant \dim W \). Пусть \( \dim V = n, \dim W = n + l, \) где \( l \geqslant 0 \).

В том случае, когда \( \operatorname{Ker}\,A \cap \operatorname{Ker}\,B = U \neq 0 \), неразложимая пара отображений имеет вид \( A, B : U \to 0 \), причём \( \dim U = 1 \). А в том случае, когда \( \operatorname{Im}\,A + \operatorname{Im}\,B = U \neq W \), неразложимая пара отображений имеет вид \( A, B : 0 \to U^\perp \), где \( U^\perp \) — дополнение к \( U \) в \( W \); при этом \( \dim U = 1 \). Поэтому в дальнейшем будем считать, что \( \operatorname{Ker}\,A \cap \operatorname{Ker}\,B = 0 \) и \( \operatorname{Im}\,A + \operatorname{Im}\,B = W \).

Рассмотрим подпространства

\[
K = \operatorname{Im}\,A \cap \operatorname{Im}\,B \quad \text{и} \quad L = A^{-1}(K) \cap B^{-1}(K).
\]

Если \( \dim \operatorname{Ker}\,A = a \) и \( \dim \operatorname{Ker}\,B = b \), то \( \dim \operatorname{Im}\,A = n - a \) и \( \dim \operatorname{Im}\,B = n - b \). Поэтому \( \dim K + (n + l) = (n - a) + (n - b) \), т. е. \( \dim K = n - l - a - b \). Ясно также, что

\[
\dim A^{-1}(K) = \dim \operatorname{Ker}\,A + \dim K = a + (n - l - a - b) = n - l - b
\]
и \( \dim B^{-1}(K) = n - l - a \). Поэтому
\[
\dim L \geqslant \dim A^{-1}(K) + \dim B^{-1}(K) - \dim V = n - a - b - 2l.
\]

Положим \( \dim L = n - a - b - 2l + r \), где \( r \geqslant 0 \).

Рассмотрим подпространство \( (\operatorname{Ker}\,A)_L = L \cap \operatorname{Ker}\,A \) и возьмём его дополнение \( (\operatorname{Ker}\,A)_N \) в пространстве \( \operatorname{Ker}\,A \). Аналогично определим подпространства \( (\operatorname{Ker}\,B)_L \) и \( (\operatorname{Ker}\,B)_N \).

В пространстве \( A^{-1}(K) \) возьмём дополнение \( A^{-1}(K)_N \) к пространству \( L \oplus (\operatorname{Ker}\,A)_N \). Аналогично определим подпространство \( B^{-1}(K)_N \).