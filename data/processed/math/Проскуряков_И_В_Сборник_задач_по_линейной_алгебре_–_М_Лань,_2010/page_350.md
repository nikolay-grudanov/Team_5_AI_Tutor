---
source_image: page_350.png
page_number: 350
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.35
tokens: 5901
characters: 2872
timestamp: 2025-12-24T07:13:41.740562
finish_reason: stop
---

486. Указание. Вычислить первый определитель, используя результат задачи 479.

487. \((-2)^{n-1}(n - 2p)\), если \(n\) и \(p\) взаимно просты; 0, если \(n\) и \(p\) не взаимно просты.

Указание. Использовать результат задачи 479 и свойства корней \(n\)-й степени из единицы, в частности, то, что при \(p\), взаимно простом с \(n\), числа \(\varepsilon_1^p, \varepsilon_2^p, \ldots, \varepsilon_n^p\) снова являются всеми значениями \(\sqrt[n]{1}\), а при \(p\), не взаимно простом с \(n\), найдется \(\varepsilon_k \neq 1\), для которого \(\varepsilon_k^p = 1\).

488. \([3 + (n - p)b](a - b)^{n-1}\), если \(n\) и \(p\) взаимно просты; 0, если \(n\) и \(p\) не взаимно просты.

Указание. Воспользоваться указанием к предыдущей задаче.

489. \(2^{n-1} (\cos^n \frac{\pi}{n} - 1)\).

Указание. Положить \(\cos \frac{j\pi}{n} = \frac{\varepsilon_1^j + \varepsilon_1^{-j}}{2}\), где \(\varepsilon_1 = \cos \frac{\pi}{n} + i \sin \frac{\pi}{n}\), использовать результат задачи 479 и то, что для любого \(a\) имеем \(\prod_{k=0}^{n-1} (a - \varepsilon_1^{2k}) = a^n - 1\) и \(\varepsilon_1^n = -1\).

490.

\[
\frac{[\cos \theta - \cos(n+1)\theta]^n - (1 - \cos n\theta)^n}{2(1 - \cos \theta)} =
\]
\[
= 2^{n-2} \sin^{n-2} \frac{n\theta}{2} \left[ \sin^n \frac{(n+2)\theta}{2} - \sin^n \frac{n\theta}{2} \right].
\]

Указание. Положить \(\varepsilon = \cos \frac{2\pi}{n} + i \sin \frac{2\pi}{n}\), \(\eta = \cos \theta + i \sin \theta\) и воспользоваться результатом задачи 479.

491. \((-1)^n 2^{n-2} \sin^{n-2} \frac{nh}{2} \left[ \cos^n \left( a + \frac{nh}{2} \right) - \cos^n \left( a + \frac{(n-2)h}{2} \right) \right]\).

492. \((-1)^{n-1} \frac{(n+1)(2n+1)n^{n-2}}{12} [(n+2)^n - n^n]\).

Указание. Использовать результат задачи 479 и соотношения \(1^2 + 2^2 + 3^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6}\) и \(1 + 4\varepsilon + 9\varepsilon^2 + \cdots + n^2 \varepsilon^{n-1} = -\frac{n^1(1-\varepsilon)+2n}{(1-\varepsilon)^2}\), где \(\varepsilon\) — корень \(n\)-й степени из 1, отличный от 1. Для получения последнего равенства умножить и разделить левую часть на \(1 - \varepsilon\).

493. \(f(\eta_1)f(\eta_2) \ldots f(\eta_n)\), где \(f(x) = a_1 + a_2 x + a_3 x^2 + \cdots + a_n x^{n-1}\) и \(\eta_1, \eta_2, \ldots, \eta_n\) — все значения корня \(\sqrt[n]{-1}\), например, \(\eta_k = \cos \frac{(2k-1)\pi}{n} + i \sin \frac{(2k-1)\pi}{n}\).

Указание. Данный определитель умножить на определитель Вандермонда, составленный из чисел \(\eta_1, \eta_2, \ldots, \eta_n\).

494. \(f(\alpha_1)f(\alpha_2) \ldots f(\alpha_n)\), где \(f(x) = a_1 + a_2 x + a_3 x^2 + \cdots + a_n x^{n-1}\) и \(\alpha_1, \alpha_2, \ldots, \alpha_n\) — все значения корня \(n\)-й степени из \(z\).

495. Указание. Обозначив корни степени \(2n\) из 1 через \(\varepsilon_k = \cos \frac{k\pi}{n} + i \sin \frac{k\pi}{n}, k = 0, 1, 2, \ldots, 2n-1\), показать, что числа \(\varepsilon_k\)