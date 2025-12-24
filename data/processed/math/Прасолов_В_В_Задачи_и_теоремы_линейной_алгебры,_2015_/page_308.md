---
source_image: page_308.png
page_number: 308
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.51
tokens: 6460
characters: 2428
timestamp: 2025-12-24T08:15:53.027077
finish_reason: stop
---

Доказательство. Приведём матрицы \( A \) и \( B \) к жордановой нормальной форме (достаточно привести к треугольному виду) и в тензорном произведении рассмотрим базис, являющийся произведением этих базисов. Остаётся заметить, что \( J_p(\alpha) \otimes J_q(\beta) \) — верхняя треугольная матрица с диагональю \( (\alpha\beta, \ldots, \alpha\beta) \), а \( J_p(\alpha) \otimes I_q \) и \( I_p \otimes J_q(\beta) \) — верхние треугольные матрицы с диагоналями \( (\alpha, \ldots, \alpha) \) и \( (\beta, \ldots, \beta) \).

Следствие. \( \operatorname{tr}(A \otimes B) = (\operatorname{tr} A)(\operatorname{tr} B) \) и \( \det(A \otimes B) = (\det A)^n (\det B)^m \).

29.6. Матричные уравнения

Тензорное произведение операторов можно применить для решения матричных уравнений вида

\[
A_1 X B_1 + \ldots + A_r X B_r = C,
\]

где

\[
V^k \xrightarrow{B_i} V^l \xrightarrow{X} V^m \xrightarrow{A_i} V^n.
\]

Покажем, что при естественных отождествлениях \( \operatorname{Hom}(V^l, V^m) = (V^l)^* \otimes V^m \) и \( \operatorname{Hom}(V^k, V^n) = (V^k)^* \otimes V^n \) отображение \( X \mapsto A_i X B_i \) отождествляется с \( B_i^T \otimes A_i \), а значит, уравнение (1) можно переписать в виде

\[
(B_1^T \otimes A_1 + \ldots + B_r^T \otimes A_r) X = C,
\]

где \( X \in (V^l)^* \otimes V^m \) и \( C \in (V^k)^* \otimes V^n \) (т. е. матрицы \( X \) и \( C \) мы рассматриваем здесь как векторы в тензорных произведениях). В самом деле, если элемент \( f \otimes v \in (V^l)^* \otimes V^m \) соответствует отображению \( X x = (f \otimes v)x = f(x)v \), то элемент \( B^T f \otimes Av \in (V^k)^* \otimes V^n \) соответствует отображению \( (B^T f \otimes Av)y = f(By)Av = AXBy \).

Теорема 29.6.1. Пусть \( A \) и \( B \) — квадратные матрицы порядков \( m \) и \( n \), \( X \) и \( C \) — матрицы размером \( m \times n \), причем матрицы \( A, B, C \) заданы, а матрица \( X \) неизвестна. Уравнение \( AX - XB = C \) имеет единственное решение тогда и только тогда, когда матрицы \( A \) и \( B \) не имеют общих собственных значений.

Доказательство. Данное уравнение можно переписать в виде

\[
(I_n \otimes A - B^T \otimes I_m) X = C.
\]

Собственные значения оператора \( I_n \otimes A - B^T \otimes I_m \) равны \( \alpha_i - \beta_j \), где \( \alpha_i \) — собственные значения оператора \( A \), \( \beta_j \) — собственные значения оператора \( B^T \) (т. е. собственные значения оператора \( B \)). Ясно, что