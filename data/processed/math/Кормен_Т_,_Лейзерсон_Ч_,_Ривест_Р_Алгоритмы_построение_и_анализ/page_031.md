---
source_image: page_031.png
page_number: 31
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 57.91
tokens: 11575
characters: 1982
timestamp: 2025-12-24T06:21:30.198931
finish_reason: stop
---

Стандартные функции и обозначения

монотонно убывает (is monotonically decreasing), если \( f(m) \geq f(n) \) при \( m \leq n \). Говорят, что функция \( f(n) \) строго возрастает (is strictly increasing), если \( f(m) < f(n) \) при \( m < n \). Говорят, что функция \( f(n) \) строго убывает (is strictly decreasing), если \( f(m) > f(n) \) при \( m < n \).

Целые приближения снизу и сверху

Для любого вещественного числа \( x \) через \( \lfloor x \rfloor \) (the floor of \( x \)) мы обозначаем его целую часть, т.е. наибольшее целое число, не превосходящее \( x \). Симметричным образом \( \lceil x \rceil \) (the ceiling of \( x \)) обозначает наименьшее целое число, не меньшее \( x \). Очевидно,

\[
x - 1 < \lfloor x \rfloor \leq x \leq \lceil x \rceil < x + 1
\]

для любого \( x \). Кроме того,

\[
\lceil n/2 \rceil + \lfloor n/2 \rfloor = n
\]

для любого целого \( n \). Наконец, для любого \( x \) и для любых целых положительных \( a \) и \( b \) имеем

\[
\lceil \lceil x/a \rceil / b \rceil = \lceil x/ab \rceil \tag{2.3}
\]

и

\[
\lfloor \lfloor x/a \rfloor / b \rfloor = \lfloor x/ab \rfloor \tag{2.4}
\]

(чтобы убедиться в этом, полезно заметить, что для любого \( z \) и для целого \( n \) свойства \( n \leq z \) и \( n \leq \lfloor z \rfloor \) равносильны).

Функции \( x \mapsto \lfloor x \rfloor \) и \( x \mapsto \lceil x \rceil \) монотонно возрастают.

Многочлены

Многочленом (полиномом) степени \( d \) от переменной \( n \) (polynomial in \( n \) of degree \( d \)) называют функцию

\[
p(n) = \sum_{i=0}^d a_i n^i
\]

(\( d \) — неотрицательное целое число). Числа \( a_0, a_1, \ldots, a_d \) называют коэффициентами (coefficients) многочлена. Мы считаем, что старший коэффициент \( a_d \) не равен нулю (если это не так, уменьшим \( d \) — это можно сделать, если только многочлен не равен нулю тождественно).

Для больших значений \( n \) знак многочлена \( p(n) \) определяется старшим коэффициентом (остальные члены малы по сравнению с ним),