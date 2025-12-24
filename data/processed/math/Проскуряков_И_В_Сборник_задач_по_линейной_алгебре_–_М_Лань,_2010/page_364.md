---
source_image: page_364.png
page_number: 364
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.56
tokens: 5611
characters: 1912
timestamp: 2025-12-24T07:13:55.230480
finish_reason: stop
---

604. Указание. Для установления требуемого равенства в тождестве

\[
(x + 1)^n = x^n + C_n^{n-1} x^{n-1} + C_n^{n-2} x^{n-2} + \cdots + C_n^1 x + x^0
\]

положить \( x = 1, 2, 3, \ldots, k - 1 \) и полученные равенства сложить. В установленном равенстве заменить \( n \) на \( n - 1, n - 2, \ldots, 2, 1 \) и из полученной системы \( n \) линейных уравнений относительно \( s_0(k), s_1(k), \ldots, s_{n-1}(k) \) найти \( s_{n-1}(k) \).

605.

\[
l_n = \begin{vmatrix}
\frac{2}{3!} & 1 & 0 & \cdots & 0 \\
\frac{4}{5!} & \frac{1}{2!} & 1 & \cdots & 0 \\
\frac{6}{7!} & \frac{1}{4!} & \frac{1}{2!} & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
\frac{2n}{(2n+1)!} & \frac{1}{(2n-2)!} & \frac{1}{(2n-4)!} & \cdots & \frac{1}{2!}
\end{vmatrix}.
\]

Указание. Получить тождество

\[
x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots = x \left( 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots \right) (1 + l_1 x^2 + l_2 x^4 + \ldots).
\]

606.

\[
f_n = \begin{vmatrix}
\frac{2}{3!} & 1 & 0 & \cdots & 0 \\
\frac{4}{5!} & \frac{1}{3!} & 1 & \cdots & 0 \\
\frac{6}{7!} & \frac{1}{5!} & \frac{1}{3!} & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
\frac{2n}{(2n+1)!} & \frac{1}{(2n-1)!} & \frac{1}{(2n-3)!} & \cdots & \frac{1}{3!}
\end{vmatrix}.
\]

607.

\[
a_n = \frac{1}{n!} = \begin{vmatrix}
\frac{1}{1!} & 1 & 0 & 0 & \cdots & 0 \\
\frac{1}{2!} & \frac{1}{1!} & 1 & 0 & \cdots & 0 \\
\frac{1}{3!} & \frac{1}{2!} & \frac{1}{1!} & 1 & \cdots & 0 \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
\frac{1}{n!} & \frac{1}{(n-1)!} & \frac{1}{(n-2)!} & \frac{1}{(n-3)!} & \cdots & \frac{1}{1!}
\end{vmatrix}.
\]

Указание. Получить тождество

\[
1 = (1 - a_1 x + a_2 x^2 - a_3 x^3 + \cdots) \left( 1 + \frac{x}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} \right),
\]

получить уравнения для определения \( a_1, a_2, \ldots, a_n \).

608. 2. 609. 3. 610. 3. 611. 2.