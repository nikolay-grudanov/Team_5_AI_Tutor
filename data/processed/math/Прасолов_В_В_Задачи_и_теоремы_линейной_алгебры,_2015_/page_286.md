---
source_image: page_286.png
page_number: 286
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.38
tokens: 6558
characters: 2431
timestamp: 2025-12-24T08:15:17.132951
finish_reason: stop
---

Доказательство. Если оператор \( P \) эрмитов, то

\[
\operatorname{Ker} P = (\operatorname{Im} P^*)^\perp = (\operatorname{Im} P)^\perp.
\]

Предположим теперь, что \( P \) — проектор и \( \operatorname{Im} P \perp \operatorname{Ker} P \). Векторы \( x - Px \) и \( y - Py \) лежат в \( \operatorname{Ker} P \), поэтому \( (Px, y - Py) = 0 \) и \( (Py, x - Px) = 0 \), т. е. \( (Px, y) = (Px, Py) = (x, Py) \).

Замечание. Если проектор \( P \) эрмитов, то \( (Px, y) = (Px, Py) \); в частности, \( (Px, x) = \|Px\|^2 \).

Теорема 27.2.2. Проектор \( P \) эрмитов тогда и только тогда, когда \( \|Px\| \leq \leq \|x\| \) для всех \( x \).

Доказательство. Если оператор \( P \) эрмитов, то \( x - Px \perp Px \), поэтому \( \|x\|^2 = \|Px\|^2 + \|Px - x\|^2 \geq \|Px\|^2 \).

Докажем теперь, что если \( \|Px\| \leq \|x\| \), то \( \operatorname{Ker} P \perp \operatorname{Im} P \). Предположим, что вектор \( v \in \operatorname{Im} P \) не перпендикулярен \( \operatorname{Ker} P \) и \( v_1 \) — проекция вектора \( v \) на \( \operatorname{Ker} P \). Тогда \( \|v - v_1\| < \|v\| \) и \( v = P(v - v_1) \), поэтому \( \|v - v_1\| < \|P(v - v_1)\| \). Получено противоречие.

Эрмитовы проекторы \( P \) и \( Q \) называют ортогональными, если \( \operatorname{Im} P \perp \perp \operatorname{Im} Q \), т. е. \( PQ = QP = 0 \).

Теорема 27.2.3. Пусть \( P_1, \ldots, P_n \) — эрмитовы проекторы. Оператор \( P = P_1 + \ldots + P_n \) является проектором тогда и только тогда, когда \( P_i P_j = 0 \) при \( i \neq j \).

Доказательство. Если \( P_i P_j = 0 \) при \( i \neq j \), то \( P^2 = (P_1 + \ldots + P_n)^2 = P_1^2 + \ldots + P_n^2 = P_1 + \ldots + P_n = P \).

Предположим теперь, что \( P = P_1 + \ldots + P_n \) — проектор. Этот проектор эрмитов, значит, если \( x \in \operatorname{Im} P_i \), то \( x = P_i x \) и

\[
\|x\|^2 = \|P_i x\|^2 \leq \|P_1 x\|^2 + \ldots + \|P_n x\|^2 = (P_1 x, x) + \ldots + (P_n x, x) =
= (Px, x) = \|Px\|^2 \leq \|x\|^2.
\]

Поэтому \( P_j x = 0 \) при \( i \neq j \), т. е. \( P_j P_i = 0 \).

27.3. Матрица проектора на подпространство

Пусть \( W \subset V; a_1, \ldots, a_k \) — базис \( W \). Рассмотрим матрицу \( A \) размера \( n \times k \), столбцами которой являются координаты векторов \( a_1, \ldots, a_k \) относительно ортонормированного базиса пространства \( V \). Тогда \( \operatorname{rk} A^*A = \operatorname{rk} A = k \), поэтому матрица \( A^*A \) невырождена.