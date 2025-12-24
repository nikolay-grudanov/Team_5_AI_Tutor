---
source_image: page_073.png
page_number: 73
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.69
tokens: 6360
characters: 1692
timestamp: 2025-12-24T08:09:28.433261
finish_reason: stop
---

Эта формула показывает, что \( S_{2k+1}(n) \) выражается через \( n(n-1) = 2U(n) \) и делится на \([n(n-1)]^2\).

Чтобы получить выражение для \( S_{2k} \), воспользуемся равенством

\[
n^{r+1}(n-1)^r = \prod_{x=1}^{n-1} (x^r(x+1)^{r+1} - (x-1)^r x^{r+1}) =
\]
\[
= \cdot x^{2r} \left[ \binom{r+1}{1} + \binom{r}{1} \right] + \cdot x^{2r-1} \left[ \binom{r+1}{2} - \binom{r}{2} \right] +
\]
\[
+ \cdot x^{2r-2} \left[ \binom{r+1}{3} + \binom{r}{3} \right] + \cdot x^{2r-3} \left[ \binom{r+1}{4} - \binom{r}{4} \right] + \ldots =
\]
\[
= \left[ \binom{r+1}{1} + \binom{r}{1} \right] \cdot x^{2r} + \left[ \binom{r+1}{3} + \binom{r}{3} \right] \cdot x^{2r-2} + \ldots
\]
\[
\ldots + \binom{r}{1} \cdot x^{2r-1} + \binom{r}{3} \cdot x^{2r-3} + \ldots
\]

Суммы нечётных степеней можно уничтожить с помощью (1). В результате получим

\[
n^{r+1}(n-1)^r = \frac{n^r(n-1)^r}{2} + \left[ \binom{r+1}{1} + \binom{r}{1} \right] \cdot x^{2r} +
\]
\[
+ \left[ \binom{r+1}{3} + \binom{r}{3} \right] \cdot x^{2r-2} + \ldots,
\]

т. е.

\[
n^i(n-1)^i \left( \frac{2n-1}{2} \right) = \prod_j \left[ \binom{i+1}{2(i-j)+1} + \binom{i}{2(i-j)+1} \right] S_{2j}(n).
\]

Теперь аналогично предыдущему случаю получаем

\[
\begin{pmatrix}
S_2(n) \\
S_4(n) \\
S_6(n) \\
\vdots
\end{pmatrix}
= \frac{2n-1}{2} \| b_{ij} \|^{-1}
\begin{pmatrix}
n(n-1) \\
n^2(n-1)^2 \\
n^3(n-1)^3 \\
\vdots
\end{pmatrix},
\]

где \( b_{ij} = \binom{i+1}{2(i-j)+1} + \binom{i}{2(i-j)+1} \).

Простые вычисления показывают, что \( S_2(n) = \frac{2n-1}{2} \cdot \frac{n(n-1)}{3} \). Поэтому многочлены \( S_4(n), S_6(n), \ldots \) делятся на \( S_2(n) \), причем \( \frac{S_{2k}(n)}{S_2(n)} \) является многочленом от \( n(n-1) = 2U(n) \).