---
source_image: page_292.png
page_number: 292
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.18
tokens: 6003
characters: 1126
timestamp: 2025-12-24T08:15:17.247344
finish_reason: stop
---

Проверим, что \( S \) — инволюция. Равенства \( S^2 e_i = e_i \) и \( S^2 \varepsilon_j = \varepsilon_j \) очевидны при \( i \neq 1 \) и \( j \neq n \). Далее,

\[
S^2 e_1 = S(-\beta_1 \varepsilon_1 - \ldots - \beta_n \varepsilon_n) =
= -\beta_1 e_2 - \ldots - \beta_{n-1} e_n + \beta_n (\alpha_n e_1 + \ldots + \alpha_1 e_n) =
= e_1 + (\beta_n \alpha_{n-1} - \beta_1) e_2 + \ldots + (\beta_n \alpha_1 - \beta_{n-1}) e_n = e_1.
\]

Аналогично \( S^2 \varepsilon_n = \varepsilon_n \).

Следствие. Если \( B \) — невырожденная матрица и \( X^T B X = B \), то матрицу \( X \) можно представить в виде произведения двух инволюций.

Доказательство. Если \( X^T B X = B \), то \( X^T = B X^{-1} B^{-1} \), т. е. матрицы \( X^T \) и \( X^{-1} \) подобны. Кроме того, матрицы \( X \) и \( X^T \) подобны для любой матрицы \( X \) (см. задачу 14.2).

Задачи

28.1. Найдите все матрицы порядка 2, являющиеся инволюциями.

28.2. Пусть \( A \) — симметрическая матрица, \( H = (\bar{A} A + I)^{-1} (\bar{A} A - I) \) и \( S = 2A (\bar{A} A + I)^{-1} \). Докажите, что \( \begin{pmatrix} -H & S \\ S & \bar{H} \end{pmatrix} \) — инволюция.