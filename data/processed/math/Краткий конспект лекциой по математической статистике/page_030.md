---
source_image: page_030.png
page_number: 30
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 76.05
tokens: 12463
characters: 2733
timestamp: 2025-12-24T07:04:12.037360
finish_reason: stop
---

Найдем информацию Фишера относительно параметра \( a \) (считая, что имеется один неизвестный параметр — \( a \)).

\[
f_{(a,\sigma^2)}(X_1) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(X_1 - a)^2}{2\sigma^2} \right)
\]
\[
\ln f_{(a,\sigma^2)}(X_1) = -\ln (2\pi\sigma^2)^{1/2} - \frac{(X_1 - a)^2}{2\sigma^2}
\]
\[
\frac{\partial}{\partial a} \ln f_{(a,\sigma^2)}(X_1) = \frac{(X_1 - a)}{\sigma^2}
\]
\[
I(a) = E_{(a,\sigma^2)} \left( \frac{\partial}{\partial a} \ln f_{(a,\sigma^2)}(X_1) \right)^2 = \frac{E_{(a,\sigma^2)} (X_1 - a)^2}{\sigma^4} = \frac{D_{(a,\sigma^2)} X_1}{\sigma^4} = \frac{1}{\sigma^2}.
\]

Итак, \( I(a) = 1/\sigma^2 \). Найдем дисперсию оценки \( \overline{X} \). По теореме о свойствах \( S_n / n \) из прошлого семестра, которую невредно вспомнить,

\[
D_{(a,\sigma^2)} \overline{X} \stackrel{!}{=} \frac{1}{n} D_{(a,\sigma^2)} X_1 = \frac{\sigma^2}{n}.
\]

Замечание 14. Тем, кто не желает обременять память воспоминаниями, предлагается воспользоваться свойствами дисперсии суммы независимых (и одинаково распределенных) случайных величин и доказать равенство

\[
D \overline{X} \equiv \frac{1}{n} D X_1
\]

Далее, сравнивая левую и правую части в неравенстве Рао-Крамера, получаем равенство:

\[
D_{(a,\sigma^2)} \overline{X} = \frac{\sigma^2}{n} = \frac{1}{n I(a)}.
\]

То есть оценка \( a^* = \overline{X} \) эффективна (обладает наименьшей дисперсией среди несмещенных оценок).

Пример 19. Пусть \( X_1, \ldots, X_n \) — выборка объема \( n \) из нормального распределения \( N_{0,\sigma^2} \), где \( \sigma > 0 \). Проверим, является ли оценка \( \sigma^{2*} = \frac{1}{n} \sum_{i=1}^n X_i^2 = \overline{X^2} \in K_0 \) эффективной.

Упражнение. Получить эту оценку методом моментов и методом максимального правдоподобия.

Найдем информацию Фишера относительно параметра \( \sigma^2 \).

\[
f_{\sigma^2}(X_1) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{X_1^2}{2\sigma^2} \right)
\]
\[
\ln f_{\sigma^2}(X_1) = -\ln (2\pi)^{1/2} - \frac{1}{2} \ln \sigma^2 - \frac{X_1^2}{2\sigma^2}
\]
\[
\frac{\partial}{\partial \sigma^2} \ln f_{\sigma^2}(X_1) = -\frac{1}{2\sigma^2} + \frac{X_1^2}{2\sigma^4}
\]
\[
I(\sigma^2) = E_{\sigma^2} \left( \frac{\partial}{\partial \sigma^2} \ln f_{\sigma^2}(X_1) \right)^2 = E_{\sigma^2} \left( \frac{X_1^2}{2\sigma^4} - \frac{1}{2\sigma^2} \right)^2 = \frac{1}{4\sigma^8} E_{\sigma^2} (X_1^2 - \sigma^2)^2 = \frac{1}{4\sigma^8} D_{\sigma^2} X_1^2.
\]

Осталось найти
\[
D_{\sigma^2} X_1^2 = E_{\sigma^2} X_1^4 - (E_{\sigma^2} X_1^2)^2 = E_{\sigma^2} X_1^4 - \sigma^4.
\]

Найдем четвертый момент \( X_1 \). Для тех, кто помнит некоторые формулы вероятности:
\[
E \xi^{2k} = (2k-1)!! = (2k-1)(2k-3) \cdot \ldots \cdot 3 \cdot 1 \text{ при } \xi \in N_{0,1},
\]