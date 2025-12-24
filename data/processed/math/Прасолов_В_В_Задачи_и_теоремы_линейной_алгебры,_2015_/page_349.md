---
source_image: page_349.png
page_number: 349
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 51.30
tokens: 7160
characters: 3741
timestamp: 2025-12-24T08:17:25.106927
finish_reason: stop
---

31.2. Легко проверить, что \( G = XJX^T \), где \( J = \mathrm{diag}\left( \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \ldots, \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \right) \).
Поэтому \( \mathrm{Pf}(G) = \det X \).

§ 32. Разложимые тензоры

32.1. Ясно, что если \( \omega = \omega_1 \wedge e_1 \wedge \ldots \wedge e_r \), то \( \omega \wedge e_i = 0 \). Предположим теперь, что \( w \wedge e_i = 0 \) при \( i = 1, \ldots, r \) и \( e_1 \wedge \ldots \wedge e_r \neq 0 \). Дополним векторы \( e_1, \ldots, e_r \) до базиса \( e_1, \ldots, e_n \) пространства \( V \). Тогда \( \omega = \bullet\ a_{i_1 \ldots i_k} e_{i_1} \wedge \ldots \wedge e_{i_k} \), причём
• \( a_{i_1 \ldots i_k} e_{i_1} \wedge \ldots \wedge e_{i_k} \wedge e_i = \omega \wedge e_i = 0 \) при \( i = 1, \ldots, r \). Если ненулевые тензоры \( e_{i_1} \wedge \ldots \wedge e_{i_k} \wedge e_i \) линейно зависимы, то тензоры \( e_{i_1} \wedge \ldots \wedge e_{i_k} \) тоже линейно зависимы. Поэтому \( a_{i_1 \ldots i_k} = 0 \) при \( i \notin \{i_1, \ldots, i_k\} \). Следовательно, \( a_{i_1 \ldots i_k} \neq 0 \), только если \( \{1, \ldots, r\} \subset \{i_1, \ldots, i_k\} \), а значит,
\[
\omega = \left( \bullet\ b_{i_1 \ldots i_{k-r}} e_{i_1} \wedge \ldots \wedge e_{i_{k-r}} \right) \wedge e_1 \wedge \ldots \wedge e_r.
\]

32.2. Пусть \( e_1, \ldots, e_n \) — базис \( V \), \( \varepsilon_1, \ldots, \varepsilon_n \) — двойственный базис \( V^* \). Можно считать, что \( \omega = e_1 \wedge \ldots \wedge e_n \). Пусть \( \alpha = \varepsilon_{i_1} \wedge \ldots \wedge \varepsilon_{i_p} \), где \( i_1 < \ldots < i_p \). Тогда
\[
\langle i(\alpha)\omega, \bullet\ x_{j_1 \ldots j_{n-p}} \varepsilon_{j_1} \wedge \ldots \wedge \varepsilon_{j_{n-p}} \rangle =
= \langle e_1 \wedge \ldots \wedge e_n, \bullet\ x_{j_1 \ldots j_{n-p}} \varepsilon_{i_1} \wedge \ldots \wedge \varepsilon_{i_p} \wedge \varepsilon_{j_1} \wedge \ldots \wedge \varepsilon_{j_{n-p}} \rangle =
= \frac{1}{n!} x_{j_1 \ldots j_{n-p}},
\]
где набор индексов \( j_1, \ldots, j_{n-p} \) дополняет набор \( i_1, \ldots, i_p \). Таким образом, \( i(\varepsilon_{i_1} \wedge \ldots \wedge \varepsilon_{i_p})\omega = \varepsilon_{j_1} \wedge \ldots \wedge \varepsilon_{j_{n-p}} \). Ясно, что такое отображение является изоморфизмом.

Любой разложимый элемент \( \alpha \) можно представить в виде \( \alpha = \varepsilon_1 \wedge \ldots \wedge \varepsilon_p \). Дополним векторы \( \varepsilon_1, \ldots, \varepsilon_p \) до базиса \( \varepsilon_1, \ldots, \varepsilon_n \). Пусть \( e_1, \ldots, e_n \) — двойственный базис. Если \( \omega = e_1 \wedge \ldots \wedge e_n \), то \( i(\alpha)\omega = e_{p+1} \wedge \ldots \wedge e_n \).

32.3. Первое решение. Согласно задаче 32.2 пространство \( \Lambda^{n-1}V \) изоморфно \( \Lambda^1 V^* \cong V^* \), причём при этом изоморфизме разложимые элементы \( \Lambda^1 V^* \) соответствуют разложимым элементам \( \Lambda^{n-1}V \). Но в \( \Lambda^1 V^* \) все элементы разложимые.

Второе решение. Рассмотрим линейное отображение \( f : V \to \Lambda^n(V) \), заданное формулой \( f(v) = v \wedge \omega \). Так как \( \dim \Lambda^n(V) = 1 \), то \( \dim \mathrm{Ker}\ f \geq n-1 \). Поэтому существуют линейно независимые векторы \( e_1, \ldots, e_{n-1} \), лежащие в \( \mathrm{Ker}\ f \), т. е. \( e_i \wedge \omega = 0 \) при \( i = 1, \ldots, n-1 \). Согласно задаче 32.1 \( \omega = \lambda e_1 \wedge \ldots \wedge e_{n-1} \).

32.4. Для кососимметрического тензора \( \omega \in \Lambda^2(\mathbb{R}^4) \) условие \( \omega \wedge \omega = 0 \) эквивалентно равенству \( a_{12}a_{34} - a_{13}a_{24} + a_{14}a_{23} = 0 \). В свою очередь, это равенство является единственным соотношением Плюккера в рассматриваемой ситуации.