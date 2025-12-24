---
source_image: page_165.png
page_number: 165
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.69
tokens: 6124
characters: 1398
timestamp: 2025-12-24T08:11:54.540698
finish_reason: stop
---

10.4. Многочлены Чебышёва

Многочленом Чебышёва называют многочлен \( T_n(x) \), для которого \( T_n(\cos \varphi) = \cos n\varphi \) для всех \( \varphi \). Формула

\[
\cos(n+1)\varphi + \cos(n-1)\varphi = 2 \cos n\varphi \cos \varphi
\]

показывает, что \( T_n(x) \) действительно является многочленом (степени \( n \)), причём семейство этих многочленов определяется рекуррентным соотношением

\[
T_{n+1}(x) = 2x T_n(x) - T_{n-1}(x)
\]

и начальными условиями \( T_0(x) = 1 \) и \( T_1(x) = x \).

Следующее утверждение показывает, что многочлены Чебышёва образуют ортогональную систему относительно скалярного произведения \( (f, g) = \int_{-1}^1 \frac{1}{\sqrt{1-x^2}} f(x)g(x) \, dx \).

Теорема 10.4.1. Если одно из чисел \( n \) или \( m \) больше нуля, то

\[
\int_{-1}^1 \frac{1}{\sqrt{1-x^2}} T_n(x) T_m(x) \, dx = \frac{\pi}{2} \delta_{mn},
\]
\[
\int_{-1}^1 \frac{1}{\sqrt{1-x^2}} T_0(x) T_0(x) \, dx = \pi.
\]

Доказательство. Сделав замену \( x = \cos \varphi \), получим

\[
\int_{-1}^1 \frac{1}{\sqrt{1-x^2}} T_n(x) T_m(x) \, dx = \int_0^\pi \cos n\varphi \sin m\varphi \, d\varphi =
\]
\[
= \int_0^\pi \frac{\cos(n+m)\varphi + \cos(n-m)\varphi}{2} \, d\varphi.
\]

Если \( n \neq m \), то мы получаем 0, поскольку \( \int_0^\pi \cos k\varphi \, d\varphi = 0 \) при \( k \neq 0 \).

Если же \( n = m \neq 0 \), то мы получаем \( \int_0^\pi \frac{d\varphi}{2} = \frac{\pi}{2} \). □