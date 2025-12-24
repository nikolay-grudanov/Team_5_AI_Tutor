---
source_image: page_150.png
page_number: 150
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.14
tokens: 7888
characters: 1118
timestamp: 2025-12-24T07:29:32.542725
finish_reason: stop
---

где \( \varepsilon_1(t), \varepsilon_2(t) \to 0 \) при \( t \to 0 \). Складывая два последних равенства, получим (2.9), так как \( f_{\xi}'(0) = it M_{\xi} \). Аналогично проверяется следующее утверждение. Если \( M_{\xi^2} \) существует, то

\[
f_{\xi}(t) = 1 + it M_{\xi} - \frac{t^2}{2} M_{\xi^2} + t^2 \varepsilon(t),
\]

где \( \varepsilon(t) \to 0 \) при \( t \to 0 \).

В предположении существования \( M_{\xi^3} \) дадим другую оценку остаточного члена в (2.10).
Из равенства

\[
e^{ix} - 1 = \int_0^x i e^{iu} du
\]

следует, что \( |e^{ix} - 1| \leq \int_0^{|x|} du = |x| \), так как \( |i e^{iu}| \leq 1 \).
Так как

\[
e^{ix} - 1 - ix = i \int_0^x (e^{iu} - 1) du,
\]

то воспользовавшись оценкой \( |e^{ix} - 1| \leq |x| \), получим, что

\[
|e^{ix} - 1 - ix| \leq \int_0^{|x|} u du = \frac{|x|^2}{2}.
\]

Применив эту оценку к равенству

\[
e^{ix} - 1 - ix + \frac{x^2}{2} = i \int_0^x (e^{iy} - 1 - iy) dy,
\]

получим

\[
\left| e^{ix} - 1 - ix + \frac{x^2}{2} \right| \leq \frac{|x|^3}{6}.
\]

Отсюда

\[
e^{itx} = 1 + itx - \frac{t^2 x^2}{2} + R_1(t, x),
\]
\[
|R_1(t, x)| \leq \frac{1}{6} |tx|^3.
\]