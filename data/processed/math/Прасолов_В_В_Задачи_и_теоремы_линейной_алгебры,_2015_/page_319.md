---
source_image: page_319.png
page_number: 319
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.85
tokens: 6713
characters: 2916
timestamp: 2025-12-24T08:16:21.468986
finish_reason: stop
---

{i_1, \ldots, i_p} в множестве \{1, \ldots, n\} и \sigma = (i_1, \ldots, i_p, j_1, \ldots, j_{n-p}); при этом предполагается, что \(i_1 < \ldots < i_p\) и \(j_1 < \ldots < j_{n-p}\). Отображение * переводит базис пространства \(\Lambda^p V\) в базис пространства \(\Lambda^{n-p} V\), поэтому оно является изоморфизмом. Это отображение называют отображением Ходжа.

Теорема 30.6.1. Квадрат отображения Ходжа действует на пространстве \(\Lambda^p V\) как умножение на \((-1)^{(n-p)p}\).

Доказательство. Ясно, что \(*(*(e_{i_1} \wedge \ldots \wedge e_{i_p})) = (-1)^{\sigma \tau} e_{i_1} \wedge \ldots \wedge e_{i_p}\), где \(\sigma = (i_1, \ldots, i_p, j_1, \ldots, j_{n-p})\) и \(\tau = (j_1, \ldots, j_{n-p}, i_1, \ldots, i_p)\). В перестановках \(\sigma\) и \(\tau\) элементы набора \((i_1, \ldots, i_p)\) не образуют инверсий; элементы набора \((j_1, \ldots, j_{n-p})\) тоже не образуют инверсий. Кроме того, для любой пары индексов \(\alpha\) и \(\beta\) ровно одна из пар \((i_\alpha, j_\beta)\) и \((j_\beta, i_\alpha)\) образует инверсию. Поэтому сумма числа инверсий в перестановке \(\sigma\) и числа инверсий в перестановке \(\tau\) равна \(p(n - p)\).

Отображение Ходжа зависит от выбора базиса в пространстве \(V\). Например, если вместо базиса \(e_1, e_2\) в 2-мерном пространстве взять базис \(\varepsilon_1, \varepsilon_2\), где \(\varepsilon_1 = e_2, \varepsilon_2 = e_1\), то отображение Ходжа изменит знак. Но если вместо одного ортонормированного базиса взять другой ортонормированный базис, который одинаково ориентирован с первым, то отображение Ходжа не изменится. Другими словами, имеет место следующее утверждение.

Теорема 30.6.2. Выбор скалярного произведения и ориентации в пространстве \(V\) однозначно задаёт отображение Ходжа.

Доказательство. Пусть \(A\) — ортогональная матрица, причём \(\det A = 1\). В таком случае \(\operatorname{adj} A = A^{-1} = A^T\), поэтому, применяя тождество Якоби (теорема 2.6.3), получаем, что для любой перестановки

\[
\tau = \begin{pmatrix}
\alpha_1 & \cdots & \alpha_p & \alpha_{p+1} & \cdots & \alpha_n \\
i_1 & \cdots & i_p & j_1 & \cdots & j_{n-p}
\end{pmatrix}
\]

имеет место равенство

\[
\left| \begin{array}{cccc}
a_{\alpha_1 i_1} & \cdots & a_{\alpha_1 i_p} \\
\cdots & \cdots & \cdots \\
a_{\alpha_p i_1} & \cdots & a_{\alpha_p i_p}
\end{array} \right| = (-1)^\tau \left| \begin{array}{cccc}
a_{\alpha_{p+1}, j_1} & \cdots & a_{\alpha_{p+1}, j_{n-p}} \\
\cdots & \cdots & \cdots \\
a_{\alpha_n, j_1} & \cdots & a_{\alpha_n, j_{n-p}}
\end{array} \right|.
\]

Поэтому отображение *, которое задаётся базисом \(e_1, \ldots, e_n\), переводит вектор

\[
A e_{\alpha_1} \wedge \ldots \wedge A e_{\alpha_p} = \bigotimes_{i_1 < \ldots < i_p} \left| \begin{array}{cccc}
a_{\alpha_1 i_1} & \cdots & a_{\alpha_1 i_p} \\
\cdots & \cdots & \cdots \\
a_{\alpha_p i_1} & \cdots & a_{\alpha_p i_p}
\end{array} \right| e_{i_1} \wedge \ldots \wedge e_{i_p}
\]