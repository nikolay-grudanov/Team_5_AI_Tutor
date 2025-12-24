---
source_image: page_185.png
page_number: 185
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.59
tokens: 6220
characters: 1484
timestamp: 2025-12-24T08:12:22.052566
finish_reason: stop
---

12.5. Неравенства для норм

Теорема 12.5.1 [Du]. Пусть \( u \) и \( v \) — ненулевые векторы нормированного пространства. Тогда

\[
\|u - v\| \geq \frac{1}{4}(\|u\| + \|v\|)\left\|\frac{u}{\|u\|} - \frac{v}{\|v\|}\right\|,
\]

причём константу \( 1/4 \) нельзя увеличить.

Доказательство. Ясно, что

\[
\|u\|\left\|\frac{u}{\|u\|} - \frac{v}{\|v\|}\right\| \leq \|u\|\left\|\frac{u}{\|u\|} - \frac{v}{\|u\|}\right\| + \|u\|\left\|\frac{v}{\|u\|} - \frac{v}{\|v\|}\right\| \leq
\]
\[
\leq \|u - v\| + \frac{\|(\|v\| - \|u\|)v\|}{\|v\|} \leq \|u - v\| + \left|\|v\| - \|u\|\right| \leq 2\|u - v\|.
\]

Аналогично

\[
\|v\|\left\|\frac{u}{\|u\|} - \frac{v}{\|v\|}\right\| \leq 2\|u - v\|.
\]

Сложив эти два неравенства, получаем требуемое.

Предположим теперь, что неравенство

\[
\|u - v\| \geq C(\|u\| + \|v\|)\left\|\frac{u}{\|u\|} - \frac{v}{\|v\|}\right\|
\]

имеет место для любых ненулевых векторов в любом нормированном пространстве. Рассмотрим пространство \( \mathbb{R}^2 \) с нормой

\[
\|(x, y)\| = |x| + |y|.
\]

Выберем в нём векторы \( u = (1, \varepsilon) \) и \( v = (1, 0) \), где \( \varepsilon > 0 \). Для этих векторов неравенство (1) принимает вид

\[
\varepsilon > C(2 + \varepsilon) \frac{2\varepsilon}{1 + \varepsilon},
\]

т. е. \( C \leq \frac{1 + \varepsilon}{4 + 2\varepsilon} \). Следовательно, \( C \leq 1/4 \).

Теорема 12.5.2 [Du]. В нормированном пространстве со скалярным произведением константу \( 1/4 \) в теореме 12.5.1 можно заменить на \( 1/2 \).