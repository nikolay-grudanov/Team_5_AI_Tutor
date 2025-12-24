---
source_image: page_164.png
page_number: 164
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.83
tokens: 5684
characters: 2644
timestamp: 2025-12-24T07:09:04.283250
finish_reason: stop
---

1003. Будем называть \( \lambda \)-матрицу **унимодулярной**, если ее определитель является многочленом нулевой степени относительно \( \lambda \), т. е. константой, отличной от нуля. Найти нормальную диагональную форму унимодулярной \( \lambda \)-матрицы.

1004. Доказать, что матрица, обратная к \( \lambda \)-матрице, тогда и только тогда будет \( \lambda \)-матрицей, когда данная матрица \( A \) унимодулярна.

*1005. Доказать утверждение: для того чтобы две прямоугольные \( \lambda \)-матрицы \( A \) и \( B \), каждая из \( m \) строк и \( n \) столбцов, были эквивалентны, необходимо и достаточно выполнение равенства \( B = PAQ \), где \( P \) и \( Q \) — унимодулярные \( \lambda \)-матрицы порядков \( m \) и \( n \) соответственно. Показать, что требуемые матрицы \( P \) и \( Q \) можно найти так: найдя ряд элементарных преобразований, переводящий \( A \) в \( B \), применить все преобразования строк в том же порядке к единичной матрице \( E_m \) порядка \( m \), а все преобразования столбцов в том же порядке к единичной матрице \( E_n \) порядка \( n \).

Для данной \( \lambda \)-матрицы \( A \) методом, указанным в задаче 1005, найти унимодулярные матрицы \( P, Q \) такие, что матрица \( B = PAQ \) имеет нормальную диагональную форму (матрицы \( P \) и \( Q \) определяются не однозначно):

1006. \( A = \begin{pmatrix} \lambda^2 - \lambda + 4 & \lambda^2 + 3 \\ \lambda^2 - 2\lambda + 3 & \lambda^2 - \lambda + 2 \end{pmatrix} \).

1007. \( A = \begin{pmatrix} \lambda^4 + 4\lambda^3 + 4\lambda^2 + \lambda + 2 & \lambda^3 + 4\lambda^2 + 4\lambda \\ \lambda^4 + 5\lambda^3 + 8\lambda^2 + 5\lambda + 2 & \lambda^3 + 5\lambda^2 + 8\lambda + 4 \end{pmatrix} \).

1008. \( A = \begin{pmatrix} \lambda^4 + 3\lambda^3 - 5\lambda^2 + \lambda + 1 & 2\lambda^4 + 3\lambda^3 - 5\lambda^2 + \lambda - 1 & 2\lambda^4 + 2\lambda^3 - 4\lambda^2 \\ \lambda^4 - \lambda^3 + 1 & 2\lambda^4 - \lambda^3 - \lambda^2 & 2\lambda^4 - 2\lambda^3 \\ \lambda^4 + 2\lambda^3 - 4\lambda^2 + \lambda + 1 & 2\lambda^4 - 2\lambda^3 - 4\lambda^2 + \lambda - 1 & 2\lambda^4 + \lambda^3 - 3\lambda^2 \end{pmatrix} \).

Для данных \( \lambda \)-матриц \( A \) и \( B \) найти унимодулярные \( \lambda \)-матрицы \( P \) и \( Q \), удовлетворяющие равенству \( B = PAQ \) (матрицы \( P \) и \( Q \) определяются не однозначно (см. задачу 1005)):

1009.
\[
A = \begin{pmatrix} 2\lambda^2 - \lambda + 1 & 3\lambda^2 - 2\lambda + 1 \\ 2\lambda^2 + \lambda - 1 & 3\lambda^2 + \lambda - 2 \end{pmatrix};
\]
\[
B = \begin{pmatrix} 3\lambda^3 + 7\lambda + 2 & 3\lambda^3 + 4\lambda - 1 \\ 2\lambda^3 + 5\lambda + 1 & 2\lambda^3 + 3\lambda - 1 \end{pmatrix}.
\]