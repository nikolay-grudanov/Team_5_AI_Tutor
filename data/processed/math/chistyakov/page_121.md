---
source_image: page_121.png
page_number: 121
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.17
tokens: 5446
characters: 1937
timestamp: 2025-12-24T07:29:02.007240
finish_reason: stop
---

можно воспользоваться формулой

\[
M \eta_n = M \xi_1 + M \xi_2 + \ldots + M \xi_n.
\]

Однако \( D \eta_n \) уже не равна сумме дисперсий \( D \xi_k \). Для вычисления \( D \eta_n \) можно использовать формулу (3.2). Так как \( \xi_k^2(\omega) = \xi_k(\omega), \omega \in \Omega \) (действительно \( \xi_k(\omega) = 1 \) или \( \xi_k(\omega) = 0 \)), то

\[
\eta_n^2 = \sum_{k=1}^n \xi_k^2 + \sum_{k \neq l} \xi_k \xi_l = \sum_{k=1}^n \xi_k + \sum_{k \neq l} \xi_k \xi_l = \eta_n + \sum_{k \neq l} \xi_k \xi_l.
\]

Таким образом,

\[
D \eta_n = M \eta_n^2 - (M \eta_n)^2 = \sum_{k \neq l} M \xi_k \xi_l + M \eta_n - (M \eta_n)^2.
\]

Суммой вида (3.8) является, например, случайная величина в задаче 7, стр. 128.

§ 4. Ковариация. Коэффициент корреляции

При доказательстве формулы (3.5) нам потребовалось вычислить \( M[(\xi_1 - M \xi_1)(\xi_2 - M \xi_2)] \). Это число называется ковариацией случайных величин \( \xi_1, \xi_2 \) и обозначается \( \operatorname{cov}(\xi_1, \xi_2) \). Таким образом,

\[
\operatorname{cov}(\xi_1, \xi_2) = M[(\xi_1 - M \xi_1)(\xi_2 - M \xi_2)]. \tag{4.1}
\]

Отсюда, используя свойства математического ожидания, легко получить следующую формулу:

\[
\operatorname{cov}(\xi_1, \xi_2) = M \xi_1 \xi_2 - M \xi_1 \cdot M \xi_2. \tag{4.2}
\]

Очевидно, что

\[
\operatorname{cov}(\xi, \xi) = D \xi, \quad \operatorname{cov}(\xi_1, \xi_2) = \operatorname{cov}(\xi_2, \xi_1).
\]

Из (3.6) и (4.1) следует формула для дисперсии суммы двух произвольных (не обязательно зависимых) случайных величин:

\[
D(\xi_1 + \xi_2) = D \xi_1 + D \xi_2 + 2 \operatorname{cov}(\xi_1, \xi_2). \tag{4.3}
\]

Теорема 4.1. Если для случайных величин \( \xi_1, \xi_2, \ldots, \xi_n \) существуют \( \operatorname{cov}(\xi_i, \xi_j) = \sigma_{ij}, i, j = 1, \ldots, n \), то при любых постоянных \( c_1, c_2, \ldots, c_n \) имеем

\[
D(c_1 \xi_1 + c_2 \xi_2 + \ldots + c_n \xi_n) = \sum_{i, j=1}^n \sigma_{ij} c_i c_j. \tag{4.4}
\]