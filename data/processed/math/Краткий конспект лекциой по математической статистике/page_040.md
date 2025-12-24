---
source_image: page_040.png
page_number: 40
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 59.83
tokens: 12449
characters: 2568
timestamp: 2025-12-24T07:04:22.605391
finish_reason: stop
---

6.4 Преобразования нормальных выборок

Пусть \( \vec{X} = (X_1, \ldots, X_n) \) — выборка из \( N_{0,1} \) (набор независимых и одинаково распределенных величин). Пусть \( C \) — ортогональная матрица \( (n \times n) \), т.е. \( CC^T = E = \begin{pmatrix} 1 & 0 \\ \vdots & \ddots \\ 0 & 1 \end{pmatrix} \). Введем вектор \( \vec{Y} = \vec{X} \cdot C \) с координатами \( Y_i = \sum_{j=1}^n X_j C_{ji} \).

**Лемма 8.** Координаты вектора \( \vec{Y} \) независимы и имеют стандартное нормальное распределение.

**Доказательство.** Воспользуемся свойством, утверждающим, что по характеристической функции однозначно восстанавливается распределение. Это верно и для характеристической функции вектора.

**Определение 19.** Характеристической функцией вектора \( \vec{\xi} = (\xi_1, \ldots, \xi_n) \) называется функция переменного \( \vec{t} = (t_1, \ldots, t_n) \)

\[
\varphi_{\vec{\xi}}(\vec{t}) = \mathbb{E} e^{i \vec{t} \cdot \vec{\xi}^T} = \mathbb{E} e^{i \sum_{j=1}^n t_j \xi_j}
\]

Характеристическая функция вектора \( \vec{X} \) равна

\[
\varphi_{\vec{X}}(\vec{t}) = \mathbb{E} e^{i \sum_{j=1}^n t_j X_j} = \prod_{j=1}^n \mathbb{E} e^{i t_j X_j} = \prod_{j=1}^n \varphi_{X_j}(t_j) =
\]
\[
= \prod_{j=1}^n \varphi_{X_j}(t_j) = \prod_{j=1}^n e^{-t_j^2/2} = e^{-\frac{1}{2} \sum_{j=1}^n t_j^2}.
\] (11)

Вычислим х.ф. вектора \( \vec{Y} = \vec{X} \cdot C \):

\[
\varphi_{\vec{Y}}(\vec{t}) = \mathbb{E} e^{i \vec{t} \vec{Y}^T} = \mathbb{E} e^{i \vec{t} C^T \vec{X}^T} = \left[ \text{заменим } \vec{t} = \vec{u} \cdot C \right] = \mathbb{E} e^{i \vec{u} C \cdot C^T \vec{X}^T} = \mathbb{E} e^{i \vec{u} \vec{X}^T} = e^{-\frac{1}{2} \sum_{j=1}^n u_j^2} \quad \text{(по (11))}.
\]

Так как \( C \) ортогональна, то \( \sum_{j=1}^n u_j^2 = \sum_{j=1}^n t_j^2 \) (доказать!). Поэтому

\[
\varphi_{\vec{Y}}(\vec{t}) = e^{-\frac{1}{2} \sum_{j=1}^n u_j^2} = e^{-\frac{1}{2} \sum_{j=1}^n t_j^2} = \varphi_{\vec{X}}(\vec{t}),
\]

и вектор \( \vec{Y} \) распределен так же, как и вектор \( \vec{X} \).

**Лемма 9.** Пусть \( \vec{X} = (X_1, \ldots, X_n) \in N_{0,1} \), независимы, \( C \) — ортогональная матрица и \( \vec{Y} = \vec{X} \cdot C \). Тогда для любого \( k = 1, \ldots, n \)

\[
T(\vec{X}) = \sum_{i=1}^n X_i^2 - Y_1^2 - \ldots - Y_k^2 \in H_{n-k} \text{ и не зависит от } Y_1, \ldots, Y_k.
\]

**Доказательство.** Поскольку \( \vec{Y} = \vec{X} \cdot C \), то \( \sum_{i=1}^n X_i^2 = \sum_{i=1}^n Y_i^2 \). Тогда

\[
T(\vec{X}) = \sum_{i=1}^n Y_i^2 - Y_1^2 - \ldots - Y_k^2 = Y_{k+1}^2 + \ldots + Y_n^2 \in H_{n-k}
\]

и не зависит от \( Y_1, \ldots, Y_k \).