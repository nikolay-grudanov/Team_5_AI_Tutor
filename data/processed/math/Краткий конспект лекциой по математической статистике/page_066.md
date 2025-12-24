---
source_image: page_066.png
page_number: 66
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.05
tokens: 12691
characters: 3539
timestamp: 2025-12-24T07:05:14.998003
finish_reason: stop
---

Замечание 33. Нижне символом \( D\vec{\varepsilon} = \mathbb{E}(\vec{\varepsilon}\vec{\varepsilon}^T) \) обозначена матрица ковариаций вектора \( \vec{\varepsilon} \), т.е. матрица, \((i, j)\)-й элемент которой равен

\[
\operatorname{cov}(\varepsilon_i, \varepsilon_j) = \mathbb{E}(\varepsilon_i - \mathbb{E}\varepsilon_i)(\varepsilon_j - \mathbb{E}\varepsilon_j) = \begin{cases}
0, & i \neq j \\
\sigma^2, & i = j
\end{cases}.
\]

Для произвольного случайного вектора \( \vec{x} \), координаты которого имеют вторые моменты, \( D\vec{x} = \mathbb{E}\left( (\vec{x} - \mathbb{E}\vec{x})(\vec{x} - \mathbb{E}\vec{x})^T \right) \) — матрица, \((i, j)\)-й элемент которой равен

\[
\operatorname{cov}(\vec{x}_i, \vec{x}_j) = \mathbb{E}(\vec{x}_i - \mathbb{E}\vec{x}_i)(\vec{x}_j - \mathbb{E}\vec{x}_j).
\]

2. \( \hat{\beta} \) — несмещенная оценка для \( \vec{\beta} \):

\[
\mathbb{E}\hat{\beta} = \vec{\beta} + A^{-1}Z\mathbb{E}\vec{\varepsilon} \equiv \vec{\beta}.
\]

3. Матрица ковариаций вектора \( \hat{\beta} \):

\[
D\hat{\beta} = \mathbb{E}(\hat{\beta} - \mathbb{E}\hat{\beta})(\hat{\beta} - \mathbb{E}\hat{\beta})^T = \mathbb{E}(\hat{\beta} - \vec{\beta})(\hat{\beta} - \vec{\beta})^T =
\]
\[
\mathbb{E}(A^{-1}Z\vec{\varepsilon})(A^{-1}Z\vec{\varepsilon})^T = \mathbb{E}(A^{-1}Z\vec{\varepsilon}\vec{\varepsilon}^T Z^T A^{-1}{}^T)
\]

И так как \( A = ZZ^T, A^T = A, \mathbb{E}\vec{\varepsilon}\vec{\varepsilon}^T = \sigma^2 E \), где \( E \) — единичная матрица, имеем:

\[
D\hat{\beta} = \sigma^2 (A^{-1}ZZ^T A^{-1}{}^T) = \sigma^2 A^{-1}.
\]

9.6 Оптимальный выбор матрицы плана

Как и в теории точечного оценивания, о качестве несмещенной оценки \( \hat{\beta} \) для вектора \( \vec{\beta} \) можно судить по величине ее «среднего квадратического отклонения», которое в многомерном случае описывают величиной \( D\hat{\beta} = \mathbb{E}(\hat{\beta} - \vec{\beta})(\hat{\beta} - \vec{\beta})^T \).

Если мы управляем экспериментом, т.е. можем сами задавать значения факторов \( Z_1, \ldots, Z_k \) (матрицу плана) и наблюдать затем результаты \( n \) экспериментов \( X_1, \ldots, X_n \), то разумно задаться вопросом: как зависит \( D\hat{\beta} \) от выбора матрицы плана \( Z \)?

Введем следующее ограничение:

Предположение 3. Пусть \( a_1, \ldots, a_k \) — ненулевые фиксированные числа. Будем рассматривать матрицы плана \( Z \), у которых

\[
\sum_{i=1}^n (Z_j^{(i)})^2 = a_j, \quad j = 1, \ldots, k.
\]

Замечание 34. Мы доказали, что \( D\hat{\beta} = \sigma^2 A^{-1} \) — матрица ковариаций вектора \( \hat{\beta} \). Ее диагональные элементы равны \( D\hat{\beta}_j = \sigma^2 (A^{-1})_{jj} \). Если не требовать выполнения Предположения 3, то заменой \( Z \) на \( cZ \) можно добиться, что \( A^{-1} \) заменится на \( \frac{1}{c^2} A^{-1} \) и вместо \( D\hat{\beta}_j = \sigma^2 (A^{-1})_{jj} \) получится \( D\hat{\beta}_j = \frac{1}{c^2} \sigma^2 (A^{-1})_{jj} \). (А получится ли? Что-то тут не так! :-))***

Следующая теорема может быть доказана из свойств матрицы \( A \) (рекомендую попытаться доказать):

Теорема 18. Предположение 3 \( \implies \) \( D\hat{\beta}_j \geq \frac{\sigma^2}{a_j^2} \) для любого \( j = 1, \ldots, k \). В неравенстве достигается равенство если (и только если) строки матрицы \( Z \) ортогональны, т.е.

\[
\sum_{i=1}^n Z_l^{(i)} Z_j^{(i)} = 0 \quad \forall \quad l \neq j.
\]

Следствие 6. Если строки матрицы \( Z \) ортогональны, то матрица \( A \) имеет диагональный вид, и \( (A)_{jj} = a_j^2 \). Это означает, что координаты вектора \( \hat{\beta} \) некоррелированы.