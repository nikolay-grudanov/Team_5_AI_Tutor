---
source_image: page_482.png
page_number: 482
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.04
tokens: 6363
characters: 1845
timestamp: 2025-12-24T08:20:35.109225
finish_reason: stop
---

поэтому из неё нужно вычесть первую строку, умноженную на \( g''/g \), и новую вторую строку, умноженную на \( g'/g \), и т. д.

**Следствие. Если \( f_1 \neq 0 \), то**

\[
W(f_1, \ldots, f_n) = f_1^n W\left( \left( \frac{f_2}{f_1} \right)', \ldots, \left( \frac{f_n}{f_1} \right)' \right).
\]

**Доказательство.** Согласно лемме

\[
W(f_1, \ldots, f_n) = f_1^n W\left( 1, \frac{f_2}{f_1}, \ldots, \frac{f_2}{f_1} \right) =
\]
\[
= f_1^n \begin{vmatrix}
1 & f_2/f_1 & \ldots & f_n/f_1 \\
0 & (f_2/f_1)' & \ldots & (f_n/f_1)'
\end{vmatrix} =
\]
\[
= f_1^n W\left( \left( \frac{f_2}{f_1} \right)', \ldots, \left( \frac{f_n}{f_1} \right)' \right).
\]

**Теорема 53.4.1. Если \( W(f_1, \ldots, f_n) = 0 \) на интервале \((a, b)\), то функции \( f_1, \ldots, f_n \) линейно зависимы на некотором интервале \((c, d) \subset (a, b)\).**

**Доказательство [Kr2].** Применим индукцию по \( n \). При \( n = 1 \) из равенства \( W(f_1) = 0 \) следует, что \( f_1 = 0 \). Пусть \( n > 1 \). Если \( f_1 = 0 \) на \((a, b)\), то линейная зависимость очевидна. Поэтому будем считать, что можно выбрать интервал, на котором \( f_1 \) не обращается в нуль. На этом интервале

\[
W\left( \left( \frac{f_2}{f_1} \right)', \ldots, \left( \frac{f_n}{f_1} \right)' \right) = \frac{1}{f_1^n} W(f_1, \ldots, f_n) = 0.
\]

По предположению индукции можно выбрать интервал, на котором функции \( (f_2/f_1)', \ldots, (f_n/f_1)' \) линейно зависимы, т. е.

\[
\left( \frac{c_2 f_2 + \ldots + c_n f_n}{f_1} \right)' \equiv 0.
\]

Следовательно, \( c_2 f_2 + \ldots + c_n f_n \equiv c f_1 \).

**Задачи**

**53.1.** Пусть \( A = \begin{pmatrix} 0 & -t \\ t & 0 \end{pmatrix} \). Вычислите \( e^A \).

**53.2.** а) Докажите, что если \([A, B] = 0\), то \( e^{A+B} = e^A e^B \).
    б) Докажите, что если \( e^{(A+B)t} = e^{At} e^{Bt} \) при всех \( t \), то \([A, B] = 0\).