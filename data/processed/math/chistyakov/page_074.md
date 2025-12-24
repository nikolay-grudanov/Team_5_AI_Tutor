---
source_image: page_074.png
page_number: 74
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.43
tokens: 8091
characters: 2573
timestamp: 2025-12-24T07:27:55.709678
finish_reason: stop
---

Ности элементарных событий. Например, положим \( P(B_4(0111)) = = qppp = qp^3 \); в общем случае

\[
P(B_{n_k}(\varepsilon_1 \varepsilon_2 \ldots \varepsilon_{n_k})) = p^{\varepsilon_1} q^{1-\varepsilon_1} p^{\varepsilon_2} q^{1-\varepsilon_2} \ldots p^{\varepsilon_{n_k}} q^{1-\varepsilon_{n_k}},
\]

Тогда

\[
P(A_{n_1 n_2 \ldots n_k}(E_k)) = \sum P(B_{n_k}(\varepsilon_1 \varepsilon_2 \ldots \varepsilon_{n_k})),
\]

где суммирование проводится по всем значениям вектора \((\varepsilon_1, \varepsilon_2, \ldots, \varepsilon_{n_k})\), удовлетворяющим условию \((\varepsilon_1, \varepsilon_2, \ldots, \varepsilon_{n_k}) \in E_k\).

Одно и то же событие из алгебры \(F_0\) можно записать несколькими способами; можно формально увеличить число координат, на которые накладываются ограничения, а в множестве \(E_k\) вновь введенным координатам разрешить принимать любые значения. Например, события

\[
A_1(l) = \{ (l e_2 e_3 \ldots e_n \ldots ) \},
\]
\[
A_{12}(\{(1, 0), (1, 1)\}) = \{ (10e_3 \ldots ), (11e_3 \ldots ) \}
\]

совпадают. В связи с этим нужно проверить, что вероятность определяется формулой (4.2) однозначно. Для событий (4.3) имеем

\[
A_1(l) = B_1(l), \quad A_{12}(\{(1, 0), (1, 1)\}) = B_{12}(1, 0) + B_{12}(1, 1)
\]

и, следовательно, по формулам (4.1), (4.2)

\[
P(A_1(l)) = p, \quad P(A_{12}(\{(1, 0), (1, 1)\})) = pq + p^2 = p.
\]

Таким образом, при различной форме записи одного и того же события получили одинаковые значения вероятности. Аналогично проверяется общий случай.

Покажем теперь, что для вероятности, определенной формулами (4.1), (4.2), выполняется аксиома А4. Пусть \(C_1, C_2 \in F_0\). \(C_1 C_2 = \varnothing\) и \(n\) — наибольший номер координаты, на которую накладываются ограничения в какой-либо фиксированной форме записи событий \(C_1\) и \(C_2\). Тогда \(C_1\) и \(C_2\) можно записать в виде

\[
C_1 = A_{12 \ldots n}(E'_n), \quad C_2 = A_{12 \ldots n}(E''_n), \quad E'_n E''_n = \varnothing
\]

и, следовательно,

\[
\begin{align*}
P(C_1 + C_2) &= \sum_{\varepsilon \in E'_n + E''_n} P(B_n(\varepsilon)) = \\
&= \sum_{\varepsilon \in E'_n} P(B_n(\varepsilon)) + \sum_{\varepsilon \in E''_n} P(B_n(\varepsilon)) = P(C_1) + P(C_2), \\
\varepsilon &= (\varepsilon_1 \varepsilon_2 \ldots \varepsilon_n).
\end{align*}
\]

Проверим свойство непрерывности вероятности \(P\), определенной на \(F_0\). Если \(A_1 \supset A_2 \supset \ldots \supset A_n \supset A_{n+1} \supset \ldots\) и \(\bigcap_{n=1}^{\infty} A_n = \varnothing\), то, начиная с некоторого \(n_1\) имеем \(A_n = \varnothing\) (если бы \(A_n \neq \varnothing\) при