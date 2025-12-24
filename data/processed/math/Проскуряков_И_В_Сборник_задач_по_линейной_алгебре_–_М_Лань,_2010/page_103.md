---
source_image: page_103.png
page_number: 103
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.65
tokens: 5693
characters: 2010
timestamp: 2025-12-24T07:07:52.178551
finish_reason: stop
---

*600. Разлагая функцию \( \frac{x}{\ln(1+x)} \) в степенной ряд, получим
\[
\frac{x}{\ln(1+x)} = 1 + h_1 x + h_2 x^2 + h_3 x^3 + \ldots
\]
Показать, что
\[
h_n = \begin{vmatrix}
\frac{1}{2} & 1 & 0 & 0 & \ldots & 0 \\
\frac{1}{3} & \frac{1}{2} & 1 & 0 & \ldots & 0 \\
\frac{1}{4} & \frac{1}{3} & \frac{1}{2} & 1 & \ldots & 0 \\
\cdots & \cdots & \cdots & \cdots & \cdots & \cdots \\
\frac{1}{n+1} & \frac{1}{n} & \frac{1}{n-1} & \frac{1}{n-2} & \ldots & \frac{1}{2}
\end{vmatrix}.
\]

601. Известно, что \( \frac{1}{\cos x} = 1 + \frac{e_1}{2!} x^2 + \frac{e_2}{4!} x^4 + \frac{e_3}{6!} x^6 + \ldots \), где \( e_1, e_2, e_3, \ldots \) — так называемые числа Эйлера. Показать, что
\[
e_n = (2n)! \begin{vmatrix}
\frac{1}{2!} & 1 & 0 & 0 & \ldots & 0 \\
\frac{1}{4!} & \frac{1}{2!} & 1 & 0 & \ldots & 0 \\
\frac{1}{6!} & \frac{1}{4!} & \frac{1}{2!} & 1 & \ldots & 0 \\
\cdots & \cdots & \cdots & \cdots & \cdots & \cdots \\
\frac{1}{2n!} & \frac{1}{(2n-2)!} & \frac{1}{(2n-4)!} & \frac{1}{(2n-6)!} & \ldots & \frac{1}{2!}
\end{vmatrix}.
\]

*602. В разложении \( \frac{x}{e^x - 1} = 1 + b_1 x + b_2 x^2 + b_3 x^3 + \ldots \) коэффициент \( b_{2n} = \frac{(-1)^{n-1} B_n}{(2n)!} \), где \( B_n \) — так называемые числа Бернулли.
Показать, что
\[
B_n = (-1)^{n+1}(2n)! \begin{vmatrix}
\frac{1}{2!} & 1 & 0 & 0 & \ldots & 0 \\
\frac{1}{3!} & \frac{1}{2!} & 1 & 0 & \ldots & 0 \\
\frac{1}{4!} & \frac{1}{3!} & \frac{1}{2!} & 1 & \ldots & 0 \\
\cdots & \cdots & \cdots & \cdots & \cdots & \cdots \\
\frac{1}{(2n+1)!} & \frac{1}{(2n)!} & \frac{1}{(2n-1)!} & \frac{1}{(2n-2)!} & \ldots & \frac{1}{2!}
\end{vmatrix}.
\]
Далее показать, что
\[
b_{2n-1} = \begin{vmatrix}
\frac{1}{2!} & 1 & 0 & 0 & \ldots & 0 \\
\frac{1}{3!} & \frac{1}{2!} & 1 & 0 & \ldots & 0 \\
\frac{1}{4!} & \frac{1}{3!} & \frac{1}{2!} & 1 & \ldots & 0 \\
\cdots & \cdots & \cdots & \cdots & \cdots & \cdots \\
\frac{1}{(2n)!} & \frac{1}{(2n-1)!} & \frac{1}{(2n-2)!} & \frac{1}{(2n-3)!} & \ldots & \frac{1}{2!}
\end{vmatrix} = 0
\]
при \( n > 1 \).