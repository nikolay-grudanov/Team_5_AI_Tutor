---
source_image: page_162.png
page_number: 162
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.23
tokens: 7490
characters: 1216
timestamp: 2025-12-24T07:29:49.886921
finish_reason: stop
---

§ 1. Определение. Основные свойства

Определение цепи Маркова как частного случая общей схемы испытаний было дано в гл. 3. Дадим прямое определение. Последовательностью T испытаний, являющихся цепью Маркова с N состояниями, будем называть вероятностное пространство \((\Omega, \mathcal{F}, P)\), в котором

\[
\Omega = \{(l_0 l_1 \ldots l_T)\}, \quad l_i = 1, 2, \ldots, N, \quad t = 0, 1, \ldots, T,
\]

и вероятности \(p(l_0 l_1 \ldots l_T)\), приписываемые элементарным событиям \(\omega = (l_0 l_1 \ldots l_T)\), задаются формулой

\[
p(l_0 l_1 \ldots l_T) = q_{l_0} p_{l_0 l_1} p_{l_1 l_2} \cdots p_{l_{T-1} l_T},
\]

где

\[
q_k \geq 0, \quad k = 1, \ldots, N, \quad \sum_{k=1}^N q_k = 1
\]

и элементы матрицы

\[
P = \begin{pmatrix}
p_{11} & p_{12} & \cdots & p_{1N} \\
p_{21} & p_{22} & \cdots & p_{2N} \\
\cdots & \cdots & \cdots & \cdots \\
p_{N1} & p_{N2} & \cdots & p_{NN}
\end{pmatrix}
\]

удовлетворяют условию

\[
p_{ij} \geq 0, \quad i, j = 1, \ldots, N; \quad \sum_{j=1}^N p_{ij} = 1, \quad i = 1, \ldots, N.
\]

Алгебра событий \(\mathcal{F}\) состоит из всех подмножеств \(\Omega\); вероятность определяется формулой (1.6.6):

\[
P(A) = \sum_{(l_0 l_1 \ldots l_T) \in A} P(l_0 l_1 \ldots l_T).
\]