---
source_image: page_310.png
page_number: 310
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.50
tokens: 6456
characters: 2193
timestamp: 2025-12-24T08:15:56.862807
finish_reason: stop
---

Доказательство. Уравнение \((I \otimes A - B^T \otimes I)X = \lambda X\) имеет ненулевое решение тогда и только тогда, когда \(\lambda\) — собственное значение оператора \(I \otimes A - B^T \otimes I\), т. е. \(\lambda = \alpha_i - \beta_j\).

29.7. Подпространство, соответствующее полилинейной функции

Полилинейной функции \(f \in \mathrm{Hom}(V \times \ldots \times V, K) \cong (V^*)^{\otimes p}\) можно сопоставить подпространство \(W_f \subset V^*\), порождённое ковекторами \(\xi\) вида \(\xi(x) = f(a_1, \ldots, a_{i-1}, x, a_i, \ldots, a_{p-1})\), где векторы \(a_i, \ldots, a_{p-1}\) и число \(i\) фиксированы.

Теорема 29.7.1. Полилинейная функция \(f\) лежит в подпространстве \(W_f^{\otimes p}\).

Доказательство. Пусть \(\varepsilon_1, \ldots, \varepsilon_r\) — базис \(W_f\); дополним его до базиса \(\varepsilon_1, \ldots, \varepsilon_n\) пространства \(V^*\). Требуется доказать, что
\[
f = \bullet\ f_{i_1 \ldots i_p} \varepsilon_{i_1} \otimes \ldots \otimes \varepsilon_{i_p},
\]
где \(f_{i_1 \ldots i_p} = 0\), когда один из индексов \(i_1, \ldots, i_p\) больше \(r\). Пусть \(e_1, \ldots, e_n\) — базис, двойственный к \(\varepsilon_1, \ldots, \varepsilon_n\). Так как
\[
f(a_1, \ldots, x, \ldots, a_{p-1}) = \bullet\ \alpha_i \varepsilon_i(x),
\]
то \(f(e_{j_1}, \ldots, e_{j_p}) = 0\), если хотя бы одно из чисел \(j_1, \ldots, j_p\) больше \(r\); кроме того, \(\varepsilon_{i_1} \otimes \ldots \otimes \varepsilon_{i_p}(e_{j_1}, \ldots, e_{j_p}) = 1\), если \(i_1 = j_1, \ldots, i_p = j_p\), а во всех остальных случаях эта величина равна нулю.

Теорема 29.7.2. Если ковекторы \(\varepsilon_1, \ldots, \varepsilon_r\) таковы, что
\[
f = \bullet\ f_{i_1 \ldots i_p} \varepsilon_{i_1} \otimes \ldots \otimes \varepsilon_{i_p},
\]
то \(W_f \subset \langle \varepsilon_1, \ldots, \varepsilon_r \rangle\).

Доказательство. Ясно, что
\[
f(a_1, \ldots, a_{k-1}, x, a_k, \ldots, a_{p-1}) =
= \bullet\ f_{i_1 \ldots i_p} \varepsilon_{i_1}(a_1) \ldots \varepsilon_{i_k}(x) \ldots \varepsilon_{i_p}(a_{p-1}) = \bullet\ c_s \varepsilon_s(x).
\]

Задачи

29.1. Докажите, что \(v \otimes w = v' \otimes w' \neq 0\) тогда и только тогда, когда \(v = \lambda v'\) и \(w' = \lambda w\).