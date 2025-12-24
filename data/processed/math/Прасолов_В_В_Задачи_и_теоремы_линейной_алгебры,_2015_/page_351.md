---
source_image: page_351.png
page_number: 351
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.70
tokens: 6962
characters: 3430
timestamp: 2025-12-24T08:17:21.770826
finish_reason: stop
---

Т = • \( \alpha_i u_1^i \otimes \ldots \otimes u_p^i + \ldots \); разложив элементы, обозначенные многоточием, по базису \( e_1, \ldots, e_n \), легко проверить, что любая их линейная комбинация, не равная нулю, не может лежать в \( T_0^p(U) \). А так как \( T \in T_0^p(U) \), то \( T = • \alpha_i u_1^i \otimes \ldots \otimes u_p^i \), т. е. ранг элемента \( T \) в \( T_0^p(U) \) не больше, чем в \( T_0^p(V) \). Обратное неравенство очевидно.

33.2. Пусть \( e_1^{\otimes p} + \ldots + e_k^{\otimes p} = u_1^1 \otimes \ldots \otimes u_p^1 + \ldots + u_1^r \otimes \ldots \otimes u_p^r \). Согласно задаче 33.1 можно считать, что \( u_j^i \in \langle e_1, \ldots e_k \rangle \). Тогда \( u_1^i = • \alpha_{ij} e_j \), т. е.

\[
• \prod_i u_1^i \otimes \ldots \otimes u_p^i = • \prod_j e_j \otimes (• \prod_i \alpha_{ij} u_2^i) \otimes \ldots \otimes u_p^i.
\]

Следовательно,

\[
• \prod_i \alpha_{ij} u_2^i \otimes \ldots \otimes u_p^i = e_j^{\otimes p-1},
\]

поэтому \( k \) линейно независимых тензоров \( e_1^{\otimes p-1}, \ldots, e_k^{\otimes p-1} \) лежат в пространстве \( \langle u_2^1 \otimes \ldots \otimes u_p^1, \ldots, u_2^r \otimes \ldots \otimes u_p^r \rangle \), размерность которого не превосходит \( r \). Следовательно, \( r \geq k \).

§ 34. Линейные отображения пространств матриц

34.1. Предположим, что \( AXB \equiv X^T \). Тогда матрицы \( A \) и \( B \) имеют размер \( n \times m \) и \( • a_{ik} x_{ks} b_{sj} \equiv x_{ji} \). Следовательно, \( a_{ij} b_{ij} = 1 \) и \( a_{ik} b_{sj} = 0 \), если \( k \neq j \) или \( s \neq i \).
Из первого набора равенств следует, что все элементы матриц \( A \) и \( B \) ненулевые, но тогда второй набор равенств выполняться не может.

34.2. Пусть \( B, X \in M_{n,n} \). Уравнение \( BX = \lambda X \) имеет ненулевое решение \( X \) тогда и только тогда, когда \( \lambda \) — собственное значение матрицы \( B \). Если \( \lambda \) — собственное значение матрицы \( B \), то \( BX = \lambda X \) для некоторой ненулевой матрицы \( X \). Поэтому \( f(B)f(X) = \lambda f(X) \), а значит, \( \lambda \) — собственное значение матрицы \( f(B) \). Пусть \( B = \operatorname{diag}(\beta_1, \ldots, \beta_n) \), где \( \beta_i \) — попарно различные ненулевые числа. Тогда матрица \( f(B) \) подобна \( B \), т. е. \( f(B) = A_1 B A_1^{-1} \).

Пусть \( g(X) = A_1^{-1} f(X) A_1 \). Тогда \( g(B) = B \). Если \( X = \| x_{ij} \|_1^n \), то \( BX = \| \beta_i x_{ij} \|_1^n \) и \( XB = \| x_{ij} \beta_j \|_1^n \). Поэтому \( BX = \beta_i X \), только если все строки матрицы \( X \), кроме \( i \)-й, нулевые, а \( XB = \beta_j X \), только если все столбцы матрицы \( X \), кроме \( j \)-го, нулевые. Пусть \( I_{ij} \) — матрица, единственный ненулевой элемент которой равен 1 и стоит в \( i \)-й строке и \( j \)-м столбце. Тогда \( Bg(I_{ij}) = \beta_i g(I_{ij}) \) и \( g(I_{ij}) B = \beta_j g(I_{ij}) \), а значит, \( g(I_{ij}) = \alpha_{ij} I_{ij} \). Легко проверить, что \( I_{ij} = I_{i1} I_{1j} \). Поэтому \( \alpha_{ij} = \alpha_{i1} \alpha_{1j} \). Кроме того, \( I_{ii}^2 = I_{ii} \), поэтому \( \alpha_{ii}^2 = \alpha_{ii} \), а значит, \( \alpha_{i1} \alpha_{1i} = 1 \), т. е. \( \alpha_{1i} = 1 / \alpha_{i1} \). Следовательно, \( \alpha_{ij} = \alpha_{i1} / \alpha_{1j} \). Поэтому \( g(X) = A_2 X A_2^{-1} \), где \( A_2 = \operatorname{diag}(\alpha_{11}, \ldots, \alpha_{n1}) \), а значит, \( f(X) = AXA^{-1} \), где \( A = A_1 A_2 \).