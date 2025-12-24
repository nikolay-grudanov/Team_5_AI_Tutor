---
source_image: page_003.png
page_number: 3
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.63
tokens: 4613
characters: 4146
timestamp: 2025-12-23T22:29:38.389281
finish_reason: stop
---

\[
+ y_m^2 \left[ -\frac{t_m}{2(t_m - t_{m-1})} + O \left( \max \left( \frac{1}{n^\alpha}, \frac{1}{n^{1-\alpha}} \right) \right) \right] + \sum_{j=1}^{m-1} y_j y_{j+1} \left[ \frac{\sqrt{t_j t_{j+1}}}{t_{j+1} - t_j} + O \left( \frac{1}{n^\alpha} \right) \right] + O \left( \frac{1}{n^{\alpha/2}} \right).
\]
(4)

Преобразуя его, будем иметь
\[
\ln h(x_1, \ldots, x_n) =
\]
\[
= C - \frac{1}{2} \left[ y_1^2 \frac{t_2}{t_2 - t_1} + \sum_{j=2}^{m-1} y_j^2 \frac{t_j (t_{j+1} - t_{j-1})}{(t_j - t_{j-1})(t_{j+1} - t_j)} + y_m^2 \frac{t_m}{t_m - t_{m-1}} - 2 \sum_{j=1}^{m-1} y_j y_{j+1} \frac{\sqrt{t_j t_{j+1}}}{t_{j+1} - t_j} \right] +
\]
\[
+ O \left( \max \left( \frac{1}{n^{\alpha/2}}, \frac{1}{n^{1-\alpha}} \right) \right).
\]
(5)

Из (4), (5) следует, что вектор \((Y_1, \ldots, Y_m)\) асимптотически при \(n \to \infty\) имеет \(m\)-мерное нормальное распределение с вектором нулевых математических ожиданий. Элементы матрицы \(A = (A_{ij})\) коэффициентов квадратичной формы в соотношении (5) определяются следующим образом:
\[
A_{11} = \frac{t_2}{t_2 - t_1}, \quad A_{jj} = \frac{t_j (t_{j+1} - t_{j-1})}{(t_j - t_{j-1})(t_{j+1} - t_j)}, \quad 2 \leq j \leq m-1, \quad A_{mm} = \frac{t_m}{t_m - t_{m-1}},
\]
\[
A_{j,j+1} = A_{j+1,j} = -\frac{\sqrt{t_j t_{j+1}}}{(t_{j+1} - t_j)}, \quad A_{ij} = 0 \quad \text{при } |i - j| > 1.
\]

Матрица, обратная к \(A\), т. е. ковариационная матрица величин \(Y_i\), асимптотически имеет элементы \(\operatorname{cov}(Y_i, Y_j) = \sqrt{t_i / t_j}, i \leq j\). Так как
\[
X_{n_i}^{(n)} = \frac{t_i^{1/2}}{n^{1-\alpha/2}} Y_i + \frac{t_i}{n^{1-\alpha}}, \quad i = 1, \ldots, m,
\]
то в том случае, когда исходное распределение \(F\) является равномерным на отрезке \((0,1)\), вектор \((X_{n_1}^{(n)}, \ldots, X_{n_m}^{(n)})\) асимптотически при \(n \to \infty\) имеет \(m\)-мерное нормальное распределение с вектором математических ожиданий \((t_1 / n^{1-\alpha}, \ldots, t_m / n^{1-\alpha})\) и ковариациями \(\operatorname{cov}(X_{n_i}^{(n)}, X_{n_j}^{(n)}) = t_i / n^{2-\alpha}, i \leq j\).

Для доказательства теоремы в общем случае воспользуемся следующей леммой [9, гл. 9, § 9.2].

Лемма. Если случайные величины \(Z_{n,i}, i = 1, \ldots, m\), имеют асимптотически \(m\)-мерное нормальное распределение с математическими ожиданиями \(\mu_{n,i}\), дисперсиями \(\sigma_{n,i}^2, \sigma_{n,i}^2 \to 0\) при \(n \to \infty\), и ковариациями \(\rho_{i,j} \sigma_{n,i} \sigma_{n,j}\), и если \(g_i(Z_{n,i})\) — однозначные функции с не равными нулю в некоторых окрестностях точек \(Z_{n,i} = \mu_{n,i}\) и непрерывными производными \(g_i'(Z_{n,i})\), то сами \(g_i(Z_{n,i})\) асимптотически имеют \(m\)-мерное нормальное распределение с математическими ожиданиями \(g_i(\mu_{n,i})\) и ковариациями \(\rho_{i,j} \sigma_{n,i} \sigma_{n,j} g_i'(\mu_{n,i}) g_j'(\mu_{n,j})\).

Полагая \(Z_{n,i} = X_{n_i}^{(n)}\), \(\mu_{n,i} = t_i / n^{1-\alpha}\), \(\rho_{i,j} \sigma_{n,i} \sigma_{n,j} = t_i / n^{2-\alpha}, i \leq j\), получим, что преобразование \(g_i(X_{n_i}^{(n)}) = F^{-1}(X_{n_i}^{(n)})\) удовлетворяет условиям леммы,
\[
g_i(\mu_{n,i}) = F^{-1}(\mu_{n,i}) = d_{n,t_i}, \qquad g_i'(\mu_{n,i}) = \frac{dg_i(\mu_{n,i})}{d\mu_{n,i}} = \frac{1}{f(d_{n,t_i})}, \quad i = 1, \ldots, m.
\]
Выразим величину \(1/f(d_{n,t_i})\) через \(c_{n,t_i}\), используя соотношение (2), после чего получим значения для ковариаций, указанные в формулировке теоремы. Доказательство теоремы завершено.

Введем обозначение \(z_F = \inf \{x : F(x) > 0\}, 0 < \alpha < 1, t > 0\), и рассмотрим типичные классы распределений, широко используемые в статистических приложениях.

Класс \(B_1\):
\[
F(x) \sim a|x|^{\gamma} \exp(-b|x|^{\Delta}), \quad f(x) \sim ab \Delta |x|^{\gamma+\Delta-1} \exp(-b|x|^{\Delta}) \text{ при } x \to -\infty, \quad a, b, \Delta > 0,
\]
\[
d_{n,t} = - \left( \frac{(1-\alpha) \ln n}{b} \right)^{1/\Delta} \left( 1 + \frac{\gamma \ln \ln n + \ln c}{\Delta^2 (1-\alpha) \ln n} \right), \quad c = \left( \frac{1-\alpha}{b} \right)^{\gamma} \left( \frac{a}{t} \right)^{\Delta},
\]
\[
c_{n,t} = \left( \frac{(1-\alpha) \ln n}{b} \right)^{(1-\Delta)/\Delta} \frac{1}{\Delta b t^{1/2} n^{\alpha/2}}.
\]