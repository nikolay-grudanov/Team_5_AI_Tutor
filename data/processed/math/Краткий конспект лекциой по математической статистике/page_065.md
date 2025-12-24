---
source_image: page_065.png
page_number: 65
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.88
tokens: 12345
characters: 2624
timestamp: 2025-12-24T07:05:09.454278
finish_reason: stop
---

Определение 34. Уравнение \( Z \vec{X} = A \vec{\beta} \) называется нормальным уравнением.

Теорема 17. 1. Если \( \hat{\beta} \) — произвольное решение нормального уравнения, то \( \hat{\beta} \) — ОМНК.
2. Если \( \det A \neq 0 \) \( \implies \) \( \hat{\beta} = A^{-1} Z \vec{X} \) — единственная ОМНК.

Стоп! Упражнение. Что именно нужно доказывать в п. 1 теоремы? Нужно ли доказывать п. 2?

Замечание 31. Предположение 1 и лемма 12 \( A t = 0 \) имеет ненулевые решения (и много) \( \implies \det A \neq 0 \) (т.к. иначе система уравнений \( A \) не положительно определена).

Доказательство теоремы 17.

\[
S(\vec{\beta}) = (\vec{X} - Z^T \vec{\beta})^T \cdot (\vec{X} - Z^T \vec{\beta}) = \left( \vec{X} - Z^T \hat{\beta} + Z^T (\hat{\beta} - \vec{\beta}) \right)^T \cdot \left( \vec{X} - Z^T \hat{\beta} + Z^T (\hat{\beta} - \vec{\beta}) \right) =
\]
\[
= S(\hat{\beta}) + (\hat{\beta} - \vec{\beta})^T (Z \vec{X} - A \hat{\beta}) + \left( (\hat{\beta} - \vec{\beta})^T (Z \vec{X} - A \hat{\beta}) \right)^T + (\hat{\beta} - \vec{\beta})^T Z \cdot Z^T (\hat{\beta} - \vec{\beta}).
\]

Поскольку \( \hat{\beta} \) — решение нормального уравнения, второе и третье слагаемое обращается в ноль. Далее,
\[
S(\vec{\beta}) = S(\hat{\beta}) + (\hat{\beta} - \vec{\beta})^T A (\hat{\beta} - \vec{\beta}) \geq S(\hat{\beta})
\]
поскольку матрица \( A \) положительно определена. Итак, \( \hat{\beta} \) — ОМНК, т.к. она минимизирует \( S(\vec{\beta}) \).

Пример 35. Полиномиальная регрессия (продолжение примера 33) Имеем \( n \) наблюдений
\[
\begin{cases}
X_1 = 1 \cdot \theta_0 + t_1 \theta_1 + t_1^2 \theta_2 + \ldots + t_1^{k-1} \theta_{k-1} + \varepsilon_1 \\
\ldots \\
X_n = 1 \cdot \theta_0 + t_n \theta_1 + t_n^2 \theta_2 + \ldots + t_n^{k-1} \theta_{k-1} + \varepsilon_n
\end{cases}
\]
Эта модель сводится к линейной модели регрессии с матрицей плана
\[
Z = \begin{pmatrix}
1 & \ldots & 1 \\
t_1 & \ldots & t_n \\
t_1^2 & \ldots & t_n^2 \\
\vdots & & \vdots \\
t_1^{k-1} & \ldots & t_n^{k-1}
\end{pmatrix}.
\]

9.5 Свойства ОМНК

1. Разница \( \hat{\beta} \) и \( \vec{\beta} \):
\[
\hat{\beta} = A^{-1} Z \vec{X} = A^{-1} Z (Z^T \vec{\beta} + \vec{\varepsilon}) = A^{-1} A \vec{\beta} + A^{-1} Z \vec{\varepsilon} = \vec{\beta} + A^{-1} Z \vec{\varepsilon}.
\]

Предположение 2. Ошибки \( \varepsilon_1, \ldots, \varepsilon_n \) некоррелированы, все имеют нулевые математические ожидания и ненулевую дисперсию \( D \varepsilon_i = E \varepsilon_i^2 = \sigma^2 < \infty, i = 1, \ldots, n \).

Замечание 32. Напоминаю, что когда речь заходит о дисперсии, термины «ненулевая» и «положительная» означают одно и то же.