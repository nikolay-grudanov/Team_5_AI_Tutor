---
source_image: page_333.png
page_number: 333
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.84
tokens: 6528
characters: 2361
timestamp: 2025-12-24T08:16:43.078093
finish_reason: stop
---

Доказательство. Достаточно рассмотреть случай, когда \( \alpha = f_1 \wedge \ldots \wedge f_p \) и \( \beta = f_{p+1} \wedge \ldots \wedge f_{p+q} \). Ясно, что

\[
d(f_1 \wedge \ldots \wedge f_{p+q}) = \sum_{i \leq p} (-1)^{i+1} f_i(v) f_1 \wedge \ldots \wedge \hat{f}_i \wedge \ldots \wedge f_{p+q} + 
\]
\[
+ \sum_{j \geq 1} (-1)^{p+j+1} f_1 \wedge \ldots \wedge \hat{f}_{p+j+1} \wedge \ldots \wedge f_{p+q} =
\]
\[
= (d\alpha) \wedge \beta + (-1)^p \alpha \wedge (d\beta).
\]

Задачи

32.1. Пусть \( \omega \in \Lambda^k V \) и \( e_1 \wedge \ldots \wedge e_r \neq 0 \) для некоторых \( e_i \in V \). Докажите, что \( \omega = \omega_1 \wedge e_1 \wedge \ldots \wedge e_r \) тогда и только тогда, когда \( \omega \wedge e_i = 0 \) для \( i = 1, \ldots, r \).

32.2. Пусть \( \dim V = n \) и \( \omega \in \Lambda^n V, \omega \neq 0 \). Докажите, что отображение \( \Lambda^p V^* \to \Lambda^{n-p} V \), заданное формулой \( \alpha \mapsto i(\alpha)\omega \), является изоморфизмом, причём этот изоморфизм переводит разложимые элементы в разложимые.

32.3. Пусть \( \dim V = n \) и \( \omega \in \Lambda^{n-1} V \). Докажите, что \( \omega \) — разложимый кососимметрический тензор.

32.4. Докажите, что кососимметрический тензор \( \omega \in \Lambda^2(\mathbb{R}^4) \) разложим тогда и только тогда, когда \( \omega \wedge \omega = 0 \).

32.5. Пусть векторы \( e_1, \ldots, e_{2n} \) линейно независимы,
\[
\omega = \sum_{i=1}^n e_{2i-1} \wedge e_{2i}
\]
и \( \Lambda = \langle \omega \rangle \). Найдите размерность пространства \( W = (\Lambda^\perp)^\perp \).

32.6. Пусть тензоры \( z_1 = x_1 \wedge \ldots \wedge x_r \) и \( z_2 = y_1 \wedge \ldots \wedge y_r \) не пропорциональны, \( X = \langle x_1, \ldots, x_r \rangle \) и \( Y = \langle y_1, \ldots, y_r \rangle \). Докажите, что пространство \( \langle z_1, z_2 \rangle \) состоит из разложимых кососимметрических тензоров тогда и только тогда, когда \( \dim(X \cap Y) = r - 1 \).

32.7. Пусть подпространство \( W \subset \Lambda^k V \) состоит из разложимых кососимметрических тензоров. Сопоставим каждому элементу
\[
w = x_1 \wedge \ldots \wedge x_k \in W
\]
подпространство \( [w] = \langle x_1, \ldots, x_k \rangle \subset V \). Докажите, что либо все подпространства \( [w] \) имеют общее \( (k-1) \)-мерное подпространство, либо все они лежат в одном \( (k+1) \)-мерном подпространстве.