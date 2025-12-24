---
source_image: page_234.png
page_number: 234
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.44
tokens: 6350
characters: 1584
timestamp: 2025-12-24T07:46:48.707993
finish_reason: stop
---

113. Извлечение квадратных корней

\( C_{-n}^k = (-1)^k C_{n+k-1}^k \). Если же значения \( k \) отрицательны, то надо положить \( C_n^k = 0 \), поскольку в разложения (29) и (30) не входят слагаемые с отрицательными степенями \( t \). По тем же соображениям \( C_n^k = 0 \) при \( 0 \leq n < k \).

113. Извлечение квадратных корней

Теперь мы знаем, как выглядит бином Ньютона не только для целых, но и для дробных (и даже для иррациональных) значений показателя. Посмотрим, что получится при \( n = \frac{1}{2} \) и \( n = -\frac{1}{2} \).

При \( n = \frac{1}{2} \) формула Ньютона принимает вид

\[
(1 + x)^{\frac{1}{2}} = 1 + \frac{1}{2}x + \frac{1}{2}\left(\frac{1}{2} - 1\right)x^2 + \frac{1}{2}\left(\frac{1}{2} - 1\right)\left(\frac{1}{2} - 2\right)x^3 + \ldots + \frac{1}{2}\left(\frac{1}{2} - 1\right) \ldots \left(\frac{1}{2} - k + 1\right)x^k + \ldots
\]

Преобразуя это выражение, получаем

\[
(1 + x)^{\frac{1}{2}} = 1 + \frac{1}{2}x - \frac{1}{2 \cdot 4}x^2 + \frac{1 \cdot 3}{2 \cdot 4 \cdot 6}x^3 - \ldots + (-1)^{k-1} \frac{1 \cdot 3 \ldots (2k-3)}{2 \cdot 4 \ldots 2k}x^k + \ldots
\]

Точно так же при \( n = -\frac{1}{2} \) выводим, что

\[
(1 + x)^{-\frac{1}{2}} = 1 - \frac{1}{2}x + \frac{1 \cdot 3}{2 \cdot 4}x^2 - \frac{1 \cdot 3 \cdot 5}{2 \cdot 4 \cdot 6}x^3 + \ldots + (-1)^k \frac{1 \cdot 3 \ldots (2k-1)}{2 \cdot 4 \ldots 2k}x^k + \ldots
\]

Полученные формулы можно записать иначе. Для этого заметим, что

\[
\frac{1 \cdot 3 \ldots (2k-3)}{2 \cdot 4 \ldots 2k} = \frac{(2k-2)!}{k \cdot 2^{2k-1}((k-1)!)^2} = \frac{1}{k \cdot 2^{2k-1}} C_{2k-2}^{k-1}
\]