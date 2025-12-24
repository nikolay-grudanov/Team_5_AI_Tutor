---
source_image: page_110.png
page_number: 110
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.29
tokens: 11663
characters: 2010
timestamp: 2025-12-24T08:29:24.826624
finish_reason: stop
---

При \( n \to \infty \), пользуясь «замечательным пределом» \( \left(1 + \frac{x}{n}\right)^n \to e^x \), получим

\[
\varphi_{S_n/n}(t) = \left(1 + \frac{ita}{n} + o\left(\left|\frac{t}{n}\right|\right)\right)^n \to e^{ita},
\]

что и требовалось доказать.

\subsection*{15.4 Доказательство центральной предельной теоремы}

Пусть \( \xi_1, \xi_2, \ldots \) — последовательность независимых и одинаково распределенных случайных величин с конечной и ненулевой дисперсией. Обозначим через \( a \) математическое ожидание \( E\xi_1 \) и через \( \sigma^2 \) — дисперсию \( D\xi_1 \). Требуется доказать, что

\[
\frac{S_n - na}{\sigma \sqrt{n}} = \frac{\xi_1 + \cdots + \xi_n - na}{\sigma \sqrt{n}} \Rightarrow N_{0,1}.
\]

Введем стандартизованные случайные величины \( \zeta_i = \frac{\xi_i - a}{\sigma} \) — независимые с.в. с нулевыми математическими ожиданиями и единичными дисперсиями. Пусть \( Z_n \) есть их сумма \( Z_n = \zeta_1 + \cdots + \zeta_n = (S_n - na)/\sigma \). Требуется доказать, что

\[
\frac{Z_n}{\sqrt{n}} \Rightarrow N_{0,1}.
\]

Характеристическая функция величины \( Z_n/\sqrt{n} \) равна

\[
\varphi_{Z_n/\sqrt{n}}(t) \overset{\Phi3}{=} \varphi_{Z_n}\left(\frac{t}{\sqrt{n}}\right) \overset{\Phi4}{=} \left(\varphi_{\zeta_1}\left(\frac{t}{\sqrt{n}}\right)\right)^n.
\]

Характеристическую функцию с.в. \( \zeta_1 \) можно разложить в ряд Тейлора, в коэффициентах которого использовать известные моменты \( E\zeta_1 = 0, E\zeta_1^2 = D\zeta_1 = 1 \). Получим

\[
\varphi_{\zeta_1}(t) \overset{\Phi6}{=} 1 + it E\zeta_1 - \frac{t^2}{2} E\zeta_1^2 + o(t^2) = 1 - \frac{t^2}{2} + o(t^2).
\]

Подставим это разложение, взятое в точке \( t/\sqrt{n} \), в равенство (25) и устремим \( n \) к бесконечности. Еще раз воспользуемся замечательным пределом.

\[
\varphi_{Z_n/\sqrt{n}}(t) = \left(\varphi_{\zeta_1}\left(\frac{t}{\sqrt{n}}\right)\right)^n = \left(1 - \frac{t^2}{2n} + o\left(\frac{t^2}{n}\right)\right)^n \to \exp\left\{-\frac{t^2}{2}\right\} \quad \text{при} \quad n \to \infty.
\]