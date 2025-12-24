---
source_image: page_108.png
page_number: 108
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 50.04
tokens: 11955
characters: 2744
timestamp: 2025-12-24T08:29:25.800739
finish_reason: stop
---

Для независимых с. в. с распределениями Пуассона \( \Pi_\lambda \) и \( \Pi_\mu \) х. ф. суммы

\[
\varphi_{\xi+\eta}(t) = \varphi_\xi(t)\, \varphi_\eta(t) = \exp \left\{ \lambda \left( e^{it} - 1 \right) \right\} \exp \left\{ \mu \left( e^{it} - 1 \right) \right\} = \exp \left\{ (\lambda + \mu) \left( e^{it} - 1 \right) \right\}
\]

равна характеристической функции распределения Пуассона с параметром \( \lambda + \mu \).

Для независимых с. в. с биномиальными распределениями \( B_{n,p} \) и \( B_{m,p} \) х. ф. суммы

\[
\varphi_{\xi+\eta}(t) = \varphi_\xi(t)\, \varphi_\eta(t) = (1 - p + pe^{it})^n \left( 1 - p + pe^{it} \right)^m = (1 - p + pe^{it})^{n+m}.
\]

равна характеристике функции биномиального распределения с параметрами \( n + m, p \).

Для \( n \) независимых с. в. с показательным распределением \( E_\alpha \) х. ф. суммы

\[
\varphi_{\xi_1+\ldots+\xi_n}(t) = (\varphi_{\xi_1}(t))^n = \left( \frac{\alpha}{\alpha - it} \right)^n = \left( 1 - \frac{it}{\alpha} \right)^{-n}
\]

равна характеристике функции гамма-распределения с параметрами \( \alpha, n \).

**Ф5.** Пусть существует момент порядка \( k = 1, 2, \ldots \) случайной величины \( \xi \), то есть \( \mathbb{E}|\xi|^k < \infty \). Тогда ее характеристическая функция \( \varphi_\xi(t) \) непрерывно дифференцируема \( k \) раз, и ее \( k \)-я производная в нуле связана с моментом порядка \( k \) равенством:

\[
\varphi_\xi^{(k)}(0) = \left. \left( \frac{d^k}{dt^k} \mathbb{E} e^{it\xi} \right) \right|_{t=0} = \left. \left( \mathbb{E} i^k \xi^k e^{it\xi} \right) \right|_{t=0} = i^k \mathbb{E} \xi^k.
\]

Существование и непрерывность \( k \)-й производной, равно как и законность переноса производной под знак математического ожидания мы доказывать не будем.

**Упражнение 30.** Доказать, что для с. в. \( \xi \) со стандартным нормальным распределением момент четного порядка \( 2k \) равен \( \mathbb{E} \xi^{2k} = (2k-1)!! \overset{\text{def}}{=} (2k-1) \cdot (2k-3) \cdot \ldots \cdot 3 \cdot 1 \).
Доказать по определению, что все моменты нечетных порядков стандартного нормального распределения существуют и равны нулю.

Как только появились производные высших порядков, самое время разложить функцию в ряд Тейлора.

**Ф6.** Пусть существует момент порядка \( k = 1, 2, \ldots \) случайной величины \( \xi \), то есть \( \mathbb{E}|\xi|^k < \infty \). Тогда ее характеристическая функция \( \varphi_\xi(t) \) в окрестности точки \( t = 0 \) разлагается в ряд Тейлора

\[
\varphi_\xi(t) = \varphi_\xi(0) + \sum_{j=1}^k \frac{t^j}{j!} \varphi_\xi^{(j)}(0) + o(|t^k|) = 1 + \sum_{j=1}^k \frac{i^j t^j}{j!} \mathbb{E} \xi^j + o(|t^k|) = 1 + it \mathbb{E} \xi - \frac{t^2}{2} \mathbb{E} \xi^2 + \ldots + \frac{i^k t^k}{k!} \mathbb{E} \xi^k + o(|t^k|).
\]