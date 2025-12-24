---
source_image: page_438.png
page_number: 438
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.03
tokens: 6301
characters: 1650
timestamp: 2025-12-24T08:19:21.671669
finish_reason: stop
---

ментов, лежащих на одной прямой или одной окружности, является третий элемент, лежащий на той же прямой или окружности. Выбор знака определяется ориентацией; например, \( ie = f, if = -e \).

Пусть \( \xi = a + be \), где \( a \) и \( b \) — кватернионы. Сопряжение в алгебре Кэли задаётся формулой \( (a, b) = (\bar{a}, -b) \), т. е. \( a + be = \bar{a} - be \). Ясно, что \( \xi \overline{\xi} = (a, b)(a, b) = (a, b)(\bar{a}, -b) = (\bar{a}a + \bar{b}b, ba - ba) = \bar{a}a + \bar{b}b = a\bar{a} + b\bar{b} \), т. е. \( \xi \overline{\xi} \) — сумма квадратов координат вектора \( \xi \). Поэтому \( |\xi| = \sqrt{\xi \overline{\xi}} = \sqrt{\overline{\xi} \xi} \) — длина вектора \( \xi \).

**Теорема 46.6.1.** \( |\xi \eta| = |\xi| \cdot |\eta| \).

**Доказательство.** Пусть \( \xi = a + be \) и \( \eta = u + ve \), где \( a, b, u, v \) — кватернионы. Так как

\[
(be)u = (0, b)(u, 0) = (0, b\bar{u}) = (b\bar{u})e
\]

и

\[
(be)(ve) = (0, b)(0, v) = (-\bar{v}b, 0) = -\bar{v}b,
\]

то

\[
|\xi \eta|^2 = (au - \bar{v}b)(\bar{u}\bar{a} - \bar{b}v) + (b\bar{u} + va)(u\bar{b} + \bar{a}v).
\]

Запишем кватернион \( v \) в виде \( v = \lambda + v_1 \), где \( \lambda \) — действительное число и \( \bar{v}_1 = -v_1 \). Тогда

\[
|\xi \eta|^2 = (au - \lambda b + v_1 b)(\bar{u}\bar{a} - \lambda \bar{b} - \bar{b}v_1) + (b\bar{u} + \lambda a + v_1 a)(u\bar{b} + \lambda \bar{a} - \bar{a}v_1).
\]

Кроме того, \( |\xi|^2 |\eta|^2 = (a\bar{a} + b\bar{b})(u\bar{u} + \lambda^2 - v_1 v_1) \). Так как числа \( u\bar{u} \) и \( b\bar{b} \) действительные, то \( au\bar{u}a = a\bar{a}u\bar{u} \) и \( b\bar{b}v_1 = v_1 b\bar{b} \). Используя аналогич-