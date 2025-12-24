---
source_image: page_393.png
page_number: 393
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.44
tokens: 6811
characters: 2593
timestamp: 2025-12-24T07:51:31.353996
finish_reason: stop
---

По формуле бинома Ньютона имеем

\[
\frac{(-1)^n}{2^n} \left[ 1 + C_n^1 (-i \sqrt{3}) + C_n^2 (-i \sqrt{3})^2 + C_n^3 (-i \sqrt{3})^3 + \ldots \right] =
\]
\[
= \frac{(-1)^n}{2^n} \left[ 1 - 3C_n^2 + 9C_n^4 - \ldots - i \sqrt{3} \left( C_n^1 - 3C_n^3 + 9C_n^5 - \ldots \right) \right].
\]

Приравнивая действительные и мнимые части в обеих частях последнего равенства, получаем доказываемые соотношения.

30. Рассмотрим тождество
\[
(1 + x)^n = C_n^0 + C_n^1 x + C_n^2 x^2 + C_n^3 x^3 + \ldots + C_n^n x^n
\]
и положим в нем последовательно \( x = 1,\ x = \varepsilon,\ x = \varepsilon^2 \), где \( \varepsilon = \cos \frac{2\pi}{3} + i \sin \frac{2\pi}{3} \), и потому \( 1 + \varepsilon + \varepsilon^2 = 0 \). Получаем
\[
2^n = C_n^0 + C_n^1 + C_n^2 + C_n^3 + \ldots + C_n^n,
\]
\[
(1 + \varepsilon)^n = C_n^0 + C_n^1 \varepsilon + C_n^2 \varepsilon^2 + C_n^3 \varepsilon^3 + \ldots + C_n^n \varepsilon^n,
\]
\[
(1 + \varepsilon^2)^n = C_n^0 + C_n^1 \varepsilon^2 + C_n^2 \varepsilon^4 + C_n^3 \varepsilon^6 + \ldots + C_n^n \varepsilon^{2n}.
\]
Но \( 1 + \varepsilon^k + \varepsilon^{2k} = 0 \), если \( k \) не делится на 3, и \( 1 + \varepsilon^k + \varepsilon^{2k} = 3 \), если \( k \) делится на 3. Следовательно,
\[
2^n + (1 + \varepsilon)^n + (1 + \varepsilon^2)^n = 3(C_n^0 + C_n^3 + C_n^6 + \ldots ).
\]
Так как
\[
1 + \varepsilon = -\varepsilon^2 = -\left( \cos \frac{4\pi}{3} + i \sin \frac{4\pi}{3} \right) = \cos \frac{\pi}{3} + i \sin \frac{\pi}{3},
\]
\[
1 + \varepsilon^2 = -\varepsilon = \cos \frac{\pi}{3} - i \sin \frac{\pi}{3},
\]
то \( 2^n + (1 + \varepsilon)^n + (1 + \varepsilon^2)^n = 2^n + 2 \cos \frac{n\pi}{3} \). Отсюда и следует первое равенство. Два другие равенства получаются аналогично при рассмотрении сумм \( 2^n + \varepsilon (1 + \varepsilon)^n + \varepsilon^2 (1 + \varepsilon^2)^n \) и \( 2^n + \varepsilon^2 (1 + \varepsilon)^n + \varepsilon (1 + \varepsilon^2)^n \).

Последнее равенство выводится аналогичным образом из рассмотрения выражения \( (1 + i)^n \).

31. Мы имеем
\[
(1 + x)^p = 1 + C_p^1 x + C_p^2 x^2 + \ldots + C_p^m x^m + \ldots + C_p^p x^p,
\]
\[
(1 + x)^{-k-1} = 1 - C_{k+1}^1 x + C_{k+2}^2 x^2 - \ldots + (-1)^s C_{k+s}^s x^s + \ldots,
\]
\[
(1 + x)^{p-k-1} = 1 + C_{p-k-1}^1 x + \ldots + C_{p-k-1}^n x^n + \ldots + x^{p-k-1}.
\]
Перемножим первые два разложения и найдем коэффициент при \( x^n \). Он равен \( \sum_s (-1)^{n-s} C_{k+n-s}^{n-s} C_p^s = \sum_s (-1)^s C_{k+s}^s C_p^{n-s} \). Отсюда сразу вытекает доказываемое тождество.

Следующие тождества доказываются аналогично.

42. Доказывается с помощью индукции по \( n \).