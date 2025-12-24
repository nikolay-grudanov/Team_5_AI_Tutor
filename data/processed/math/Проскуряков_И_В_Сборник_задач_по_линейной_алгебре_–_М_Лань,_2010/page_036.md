---
source_image: page_036.png
page_number: 36
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.63
tokens: 5310
characters: 1626
timestamp: 2025-12-24T07:06:14.869800
finish_reason: stop
---

Из первого столбца выносим \(a_1 - x\), из второго \(a_2 - x\), ..., из \(n\)-го \(a_n - x\):

\[
D = (a_1 - x)(a_2 - x) \ldots (a_n - x)
\]

\[
\left| \begin{array}{cccccc}
\frac{a_1}{a_1 - x} & \frac{x}{a_2 - x} & \frac{x}{a_3 - x} & \cdots & \frac{x}{a_n - x} \\
-1 & 1 & 0 & \cdots & 0 \\
-1 & 0 & 1 & \cdots & 0 \\
\cdots & \cdots & \cdots & \cdots & \cdots \\
-1 & 0 & 0 & \cdots & 1
\end{array} \right|.
\]

Положим \(\frac{a}{a_1 - x} = 1 + \frac{x}{a_1 - x}\) и все столбцы прибавим к первому:

\[
D = (a_1 - x)(a_2 - x) \ldots (a_n - x) \times
\]

\[
\times \left| \begin{array}{cccccc}
1 + \frac{x}{a_1 - x} + \cdots + \frac{x}{a_n - x} & \frac{x}{a_2 - x} & \frac{x}{a_3 - x} & \cdots & \frac{x}{a_n - x} \\
0 & 1 & 0 & \cdots & 0 \\
0 & 0 & 1 & \cdots & 0 \\
\cdots & \cdots & \cdots & \cdots & \cdots \\
0 & 0 & 0 & \cdots & 1
\end{array} \right| =
\]

\[
= x(a_1 - x)(a_2 - x) \ldots (a_n 0x) \left( \frac{1}{x} + \frac{1}{a_1 - x} + \frac{1}{a_2 - x} + \cdots + \frac{1}{a_n - x} \right).
\]

5.2. Метод выделения линейных множителей

Определитель рассматривается как многочлен от одной или нескольких входящих в него букв. Преобразуя его, обнаруживают, что он делится на ряд линейных множителей, а значит (если эти множители взаимно просты), и на их произведение.

Сравнивая отдельные члены определителя с членами произведения линейных множителей, находят частное от деления определителя на это произведение и тем самым находят выражение определителя.

Пример 3: Вычислить определитель

\[
D = \left| \begin{array}{cccc}
0 & x & y & z \\
x & 0 & z & y \\
y & z & 0 & x \\
z & y & x & 0
\end{array} \right|.
\]