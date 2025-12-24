---
source_image: page_073.png
page_number: 73
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 67.33
tokens: 11948
characters: 2423
timestamp: 2025-12-24T08:28:10.747685
finish_reason: stop
---

11.5 Математические ожидания и дисперсии стандартных распределений

Пример 33. Распределение Бернулли \( \mathbf{B}_p \)

\[
\mathbb{E} \xi = 1 \cdot p + 0 \cdot q = p; \quad \mathbb{E} \xi^2 = 1^2 \cdot p + 0^2 \cdot q = p; \quad \mathrm{D} \xi = \mathbb{E} \xi^2 - (\mathbb{E} \xi)^2 = p - p^2 = pq.
\]

Пример 34. Биномиальное распределение \( \mathbf{B}_{n,p} \)

Воспользуемся свойством устойчивости биномиального распределения относительно суммирования — леммой 5.
Возьмем \( n \) независимых случайных величин \( \xi_1, \ldots, \xi_n \), имеющих распределение Бернулли \( \mathbf{B}_p = \mathbf{B}_{1,p} \).
Тогда их сумма \( S_n = \xi_1 + \ldots + \xi_n \) имеет распределение \( \mathbf{B}_{n,p} \).

\[
\mathbb{E} S_n = \sum_{i=1}^n \mathbb{E} \xi_i = n \mathbb{E} \xi_1 = np, \text{ так как все } \xi_i \text{ одинаково распределены и их математическое ожидание равно } p;
\]
\[
\mathrm{D} S_n = \sum_{i=1}^n \mathrm{D} \xi_i = n \mathrm{D} \xi_1 = npq, \text{ поскольку } \xi_i \text{ независимы и дисперсия каждой равна } pq.
\]

Пример 35. Геометрическое распределение \( \mathbf{G}_p \)

При \( p \in (0, 1) \)

\[
\mathbb{E} \xi = \sum_{k=1}^{\infty} k \cdot pq^{k-1} = p \cdot \sum_{k=1}^{\infty} kq^{k-1} = p \cdot \sum_{k=1}^{\infty} (q^k)' = p \cdot \left( \sum_{k=1}^{\infty} q^k \right)' = p \cdot \left( \sum_{k=0}^{\infty} q^k \right)' = p \cdot \left( \frac{1}{1-q} \right)' = p \left( \frac{1}{(1-q)^2} \right) = \frac{1}{p}.
\]

Равенство (*) появилось из-за нежелания дифференцировать сумму геометрической прогрессии, начинающейся не с 1, а с \( q \). Заметьте, что производная у добавленных слагаемых равна 0, так что производные от этих двух сумм равны.

\[
\mathbb{E} \xi^2 = \sum_{k=1}^{\infty} k^2 \cdot pq^{k-1} = p \cdot \sum_{k=1}^{\infty} k(k-1)q^{k-1} + p \cdot \sum_{k=1}^{\infty} kq^{k-1} = pq \cdot \sum_{k=1}^{\infty} k(k-1)q^{k-2} + \mathbb{E} \xi = pq \cdot \sum_{k=1}^{\infty} \frac{\partial^2}{\partial q^2} q^k + \mathbb{E} \xi =
\]
\[
= pq \cdot \left( \sum_{k=0}^{\infty} \frac{\partial^2}{\partial q^2} (q^k) \right) + \mathbb{E} \xi = pq \cdot \frac{\partial^2}{\partial q^2} \left( \frac{1}{1-q} \right) + \mathbb{E} \xi = 2pq \left( \frac{1}{(1-q)^3} \right) + \mathbb{E} \xi = \frac{2q}{p^2} + \frac{1}{p}.
\]

Поэтому

\[
\mathrm{D} \xi = \mathbb{E} \xi^2 - (\mathbb{E} \xi)^2 = \frac{2q}{p^2} + \frac{1}{p} - \frac{1}{p^2} = \frac{2q - 1 + p}{p^2} = \frac{q}{p^2}.
\]