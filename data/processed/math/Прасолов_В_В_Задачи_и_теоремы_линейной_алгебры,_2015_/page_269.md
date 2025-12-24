---
source_image: page_269.png
page_number: 269
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.58
tokens: 6372
characters: 1978
timestamp: 2025-12-24T08:14:46.273494
finish_reason: stop
---

21.6. Пусть \( A \) — эрмитова матрица порядка \( n \), \( v_1, \ldots, v_n \) — ортонормированный базис собственных векторов, соответствующих собственным значениям \( \lambda_1, \ldots, \lambda_n \). Докажите, что \( A = \sum_{k=1}^n \lambda_k v_k v_k^* \).

21.7. Докажите, что если \( -1 < \lambda < 1 \), то матрица \( A = \|a_{ij}\|_1^n \), где \( a_{ii} = 1 \) и \( a_{ij} = \lambda \) при \( i \neq j \), положительно определена.

21.8. Докажите, что если \( A \geqslant 0 \), то \( \begin{pmatrix} A & A \\ A & A \end{pmatrix} \geqslant 0 \).

21.9. Докажите, что матрица

\[
\begin{pmatrix}
1 & \frac{1}{2} & \frac{1}{3} & \cdots & \frac{1}{n} \\
\frac{1}{2} & \frac{1}{3} & \frac{1}{4} & \cdots & \frac{1}{n+1} \\
\cdots & \cdots & \cdots & \cdots & \cdots \\
\frac{1}{n} & \frac{1}{n+1} & \frac{1}{n+2} & \cdots & \frac{1}{2n-1}
\end{pmatrix}
\]

положительно определённая.

21.10. Матрица \( A \) положительно определена. Докажите, что

\[
\int_{-\infty}^{+\infty} e^{-(x, Ax)} dx = (\sqrt{\pi})^n |A|^{-1/2}.
\]

21.11. Матрицы \( A \) и \( B \) вещественные симметрические, причём матрица \( \Lambda = A^{-1}B \) диагональна. Пусть \( \Lambda e_i = \lambda_i e_i \). Докажите, что если \( \lambda_i \neq \lambda_j \), то \( (Ae_i, e_j) = (Be_i, e_j) = 0 \).

21.12. Пусть \( S \) — симметричная невырожденная матрица порядка \( n \), все элементы которой положительны. Каково наибольшее возможное число нулевых элементов матрицы \( S^{-1} \)?

21.13. Пусть \( A \geqslant 0 \) и \( B \geqslant 0 \). Докажите, что \( \operatorname{tr}(AB) \geqslant 0 \).

21.14. Пусть \( A \geqslant 0, B \geqslant 0 \) и \( A - B \geqslant 0 \). Докажите, что \( \operatorname{tr}(A^2) \geqslant \operatorname{tr}(B^2) \).

21.15. Докажите, что для любого положительного \( \lambda \) эрмитовы формы, заданные матрицами

\[
\begin{pmatrix} A & B \\ B^* & 0 \end{pmatrix} \quad \text{и} \quad \begin{pmatrix} \lambda A & B \\ B^* & 0 \end{pmatrix},
\]

имеют одинаковую сигнатуру.