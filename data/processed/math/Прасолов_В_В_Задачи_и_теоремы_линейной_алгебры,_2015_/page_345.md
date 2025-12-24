---
source_image: page_345.png
page_number: 345
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.81
tokens: 6846
characters: 3127
timestamp: 2025-12-24T08:17:07.848038
finish_reason: stop
---

Решения

§ 29. Полилинейные отображения. Тензорные произведения

29.1. Дополним векторы v и w до базисов пространств V и W. Если \( v' \otimes w' = v \otimes w \), то разложения векторов \( v' \) и \( w' \) по этим базисам имеют вид \( \lambda v \) и \( \mu w \). Ясно также, что \( \lambda v \otimes \mu w = \lambda \mu (v \otimes w) \), т. е. \( \mu = 1/\lambda \).

29.2. а) Утверждение очевидным образом следует из определения.

б) Возьмём базисы пространств Im \( A_1 \) и Im \( A_2 \) и дополним их до базисов \( \{e_i\} \) и \( \{\varepsilon_j\} \) пространств \( W_1 \) и \( W_2 \). Пространство Im \( A_1 \otimes W_2 \) порождено векторами \( e_i \otimes \varepsilon_j \), где \( e_i \in \mathrm{Im}\, A_1 \), а пространство \( W_1 \otimes \mathrm{Im}\, A_2 \) порождено векторами \( e_i \otimes \varepsilon_j \), где \( \varepsilon_j \in \mathrm{Im}\, A_2 \). Поэтому пространство \( (\mathrm{Im}\, A_1 \otimes W_2) \cap (W_1 \otimes \mathrm{Im}\, A_2) \) порождено векторами \( e_i \otimes \varepsilon_j \), где \( e_i \in \mathrm{Im}\, A_1 \) и \( \varepsilon_j \in \mathrm{Im}\, A_2 \), т. е. это пространство совпадает с Im \( A_1 \otimes \mathrm{Im}\, A_2 \).

в) Возьмём базисы пространства Ker \( A_1 \) и Ker \( A_2 \) и дополним их до базисов \( \{e_i\} \) и \( \{\varepsilon_j\} \) пространств \( V_1 \) и \( V_2 \). Отображение \( A_1 \otimes A_2 \) переводит элемент \( e_i \otimes \varepsilon_j \) в нуль, если \( e_i \in \mathrm{Ker}\, A_1 \) или \( \varepsilon_j \in \mathrm{Ker}\, A_2 \); остальные элементы вида \( e_i \otimes \varepsilon_j \) это отображение переводит в базис пространства Im \( A_1 \otimes \mathrm{Im}\, A_2 \), т. е. в линейно независимые элементы.

29.3. Выберем в пространстве \( V_1 \cap V_2 \) базис \( \{v_i\} \) и дополним его до базисов \( \{v_j^1\} \) и \( \{v_k^2\} \) пространств \( V_1 \) и \( V_2 \). В результате получим базис \( \{v_i, v_j^1, v_k^2\} \) пространства \( V_1 + V_2 \). Аналогично построим базис \( \{w_\alpha, w_\beta^1, w_\gamma^2\} \) пространства \( W_1 + W_2 \). Тогда

\[
\{v_i \otimes w_\alpha, v_i \otimes w_\beta^1, v_j^1 \otimes w_\alpha, v_j^1 \otimes w_\beta^1\}
\]

и

\[
\{v_i \otimes w_\alpha, v_i \otimes w_\gamma^2, v_k^2 \otimes w_\alpha, v_k^2 \otimes w_\gamma^2\}
\]

— базисы пространств \( V_1 \otimes W_1 \) и \( V_2 \otimes W_2 \), причём элементы этих базисов содержатся в базисе пространства \( (V_1 + V_2) \otimes (W_1 + W_2) \), т. е. они в совокупности линейно независимы. Следовательно, \( \{v_i \otimes w_\alpha\} \) — базис пространства \( (V_1 \otimes W_1) \cap (V_2 \otimes W_2) \).

29.4. Пусть \( B : V \to V_1 \) и \( D : W \to W_2 \). Достаточно проверить, что указанные операторы одинаково действуют на тензоры вида \( v \otimes w \), где \( v \in V \) и \( w \in W \). Ясно, что

\[
(A \otimes C)(B \otimes D)(v \otimes w) = (A \otimes C)(Bv \otimes Dw) =
= (ABv \otimes CDw) = ((AB) \otimes (CD))(v \otimes w).
\]

29.5. Требуется доказать, что \( a_{ij} B = a_{ji} B^T \). Для симметрических матриц это очевидно, а для кососимметрических матриц это следует из того, что \( a_{ij} = -a_{ji} \) и \( B^T = -B \).