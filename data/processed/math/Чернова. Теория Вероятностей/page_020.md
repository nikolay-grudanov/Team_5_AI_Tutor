---
source_image: page_020.png
page_number: 20
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 68.87
tokens: 11667
characters: 2042
timestamp: 2025-12-24T08:24:58.393707
finish_reason: stop
---

Свойства (Р1) — (РЗ) часто называют «аксиомами вероятности».

Определение 14. Тройка \( \langle \Omega, \mathcal{F}, \mathbf{P} \rangle \), в которой \( \Omega \) — пространство элементарных исходов, \( \mathcal{F} \) — \( \sigma \)-алгебра его подмножеств и \( \mathbf{P} \) — вероятностная мера на \( \mathcal{F} \), называется вероятностным пространством.

Докажем свойства вероятности, вытекающие из аксиом. Здесь и в дальнейшем под знаком вероятности появляются только события!

0. \( \mathbf{P}(\varnothing) = 0 \).

Доказательство. События \( A_i = \varnothing, \ i = 1, 2, \ldots \), попарно несовместны, и их объединение есть также пустое множество. По аксиоме (Р2)

\[
\mathbf{P}(\varnothing) = \sum_{i=1}^{\infty} \mathbf{P}(A_i) = \sum_{i=1}^{\infty} \mathbf{P}(\varnothing).
\]

Это возможно только в случае \( \mathbf{P}(\varnothing) = 0 \).

1. Для любого конечного набора попарно несовместных событий \( A_1, \ldots, A_n \in \mathcal{F} \) имеет место равенство

\[
\mathbf{P}\left( \bigcup_{i=1}^{n} A_i \right) = \sum_{i=1}^{n} \mathbf{P}(A_i).
\]

Доказательство. Пусть \( A_i = \varnothing \) при любом \( i > n \). Вероятности этих событий, по предыдущему свойству, равны нулю. События \( A_1, \ldots, A_n, \varnothing, \varnothing, \varnothing, \ldots \) попарно несовместны, и, по аксиоме (Р2),

\[
\mathbf{P}\left( \bigcup_{i=1}^{n} A_i \right) = \mathbf{P}\left( \bigcup_{i=1}^{\infty} A_i \right) = \sum_{i=1}^{\infty} \mathbf{P}(A_i) = \sum_{i=1}^{n} \mathbf{P}(A_i).
\]

2. \( \mathbf{P}(\overline{A}) = 1 - \mathbf{P}(A) \).

Доказательство. \( A \cup \overline{A} = \Omega \), и события \( A, \overline{A} \) несовместны. По аксиоме (РЗ) и предыдущему свойству,

\( 1 = \mathbf{P}(\Omega) = \mathbf{P}(A) + \mathbf{P}(\overline{A}) \).

3. Если \( A \subseteq B \), то \( \mathbf{P}(B \setminus A) = \mathbf{P}(B) - \mathbf{P}(A) \).

Доказательство. \( B = A \cup (B \setminus A) \), и события \( A, B \setminus A \) несовместны. По аксиоме (Р2), \( \mathbf{P}(B) = \mathbf{P}(A) + \mathbf{P}(B \setminus A) \).