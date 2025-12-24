---
source_image: page_018.png
page_number: 18
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 100.43
tokens: 12342
characters: 2521
timestamp: 2025-12-24T07:33:20.296472
finish_reason: stop
---

Задание вероятностного пространства — первый необходимый шаг при построении математической модели любого эксперимента.

Теорема 1. Вероятность обладает следующими свойствами.
1. \( \mathbf{P}(\overline{A}) = 1 - \mathbf{P}(A),\ \mathbf{P}(\varnothing) = 0 \).
2. Если \( A \subset B \), то \( \mathbf{P}(A) \leqslant \mathbf{P}(B) \) (монотонность вероятности).
3. \( \mathbf{P}(A \cup B) = \mathbf{P}(A) + \mathbf{P}(B) - \mathbf{P}(A \cap B) \).
4. \( \mathbf{P}(A \cup B) \leqslant \mathbf{P}(A) + \mathbf{P}(B) \).
5. Для любых \( A_1, \ldots, A_n \) имеет место формула включения-исключения:

\[
\mathbf{P}(A_1 \cup \ldots \cup A_n) = \sum_{i=1}^n \mathbf{P}(A_i) - \sum_{i<j} \mathbf{P}(A_i A_j) + \sum_{i<j<m} \mathbf{P}(A_i A_j A_m) - \ldots + (-1)^{n-1} \mathbf{P}(A_1 A_2 \ldots A_n).
\]

Доказательство. 1. Достоверное событие \( \Omega = A \cup \overline{A} \) есть объединение двух независимых событий \( A \) и \( \overline{A} \). Из аксиом (Р2) и (Р3) получим

\[
1 = \mathbf{P}(\Omega) = \mathbf{P}(A) + \mathbf{P}(\overline{A}),\quad \mathbf{P}(\varnothing) = 1 - \mathbf{P}(\Omega) = 0.
\]

2. Представим событие \( B \) в виде объединения двух независимых событий: \( B = A \cup (B \setminus A) \). По аксиомам (Р2) и (Р1),

\[
\mathbf{P}(B) = \mathbf{P}(A) + \mathbf{P}(B \setminus A) \geqslant \mathbf{P}(A),
\]
поскольку \( \mathbf{P}(B \setminus A) \geqslant 0 \).

3. Событие \( A \cup B \) можно разложить в объединение двух независимых событий \( A \cup B = A \cup (B \setminus AB) \). Событие \( B = (B \setminus AB) \cup AB \) тоже складывается из двух независимых событий. По аксиоме (Р2) получаем, что \( \mathbf{P}(B) = \mathbf{P}(B \setminus AB) + \mathbf{P}(AB) \) и

\[
\mathbf{P}(A \cup B) = \mathbf{P}(A) + \mathbf{P}(B \setminus AB) = \mathbf{P}(A) + \mathbf{P}(B) - \mathbf{P}(AB).
\]

4. Доказательство очевидно:

\[
\mathbf{P}(A \cup B) = \mathbf{P}(A) + \mathbf{P}(B) - \mathbf{P}(AB) \leqslant \mathbf{P}(A) + \mathbf{P}(B).
\]

5. Докажем свойство 5 для \( n = 3 \). Трижды воспользуемся свойством 3:

\[
\begin{align*}
\mathbf{P}(A \cup B \cup C) &= \mathbf{P}((A \cup B) \cup C)) = \mathbf{P}(A \cup B) + \mathbf{P}(C) - \mathbf{P}((A \cup B) \cap C) = \\
&= \mathbf{P}(A) + \mathbf{P}(B) - \mathbf{P}(AB) + \mathbf{P}(C) - \mathbf{P}(AC \cup BC) = \\
&= \mathbf{P}(A) + \mathbf{P}(B) + \mathbf{P}(C) - \mathbf{P}(AB) - \mathbf{P}(AC) - \mathbf{P}(BC) + \mathbf{P}(ABC).
\end{align*}
\]

Читатель докажет свойство 5 для произвольного \( n \) методом математической индукции. □