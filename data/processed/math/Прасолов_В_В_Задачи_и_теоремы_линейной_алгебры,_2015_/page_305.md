---
source_image: page_305.png
page_number: 305
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.15
tokens: 6565
characters: 2515
timestamp: 2025-12-24T08:15:48.318374
finish_reason: stop
---

Доказательство. Ясно, что

\[(A^*)^* = G^{-1}(G^{-1}A^T G)^T G = G^{-1}G^T A (G^{-1})^T G = G^{-1}G^T A (G^{-1}G^T)^{-1}.\]

Поэтому равенство \((A^*)^* = A\) эквивалентно тому, что матрица \(G^{-1}G^T\) коммутирует с \(A\).

Матрица \(G^{-1}G^T\) коммутирует со всеми матрицами тогда и только тогда, когда \(G^{-1}G^T = \lambda I\) (задача 42.2), т. е. \(G^T = \lambda G\). В таком случае \(G = (G^T)^T = \lambda G^T = \lambda^2 G\), поэтому \(\lambda = \pm 1\).

Следствие. Пусть \(g(x, y) — невырожденная билинейная форма, причём из равенства \(g(x, y) = g(u, v)\) следует равенство \(g(y, x) = g(v, u)\). Тогда форма \(g\) симметрическая или кососимметрическая.

Доказательство. По определению \(g(Ay, x) = g(y, A^*x)\), поэтому

\[g(x, Ay) = g(A^*x, y) = g(x, (A^*)^*y).\]

Таким образом, \((A^*)^* = A\) для любого оператора \(A\).

29.3. Изоморфизм \(V^* \otimes W \to \mathrm{Hom}(V, W)\)

Теорема 29.3.1. Пусть \(\mathrm{Hom}(V, W) — пространство линейных отображений \(V\) в \(W\). Тогда существует канонический изоморфизм \(\alpha : V^* \otimes W \to \mathrm{Hom}(V, W)\).

Доказательство. Пусть \(\{e_i\}\) и \(\{\varepsilon_j\} — базисы \(V\) и \(W\). Положим

\[\alpha(e_i^* \otimes \varepsilon_j)v = e_i^*(v)\varepsilon_j = v_i\varepsilon_j\]

и продолжим отображение \(\alpha\) по линейности. Если \(v \in V,\ f \in V^*\) и \(w \in W\), то \(\alpha(f \otimes w)v = f(v)w\), поэтому \(\alpha\) можно определить инвариантно.

Пусть \(Ae_p = \sum_q a_{qp}\varepsilon_q\), тогда \(A\left(\sum_p v_p e_p\right) = \sum_{p, q} a_{qp} v_p \varepsilon_q\). Поэтому отображению \(\alpha(e_i^* \otimes \varepsilon_j)\) соответствует матрица \((a_{qp})\), где \(a_{qp} = \delta_{qj}\delta_{pi}\). Такие матрицы образуют базис пространства \(\mathrm{Hom}(V, W)\). Ясно также, что размерности пространств \(V^* \otimes W\) и \(\mathrm{Hom}(V, W)\) равны.

Теорема 29.3.2. Пусть \(V — линейное пространство над полем \(K\). Рассмотрим отображение свёртки \(\varepsilon : V^* \otimes V \to K\), заданное формулой \(\varepsilon(x^* \otimes y) = x^*(y)\) и продолженное по линейности. Тогда \(\operatorname{tr} A = \varepsilon \alpha^{-1}(A)\) для любого линейного оператора \(A\) в пространстве \(V\).

Доказательство. Выберем в пространстве \(V\) базис. Доказательство достаточно провести для матриц \(I_{ij} = (a_{qp})\), где \(a_{qp} = \delta_{qj}\delta_{pi}\). Ясно, что \(\operatorname{tr} I_{ij} = \delta_{ij}\) и \(\varepsilon \alpha^{-1}(I_{ij}) = \varepsilon(e_i^* \otimes e_j) = e_i^*(e_j) = \delta_{ij}\).