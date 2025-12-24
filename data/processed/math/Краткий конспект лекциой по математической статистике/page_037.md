---
source_image: page_037.png
page_number: 37
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 50.79
tokens: 12253
characters: 2768
timestamp: 2025-12-24T07:04:05.770813
finish_reason: stop
---

6 РАСПРЕДЕЛЕНИЯ, СВЯЗАННЫЕ С НОРМАЛЬНЫМ

В предыдущей лекции мы построили (в числе других) точный доверительный интервал для параметра \(a\) нормального распределения при известном \(\sigma^2\). Остались нерешенными следующие проблемы:

2) построить точный ДИ для \(\sigma\) при известном \(a\),

3) построить точный ДИ для \(a\) при неизвестном \(\sigma\),

4) построить точный ДИ для \(\sigma\) при неизвестном \(a\).

Как мы уже видели, для решения этих задач требуется отыскать функции от выборки и параметров, распределение которых было бы известно. При этом в задаче (3) искомая функция не должна зависеть от \(\sigma\), а в (4) — от \(a\).

Такой особый интерес к нормальному распределению связан, разумеется, с центральной предельной теоремой — по большому счету все в этом мире нормально (или близко к тому).
Займемся поэтому распределениями, связанными с нормальным распределением, их свойствами и свойствами выборок из нормального распределения.

6.1 Гамма-распределение и его свойства

Определение 16. Случайная величина \(\xi\) имеет распределение \(\Gamma_{\alpha,\lambda}\), где \(\alpha > 0, \lambda > 0\), если \(\xi\) имеет плотность распределения

\[
f_{\alpha,\lambda}(y) = \begin{cases}
\frac{\alpha^\lambda}{\Gamma(\lambda)} y^{\lambda-1} e^{-\alpha y}, & y > 0 \\
0, & y \leq 0
\end{cases}
\]

Здесь (см. справочник, «гамма-функция»)

\[
\Gamma(\lambda) = \int_0^\infty t^{\lambda-1} e^{-t} \, dt = (\lambda - 1)\Gamma(\lambda - 1), \quad \Gamma(k) = (k-1)!,\ \Gamma(1/2) = \sqrt{\pi},\ \Gamma(1) = 1.
\]

Найдем характеристическую функцию \(\xi \in \Gamma_{\alpha,\lambda}\).

\[
\varphi_\xi(t) = \mathbb{E}e^{it\xi} = \int_0^\infty e^{ity} \frac{\alpha^\lambda}{\Gamma(\lambda)} y^{\lambda-1} e^{-\alpha y} \, dy = \frac{\alpha^\lambda}{\Gamma(\lambda)} \int_0^\infty y^{\lambda-1} e^{-(\alpha-it)y} \, dy =
\]
\[
= \frac{\alpha^\lambda}{\Gamma(\lambda)} \cdot \frac{1}{(\alpha-it)^\lambda} \int_0^\infty ((\alpha-it)y)^{\lambda-1} e^{-(\alpha-it)y} \, d(\alpha-it)y = \frac{\alpha^\lambda}{(\alpha-it)^\lambda} = \left(1 - \frac{it}{\alpha}\right)^{-\lambda}.
\]

Лемма 6. Пусть \(\xi_1, \xi_2, \ldots, \xi_n\) независимы и \(\xi_i \in \Gamma_{\alpha,\lambda_i}, i = 1, \ldots, n\). Тогда

\[
S_n = \sum_{i=1}^n \xi_i \in \Gamma_{\alpha, \sum_1^n \lambda_i}.
\]

Доказательство свойства устойчивости по суммированию (леммы 6).

\[
\varphi_{S_n}(t) = \prod_{i=1}^n \varphi_{\xi_i}(t) = \prod_{i=1}^n \left(1 - \frac{it}{\alpha}\right)^{-\lambda_i} = \left(1 - \frac{it}{\alpha}\right)^{-\sum_1^n \lambda_i},
\]

что и требовалось доказать.

Следствие 2. Пусть \(\xi_1, \xi_2, \ldots, \xi_n\) независимы, одинаково распределены и имеют показательное распределение \(\mathrm{E}_\alpha\). Тогда \(S_n = \sum_{i=1}^n \xi_i \in \Gamma_{\alpha,n}\).