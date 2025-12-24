---
source_image: page_104.png
page_number: 104
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.97
tokens: 5683
characters: 2109
timestamp: 2025-12-24T07:07:50.631181
finish_reason: stop
---

* 603. Показать, что число Бернулли \( B_n \), введенное в предыдущей задаче, может быть выражено следующими определителями \( n \)-го порядка:

\[
B_n = \frac{1}{2}(2n)! \left| \begin{array}{cccccc}
\frac{1}{3!} & 1 & 0 & 0 & \cdots & 0 \\
\frac{3}{5!} & \frac{1}{3!} & 1 & 0 & \cdots & 0 \\
\frac{5}{7!} & \frac{1}{5!} & \frac{1}{3!} & 1 & \cdots & 0 \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
\frac{2n-1}{(2n+1)!} & \frac{1}{(2n-1)!} & \frac{1}{(2n-3)!} & \frac{1}{(2n-5)!} & \cdots & \frac{1}{3!}
\end{array} \right|
\]

или

\[
B_n = 2^n (2n)! \left| \begin{array}{cccccc}
\frac{1}{4!} & \frac{1}{2!} & 0 & 0 & \cdots & 0 \\
\frac{2}{6!} & \frac{1}{4!} & \frac{1}{2!} & 0 & \cdots & 0 \\
\frac{3}{8!} & \frac{1}{6!} & \frac{1}{4!} & \frac{1}{2!} & \cdots & 0 \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
\frac{n}{(2n+2)!} & \frac{1}{(2n)!} & \frac{1}{(2n-2)!} & \frac{1}{(2n-4)!} & \cdots & \frac{1}{4!}
\end{array} \right|
\]

* 604. Обозначим через \( s_n(k) \) сумму \( n \)-х степеней чисел натурального ряда от 1 до \( k - 1 \), т. е. \( s_n(k) = 1^n + 2^n + \ldots + (k - 1)^n \). Установив равенство

\[
k^n = 1 + C_n^{n-1} s_{n-1}(k) + C_n^{n-2} s_{n-2}(k) + \cdots + C_n^1 s_1(k) + s_0(k),
\]

показать, что

\[
s_{n-1}(k) = \frac{1}{n!} \left| \begin{array}{cccccc}
k^n & C_n^{n-2} & C_n^{n-3} & \cdots & C_n^1 & 1 \\
k^{n-1} & C_{n-1}^{n-2} & C_{n-1}^{n-3} & \cdots & C_{n-1}^1 & 1 \\
k^{n-2} & 0 & C_{n-2}^{n-3} & \cdots & C_{n-2}^1 & 1 \\
\vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
k^2 & 0 & 0 & \cdots & C_2^1 & 1 \\
k & 0 & 0 & \cdots & 0 & 0
\end{array} \right|.
\]

* 605. Представить в виде определителя \( n \)-й коэффициент \( l_n \) разложения \( \frac{\tg x}{x} = 1 + l_1 x^2 + l_2 x^4 + \cdots + l_n x^{2n} + \ldots \).

606. Представить в виде определителя \( n \)-й коэффициент \( f_n \) разложения \( x \ctg x = 1 - f_1 x^2 - f_2 x^4 - \cdots - f_n x^{2n} - \ldots \).

* 607. Выразив \( n \)-й коэффициент \( a_n \) разложения \( e^{-x} = 1 - a_1 x + a_2 x^2 - a_3 x^3 + \ldots \) в виде определителя, найти отсюда значение определителя.