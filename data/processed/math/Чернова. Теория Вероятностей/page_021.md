---
source_image: page_021.png
page_number: 21
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 55.77
tokens: 11931
characters: 2370
timestamp: 2025-12-24T08:25:23.865358
finish_reason: stop
---

4. Если \( A \subseteq B \), то \( \mathbf{P}(A) \leqslant \mathbf{P}(B) \).

Доказательство. По предыдущему свойству, \( \mathbf{P}(A) = \mathbf{P}(B) - \mathbf{P}(B \setminus A) \leqslant \mathbf{P}(B) \). Последнее неравенство следует из (Р1), т.к. \( \mathbf{P}(B \setminus A) \geqslant 0 \).

5. \( 0 \leqslant \mathbf{P}(A) \leqslant 1 \).

Доказательство. \( \mathbf{P}(A) \geqslant 0 \) по (Р1), и т.к. \( A \subseteq \Omega \), то по предыдущему свойству \( \mathbf{P}(A) \leqslant \mathbf{P}(\Omega) = 1 \).

6. \( \mathbf{P}(A \cup B) = \mathbf{P}(A) + \mathbf{P}(B) - \mathbf{P}(A \cap B) \).

Доказательство. \( A \cap B \subseteq B \), поэтому \( \mathbf{P}(B \setminus (A \cap B)) = \mathbf{P}(B) - \mathbf{P}(A \cap B) \). Но события \( A \) и \( B \setminus (A \cap B) \) независимы, поэтому
\[
\mathbf{P}(A \cup B) = \mathbf{P}(A \cup B \setminus (A \cap B)) = \mathbf{P}(A) + \mathbf{P}(B \setminus (A \cap B)) = \mathbf{P}(A) + \mathbf{P}(B) - \mathbf{P}(A \cap B).
\]

7. \( \mathbf{P}(A \cup B) \leqslant \mathbf{P}(A) + \mathbf{P}(B) \).

Доказательство. Сразу следует из предыдущего свойства и аксиомы (Р1).

8. \( \mathbf{P}(A_1 \cup \ldots \cup A_n) \leqslant \sum_{i=1}^n \mathbf{P}(A_i) \). Доказать методом математической индукции.

9.
\[
\mathbf{P}(A_1 \cup A_2 \cup \ldots \cup A_n) = \sum_{i=1}^n \mathbf{P}(A_i) - \sum_{i<j} \mathbf{P}(A_i \cap A_j) + \sum_{i<j<m} \mathbf{P}(A_i \cap A_j \cap A_m) - \ldots + (-1)^{n-1} \mathbf{P}(A_1 \cap A_2 \cap \ldots \cap A_n).
\]
(2)

Доказательство. Воспользуемся методом математической индукции. Базис индукции при \( n = 2 \) — свойство 6 выше. Пусть свойство 9 верно при \( n = k - 1 \). Докажем, что тогда оно верно при \( n = k \).

\[
\mathbf{P}\left( \bigcup_{i=1}^k A_i \right) = \mathbf{P}\left( \left( \bigcup_{i=1}^{k-1} A_i \right) \cup A_k \right) = \mathbf{P}\left( \bigcup_{i=1}^{k-1} A_i \right) + \mathbf{P}(A_k) - \mathbf{P}\left( A_k \cap \bigcup_{i=1}^{k-1} A_i \right)
\]
(3)

По предположению индукции, первое слагаемое в правой части (3) равно
\[
\mathbf{P}\left( \bigcup_{i=1}^{k-1} A_i \right) = \sum_{i=1}^{k-1} \mathbf{P}(A_i) - \sum_{1 \leq i < j \leq k-1} \mathbf{P}(A_i \cap A_j) + \sum_{1 \leq i < j < m \leq k-1} \mathbf{P}(A_i \cap A_j \cap A_m) - \ldots + (-1)^{k-2} \mathbf{P}(A_1 \cap A_2 \cap \ldots \cap A_{k-1}).
\]
(4)

Вычитаемое в правой части (3) равно