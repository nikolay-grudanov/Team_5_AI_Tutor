---
source_image: page_129.png
page_number: 129
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.10
tokens: 6383
characters: 2237
timestamp: 2025-12-24T08:11:00.081568
finish_reason: stop
---

Задачи

6.1. Пусть \( A \) — вещественная матрица. Докажите, что \( \operatorname{rk} A^T A = \operatorname{rk} A \).

6.2. Пусть \( A \) — линейный оператор. Докажите, что
\[
\dim \operatorname{Ker} A^{n+1} = \dim \operatorname{Ker} A + \sum_{k=1}^n \dim (\operatorname{Im} A^k \cap \operatorname{Ker} A)
\]
и
\[
\dim \operatorname{Im} A = \dim \operatorname{Im} A^{n+1} + \sum_{k=1}^n \dim (\operatorname{Im} A^k \cap \operatorname{Ker} A).
\]

6.3. Докажите, что линейную функцию \( f \) можно представить в виде линейной комбинации линейных функций \( f_1, \ldots, f_k \) тогда и только тогда, когда \( \bigcap_{i=1}^k \operatorname{Ker} f_i \subset \operatorname{Ker} f \).

6.4. Пусть \( A : U \to V \) и \( B : V \to W \) — линейные отображения, для которых \( BA = 0 \). Тогда определено факторпространство \( \operatorname{Ker} B / \operatorname{Im} A \). Докажите, что \( \operatorname{Ker} A^* / \operatorname{Im} B^* \) — двойственное пространство для \( \operatorname{Ker} B / \operatorname{Im} A \).

§ 7. Базисы. Линейная независимость

7.1. Характеристический многочлен оператора

Различным объектам — линейным отображениям, квадратичным формам, кососимметрическим формам — можно сопоставить матрицу, выбрав предварительно базис. При переходе к другому базису эта матрица может измениться. Для наглядности мы, забегая несколько вперед, соберём вместе законы преобразований этих матриц при замене базиса.

Рассмотрим линейное отображение \( f : V \to W \). Пусть \( x \) — столбец \( (x_1, \ldots, x_n) \), \( e \) — строка \( (e_1, \ldots, e_n) \) и \( \varepsilon \) — строка \( (\varepsilon_1, \ldots, \varepsilon_m) \), причём строки \( e \) и \( \varepsilon \) составлены из базисных векторов. Тогда \( A \) будет матрицей отображения \( f \) относительно базисов \( e \) и \( \varepsilon \), если \( f(ex) = \varepsilon Ax \). Пусть \( e' = eP \) и \( \varepsilon' = \varepsilon Q \) — другие базисы. Тогда \( f(e'x) = f(ePx) = \varepsilon APx = \varepsilon' Q^{-1} APx \), поэтому \( A' = Q^{-1} AP \) — матрица отображения \( f \) относительно базисов \( e' \) и \( \varepsilon' \). Особенно важен тот случай, когда \( V = W \), т. е. \( f \) — линейный оператор, и \( P = Q \). В этом случае \( A' = P^{-1} AP \).