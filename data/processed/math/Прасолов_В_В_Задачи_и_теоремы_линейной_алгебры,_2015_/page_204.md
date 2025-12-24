---
source_image: page_204.png
page_number: 204
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 8.95
tokens: 5825
characters: 771
timestamp: 2025-12-24T08:12:40.171635
finish_reason: stop
---

Мы доказали, что такое неравенство имеет место для всех целых неотрицательных \( t \). При \( t \to \infty \) получаем \( d(x + y, 0) \leq 0 \), т. е. \( x + y = 0 \), что и требовалось.

Пусть теперь \( a \) — произвольное число между 0 и 1. При необходимости меняя местами \( x \) и \( y \), можно добиться, чтобы число \( a \) удовлетворяло неравенствам \( 0 < a < 1/2 \). Тогда если \( d(w, 0) \leq ad(w, x) + (1 - a)d(w, y) \), то

\[
d(w, 0) \leq d(aw, ax) + d(w - aw, y - ay) \leq \\
\leq d(aw, ax) + d(w - aw, aw) + d(aw, y - ay) = \\
\leq d(aw, ax) + (1 - 2a)d(w, 0) + d(aw, y - ay),
\]

т. е. \( 2d(aw, 0) \leq d(aw, ax) + d(aw, y - ay) \). Это неравенство имеет место для всех \( w \). Поэтому, как было доказано выше, \( ax + y - ay = 0 \), что и требовалось.