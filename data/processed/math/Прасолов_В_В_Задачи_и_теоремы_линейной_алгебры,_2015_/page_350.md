---
source_image: page_350.png
page_number: 350
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 59.46
tokens: 7387
characters: 4337
timestamp: 2025-12-24T08:17:37.139064
finish_reason: stop
---

32.5. Пусть \( W_1 = \langle e_1, \ldots, e_{2n} \rangle \). Докажем, что \( W = W_1 \). Пространство \( W \) является наименьшим пространством, для которого \( \Lambda \subset \Lambda^2 W \) (теорема 32.2.1). Ясно, что \( \Lambda \subset \Lambda^2 W_1 \), поэтому \( W \subset W_1 \) и \( \dim W \leq \dim W_1 = 2n \). С другой стороны, \( \Lambda^n \omega = n! \, e_1 \wedge \ldots \wedge e_{2n} \) (см. задачу 30.3) и \( \Lambda^2 \omega \in \Lambda^{2n} W \). Поэтому \( \Lambda^{2n} W \neq 0 \), т. е. \( \dim W \geq 2n \).

32.6. При замене базисов пространств \( X \) и \( Y \) тензоры \( z_1 \) и \( z_2 \) заменяются на пропорциональные им тензоры, поэтому можно считать, что \( z_1 + z_2 = (v_1 \wedge \ldots \wedge v_k) \wedge (x_1 \wedge \ldots \wedge x_{r-k} + y_1 \wedge \ldots \wedge y_{r-k}) \), где \( v_1, \ldots, v_k \) — базис пространства \( X \cap Y \), а векторы \( x_1, \ldots, x_{r-k} \) и \( y_1, \ldots, y_{r-k} \) дополняют его до базисов пространств \( X \) и \( Y \). Предположим, что \( z_1 + z_2 = u_1 \wedge \ldots \wedge u_r \). Пусть \( u = v + x + y \), где \( v \in \langle v_1, \ldots, v_k \rangle \), \( x \in \langle x_1, \ldots, x_{r-k} \rangle \) и \( y \in \langle y_1, \ldots, y_{r-k} \rangle \). Тогда \( (z_1 + z_2) \wedge u = (v_1 \wedge \ldots \wedge v_k) \wedge (x_1 \wedge \ldots \wedge x_{r-k} \wedge y + y_1 \wedge \ldots \wedge y_{r-k} \wedge x) \). Если \( r - k > 1 \), то ненулевые тензоры \( x_1 \wedge \ldots \wedge x_{r-k} \wedge y \) и \( y_1 \wedge \ldots \wedge y_{r-k} \wedge x \) будут линейно независимы. Значит, в этом случае из равенства \( (z_1 + z_2) \wedge u = 0 \) следует, что \( u \in \langle v_1, \ldots, v_k \rangle \), т. е. \( \langle u_1, \ldots, u_r \rangle \subset \langle v_1, \ldots, v_k \rangle \) и \( r \leq k \). Получено противоречие, поэтому \( r - k = 1 \).

32.7. Любые два подпространства \([w_1]\) и \([w_2]\) имеют общее \((k-1)\)-мерное подпространство (см. задачу 32.6). Остаётся воспользоваться теоремой 9.9.1.

32.8. Если \( \Lambda \subset \Lambda^k W_1 \) и \( v^* \in W_1^\perp \), то \( i(v^*)\Lambda = 0 \), поэтому \( W_1^\perp \subset \Lambda^\perp \), а значит, \( W_1 \supset (\Lambda^\perp)^\perp \). Остаётся доказать, что \( \Lambda \subset \Lambda^k W \). Пусть \( V = W \oplus U \), \( u_1, \ldots, u_a \) — базис пространства \( U \), \( w_1, \ldots, w_{n-a} \) — базис пространства \( W \), \( u_1^*, \ldots, w_{n-a}^* \) — двойственный базис пространства \( V^* \). Тогда \( u_j^* \in W^\perp = \Lambda^\perp \), поэтому \( i(u_j^*)\Lambda = 0 \). Если \( j \in \{j_1, \ldots, j_b\} \) и \( \{j'_1, \ldots, j'_{b-1}\} \cup \{j\} = \{j_1, \ldots, j_b\} \), то отображение \( i(u_j^*) \) переводит тензор \( w_{i_1} \wedge \ldots \wedge w_{i_{k-b}} \wedge u_{j_1} \wedge \ldots \wedge u_{j_b} \) в \( \lambda w_{i_1} \wedge \ldots \wedge w_{i_{k-b}} \wedge u_{j'_1} \wedge \ldots \wedge u_{j'_{b-1}} \); в противном случае отображение \( i(u_j^*) \) переводит этот тензор в нуль. Поэтому
\[
i(u_j^*) \wedge^{k-b} W \otimes \wedge^b U \subset \wedge^{k-b} W \otimes \wedge^{b-1} U.
\]
Пусть \( \bullet \Lambda_\alpha \otimes u_\alpha \) — компонента некоторого элемента пространства \( \Lambda \), лежащая в пространстве \( \wedge^{k-1} W \otimes \wedge^1 U \). Тогда \( i(u_\beta^*)(\bullet \Lambda_\alpha \otimes u_\alpha) = 0 \), а значит,
\[
0 = \left\langle i(u_\beta^*) \bullet \Lambda_\alpha \otimes u_\alpha, f \right\rangle = \left\langle \bullet \Lambda_\alpha \otimes u_\alpha, u_\beta^* \wedge f \right\rangle = \langle \Lambda_\beta \otimes u_\beta, u_\beta^* \wedge f \rangle \text{ для всех } f.
\]
Но если \( \Lambda_\beta \otimes u_\beta \neq 0 \), то \( f \) можно подобрать так, что \( \langle \Lambda_\beta \otimes u_\beta, u_\beta^* \wedge f \rangle \neq 0 \). Аналогично доказывается, что компоненты любого элемента пространства \( \Lambda \) в слагаемых \( \wedge^{k-i} W \otimes \wedge^i U \) нулевые при \( i > 0 \).

§ 33. Тензорный ранг

33.1. Дополним базис \( e_1, \ldots, e_k \) пространства \( U \) до базиса \( e_1, \ldots, e_n \) пространства \( V \). Пусть \( T = \bullet \alpha_i v_1^i \otimes \ldots \otimes v_p^i \). Каждый элемент \( v_j^i \in V \) можно представить в виде \( v_j^i = u_j^i + w_j^i \), где \( u_j^i \in U \) и \( w_j^i \in \langle e_{k+1}, \ldots, e_n \rangle \). Поэтому