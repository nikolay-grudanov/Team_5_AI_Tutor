---
source_image: page_060.png
page_number: 60
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.71
tokens: 5397
characters: 1470
timestamp: 2025-12-24T07:06:44.417800
finish_reason: stop
---

*386.
\[
\begin{vmatrix}
1 & \binom{2}{2} & 0 & 0 & \ldots & 0 \\
1 & \binom{3}{2} & \binom{3}{3} & 0 & \ldots & 0 \\
1 & \binom{4}{2} & \binom{4}{3} & \binom{4}{4} & \ldots & 0 \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
1 & \binom{n}{2} & \binom{n}{3} & \binom{n}{4} & \ldots & \binom{n}{n} \\
1 & \binom{n+1}{2} & \binom{n+1}{3} & \binom{n+1}{4} & \ldots & \binom{n+1}{n}
\end{vmatrix}
\]

*387.
\[
\begin{vmatrix}
2 & 3 & 4 & \ldots & n \\
3 & 6 & 10 & \ldots & \frac{n(n+1)}{2!} \\
4 & 10 & 20 & \ldots & \frac{n(n+1)(n+2)}{3!} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
n & \frac{n(n+1)}{2!} & \frac{n(n+1)(n+2)}{3!} & \ldots & \frac{n(n+1)\ldots(2n-2)}{(n-1)!}
\end{vmatrix}
\]

*388.
\[
\begin{vmatrix}
1 & 0 & 0 & 0 & \ldots & 0 & 1 \\
1 & \binom{1}{1} & 0 & 0 & \ldots & 0 & x \\
1 & \binom{2}{1} & \binom{2}{2} & 0 & \ldots & 0 & x^2 \\
1 & \binom{3}{1} & \binom{3}{2} & \binom{3}{3} & \ldots & 0 & x^3 \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
1 & \binom{n}{1} & \binom{n}{2} & \binom{n}{3} & \ldots & \binom{n}{n-1} & x^n
\end{vmatrix}
\]

*389.
\[
\begin{vmatrix}
1 & 0 & 0 & 0 & 0 & \ldots & 1 \\
1 & 1! & 0 & 0 & 0 & \ldots & x \\
1 & 2 & 2! & 0 & 0 & \ldots & x^2 \\
1 & 3 & 3\cdot2 & 3! & 0 & \ldots & x^3 \\
1 & 4 & 4\cdot3 & 4\cdot3\cdot2 & 4! & \ldots & x^4 \\
\vdots & \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
1 & n & n(n-1) & n(n-1)(n-2) & n(n-1)(n-2)(n-3) & \ldots & x^n
\end{vmatrix}
\]