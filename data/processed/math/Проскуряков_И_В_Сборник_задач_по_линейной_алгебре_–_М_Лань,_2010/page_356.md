---
source_image: page_356.png
page_number: 356
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.23
tokens: 5793
characters: 2527
timestamp: 2025-12-24T07:13:50.797968
finish_reason: stop
---

529. Указание. При доказательстве утверждения 2) показать, что вектор \( \mathbf{a}_i = (a_{i1}, a_{i2}, \ldots, a_{in}) \) можно представить в виде \( \mathbf{a}_{ii} = a_{i1}e_1 + a_{i2}e_2 + \cdots + a_{in}e_n \). Далее показать, что при перестановке двух векторов функция \( f(\mathbf{a}_1, \mathbf{a}_2, \ldots, \mathbf{a}_n) \) меняет знак. При доказательстве этого, например, для векторов \( \mathbf{a}_1, \mathbf{a}_2, \) рассмотреть \( f(\mathbf{a}_1 + \mathbf{a}_2, \mathbf{a}_1 + \mathbf{a}_2, \mathbf{a}_3, \ldots, \mathbf{a}_n) \).

530. Указание. Доказать, что функция \( f(\mathbf{a}_1, \mathbf{a}_2, \ldots, \mathbf{a}_n) = |AB| \) от строк матрицы \( A \) обладает свойствами (\( \alpha \)) и (\( \beta \)) и что \( f(e_1, e_2, \ldots, e_n) = |B| \).

531. Положим \( f(e_{i_1}, e_{i_2}, \ldots, e_{i_n}) = 1 \) при любых \( i_1, i_2, \ldots, i_n = 1, 2, \ldots, n \) (одинаковых или различных). В силу (\( \alpha \)), полагая \( \mathbf{a}_i = \sum_{j=1}^n a_{ij}e_j \), получим

\[
f(\mathbf{a}_1, \mathbf{a}_2, \ldots, \mathbf{a}_n) = \sum_{i_1, i_2, \ldots, i_n = 1}^n a_{1,i_1} a_{2,i_2} \ldots a_{n,i_n}.
\]

Этим функция \( f(\mathbf{a}_1, \mathbf{a}_2, \ldots, \mathbf{a}_n) \) определена. Очевидно, она при перестановке векторов не меняется, т. е. в случае поля характеристики 2 меняет знак. Поэтому (\( \beta' \)) выполнено, а (\( \beta \)), очевидно, не выполняется.

532. \( (-1)^{C_n^2 C_{n-1}^2} n^{n/2} = i^{(n-1)(3n-2)/2} n^{n/2} \).

Решение. Умножая данный определитель \( D \) сам на себя и замечая, что \( \varepsilon^k = 1 \) тогда и только тогда, когда \( k \) делится на \( n \), получим

\[
D^2 = \begin{vmatrix}
n & 0 & \ldots & 0 & 0 \\
0 & 0 & \ldots & 0 & n \\
0 & 0 & \ldots & n & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
0 & n & \ldots & 0 & 0
\end{vmatrix} = (-1)^{C_{n-1}^2} n^n,
\]

откуда \( D = \pm i^{C_{n-1}^2} n^{n/2} \) и для модуля \( D \) находим: \( |D| = n^{n/2} \). Остается определить аргумент. Вычисляя \( D \) как определитель Вандермонда чисел \( 1, \varepsilon, \varepsilon^2, \ldots, \varepsilon^{n-1} \) и полагая затем \( \varepsilon = \alpha^2 \), где \( \alpha = \cos \frac{\pi}{n} + i \sin \frac{\pi}{n} \), получим

\[
D = \prod_{0 \leq j < k \leq n-1} (\varepsilon^k - \varepsilon^j) = \prod_{0 \leq j < k \leq n-1} (\alpha^{2k} - \alpha^{2j}) =
\]
\[
= \prod_{0 \leq j < k \leq n-1} \alpha^{k+j} (\alpha^{k-j} - \alpha^{-(k-j)}) =
\]
\[
= \prod_{0 \leq j < k \leq n-1} \alpha^{j+k} \prod_{0 \leq j < k \leq n-1} 2i \sin \frac{(k-j)\pi}{n}.
\]