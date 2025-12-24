---
source_image: page_405.png
page_number: 405
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.32
tokens: 5636
characters: 2754
timestamp: 2025-12-24T07:15:07.065775
finish_reason: stop
---

1147. Указание. Показать, что \( g(A) = h(A) \) тогда и только тогда, когда \( g(\lambda) - h(\lambda) \) делится на \( \psi(\lambda) \).

1149. В данном случае минимальный многочлен совпадает с характеристическим (с точностью до знака). \( r(\lambda) \) есть обычный интерполяционный многочлен Лагранжа.

\[
f(A) = \sum_{k=1}^n f(\lambda_k) \frac{(A-\lambda_1 E)\ldots(A-\lambda_{k-1} E)(A-\lambda_{k+1} E)\ldots(A-\lambda_n E)}{(\lambda_k-\lambda_1)\ldots(\lambda_k-\lambda_{k-1})(\lambda_k-\lambda_{k+1})\ldots(\lambda_k-\lambda_n)},
\]

где \( \lambda_1, \lambda_2, \ldots, \lambda_n \) — характеристические числа матрицы \( A \) (по условию различные).

1150. \( r(\lambda) \) есть обычный интерполяционный многочлен Лагранжа.

\[
f(A) = \sum_{k=1}^s f(\lambda_k) \frac{(A-\lambda_1 E)\ldots(A-\lambda_{k-1} E)(A-\lambda_{k+1} E)\ldots(A-\lambda_s E)}{(\lambda_k-\lambda_1)\ldots(\lambda_k-\lambda_{k-1})(\lambda_k-\lambda_{k+1})\ldots(\lambda_k-\lambda_s)}.
\]

1151. Решение. Покажем, во-первых, что если интерполяционный многочлен Лагранжа–Сильвестра \( r(\lambda) \) существует, то он определяется равенствами (1) и (2). Пусть

\[
\frac{r(\lambda)}{\psi(\lambda)} = \sum_{k=1}^s \left[ \frac{\alpha_{k,1}}{(\lambda-\lambda_k)^{r_k}} + \cdots + \frac{\alpha_{k,r_k}}{(\lambda-\lambda_k)^{r_k}} \right]
\]

— разложение дроби на простейшие. Умножая это равенство на \( \psi(\lambda) \), получим равенство (1). Для установления равенств (2) умножим равенство (3) на \( (\lambda-\lambda_k)^{r_k} \). Получим

\[
\frac{r(\lambda)}{\psi_k(\lambda)} = \alpha_{k,1} + \alpha_{k,2}(\lambda-\lambda_k) + \cdots + \alpha_{k,r_k}(\lambda-\lambda_k)^{r_k-1} + (\lambda-\lambda_k)^{r_k} \varphi(\lambda),
\]

где \( \varphi(\lambda) \) — рациональная функция, имеющая смысл при \( \lambda = \lambda_k \) вместе со всеми своими производными. Беря от обеих частей равенства (4) \((j-1)\)-ю производную при \( \lambda = \lambda_k \) и пользуясь тем, что значения \( r(\lambda) \) и \( f(\lambda) \) на спектре матрицы совпадают, мы и получим равенства (2). Во-вторых, покажем, что многочлен \( r(\lambda) \), определенный равенствами (1) и (2), является интерполяционным многочленом Лагранжа–Сильвестра для функции \( f(\lambda) \) на спектре матрицы \( A \). Из равенства (1) видно, что степень \( r(\lambda) \) ниже степени \( \psi(\lambda) \). Далее, положим

\[
\varphi_k(\lambda) = \alpha_{k,1} + \alpha_{k,2}(\lambda-\lambda_k) + \cdots + \alpha_{k,r_k}(\lambda-\lambda_k)^{r_k-1}.
\]

Из равенств (2) следует, что при \( \lambda = \lambda_k \) значения функции \( \varphi_k(\lambda) \) и ее производных порядка \( j < r_k \) совпадают соответственно со значениями функции \( \frac{f(\lambda)}{\psi_k(\lambda)} \) и ее производных того же порядка. Поэтому,