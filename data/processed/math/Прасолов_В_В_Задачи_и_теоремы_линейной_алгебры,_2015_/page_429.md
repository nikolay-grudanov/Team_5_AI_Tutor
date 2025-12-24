---
source_image: page_429.png
page_number: 429
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.53
tokens: 6651
characters: 2431
timestamp: 2025-12-24T08:19:27.060708
finish_reason: stop
---

43.9. а) Если \( \operatorname{tr} Z = 0 \), то \( Z = [X, Y] \) (см. п. 43.2), поэтому \( \operatorname{tr}(AZ) = \operatorname{tr}(AXY) - \operatorname{tr}(AYX) = 0 \). Следовательно, \( A = \lambda I \) (см. задачу 5.1).

б) Для любой линейной функции \( f \) на пространстве матриц существует такая матрица \( A \), что \( f(X) = \operatorname{tr}(AX) \). А так как \( f(XY) = f(YX) \), то \( \operatorname{tr}(AXY) = \operatorname{tr}(AYX) \). Следовательно, \( A = \lambda I \).

§ 44. Теория реплик

44.1. Ясно, что оператор \( B = \lambda A \) является репликой \( A \). Докажем, что для нильпотентного оператора \( A \) любая реплика имеет вид \( \lambda A \). Выберем натуральное число \( r \) так, что \( A^{r-1} \neq 0 \) и \( A^r = 0 \). Тогда матрицы \( A^k, 0 \leq k \leq r-1 \), линейно независимы и матрицы \( A^i \otimes A^j, 0 \leq i, j \leq r-1 \), тоже линейно независимы.

Поскольку \( A_{2,0} = A \otimes I + I \otimes A \) и \( A^r = 0 \), получаем

\[
A_{2,0}^m = \sum_{i=0}^m \binom{m}{i} A^i \otimes A^{m-i} =
\begin{cases}
\sum_{i=0}^m \binom{m}{i} A^i \otimes A^{m-i} & \text{при } m < r; \\
\sum_{i=m-r+1}^{r-1} \binom{m}{i} A^i \otimes A^{m-i} & \text{при } r \leq m \leq 2r-2; \\
0 & \text{при } m \geq 2r-1.
\end{cases}
\]

Если \( A \Rightarrow B \), то \( A_{2,0} \Rightarrow B_{2,0} \), поэтому согласно теореме 44.1.1

\[
B = \alpha_1 A + \alpha_2 A^2 + \ldots + \alpha_{r-1} A^{r-1}, \tag{1}
\]
\[
B_{2,0} = \beta_1 A_{2,0} + \beta_2 A_{2,0}^2 + \ldots + \beta_{2r-2} A_{2,0}^{2r-2}. \tag{2}
\]

Из равенства (1) следует, что

\[
B_{2,0} = B \otimes I + I \otimes B = \sum_{i=1}^{r-1} \alpha_i (A^i \otimes I + I \otimes A^i).
\]

С другой стороны, если мы подставим выражение для \( A_{2,0}^m \) в (2), то получим

\[
B_{2,0} = \sum_{m=1}^{r-1} \beta_m \left( \sum_{i=1}^m \binom{m}{i} A^i \otimes A^{m-i} \right) + \sum_{m=r}^{2r-2} \beta_m \left( \sum_{i=m-r+1}^{r-1} \binom{m}{i} A^i \otimes A^{m-i} \right).
\]

Сравнивая эти два выражения для \( B_{2,0} \), получаем

\[
\alpha_1 = \beta_1, \quad \ldots, \quad \alpha_{r-1} = \beta_{r-1}, \quad \beta_r = 0, \quad \ldots, \quad \beta_{2r-2} = 0.
\]

Более того, если \( \beta_m \neq 0 \) для некоторого \( m \geq 2 \), то мы получаем равенства \( \binom{m}{1} = \ldots = \binom{m}{m-1} = 0 \), чего не может быть, так как \( \binom{m}{1} = m \). Следовательно, \( \alpha_m = \beta_m = 0 \) при \( m \geq 2 \), т. е. \( B = \alpha_1 A \).