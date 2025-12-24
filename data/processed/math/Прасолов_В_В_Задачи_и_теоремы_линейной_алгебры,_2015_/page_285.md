---
source_image: page_285.png
page_number: 285
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.16
tokens: 6465
characters: 2401
timestamp: 2025-12-24T08:15:13.183050
finish_reason: stop
---

§ 27. Проекторы

Оператор \( P : V \to V \) называют проектором (или идемпотентом), если \( P^2 = P \).

27.1. Канонический вид матрицы проектора

Теорема 27.1.1. Матрица проектора \( P \) в некотором базисе имеет вид \( \operatorname{diag}(1, \ldots, 1, 0, \ldots, 0) \).

Доказательство. Любой вектор \( v \in V \) можно представить в виде \( v = Pv + (v - Pv) \), где \( Pv \in \operatorname{Im} P \) и \( v - Pv \in \operatorname{Ker} P \). Кроме того, если \( x \in \operatorname{Im} P \cap \operatorname{Ker} P \), то \( x = 0 \). В самом деле, тогда \( x = Py \) и \( Px = 0 \), поэтому \( 0 = Px = P^2 y = Py = x \). Следовательно, \( V = \operatorname{Im} P \oplus \operatorname{Ker} P \). Выберем в качестве базиса \( V \) объединение базисов \( \operatorname{Im} P \) и \( \operatorname{Ker} P \). В этом базисе матрица оператора \( P \) имеет требуемый вид.

Следствие 1. Существует взаимно однозначное соответствие между проекторами и разложениями \( V = W_1 \oplus W_2 \). Каждому такому разложению соответствует проектор \( P(w_1 + w_2) = w_1 \) для \( w_1 \in W_1 \) и \( w_2 \in W_2 \), а каждому проектору соответствует разложение \( V = \operatorname{Im} P \oplus \operatorname{Ker} P \).

Оператор \( P \) можно назвать проекцией на \( W_1 \) параллельно \( W_2 \).

Следствие 2. Если \( P \) — проектор, то \( \operatorname{rk} P = \operatorname{tr} P \).

Теорема 27.1.2. Если \( P \) — проектор, то \( I - P \) — тоже проектор, причём \( \operatorname{Ker}(I - P) = \operatorname{Im} P \) и \( \operatorname{Im}(I - P) = \operatorname{Ker} P \).

Доказательство. Если \( P^2 = P \), то \( (I - P)^2 = I - 2P + P^2 = I - P \). Согласно доказательству теоремы 27.1.1 \( \operatorname{Ker} P \) состоит из векторов \( v - Pv \), т. е. \( \operatorname{Ker} P = \operatorname{Im}(I - P) \). Аналогично \( \operatorname{Ker}(I - P) = \operatorname{Im} P \).

Следствие. Если \( P \) — проекция на \( W_1 \) параллельно \( W_2 \), то \( I - P \) — проекция на \( W_2 \) параллельно \( W_1 \).

27.2. Эрмитовы проекторы

Пусть \( P \) — проектор и \( V = \operatorname{Im} P \oplus \operatorname{Ker} P \). Если \( \operatorname{Im} P \perp \operatorname{Ker} P \), то \( Pv \) — ортогональная проекция вектора \( v \) на \( \operatorname{Im} P \) (см. п. 9.3).

Теорема 27.2.1. Проектор \( P \) эрмитов тогда и только тогда, когда
\[
\operatorname{Im} P \perp \operatorname{Ker} P.
\]