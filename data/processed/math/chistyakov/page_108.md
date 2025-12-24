---
source_image: page_108.png
page_number: 108
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.98
tokens: 8810
characters: 1692
timestamp: 2025-12-24T07:28:41.962680
finish_reason: stop
---

М\(\xi_1 = 1 - 2 \ln 2\). Однако \(M_{\xi_2}\) по определению не существует, так как ряд \(\sum_{k=1}^{\infty} |(-1)^k k| \cdot \frac{1}{k(k+1)}\) расходится.

Пример 3. Пусть в абсолютно непрерывном вероятностном пространстве \((\Omega, \mathcal{F}, P)\) (§ 6 гл. 1)
\[
\Omega = \{(u, v): u^2 + v^2 \leq 9\}, \quad \pi(u, v) = \frac{1}{9\pi}, \quad (u, v) \in \Omega.
\]
Рассмотрим случайные величины: \(\xi_1 = \sqrt{u^2 + v^2}, \xi_2 = k\), если \(k-1 \leq \sqrt{u^2 + v^2} < k, k = 1, 2, 3;\)
\[
\xi_3 = \xi_3(u, v) = \begin{cases}
\sqrt{u^2 + v^2}, & \text{если } \sqrt{u^2 + v^2} < 1, \\
1, & \text{если } \sqrt{u^2 + v^2} \geq 1.
\end{cases}
\]
По формуле (1.5) находим
\[
M_{\xi_k} = \iint_{\Omega} \xi_k(u, v) \frac{1}{9\pi} du dv.
\]
При вычислении этого интеграла естественно перейти к полярным координатам: \(u = \rho \cos \varphi, v = \rho \sin \varphi\). Тогда
\[
M_{\xi_k} = \iint_{\Omega} \xi_k(\rho \cos \varphi, \rho \sin \varphi) \frac{\rho}{9\pi} d\rho d\varphi.
\]
Отсюда
\[
M_{\xi_1} = \iint_{\Omega} \frac{\rho^2}{9\pi} d\rho d\varphi = \frac{2}{9} \int_0^3 \rho^2 d\rho = \frac{2}{9} \cdot \frac{\rho^3}{3} \Bigg|_0^3 = 2,
\]
\[
M_{\xi_2} = \frac{1}{9\pi} \int_0^{2\pi} d\varphi \left( \int_0^1 \rho d\rho + \int_1^2 2\rho d\rho + \int_2^3 3\rho d\rho \right) = \frac{22}{9},
\]
\[
M_{\xi_3} = \frac{1}{9\pi} \int_0^{2\pi} d\varphi \left( \int_0^1 \rho^2 d\rho + \int_1^3 \rho d\rho \right) = \frac{26}{27}.
\]
Отметим, что в данном примере величина \(\xi_1\) абсолютно непрерывна, \(\xi_2\) — дискретна, а \(\xi_3\) — смешанного типа. Действительно,
\[
F_{\xi_1}(x) = P(\xi_1 < x) = \iint_{u^2 + v^2 < x^2} \frac{1}{9\pi} du dv = \frac{x^2}{9}, \quad x \in [0, 3],
\]