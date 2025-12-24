---
source_image: page_095.png
page_number: 95
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 71.31
tokens: 12124
characters: 2990
timestamp: 2025-12-24T08:29:13.790953
finish_reason: stop
---

Поскольку \( \mathbf{D} \xi_1 = 1/2 \cdot 1/2 = 1/4 \), искомая оценка сверху выглядит так:

\[
\mathbf{P} \left( \left| \frac{S_n}{n} - \frac{1}{2} \right| > 0,01 \right) \leqslant \frac{\mathbf{D} \xi_1}{n \cdot 0,01^2} = \frac{1}{4 \cdot 10^4 \cdot 10^{-4}} = \frac{1}{4}.
\]

Иначе говоря, неравенство Чебышёва позволяет заключить, что, в среднем, не более чем в четверти случаев при 10 000 подбрасываниях монеты частота выпадения герба будет отличаться от 1/2 более чем на одну сотую. Мы увидим, насколько это грубая оценка, когда познакомимся с центральной предельной теоремой.

**Пример 49.**

*Задача.* Пусть \( \xi_1, \xi_2, \ldots \) — последовательность случайных величин, дисперсии которых ограничены одной и той же постоянной \( C \), а ковариации любых с. в. \( \xi_i \) и \( \xi_j \) (\( i \neq j \)), не являющихся соседними в последовательности, равны нулю. Удовлетворяет ли эта последовательность ЗБЧ?

*Решение.* Воспользуемся неравенством (23) и свойством 14:

\[
\mathbf{P} \left( \left| \frac{S_n}{n} - \mathbf{E} \left( \frac{S_n}{n} \right) \right| > \varepsilon \right) \leqslant \frac{\mathbf{D} \left( \frac{S_n}{n} \right)}{\varepsilon^2} = \frac{\mathbf{D} S_n}{n^2 \varepsilon^2}; \quad \mathbf{D} (\xi_1 + \ldots + \xi_n) = \sum_{i=1}^n \mathbf{D} \xi_i + 2 \sum_{i<j} \operatorname{cov}(\xi_i, \xi_j).
\]

Но для \( i < j \), по условию, \( \operatorname{cov}(\xi_i, \xi_j) = 0 \), если \( i \neq j-1 \). Следовательно, в сумме \( \sum_{i<j} \operatorname{cov}(\xi_i, \xi_j) \) равны нулю все слагаемые кроме, может быть, \( \operatorname{cov}(\xi_1, \xi_2), \operatorname{cov}(\xi_2, \xi_3), \ldots, \operatorname{cov}(\xi_{n-1}, \xi_n) \) (их ровно \( n-1 \) штука).

Оценим каждое из них, используя одно из свойств коэффициента корреляции (*какое?*)

\[
\operatorname{cov}(\xi_i, \xi_j) \leqslant \sqrt{\mathbf{D} \xi_i} \sqrt{\mathbf{D} \xi_j} \leqslant \sqrt{C} \sqrt{C} = C,
\]

так как для любого \( 1 \leqslant i \leqslant n \), по условию, \( \mathbf{D} \xi_i \leqslant C \). Итак,

\[
\mathbf{P} \left( \left| \frac{S_n}{n} - \mathbf{E} \left( \frac{S_n}{n} \right) \right| > \varepsilon \right) \leqslant \frac{\mathbf{D} S_n}{n^2 \varepsilon^2} = \frac{\sum_{i=1}^n \mathbf{D} \xi_i + 2 \sum_{i<j} \operatorname{cov}(\xi_i, \xi_j)}{n^2 \varepsilon^2} = \frac{\sum_{i=1}^n \mathbf{D} \xi_i + 2 \sum_{i=1}^{n-1} \operatorname{cov}(\xi_i, \xi_{i+1})}{n^2 \varepsilon^2} \leqslant \frac{nC + 2(n-1)C}{n^2 \varepsilon^2} \to 0
\]

при \( n \to \infty \), то есть последовательность \( \xi_1, \xi_2, \ldots \) удовлетворяет ЗБЧ.

**Упражнение 27.**
Привести пример последовательности с. в. \( \xi_1, \xi_2, \ldots \) такой, что ковариации «несоседних» величин равны нулю.
Привести пример последовательности с. в. \( \xi_1, \xi_2, \ldots \) такой, что ковариации «несоседних» величин равны нулю, а ковариации соседних — не равны. Можно попробовать построить такую последовательность с помощью другой последовательности, составленной из независимых с. в.