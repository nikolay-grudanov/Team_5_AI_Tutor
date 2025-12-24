---
source_image: page_212.png
page_number: 212
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.38
tokens: 6279
characters: 1907
timestamp: 2025-12-24T08:13:16.749593
finish_reason: stop
---

Доказательство. Складывая равенства • \( a_{1j} x_j = \lambda x_1, \ldots, \) • \( a_{nj} x_j = \lambda x_n, \) получаем • \( a_{ij} x_j = \lambda \cdot x_j. \) Но

\[
\bullet \quad a_{ij} x_j = \bullet \left( x_j \bullet a_{ij} \right) = \bullet x_j,
\]

поскольку • \( i a_{ij} = 1. \) Таким образом, \( \lambda \cdot x_j = \bullet x_j, \) причём • \( x_j \neq 0. \)
Следовательно, \( \lambda = 1. \)

Теорема 13.7.2. Если сумма абсолютных величин элементов каждого столбца квадратной матрицы \( A \) не превосходит 1, то все её собственные значения не превосходят 1.

Доказательство. Пусть \( (x_1, \ldots, x_n) \) — собственный вектор, соответствующий собственному значению \( \lambda. \) Тогда

\[
|\lambda x_i| = \left| \bullet a_{ij} x_j \right| \leq \bullet |a_{ij}| \cdot |x_j|, \quad i = 1, \ldots, n.
\]

Складывая эти неравенства, получаем

\[
|\lambda| \cdot |x_i| \leq \bullet |a_{ij}| \cdot |x_j| \leq \bullet \left( |x_j| \bullet |a_{ij}| \right) \leq \bullet |x_j|,
\]

поскольку • \( i |a_{ij}| \leq 1. \) Поделив обе части этого неравенства на ненулевое число • \( |x_j|, \) получим \( |\lambda| \leq 1. \)

Замечание. Теорема 13.7.2 остаётся верной и в том случае, когда некоторые столбцы матрицы \( A \) нулевые.

Теорема 13.7.3. Пусть \( A = \| a_{ij} \|_1^n, S_j = \bullet_{i=1}^n |a_{ij}|. \) Тогда

\[
\bullet_{j=1}^n S_j^{-1} |a_{jj}| \leq \operatorname{rk} A,
\]

где слагаемые, соответствующие нулевым значениям \( S_j, \) можно заменить нулями.

Доказательство. Умножая столбцы матрицы \( A \) на некоторые ненулевые элементы, мы всегда можем добиться, чтобы числа \( S_j \) для новой матрицы были равны 0 или 1, причём \( a_{jj} \geq 0. \) Ранг матрицы при таких преобразованиях не изменяется. Применяя теорему 13.7.2 к новой матрице, получаем

\[
\bullet |a_{jj}| = \bullet a_{jj} = \operatorname{tr} A = \bullet \lambda_i \leq \bullet |\lambda_i| \leq \operatorname{rk} A.
\]