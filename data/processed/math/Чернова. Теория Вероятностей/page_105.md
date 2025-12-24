---
source_image: page_105.png
page_number: 105
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 51.23
tokens: 11862
characters: 2377
timestamp: 2025-12-24T08:29:23.280612
finish_reason: stop
---

Раздел 15. Характеристические функции

Всюду в этой главе \( i = \sqrt{-1} \) — мнимая единица, \( t \) — вещественная переменная, \( e^{it} = \cos t + i \sin t \) — формула Эйлера, \( \mathbf{E}(\eta + i \zeta) = \mathbf{E}\eta + i \mathbf{E}\zeta \) — способ вычисления математического ожидания комплекснозначной случайной величины \( \eta + i \zeta \), если математические ожидания ее действительной (\( \eta \)) и мнимой (\( \zeta \)) частей существуют.
Как всегда, модулем комплексного числа \( z = x + iy \) называется \( |z| = \sqrt{x^2 + y^2} \), так что \( |e^{it}| = 1 \).

Определение 53. Функция \( \varphi_{\xi}(t) = \mathbf{E} e^{it\xi} \) называется *характеристической функцией* случайной величины \( \xi \).

**15.1 Примеры вычисления**

Пример 52. Пусть с.в. \( \xi \) имеет распределение Бернулли с параметром \( p \). Ее характеристическая функция (х.ф.) равна
\[
\varphi_{\xi}(t) = \mathbf{E} e^{it\xi} = e^{it \cdot 0} \mathbf{P}(\xi = 0) + e^{it \cdot 1} \mathbf{P}(\xi = 1) = 1 - p + pe^{it}.
\]

Пример 53. Пусть с.в. \( \xi \) имеет биномиальное распределение с параметрами \( n \) и \( p \). Ее х.ф. равна
\[
\varphi_{\xi}(t) = \mathbf{E} e^{it\xi} = \sum_{k=0}^{n} e^{it \cdot k} \mathbf{P}(\xi = k) = \sum_{k=0}^{n} e^{it \cdot k} C_n^k p^k (1-p)^{n-k} = \sum_{k=0}^{n} C_n^k (pe^{it})^k (1-p)^{n-k} = (1 - p + pe^{it})^n.
\]
Последнее равенство суть бином Ньютона.

Пример 54. Пусть с.в. \( \xi \) имеет распределение Пуассона с параметром \( \lambda \). Ее х.ф. равна
\[
\varphi_{\xi}(t) = \mathbf{E} e^{it\xi} = \sum_{k=0}^{\infty} e^{it \cdot k} \mathbf{P}(\xi = k) = \sum_{k=0}^{\infty} e^{it \cdot k} \frac{\lambda^k}{k!} e^{-\lambda} = e^{-\lambda} \sum_{k=0}^{\infty} \frac{(\lambda e^{it})^k}{k!} = e^{-\lambda} e^{\lambda e^{it}} = \exp\{\lambda (e^{it} - 1)\}.
\]

Пример 55. Пусть с.в. \( \xi \) имеет показательное распределение с параметром \( \alpha \). Ее х.ф. функция равна
\[
\varphi_{\xi}(t) = \mathbf{E} e^{it\xi} = \int_0^{\infty} e^{itx} f_{\xi}(x) dx = \int_0^{\infty} e^{itx} \alpha e^{-\alpha x} dx = \int_0^{\infty} \alpha e^{-x(\alpha-it)} dx = \frac{\alpha}{\alpha - it} \left( -e^{-x(\alpha-it)} \right|_0^{\infty} ) = \frac{\alpha}{\alpha - it},
\]
поскольку при \( x \to \infty \) модуль величины \( e^{-x(\alpha-it)} = e^{-\alpha x} \cdot e^{itx} \) стремится к нулю: \( |e^{-x(\alpha-it)}| = e^{-\alpha x} \to 0 \).