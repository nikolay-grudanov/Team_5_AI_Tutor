---
source_image: page_030.png
page_number: 30
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.89
tokens: 5635
characters: 2153
timestamp: 2025-12-24T07:06:14.805021
finish_reason: stop
---

*246.
\[
\begin{vmatrix}
1 & a_1 & a_1^2 & \ldots & a_1^{i-1} & a_1^{i+1} & \ldots & a_1^n \\
1 & a_2 & a_2^2 & \ldots & a_2^{i-1} & a_2^{i+1} & \ldots & a_2^n \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
1 & a_n & a_n^2 & \ldots & a_n^{i-1} & a_n^{i+1} & \ldots & a_n^n
\end{vmatrix}
=
\]
\[
= \left( \sum_{k_1, k_2, \ldots, k_{n-i}} a_{k_1} a_{k_2} \ldots a_{k_{n-i}} \right)
\begin{vmatrix}
1 & a_1 & a_1^2 & \ldots & a_1^{n-1} \\
1 & a_2 & a_2^2 & \ldots & a_2^{n-1} \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
1 & a_n & a_n^2 & \ldots & a_n^{n-1}
\end{vmatrix},
\]
где сумма берется по всем сочетаниям из \( n \) чисел \( 1, 2, 3, \ldots, n \) по \( n - i \).

Пользуясь свойствами определителей, включая разложение по строке или столбцу, доказать тождества:

*247.
\[
\begin{vmatrix}
\cos \frac{\alpha-\beta}{2} & \sin \frac{\alpha+\beta}{2} & \cos \frac{\alpha+\beta}{2} \\
\cos \frac{\beta-\gamma}{2} & \sin \frac{\beta+\gamma}{2} & \cos \frac{\beta+\gamma}{2} \\
\cos \frac{\gamma-\alpha}{2} & \sin \frac{\gamma+\alpha}{2} & \cos \frac{\gamma+\alpha}{2}
\end{vmatrix}
=
\frac{1}{2} [\sin(\beta-\alpha) + \sin(\gamma-\beta) + \sin(\alpha-\gamma)].
\]

248.
\[
\begin{vmatrix}
\sin^2 \alpha & \sin \alpha \cos \alpha & \cos^2 \alpha \\
\sin^2 \beta & \sin \beta \cos \beta & \cos^2 \beta \\
\sin^2 \gamma & \sin \gamma \cos \gamma & \cos^2 \gamma
\end{vmatrix}
=
\sin(\alpha-\beta) \cos \alpha \cos \beta + \sin(\beta-\gamma) \cos \beta \cos \gamma +
\sin(\gamma-\alpha) \cos \gamma \cos \alpha.
\]

249.
\[
\begin{vmatrix}
(a+b)^2 & c^2 & c^2 \\
a^2 & (b+c)^2 & a^2 \\
b^2 & b^2 & (c+a)^2
\end{vmatrix}
= 2abc(a+b+c)^3.
\]

250.
\[
\begin{vmatrix}
\frac{1}{a+x} & \frac{1}{a+y} & 1 \\
\frac{1}{b+x} & \frac{1}{b+y} & 1 \\
\frac{1}{c+x} & \frac{1}{c+y} & 1
\end{vmatrix}
= \frac{(a-b)(a-c)(b-c)(x-y)}{(a+x)(b+x)(c+x)(a+y)(b+y)(c+y)}.
\]

251.
\[
\begin{vmatrix}
\frac{1}{a+x} & \frac{1}{a+y} & \frac{1}{a+z} \\
\frac{1}{b+x} & \frac{1}{b+y} & \frac{1}{b+z} \\
\frac{1}{c+x} & \frac{1}{c+y} & \frac{1}{c+z}
\end{vmatrix}
=
\frac{(a-b)(a-c)(b-c)(x-y)(x-z)(y-z)}{(a+x)(b+x)(c+x)(a+y)(b+y)(c+y)(a+z)(b+z)(c+z)}.
\]