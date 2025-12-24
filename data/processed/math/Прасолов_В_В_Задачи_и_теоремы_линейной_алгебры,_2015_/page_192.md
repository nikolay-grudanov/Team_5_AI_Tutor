---
source_image: page_192.png
page_number: 192
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.14
tokens: 6556
characters: 2544
timestamp: 2025-12-24T08:12:49.695694
finish_reason: stop
---

Значит, согласно задаче 5.10 отношение ориентированного объёма симплекса \( A_0A_1\ldots A_{r-1}B_rB_{r+1}\ldots B_n \) к объёму исходного симплекса равно

\[
\begin{vmatrix}
0 & -\frac{x_{r+1}}{x_r} & \ldots & -\frac{x_n}{x_r} \\
-\frac{x_r}{x_{r+1}} & 0 & \ldots & -\frac{x_n}{x_{r+1}} \\
\ldots & \ldots & \ldots & \ldots \\
-\frac{x_r}{x_n} & -\frac{x_{r+1}}{x_n} & \ldots & 0
\end{vmatrix};
\]

мы воспользовались тем, что \( \begin{vmatrix} I & 0 \\ X_1 & X_2 \end{vmatrix} = |X_2| \). Полученный определитель легко преобразуется к виду

\[
\frac{1}{x_r\ldots x_n} \begin{vmatrix}
0 & -x_{r+1} & \ldots & -x_n \\
-x_r & 0 & \ldots & -x_n \\
\ldots & \ldots & \ldots & \ldots \\
-x_r & -x_{r+1} & \ldots & 0
\end{vmatrix}.
\]

Прибавим к первой строке все остальные строки, вынесем для первой строки множитель \( n - r \), а затем вычтем первую строку из всех остальных. В результате получим верхнюю треугольную матрицу с элементами \( -x_r, x_{r+1}, \ldots, x_n \) на диагонали. Таким образом, рассматриваемый определитель равен \( r - n \).

§ 6. Ядро и образ оператора. Факторпространство

6.1. Пусть \( x \) — столбец такого же размера, как и матрица \( A \), и \( y = Ax \). Тогда \( y^T y = x^T A^T A x \). Ясно, что равенство \( y^T y = 0 \) выполняется только для нулевого столбца, поэтому если \( A^T A x = 0 \), то \( A x = y = 0 \). Следовательно, \( \mathrm{Ker}(A^T A) = \mathrm{Ker} A \). Матрицы \( A \) и \( A^T A \) задают отображения одного и того же линейного пространства (хотя и в пространства разной размерности, если матрица \( A \) не квадратная), поэтому \( \dim \mathrm{Im} A = \dim \mathrm{Im}(A^T A) \).

6.2. Так как для любых отображений \( A : U \to V \) и \( B : V \to W \) справедлива формула \( \dim(\mathrm{Im} A \cap \mathrm{Ker} B) = \dim \mathrm{Ker} BA - \dim \mathrm{Ker} A \) (теорема 6.1.1), то \( \dim(\mathrm{Im} A^k \cap \mathrm{Ker} A) = \dim \mathrm{Ker} A^{k+1} - \dim \mathrm{Ker} A^k \) для любого \( k \). Следовательно,

\[
\prod_{k=1}^n \dim(\mathrm{Im} A^k \cap \mathrm{Ker} A) = \dim \mathrm{Ker} A^{n+1} - \dim \mathrm{Ker} A.
\]

Для доказательства второго равенства достаточно заметить, что \( \dim \mathrm{Im} A^p = \dim V - \dim \mathrm{Ker} A^p \), где \( V \) — пространство, в котором действует оператор \( A \).

6.3. Можно считать, что первые \( r \) функций \( f_1, \ldots, f_r \) линейно независимы, а функции \( f_{r+1}, \ldots, f_k \) через них линейно выражаются. Дополним первые \( r \) функций до базиса, и пусть \( e_1, \ldots, e_n \) — двойственный ему базис. Тогда