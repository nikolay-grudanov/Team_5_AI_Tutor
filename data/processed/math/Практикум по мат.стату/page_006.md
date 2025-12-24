---
source_image: page_006.png
page_number: 6
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.13
tokens: 5743
characters: 1745
timestamp: 2025-12-24T07:38:25.570167
finish_reason: stop
---

Таблица 1

\begin{itemize}
    \item $T_k$ — случайная величина, распределенная по закону Стьюдента (t-распределение) с $k$ степенями свободы
    \item $\chi^2_k$ — случайная величина, распределенная по закону $\chi^2$ с $k$ степенями свободы
    \item $F_{k_1; k_2}$ — случайная величина, распределенная по закону Фишера (F-распределение) с $k_1$ и $k_2$ степенями свободы
    \item \[
        \Phi(x) = \frac{1}{\sqrt{2\pi}} \int_0^x e^{-\frac{t^2}{2}} dt
    \] — функция Лапласа
    \item \[
        \varphi(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}
    \] — функция Гаусса
    \item \[
        F_{m, \sigma}(x) = \frac{1}{\sqrt{2\pi} \sigma} \int_{-\infty}^x e^{-(t-m)^2/2\sigma^2} dt = \Phi\left(\frac{x-m}{\sigma}\right) + 0.5
    \] — функция распределения случайной величины $X \sim \mathrm{N}(m; \sigma)$
    \item \[
        f_{m, \sigma}(x) = \frac{1}{\sqrt{2\pi} \sigma} e^{-(x-m)^2/2\sigma^2} = \frac{1}{\sigma} \varphi\left(\frac{x-m}{\sigma}\right)
    \] — плотность распределения случайной величины $X \sim \mathrm{N}(m; \sigma)$
    \item $\overline{x}$ — выборочное среднее
    \item $\hat{\sigma}_X^2$ — выборочная дисперсия
    \item $s_X^2$ — исправленная (уточненная) выборочная дисперсия
    \item $\mathrm{R}(X, Y), \rho_{xy}$ — выборочный коэффициент корреляции случайных величин $X$ и $Y$
    \item $z_\alpha$ — 100$\alpha$-процентная точка стандартного нормального распределения
    \item $t_{k; \alpha}$ — 100$\alpha$-процентная точка распределения Стьюдента с $k$ степенями свободы
    \item $\chi^2_{k; \alpha}$ — 100$\alpha$-процентная точка $\chi^2$-распределения с $k$ степенями свободы
    \item $f_{k_1; k_2; \alpha}$ — 100$\alpha$-процентная точка F-распределения с $k_1$ и $k_2$ степенями свободы
\end{itemize}