---
source_image: page_076.png
page_number: 76
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.28
tokens: 11120
characters: 787
timestamp: 2025-12-24T08:27:27.012859
finish_reason: stop
---

Пример 42. Распределение Парето

Распределение Парето. Говорят, что \( \xi \) имеет распределение Парето с параметрами \( x_0, s \), где \( x_0 > 0, s > 0 \), если

\[
F_{\xi}(x) = \begin{cases}
1 - \left( \frac{x_0}{x} \right)^s, & x \geq x_0; \\
0, & x < x_0.
\end{cases}
\]

или

\[
f_{\xi}(x) = \begin{cases}
s \frac{x_0^s}{x^{s+1}}, & x \geq x_0; \\
0, & x < x_0.
\end{cases}
\]

У распределения Парето существуют только моменты порядка \( u < s \), поскольку \( \mathbf{E} |\xi|^u = \int_{x_0}^{\infty} x^u s \frac{x_0^s}{x^{s+1}} dx \) сходится при \( u < s \), то есть когда подынтегральная функция на бесконечности бесконечно мала по сравнению с \( 1/x \).

Посчитать момент порядка \( u < s \) распределения Парето. При каких \( s \) у этого распределения существует дисперсия?