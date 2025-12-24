---
source_image: page_038.png
page_number: 38
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.64
tokens: 11683
characters: 2133
timestamp: 2025-12-24T08:26:07.523081
finish_reason: stop
---

испытаний. Но от испытания к испытанию вероятность успеха меняться не может (см. определение схемы Бернулли).

Поэтому рассмотрим «схему серий»: есть

одно испытание   ○   с вероятностью успеха \( p_1 \)
два испытания   ○, ○   с вероятностью успеха \( p_2 \)
...
\( n \) испытаний   ○, ..., ○   с вероятностью успеха \( p_n \)
...

Вероятность успеха меняется не внутри одной серии испытаний, а от серии к серии, когда меняется общее число испытаний. Обозначим через \( \nu_n \) число успехов в \( n \)-й серии испытаний.

**Теорема 16 (Теорема Пуассона).**
Пусть \( n \to \infty, p_n \to 0 \) так, что \( np_n \to \lambda > 0 \). Тогда для любого \( k \geq 0 \) вероятность получить \( k \) успехов в \( n \) испытаниях схемы Бернулли с вероятностью успеха \( p_n \) стремится к величине \( \frac{\lambda^k}{k!} e^{-\lambda} \):

\[
\mathbf{P}(\nu_n = k) = C_n^k p_n^k (1 - p_n)^{n-k} \to \frac{\lambda^k}{k!} e^{-\lambda} \quad \text{при} \quad n \to \infty, p_n \to 0 \quad \text{так, что} \quad np_n \to \lambda > 0.
\]

**Доказательство.** Положим \( \lambda_n = n \cdot p_n \to \lambda > 0 \). По свойству 4, \( C_n^k \sim \frac{n^k}{k!} \) при фиксированном \( k \) и при \( n \to \infty \).

Тогда

\[
C_n^k p_n^k (1 - p_n)^{n-k} = C_n^k \frac{\lambda_n^k}{n^k} \left(1 - \frac{\lambda_n}{n}\right)^{n-k} \sim \frac{\lambda_n^k}{k!} \frac{\lambda_n^k}{n^k} \left(1 - \frac{\lambda_n}{n}\right)^n \left(1 - \frac{\lambda_n}{n}\right)^{-k} \to \frac{\lambda^k}{k!} e^{-\lambda}.
\]

В (8) мы использовали свойства \( \lambda_n^k \to \lambda^k \) и \( \left(1 - \frac{\lambda_n}{n}\right)^n \to e^{-\lambda} \). Докажем последнее свойство:

\[
\ln \left(1 - \frac{\lambda_n}{n}\right)^n = n \ln \left(1 - \frac{\lambda_n}{n}\right) = n \left(-\frac{\lambda_n}{n} + O\left(\frac{\lambda_n^2}{n^2}\right)\right) \to -\lambda.
\]

Для доказательства теоремы осталось в формуле (8) воспользоваться свойством 5.

**Определение 23.** Пусть \( \lambda > 0 \) — некоторая постоянная. Набор чисел \( \left\{ \frac{\lambda^k}{k!} e^{-\lambda}, k = 0, 1, 2, \ldots \right\} \) называется распределением Пуассона с параметром \( \lambda \).