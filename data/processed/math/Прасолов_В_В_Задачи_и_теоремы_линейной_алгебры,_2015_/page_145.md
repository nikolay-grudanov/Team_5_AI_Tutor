---
source_image: page_145.png
page_number: 145
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.45
tokens: 6764
characters: 2957
timestamp: 2025-12-24T08:11:35.825717
finish_reason: stop
---

этому \( A^T A = I \), а значит, \( A^T = A^{-1} \) и \( AA^T = I \). Если \( A \) — ортогональная матрица, то \( (Ax, Ay) = (x, A^T A y) = (x, y) \) (см. п. 5.3 и 5.4).

Легко проверить, что любые векторы \( e_1, \ldots, e_n \), обладающие свойством \( (e_i, e_j) = \delta_{ij} \), линейно независимы. В самом деле, если

\[
\lambda_1 e_1 + \ldots + \lambda_n e_n = 0,
\]

то \( \lambda_i = (\lambda_1 e_1 + \ldots + \lambda_n e_n, e_i) = 0 \). Аналогично можно доказать, что ортогональная система ненулевых векторов линейно независима.

**Теорема 9.2.1** (ортогонализация Грама—Шмидта). *Пусть \( e_1, \ldots, e_n \) — произвольный базис. Тогда существует ортогональный базис \( \varepsilon_1, \ldots, \varepsilon_n \), для которого \( \varepsilon_i \in \langle e_1, \ldots, e_i \rangle \) для всех \( i = 1, \ldots, n \).*

**Доказательство.** Применим индукцию по \( n \). При \( n = 1 \) утверждение очевидно. Предположим, что утверждение верно для \( n \) векторов. Рассмотрим базис \( e_1, \ldots, e_{n+1} \). По предположению индукции существует такой ортогональный базис \( \varepsilon_1, \ldots, \varepsilon_n \), что \( \varepsilon_i \in \langle e_1, \ldots, e_i \rangle \) для \( i = 1, \ldots, n \). Рассмотрим вектор \( \varepsilon_{n+1} = \lambda_1 \varepsilon_1 + \ldots + \lambda_n \varepsilon_n + e_{n+1} \). Условие \( (\varepsilon_i, \varepsilon_{n+1}) = 0 \) означает, что \( \lambda_i (\varepsilon_i, \varepsilon_i) + (e_{n+1}, \varepsilon_i) = 0 \), т. е. \( \lambda_i = -\frac{(e_{n+1}, \varepsilon_i)}{(\varepsilon_i, \varepsilon_i)} \). Взяв такие \( \lambda_i \), получим ортогональную систему векторов \( \varepsilon_1, \ldots, \varepsilon_{n+1} \), причём \( \varepsilon_{n+1} \neq 0 \), так как \( \varepsilon_{n+1} \notin \langle \varepsilon_1, \ldots, \varepsilon_n \rangle = \langle e_1, \ldots, e_n \rangle \).

**Замечание 1.** От ортогонального базиса \( \varepsilon_1, \ldots, \varepsilon_n \) можно перейти к ортонормированному базису \( \varepsilon'_1, \ldots, \varepsilon'_n \), где \( \varepsilon'_i = \frac{1}{\sqrt{(\varepsilon_i, \varepsilon_i)}} \varepsilon_i \).

**Замечание 2.** Процесс ортогонализации имеет достаточно простой геометрический смысл: из вектора \( e_{n+1} \) вычитается его ортогональная проекция на подпространство \( W = \langle e_1, \ldots, e_n \rangle \) и в результате получается вектор \( \varepsilon_{n+1} \), ортогональный \( W \).

Доказательство теоремы 9.2.1 даёт рекуррентное построение ортогонального базиса \( \varepsilon_1, \ldots, \varepsilon_n \). Явное выражение вектора \( \varepsilon_k \) через \( e_1, \ldots, e_k \) выглядит следующим образом.

**Теорема 9.2.2.** *Пусть \( e_1, \ldots, e_n \) — произвольный базис, \( g_{ij} = (e_i, e_j) \). Тогда векторы*

\[
\varepsilon_1 = e_1, \quad \varepsilon_k = \begin{pmatrix}
g_{11} & \cdots & g_{1k} \\
\cdots & \cdots & \cdots \\
g_{k-1,1} & \cdots & g_{k-1,k} \\
e_1 & \cdots & e_k
\end{pmatrix}, \quad k = 2, \ldots, n,
\]