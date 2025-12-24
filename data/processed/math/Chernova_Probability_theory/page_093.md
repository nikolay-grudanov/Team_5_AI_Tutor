---
source_image: page_093.png
page_number: 93
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 69.96
tokens: 12137
characters: 1888
timestamp: 2025-12-24T07:36:55.485350
finish_reason: stop
---

§3. Средние и дисперсии стандартных распределений

Пример 67 (геометрическое распределение \( G_p \)). Вычислим \( E \):

\[
E = \sum_{k=1}^{\infty} k p q^{k-1} = p \sum_{k=1}^{\infty} k q^{k-1} = p \sum_{k=1}^{\infty} \frac{dq^k}{dq} =
\]
\[
= p \frac{d}{dq} \left( \sum_{k=1}^{\infty} q^k \right) = p \frac{d}{dq} \left( \frac{q}{1-q} \right) = p \frac{1}{(1-q)^2} = \frac{1}{p}.
\]

Вычислим так называемый «второй факториальный момент»:

\[
E(-1) = \sum_{k=1}^{\infty} k(k-1) p q^{k-1} = p q \sum_{k=0}^{\infty} \frac{d^2 q^k}{dq^2} = p q \frac{d^2}{dq^2} \left( \sum_{k=0}^{\infty} q^k \right) =
\]
\[
= p q \frac{d^2}{dq^2} \left( \frac{1}{1-q} \right) = p q \frac{2}{(1-q)^3} = \frac{2q}{p^2}.
\]

Найдём дисперсию через второй факториальный момент:

\[
D = E(-1) + E - (E)^2 = \frac{2q}{p^2} + \frac{1}{p} - \frac{1}{p^2} = \frac{2q-1+p}{p^2} = \frac{q}{p^2}.
\]

Пример 68 (распределение Пуассона \( \Pi \)). Вычислим \( E \):

\[
E = \sum_{k=0}^{\infty} k \frac{k}{k!} e^{-} = e^{-} \sum_{k=1}^{\infty} \frac{k}{k!} = e^{-} \sum_{k=1}^{\infty} \frac{k}{(k-1)!} =
\]
\[
= e^{-} \sum_{k=1}^{\infty} \frac{k-1}{(k-1)!} = e^{-} \sum_{m=0}^{\infty} \frac{m}{m!} = e^{-} e = .
\]

Моменты более высоких порядков легко находятся через факториальные моменты \( E^{[m]} = E(-1) \ldots (-m+1) \) порядка \( m \). Так, второй факториальный момент равен

\[
E(-1) = \sum_{k=0}^{\infty} k(k-1) \frac{k}{k!} e^{-} = 2e^{-} \sum_{k=2}^{\infty} \frac{k-2}{(k-2)!} = 2e^{-} e = 2.
\]

Поэтому \( E^2 = E(-1) + E = 2 + \) и \( D = E^2 - (E)^2 = . \)

Пример 69 (равномерное распределение \( U_{a,b} \)). Математическое ожидание \( E = \frac{a+b}{2} \) мы вычислили в примере 60. Второй момент равен

\[
E^2 = \int_{-\infty}^{\infty} x^2 f(x) dx = \int_a^b x^2 \frac{1}{b-a} dx = \frac{b^3 - a^3}{3(b-a)} = \frac{a^2 + ab + b^2}{3}.
\]

Дисперсия равна \( D = E^2 - (E)^2 = \frac{(b-a)^2}{12} . \)