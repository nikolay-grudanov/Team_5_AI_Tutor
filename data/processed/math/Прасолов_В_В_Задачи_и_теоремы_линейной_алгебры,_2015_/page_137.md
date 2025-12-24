---
source_image: page_137.png
page_number: 137
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.51
tokens: 6697
characters: 2927
timestamp: 2025-12-24T08:11:19.950646
finish_reason: stop
---

что

\[
g(\lambda) = \alpha_0(\lambda)f_0(\lambda) + \ldots + \alpha_{n-1}(\lambda)f_{n-1}(\lambda).
\]

(1)

Следовательно, \( \varphi_i(g(\lambda)) = \sum_{k=0}^{n-1} \alpha_k(\lambda) \varphi_i(f_k(\lambda)) \) при \( i = 0, \ldots, n-1 \). Если \( \Delta(\lambda) \neq 0 \), то полученную систему линейных уравнений относительно \( \alpha_k(\lambda) \) можно решить с помощью правила Крамера. Поэтому \( \alpha_k(\lambda) \) — рациональная функция для всех \( \lambda \in \mathbb{C} \setminus \Delta \), где \( \Delta \) — (конечное) множество корней многочлена \( \Delta(\lambda) \).

Равенство (1) можно записать в виде \( p_\lambda(T)f_0(\lambda) = 0 \), где \( p_\lambda(T) = T^n - \alpha_{n-1}(\lambda)T^{n-1} - \ldots - \alpha_0(\lambda)I \). Пусть \( \beta_1(\lambda), \ldots, \beta_n(\lambda) \) — корни многочлена \( p_\lambda \). Тогда

\[
(T - \beta_1(\lambda)I)\ldots(T - \beta_n(\lambda)I)f_0(\lambda) = 0.
\]

Если \( \lambda \notin \Delta \), то векторы \( f_0(\lambda), \ldots, f_{n-1}(\lambda) \) линейно независимы, т. е. \( h(T)f_0(\lambda) \neq 0 \) для любого ненулевого многочлена \( h \) степени \( n-1 \). Поэтому

\[
w = (T - \beta_2(\lambda)I)\ldots(T - \beta_n(\lambda)I)f_0(\lambda) \neq 0
\]

и \( (T - \beta_1(\lambda)I)w = 0 \), т. е. \( \beta_1(\lambda) \) — собственное значение оператора \( T \). Аналогично доказывается, что \( \beta_2(\lambda), \ldots, \beta_n(\lambda) \) — собственные значения оператора \( T \). Следовательно, \( |\beta_i(\lambda)| \leq \|T\| \) (см. п. 38.1). Рациональные функции \( \alpha_0(\lambda), \ldots, \alpha_{n-1}(\lambda) \) являются элементарными симметрическими функциями от ограниченных на \( \mathbb{C} \setminus \Delta \) функций \( \beta_1(\lambda), \ldots, \beta_n(\lambda) \), поэтому они сами ограничены на \( \mathbb{C} \setminus \Delta \). Следовательно, функции \( \alpha_0(\lambda), \ldots, \alpha_{n-1}(\lambda) \) ограничены на \( \mathbb{C} \), т. е. они постоянны: \( \alpha_i(\lambda) = \alpha_i \). Пусть \( p(T) = T^n - \alpha_{n-1}T^{n-1} - \ldots - \alpha_0I \). Тогда \( p(T)f_0(\lambda) = 0 \) для \( \lambda \in \mathbb{C} \setminus \Delta \), а значит, \( p(T)f_0(\lambda) = 0 \) для всех \( \lambda \). В частности, \( p(T)\xi_0 = 0 \). Следовательно, \( p = p_0 \) и \( p_0(T)\eta = 0 \).

Задачи

7.1. Векторы \( e_1, \ldots, e_{m+1} \) в \( \mathbb{R}^n \) линейно независимы. Докажите, что среди их линейных комбинаций есть ненулевой вектор, у которого первые \( m \) координат нулевые.

7.2. В пространстве \( V^n \) даны векторы \( e_1, \ldots, e_m \). Докажите, что если \( m \geq n+2 \), то существуют такие числа \( \alpha_1, \ldots, \alpha_m \), не все равные нулю, что \( \bullet \alpha_i e_i = 0 \) и \( \bullet \alpha_i = 0 \).

7.3. Выпуклой линейной комбинацией векторов \( v_1, \ldots, v_m \) называют любой вектор \( x = t_1 v_1 + \ldots + t_m v_m \), где \( t_i \geq 0 \) и \( \bullet t_i = 1 \). Докажите, что