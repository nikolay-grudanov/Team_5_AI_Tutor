---
source_image: page_267.png
page_number: 267
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.70
tokens: 6371
characters: 1926
timestamp: 2025-12-24T08:14:40.593618
finish_reason: stop
---

Доказательство. Выберем ортонормированный базис, в котором форма \((x, Ax)\) диагональна, т. е. \((x, Ax) = \lambda_1 x_1^2 + \ldots + \lambda_n x_n^2\). Рассмотрим подпространства

\[
W_1 = \{x \mid x_{k+1} = \ldots = x_n = 0\} \quad \text{и} \quad W_2 = \{x \mid x \perp y_1, \ldots, x \perp y_{k-1}\}.
\]

Так как \(\dim W_1 = k\) и \(\dim W_2 \geq n - k + 1\), то

\[
W = W_1 \cap W_2 \neq 0.
\]

Если \(x \in W\) и \(\|x\| = 1\), то \(x \in W_1\) и

\[
(Ax, x) = \lambda_1 x_1^2 + \ldots + \lambda_k x_k^2 \geq \lambda_k (x_1^2 + \ldots + x_k^2) = \lambda_k.
\]

Поэтому \(\lambda_k \leq \max_{x \in W_1 \cap W_2} (x, Ax) \leq \max_{x \in W_2} (Ax, x)\), а значит,

\[
\lambda_k \leq \min_{y_1, \ldots, y_{k-1}} \max_{x \in W_2} (x, Ax).
\]

Рассмотрим теперь векторы \(y_i = (0, \ldots, 0, 1, 0, \ldots, 0)\) (единица стоит на \(i\)-м месте). Тогда

\[
W_2 = \{x \mid x \perp y_1, \ldots, x \perp y_{k-1}\} = \{x \mid x_1 = \ldots = x_{k-1} = 0\}.
\]

Если \(x \in W_2\) и \(\|x\| = 1\), то

\[
(x, Ax) = \lambda_k x_k^2 + \ldots + \lambda_n x_n^2 \leq \lambda_k (x_k^2 + \ldots + x_n^2) = \lambda_k.
\]

Поэтому

\[
\lambda_k \geq \max_{x \in W_2} (x, Ax) \geq \min_{y_1, \ldots, y_{k-1}} \max_{x \perp y_1, \ldots, x \perp y_{k-1}} (x, Ax).
\]

\hfill \(\square\)

21.6. Собственные значения произведения двух эрмитовых матриц

Произведение двух эрмитовых матриц \(A\) и \(B\) является эрмитовой матрицей тогда и только тогда, когда \(AB = (AB)^* = B^* A^* = BA\). Тем не менее, произведение двух положительно определённых матриц до некоторой степени схоже с положительно определённой матрицей: оно является диагонализуемой матрицей с положительными собственными значениями.

Теорема 21.6.1. Пусть \(A\) — положительно определённая матрица, \(B\) — эрмитова матрица. Тогда \(AB\) — диагонализуемая матрица, причём у неё столько же положительных, отрицательных и нулевых собственных значений, сколько и у матрицы \(B\).