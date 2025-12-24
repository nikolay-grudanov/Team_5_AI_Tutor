---
source_image: page_270.png
page_number: 270
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.20
tokens: 6492
characters: 2295
timestamp: 2025-12-24T08:14:51.115084
finish_reason: stop
---

21.16. а) Докажите, что квадратичные формы с матрицами \(\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\) и \(\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}\) эквивалентны над \(\mathbb{Q}\), но не эквивалентны над \(\mathbb{Z}\).

б) Докажите, что квадратичные формы с матрицами \(\begin{pmatrix} 0 & 1 \\ 1 & m \end{pmatrix}\) и \(\begin{pmatrix} 0 & 1 \\ 1 & n \end{pmatrix}\), где \(m\) и \(n\) — целые числа, эквивалентны над \(\mathbb{Z}\) тогда и только тогда, когда числа \(m\) и \(n\) одной чётности.

§ 22. Одновременное приведение пары эрмитовых форм к диагональному виду

22.1. Случай положительно определённой матрицы

Теорема 22.1.1. Пусть \(A\) и \(B\) — эрмитовы матрицы, причём \(A > 0\). Тогда существует такая матрица \(T\), что \(T^* A T = I\), а матрица \(T^* B T\) диагональна.

Доказательство. Для матрицы \(A\) существует такая матрица \(Y\), что \(Y^* A Y = I\) (см. п. 21.2). Матрица \(C = Y^* B Y\) эрмитова, поэтому существует такая унитарная матрица \(U\), что матрица \(U^* C U\) диагональна. А так как \(U^* I U = I\), то \(T = Y U\) — искомая матрица.

Две эрмитовых формы не всегда можно одновременно привести к диагональному виду заменой базиса. Рассмотрим, например, эрмитовы формы, соответствующие матрицам \(\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}\) и \(\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\). Пусть \(P = \begin{pmatrix} a & b \\ c & d \end{pmatrix}\) — произвольная невырожденная матрица. Тогда

\[
P^* \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} P = \begin{pmatrix} a \overline{a} & a \overline{b} \\ a \overline{b} & b \overline{b} \end{pmatrix}
\]

и

\[
P^* \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} P = \begin{pmatrix} a \overline{c} + \overline{a} c & \overline{a} d + b \overline{c} \\ a \overline{d} + \overline{b} c & b \overline{d} + \overline{b} d \end{pmatrix}.
\]

Остаётся проверить, что равенства \(\overline{a} b = 0\) и \(\overline{a} d + b \overline{c} = 0\) не могут выполняться одновременно. Если \(\overline{a} b = 0\) и матрица \(P\) невырождена, то либо \(a = 0\) и \(b \neq 0\), либо \(b = 0\) и \(a \neq 0\). В первом случае \(0 = \overline{a} d + b \overline{c} = b \overline{c}\), поэтому \(c = 0\), а во втором случае \(\overline{a} d = 0\), поэтому \(d = 0\). В обоих случаях получается вырожденная матрица \(P\).