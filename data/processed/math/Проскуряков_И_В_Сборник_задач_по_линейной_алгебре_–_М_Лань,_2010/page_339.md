---
source_image: page_339.png
page_number: 339
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.14
tokens: 5825
characters: 2693
timestamp: 2025-12-24T07:13:23.457529
finish_reason: stop
---

343. \((-1)^{n-1} \prod_{i=1}^n x_i \prod_{n \geq i > k \geq 1} (x_i - x_k) \left[ \sum_{i=1}^n \frac{a_i}{x_i f'(x_i)} \right],\) где \(f(x) = (x-x_1)(x-x_2)\ldots(x-x_n)\).
Указание. Разложить определитель по первому столбцу.

344. \((x_1 + x_2 + \cdots + x_n) \prod_{n \geq i > k \geq 1} (x_i - x_k)\).
Указание. Определитель

\[
\begin{vmatrix}
1 & x_1 & x_1^2 & \ldots & x_1^n \\
1 & x_2 & x_2^2 & \ldots & x_2^n \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
1 & x_n & x_n^2 & \ldots & x_n^n \\
1 & z & z^2 & \ldots & z^n
\end{vmatrix}
\]

вычислить двумя способами: разложением по последней строке и как определитель Вандермонда. В обоих выражениях приравнять коэффициенты при \(z^{n-1}\).

345. \(x_1 x_2 \ldots x_n \left( \frac{1}{x_1} + \frac{1}{x_2} + \cdots + \frac{1}{x_n} \right) \prod_{n \geq i > k \geq 1} (x_i - x_k)\).

346. \(\left( \sum x_{\alpha_1} x_{\alpha_2} \ldots x_{\alpha_{n-s}} \right) \prod_{n \geq i > k \geq 1} (x_i - x_k)\), где сумма берется по всем сочетаниям \(n-s\) чисел \(\alpha_1, \alpha_2, \ldots, \alpha_{n-s}\) из чисел 1, 2, ..., \(n\).

347. \([x_1 x_2 \ldots x_n - (x_1-1)(x_2-1) \ldots (x_n-1)] \prod_{n \geq i > k \geq 1} (x_i - x_k)\).
Указание. \(i\)-й элемент 1-го столбца представить в виде \(1 = x_i - (x_1-1)\) и представить определитель в виде разности двух определителей.

348. \([2x_1 x_2 \ldots x_n - (x_1-1)(x_2-1) \ldots (x_n-1)] \prod_{n \geq i > k \geq 1} (x_i - x_k)\).
Указание. Приписать первую строку 1, 0, 0, ..., 0 и первый столбец из единиц, первый столбец вычесть из остальных, единицу в левом верхнем углу представить в виде 2 - 1 и представить определитель в виде разности двух определителей относительно первой строки.

349. \(2^{n-1} \prod_{1 \leq i < k \leq n} \sin \frac{\varphi_i + \varphi_k}{2} \cdot \sin \frac{\varphi_i - \varphi_k}{2}\).
Указание. Воспользоваться тем, что \(\cos k \varphi\) выражается через \(\cos \varphi\) в виде многочлена со старшим членом \(2^{k-1} \cos^k \varphi\) (это можно вывести из формулы Муавра и равенства \(1 + C_k^2 + C_k^4 + \cdots = 2^{k-1}\)).

350. \(2^{n(n-1)} \sin \varphi_1 \sin \varphi_2 \ldots \sin \varphi_n \prod_{1 \leq i < k \leq n} \left( \sin \frac{\varphi_i + \varphi_k}{2} \cdot \sin \frac{\varphi_i - \varphi_k}{2} \right)\).
Указание. Доказать, что \(\sin k \varphi\) можно представить в виде произведения \(\sin \varphi\) на многочлен от \(\cos \varphi\) со старшим членом \(2^{k-1} \cos^{k-1} \varphi\).

351. \((a+b+c+d)(a+b-c-d)(a-b+c-d)(a-b-c+d)\).
Указание. Воспользоваться методом выделения линейных множителей.

352. \((a+b+c+d+e+f+g+h)(a+b+c+d-e-f-g-h) \times (a+b-c-d+e+f-g-h)(a+b-c-d-e-f+g+h)(a-b+c-d+e-f+g-h)(a-b-c+d+e-f-g+h)(a-b-c+d-e+f+g-h).\)