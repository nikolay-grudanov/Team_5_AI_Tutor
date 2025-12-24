---
source_image: page_236.png
page_number: 236
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.75
tokens: 6639
characters: 1932
timestamp: 2025-12-24T07:47:04.087463
finish_reason: stop
---

Аналогичные рассуждения, примененные к равенству (31), дают тождество

\[
\frac{C_{2k-4}^{k-2}}{1 \cdot (k-1)} + \frac{C_2^1 C_{2k-6}^{k-3}}{2 \cdot (k-2)} + \frac{C_4^2 C_{2k-8}^{k-2}}{3 \cdot (k-3)} + \ldots + \frac{C_{2k-4}^{k-2}}{(k-1) \cdot 1} = \frac{C_{2k-2}^{k-1}}{k},
\]

справедливое при \( k \geq 2 \).

Далее, перемножая почленно разложения (31) и (32), получаем

\[
1 = \left[ 1 + \frac{1}{2} x - \frac{1}{2 \cdot 2^3} C_2^1 x^2 + \frac{1}{3 \cdot 2^5} C_4^2 x^3 - \ldots + \frac{(-1)^{k-1}}{k \cdot 2^{2k-1}} C_{2k-2}^{k-1} x^k + \ldots \right] \times
\]
\[
\times \left[ 1 - \frac{1}{2^2} C_2^1 x + \frac{1}{2^4} C_4^2 x^2 - \frac{1}{2^6} C_6^3 x^3 + \ldots + \frac{(-1)^k}{2^{2k}} C_{2k}^k x^k + \ldots \right].
\]

Раскроем скобки в правой части этого равенства. Мы получим степенной ряд, причем из равенства 1 левой части следует, что все коэффициенты этого ряда (кроме свободного члена) равны нулю. Отсюда получаем тождество

\[
C_{2k-2}^{k-1} + \frac{1}{2} C_2^1 C_{2k-4}^{k-2} + \frac{1}{3} C_4^2 C_{2k-6}^{k-3} + \ldots + \frac{1}{k} C_{2k-2}^{k-1} = \frac{1}{2} C_{2k}^k,
\]

справедливое при \( k \geq 1 \).

Наконец, заметим, что

\[
(1 + x)^{\frac{1}{2}} (1 + x)^{-1} = (1 + x)^{-\frac{1}{2}}.
\]

Отсюда вытекает, что

\[
\left[ 1 + \frac{1}{2} x - \frac{1}{2 \cdot 2^3} C_2^1 x^2 + \frac{1}{3 \cdot 2^5} C_4^2 x^3 - \ldots + \frac{(-1)^{k-1}}{k \cdot 2^{2k-1}} C_{2k-2}^{k-1} x^k + \ldots \right] \times
\]
\[
\times \left[ 1 - x + x^2 - x^3 + \ldots + (-1)^k x^k + \ldots \right] =
\]
\[
= 1 - \frac{1}{2^2} C_2^1 x + \frac{1}{2^4} C_4^2 x^2 - \frac{1}{2^6} C_6^3 x^3 + \ldots + \frac{(-1)^k}{2^{2k}} C_{2k}^k x^k + \ldots
\]

Раскрывая скобки в обеих частях этого равенства и сравнивая коэффициенты при \( x^k \) в обеих частях, приходим к тождеству

\[
1 - \frac{1}{2 \cdot 2^2} C_2^1 - \frac{1}{3 \cdot 2^4} C_4^2 - \ldots - \frac{1}{k \cdot 2^{2k-2}} C_{2k-2}^{k-1} = \frac{1}{2^{2k-1}} C_{2k}^k.
\]