---
source_image: page_031.png
page_number: 31
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 93.51
tokens: 12819
characters: 3280
timestamp: 2025-12-24T07:04:34.054469
finish_reason: stop
---

\[
X_1 = \xi \cdot \sigma \in N_{0, \sigma^2} \implies E X_1^4 = E \xi^4 \cdot \sigma^4 = 3 \sigma^4.
\]
Для тех, кто не помнит — краткое пособие по интегрированию:

\[
E_{\sigma^2} X_1^4 = \int_{-\infty}^{\infty} y^4 \frac{1}{\sqrt{2 \pi} \sigma} e^{-\frac{y^2}{2 \sigma^2}} dy = 2 \sigma^4 \int_0^{\infty} \left( \frac{y}{\sigma} \right)^4 \frac{1}{\sqrt{2 \pi}} e^{-\frac{y^2}{2 \sigma^2}} d \left( \frac{y}{\sigma} \right) =
\]
\[
= 2 \sigma^4 \int_0^{\infty} t^4 \frac{1}{\sqrt{2 \pi}} e^{-\frac{t^2}{2}} dt = -2 \sigma^4 \frac{1}{\sqrt{2 \pi}} \int_0^{\infty} t^3 de^{-\frac{t^2}{2}} = -2 \sigma^4 \frac{1}{\sqrt{2 \pi}} \left( t^3 e^{-\frac{t^2}{2}} \Bigg|_0^{\infty} - \int_0^{\infty} e^{-\frac{t^2}{2}} dt^3 \right) =
\]
\[
= 2 \sigma^4 \frac{1}{\sqrt{2 \pi}} \cdot 3 \int_0^{\infty} t^2 e^{-\frac{t^2}{2}} dt = 3 \sigma^4 \int_{-\infty}^{\infty} \frac{1}{\sqrt{2 \pi}} t^2 e^{-\frac{t^2}{2}} dt = 3 \sigma^4 \cdot D \xi = 3 \sigma^4 \cdot 1, \quad \text{где} \quad \xi \in N_{0,1}.
\]
Итак, \( D_{\sigma^2} X_1^2 = E_{\sigma^2} X_1^4 - \sigma^4 = 2 \sigma^4. \)

\[
I(\sigma^2) = \frac{1}{4 \sigma^8} D_{\sigma^2} X_1^2 = \frac{1}{4 \sigma^8} 2 \sigma^4 = \frac{1}{2 \sigma^4}.
\]
Найдем дисперсию оценки \( \sigma^{2*} = \overline{X^2}. \)

\[
D_{\sigma^2} \overline{X^2} = \frac{1}{n^2} D_{\sigma^2} \sum_{i=1}^n X_i^2 = \frac{1}{n} D_{\sigma^2} X_1^2 = \frac{2 \sigma^4}{n}.
\]
Сравнивая левую и правую части в неравенстве Рао-Крамера, получаем равенство:

\[
D_{\sigma^2} \overline{X^2} = \frac{2 \sigma^4}{n} = \frac{1}{n I(\sigma^2)}.
\]
Таким образом, оценка \( \sigma^{2*} = \overline{X^2} \) эффективна.

**Упражнение.** Пусть \( X_1, \ldots, X_n \) — выборка объема \( n \) из нормального распределения \( N_{a, \sigma^2} \), где \( a \) известно, \( \sigma > 0 \). Проверить, является ли оценка \( \sigma^{2*} = \frac{1}{n} \sum_{i=1}^n (X_i - a)^2 = (\overline{X} - a)^2 \) эффективной. Принадлежит ли эта оценка классу \( K_0 \)? Какими методами получена? Является ли состоятельной и асимптотически нормальной?

**Пример 20.** Пусть \( X_1, \ldots, X_n \) — выборка объема \( n \) из распределения Бернулли \( B_{17p} \) (а почему бы и нет?), где \( p \in (0, 1/17) \). Проверим, является ли оценка \( p^* = \overline{X}/17 \in K_0 \) (оценка для параметра \( p! \)) эффективной.

Найдем информацию Фишера \( I(p) = E_p \left( \frac{\partial}{\partial p} \ln f_p(X_1) \right)^2 \) относительно параметра \( p \). Нам знаком только «табличный» вид «плотности» распределения Бернулли с вероятностью успеха \( 17p \):

\[
f_p(y) = P_p(X_1 = y) = \begin{cases}
17p, & \text{если } y = 1, \\
1 - 17p, & \text{если } y = 0.
\end{cases}
\]

Заметим, что то же самое можно записать иначе:

\[
f_p(y) = (17p)^y (1 - 17p)^{1-y}, \quad y = 0, 1.
\]

Теперь уже удобно и логарифмировать, и дифференцировать.

\[
f_p(X_1) = (17p)^{X_1} (1 - 17p)^{1 - X_1}
\]
\[
\ln f_p(X_1) = X_1 \ln 17 + X_1 \ln p + (1 - X_1) \ln (1 - 17p)
\]
\[
\frac{\partial}{\partial p} \ln f_p(X_1) = \frac{X_1}{p} - 17 \frac{1 - X_1}{1 - 17p} = \frac{X_1 - 17p}{p(1 - 17p)}
\]
\[
I(p) = E_p \left( \frac{\partial}{\partial p} \ln f_p(X_1) \right)^2 = \frac{E_p (X_1 - 17p)^2}{p^2 (1 - 17p)^2} = \frac{D_p X_1}{p^2 (1 - 17p)^2} = \frac{17p (1 - 17p)}{p^2 (1 - 17p)^2} = \frac{17}{p (1 - 17p)}.
\]