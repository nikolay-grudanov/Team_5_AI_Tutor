---
source_image: page_408.png
page_number: 408
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.34
tokens: 6179
characters: 2581
timestamp: 2025-12-24T07:15:21.091838
finish_reason: stop
---

1186. \( y_1^2 + y_2^2 - y_3^2 - y_4^2; \)
\( x_1 = \frac{1}{3} \sqrt{3} y_1 - \frac{1}{15} \sqrt{15} y_2 + \frac{2}{85} \sqrt{85} y_3 - \frac{1}{629} \sqrt{629} y_4, \)
\( x_2 = \frac{1}{5} \sqrt{15} y_2 - \frac{6}{85} \sqrt{85} y_3 + \frac{3}{629} \sqrt{629} y_4, \)
\( x_3 = \frac{1}{17} \sqrt{85} y_3 + \frac{6}{629} \sqrt{629} y_4, \)
\( x_4 = \frac{1}{37} \sqrt{629} y_4. \)

1187. \( 2y_1^2 + 10y_2^2 + 190y_3^2, \)
\( y_1 = x_1 - \frac{1}{2} x_2 + x_3, \)
\( y_2 = \frac{1}{2} x_2 - \frac{1}{10} x_3, \)
\( y_3 = \frac{1}{10} x_3. \)

1188. \( 3y_1^2 - 30y_2^2 + 530y_3^2; \)
\( y_1 = x_1 + \frac{2}{3} x_2 - \frac{1}{2} x_3, \)
\( y_2 = \frac{1}{3} x_2 - \frac{1}{20} x_3, \)
\( y_3 = \frac{1}{20} x_3. \)

1189. \( 2y_1^2 + 6y_2^2 - 6y_3^2 + 2y_4^2; \)
\( y_1 = \frac{1}{2} x_1 - \frac{1}{2} x_2, \)
\( y_2 = \frac{1}{2} x_2 + \frac{1}{6} x_3, \)
\( y_3 = \frac{1}{6} x_3 + \frac{1}{2} x_4, \)
\( y_4 = \frac{3}{2} x_4. \)

1190. \( x_1 = y_1 - 3y_2 - 6y_3; \)
\( x_2 = y_2 + 3y_3; \)
\( x_3 = y_3. \)

1191. \( x_1 = 2\sqrt{2} y_1 + \sqrt{2} y_2 + 5y_3; \)
\( x_2 = \frac{1}{2} \sqrt{2} y_1 + y_3; \)
\( x_3 = y_3. \)

1192. \( x_1 = y_3, \)
\( x_2 = \sqrt{2} y_2 + y_3, \)
\( x_3 = \sqrt{2} y_1 - \frac{3}{2} \sqrt{2} y_2 - (3 + \frac{3}{2} \sqrt{2}) y_3. \)

1193. \( y_1^2; \)
\( y_1 = a_1 x_1 + a_2 x_2 + \cdots + a_n x_n; \)
\( y_2 = x_2; \)
\( y_3 = x_3; \)
\( \ldots; \)
\( y_{i-1} = x_{i-1}; \)
\( y_i = x_i; \)
\( y_{i+1} = x_{i+1}; \)
\( \ldots; \)
\( y_n = x_n, \) если \( a_i \neq 0. \)

1194. \( y_1^2 + \frac{3}{4} y_2^2 + \frac{4}{6} y_3^2 + \frac{5}{8} y_4^2 + \cdots + \frac{n+1}{2n} y_n^2; \)

\[
\begin{align*}
y_1 &= x_1 + \frac{1}{2}(x_2 + x_3 + \cdots + x_n); \\
y_2 &= x_2 + \frac{1}{3}(x_3 + x_4 + \cdots + x_n); \\
&\ldots \\
y_n &= x_n.
\end{align*}
\]

1195. \( y_1^2 - y_2^2 - y_3^2 - \frac{3}{4} y_4^2 - \frac{4}{6} y_5^2 - \frac{5}{8} y_6^2 - \cdots - \frac{n-1}{2(n-2)} y_n^2; \)

\[
\begin{align*}
y_1 &= \frac{1}{2}(x_1 + x_2) + x_3 + x_4 + \cdots + x_n; \\
y_2 &= \frac{1}{2}(x_1 - x_2); \\
y_3 &= x_3 + \frac{1}{2}(x_4 + x_5 + \cdots + x_n); \\
y_4 &= x_4 + \frac{1}{3}(x_5 + x_6 + \cdots + x_n); \\
&\ldots \\
y_n &= x_n.
\end{align*}
\]

Указание. Свести к предыдущей задаче.

1196. Если \( n \) четно: \( y_1^2 - y_2^2 + y_3^2 - y_4^2 + \cdots + y_{n-1}^2 - y_n^2; \)

\[
\begin{align*}
y_i &= \frac{x_i + x_{i+1} + x_{i+2}}{2} \quad (i = 1, 3, 5, \ldots, n-3); \\
y_i &= \frac{x_{i-1} - x_i + x_{i+1}}{2} \quad (i = 2, 4, 6, \ldots, n-2); \\
y_{n-1} &= \frac{x_{n-1} + x_n}{2}, \qquad y_n = \frac{x_{n-1} - x_n}{2}.
\end{align*}
\]