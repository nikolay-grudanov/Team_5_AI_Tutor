---
source_image: page_334.png
page_number: 334
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.97
tokens: 6322
characters: 2112
timestamp: 2025-12-24T08:16:40.893800
finish_reason: stop
---

32.8. Сопоставим подпространству \( \Lambda \subset \Lambda^k V \) подпространство \( \Lambda^\perp = = \{ v^* \mid i(v^*)\Lambda = 0 \} \) в \( V^* \). Докажите, что \( W = (\Lambda^\perp)^\perp \) является минимальным подпространством в \( V \), для которого \( \Lambda \) лежит в подпространстве \( \Lambda^k W \subset \Lambda^k V \).

§ 33. Тензорный ранг

33.1. Тензорный ранг в \( V \otimes W \)

Пространство \( V \otimes W \) состоит из линейных комбинаций элементов \( v \otimes w \), но не любой элемент этого пространства можно представить в виде \( v \otimes w \). Рангом элемента \( T \in V \otimes W \) называют наименьшее число \( k \), для которого \( T = v_1 \otimes w_1 + \ldots + v_k \otimes w_k \); ранг элемента \( T \) обозначим \( \operatorname{rk} T \).

Теорема 33.1.1. Если \( T = \bullet a_{ij} e_i \otimes \varepsilon_j \), где \( \{e_i\} \) и \( \{\varepsilon_i\} \) — базисы пространств \( V \) и \( W \), то \( \operatorname{rk} T = \operatorname{rk} \|a_{ij}\| \).

Доказательство. Пусть

\[
v_p = \bullet \alpha_i^p e_i, \quad w_p = \bullet \beta_i^p \varepsilon_j,
\]

\( \alpha^p \) — столбец \( (\alpha_1^p, \ldots, \alpha_n^p) \) и \( \beta^p \) — строка \( (\beta_1^p, \ldots, \beta_m^p) \). Тогда \( \|a_{ij}\| = = \alpha^1 \beta^1 + \ldots + \alpha^k \beta^k \). Наименьшее число \( k \), для которого возможно такое разложение матрицы \( \|a_{ij}\| \), равно рангу этой матрицы (см. п. 8.2).

Следствие 1. Множество \( \{ T \in V \otimes W \mid \operatorname{rk} T \leq k \} \) замкнуто; в частности, если \( \lim_{i \to \infty} T_i = T \) и \( \operatorname{rk} T_i \leq k \), то \( \operatorname{rk} T \leq k \).

Замкнутость является следствием того, что это множество задаётся алгебраическими уравнениями.

Следствие 2. Ранг элемента вещественного пространства \( V \otimes W \) не изменяется при переходе к комплексификации.

Для элемента \( T \in V_1 \otimes \ldots \otimes V_p \) ранг можно определить аналогичным образом, т. е. как наименьшее число \( k \), для которого

\[
T = v_1^1 \otimes \ldots \otimes v_p^1 + \ldots + v_1^k \otimes \ldots \otimes v_p^k.
\]