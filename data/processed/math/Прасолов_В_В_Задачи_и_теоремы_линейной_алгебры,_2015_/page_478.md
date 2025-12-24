---
source_image: page_478.png
page_number: 478
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.19
tokens: 6341
characters: 1779
timestamp: 2025-12-24T08:20:28.842532
finish_reason: stop
---

53.2. Дифференцирование матриц

Рассмотрим семейство матриц \( X(t) = \| x_{ij}(t) \|_1^n \), элементы которых являются дифференцируемыми функциями от \( t \). Пусть \( \dot{X}(t) = \frac{dX(t)}{dt} \) — поэлементная производная матричной функции \( X(t) \).

Теорема 53.2.1. \( (XY)' = \dot{X}Y + X\dot{Y} \).

Доказательство. Если \( Z = XY \), то \( z_{ij} = \sum_k x_{ik} y_{kj} \), а значит,
\[
\dot{z}_{ij} = \sum_k \dot{x}_{ik} y_{kj} + \sum_k x_{ik} \dot{y}_{kj}.
\]
Поэтому \( \dot{Z} = \dot{X}Y + X\dot{Y} \).

Теорема 53.2.2. а) \( (X^{-1})' = -X^{-1}\dot{X}X^{-1} \).
б) \( \operatorname{tr}(X^{-1}\dot{X}) = -\operatorname{tr}((X^{-1})'\dot{X}) \).

Доказательство. а) С одной стороны, \( (X^{-1}X)' = \dot{I} = 0 \). С другой стороны, \( (X^{-1}X)' = (X^{-1})'\dot{X} + X^{-1}\dot{X} \). Поэтому \( (X^{-1})'\dot{X} = -X^{-1}\dot{X} \), а значит, \( (X^{-1})' = -X^{-1}\dot{X}X^{-1} \).
б) Так как \( \operatorname{tr}(X^{-1}X) = n \), то \( 0 = [\operatorname{tr}(X^{-1}X)]' = \operatorname{tr}((X^{-1})'\dot{X}) + \operatorname{tr}(X^{-1}\dot{X}) \).

Теорема 53.2.3. \( (e^{At})' = Ae^{At} \).

Доказательство. Так как ряд \( \sum_{k=0}^{\infty} \frac{(tA)^k}{k!} \) сходится абсолютно, то
\[
\frac{d}{dt}(e^{At}) = \sum_{k=0}^{\infty} \frac{d}{dt} \left( \frac{(tA)^k}{k!} \right) = \sum_{k=0}^{\infty} \frac{k t^{k-1} A^k}{k!} = A \sum_{k=1}^{\infty} \frac{(tA)^{k-1}}{(k-1)!} = Ae^{At}.
\]

Однородный многочлен
\[
p(x, y) = \sum_{k=0}^n a_k x^{n-k} y^k
\]
можно отождествить с вектором \( (a_0, \ldots, a_n)^T \). Легко видеть, что многочлен
\[
p_{\varphi}(x, y) = p(x \cos \varphi + y \sin \varphi, -x \sin \varphi + y \cos \varphi)
\]
получается из многочлена \( p(x, y) \) некоторым линейным преобразованием: \( p_{\varphi}(x, y) = L_{\varphi} p(x, y) \).