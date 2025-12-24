---
source_image: page_062.png
page_number: 62
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.60
tokens: 5337
characters: 1760
timestamp: 2025-12-24T07:18:38.471631
finish_reason: stop
---

аналогичны общепринятым опусканию скобок для умножения в арифметических формулах*.

1. Упрощение формул (т. е. получение эквивалентных формул, содержащих меньше число символов).
а) Поглощение:
\[
x \vee xy = x; \tag{3.17a}
\]
\[
x(x \vee y) = x. \tag{3.17b}
\]
Докажем подробно первое равенство [для его доказательства используются последовательно соотношения (3.13а), (3.9), (3.13в) и (3.13а)]:

\[
x \vee xy = x \& 1 \vee xy = x(1 \vee y) = x \& 1 = x.
\]

Второе равенство доказывается с помощью (3.9), (3.11) и первого равенства:

\[
x(x \vee y) = xx \vee xy = x \vee xy = x.
\]

б) Склеивание:
\[
xy \vee x\overline{y} = x. \tag{3.18}
\]
Доказательство:

\[
xy \vee x\overline{y} = x(y \vee \overline{y}) = x \& 1 = x.
\]

в) Обобщенное склеивание:
\[
xz \vee y\overline{z} \vee xy = xz \vee y\overline{z}. \tag{3.19}
\]
Доказывается с помощью расщепления, т. е. применения (3.18) в обратную сторону и поглощения (3.17):

\[
xz \vee y\overline{z} \vee xy = xz \vee y\overline{z} \vee xyz \vee xy\overline{z} = xz \vee y\overline{z}.
\]

г) \( x \vee \overline{x}y = x \vee y. \) \tag{3.20}

Доказательство:

\[
x \vee \overline{x}y = xy \vee x\overline{y} \vee \overline{x}y = xy \vee x\overline{y} \vee xy \vee \overline{x}y = x \vee y.
\]

д) Обобщением равенств (3.17а) и (3.20) является равенство

\[
x_1 \vee f(x_1, x_2, ..., x_n) = x_1 \vee f(0, x_2, ..., x_n). \tag{3.21}
\]

При доказательстве используется разложение по \( x_1 \), (3.17а) и (3.20):
\[
x_1 \vee f(x_1, x_2, ..., x_n) = x_1 \vee \overline{x}_1 f(0, x_2, ..., x_n) \vee \\
\vee x_1 f(1, x_2, ..., x_n) = x_1 \vee f(0, x_2, ..., x_n).
\]

* Внимательный читатель должен был обратить внимание на то, что эти два соглашения, а также соотношения (3.13) использованы уже в формуле (3.4).