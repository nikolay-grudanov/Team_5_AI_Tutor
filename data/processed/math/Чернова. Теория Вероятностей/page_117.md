---
source_image: page_117.png
page_number: 117
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.77
tokens: 11758
characters: 2175
timestamp: 2025-12-24T08:29:31.968651
finish_reason: stop
---

тогда, когда каждая из этих величин меньше \( x \).

\[
F_{\varphi_n}(x) = \mathbf{P}(\max\{\xi_1, \ldots, \xi_n\} < x) = \mathbf{P}(\xi_1 < x, \ldots, \xi_n < x)
\]
независ.
\[
= \mathbf{P}(\xi_1 < x) \cdot \ldots \cdot \mathbf{P}(\xi_n < x)
\]
ог.распрег.
\[
= \left( \mathbf{P}(\xi_1 < x) \right)^n = \left( F_{\xi_1}(x) \right)^n.
\]

Найдем функцию распределения \( F_{\psi_n}(x) \). Минимум из \( n \) величин не меньше \( x \) тогда и только тогда, когда каждая из этих величин не меньше \( x \).

\[
F_{\psi_n}(x) = \mathbf{P}(\min\{\xi_1, \ldots, \xi_n\} < x) = 1 - \mathbf{P}(\min\{\xi_1, \ldots, \xi_n\} \geqslant x)
\]
независ.
\[
= 1 - \mathbf{P}(\xi_1 \geqslant x) \cdot \ldots \cdot \mathbf{P}(\xi_n \geqslant x)
\]
ог.распрег.
\[
= 1 - \left( \mathbf{P}(\xi_1 \geqslant x) \right)^n = 1 - (1 - F_{\xi_1}(x))^n.
\]

Пример № N. Пусть с. в. \( \xi_1, \xi_2, \ldots, \xi_n, \ldots \) независимы и имеют равномерное распределение на отрезке \([0, 1]\). Докажем, что последовательность с. в. \( \varphi_1 = \xi_1, \varphi_2 = \max\{\xi_1, \xi_2\}, \ldots, \varphi_n = \max\{\xi_1, \ldots, \xi_n\}, \ldots \) сходится по вероятности к правому концу отрезка — к 1. Не употребляя термин «последовательность», можно произнести это утверждение так: «максимум из первых \( n \) случайных величин с ростом \( n \) сходится к единице по вероятности».

Есть как минимум два способа доказательства:

Способ 1. По определению. Пусть \( \varepsilon > 0 \). Найдем \( \mathbf{P}(|\varphi_n - 1| > \varepsilon) \). Заметим, что \( \varphi_n \leqslant 1 \), поскольку это максимум из с. в., принимающих значения на отрезке \([0, 1]\) ( крайняя правая из «координат \( n \) точек, брошенных наудачу на \([0, 1]\) независимо друг от друга»). Поэтому

\[
\mathbf{P}(|\varphi_n - 1| > \varepsilon) = \mathbf{P}(1 - \varphi_n > \varepsilon)
\]

Для того, чтобы установить сходимость последней вероятности к нулю, можно ее либо найти, либо оценить с помощью неравенства Чебышёва (Маркова).

1(a). Найдем эту вероятность.

\[
\mathbf{P}(1 - \varphi_n > \varepsilon) = \mathbf{P}(1 - \varepsilon > \varphi_n) = \mathbf{P}(\varphi_n < 1 - \varepsilon) = F_{\varphi_n}(1 - \varepsilon).
\]