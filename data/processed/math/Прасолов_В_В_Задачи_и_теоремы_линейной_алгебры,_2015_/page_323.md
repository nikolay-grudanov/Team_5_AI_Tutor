---
source_image: page_323.png
page_number: 323
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.72
tokens: 6594
characters: 2657
timestamp: 2025-12-24T08:16:23.154047
finish_reason: stop
---

§ 31. Пфаффиан

31.1. Определитель кососимметрической матрицы

Если \( A = \|a_{ij}\|_1^n \) — кососимметрическая матрица, то \( \det A \) является многочленом от независимых переменных \( a_{ij} \), где \( i < j \); обозначим этот многочлен \( P(a_{ij}) \). Для \( n \) нечётного \( P \equiv 0 \) (см. задачу 1.1); если \( n \) чётно, то матрицу \( A \) можно представить в виде \( A = XJX^T \), где элементы матрицы \( X \) являются рациональными функциями от переменных \( a_{ij} \) и
\[
J = \operatorname{diag}\left( \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \ldots, \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \right)
\]
(см. п. 23.2). Напомним, что это разложение следует рассматривать как разложение матриц, элементы которых являются рациональными функциями от \( a_{ij} \); для некоторых значений \( a_{ij} \) эти рациональные функции могут иметь нулевые знаменатели. Так как \( \det X = f(a_{ij})/g(a_{ij}) \), где \( f \) и \( g \) — многочлены, то \( P = \det(XJX^T) = (f/g)^2 \). Поэтому \( f^2 = Pg^2 \), т. е. \( f^2 \) делится на \( g^2 \), а значит, \( f \) делится на \( g \), т. е. \( f/g = Q \) — некоторый многочлен. В итоге получаем, что \( P = Q^2 \), где \( Q \) — многочлен от \( a_{ij} \), т. е. определитель кососимметрической матрицы, рассматриваемый как многочлен от \( a_{ij} \), где \( i < j \), является полным квадратом.

Этот результат можно получить и другим способом, дающим для многочлена \( Q \) явное выражение. Пусть в пространстве \( V \) задан базис \( e_1, \ldots, e_{2n} \). Сопоставим кососимметрической матрице \( A = \|a_{ij}\|_1^{2n} \) элемент \( \omega = \bigwedge_{i<j} a_{ij} e_i \wedge e_j \in \Lambda^2(V) \), а элементу \( \omega \) сопоставим \( \Lambda^n \omega = f(A)e_1 \wedge \ldots \wedge e_{2n} \in \Lambda^{2n}(V) \). Функция \( f(A) \) выражается через элементы матрицы \( A \).

Запишем теперь элементы \( \omega \) и \( \Lambda^n \omega \) в базисе \( \varepsilon_j = \cdot x_{ij} e_i \). Можно проверить, что
\[
\bigwedge_{i<j} a_{ij} e_i \wedge e_j = \bigwedge_{i<j} b_{ij} \varepsilon_i \wedge \varepsilon_j,
\]
где \( A = XBX^T \), и \( \varepsilon_1 \wedge \ldots \wedge \varepsilon_{2n} = (\det X)e_1 \wedge \ldots \wedge e_{2n} \). Поэтому
\[
f(A)e_1 \wedge \ldots \wedge e_{2n} = f(B)\varepsilon_1 \wedge \ldots \wedge \varepsilon_{2n} = (\det X)f(B)e_1 \wedge \ldots \wedge e_{2n},
\]
т. е. \( f(XBX^T) = (\det X)f(B) \). Если \( A \) — невырожденная кососимметрическая матрица, то её можно представить в виде \( A = XJX^T \), где
\[
J = \operatorname{diag}\left( \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \ldots, \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \right).
\]