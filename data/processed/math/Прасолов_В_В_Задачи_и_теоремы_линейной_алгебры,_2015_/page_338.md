---
source_image: page_338.png
page_number: 338
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.64
tokens: 6651
characters: 2925
timestamp: 2025-12-24T08:16:57.435880
finish_reason: stop
---

34.1. Отображения, сохраняющие ранг 1

Если \( A: U \to U \) и \( B: V \to V \) — невырожденные линейные операторы, то линейный оператор \( T = A \otimes B: U \otimes V \to U \otimes V \) сохраняет ранг элементов \( U \otimes V \). В случае когда \( \dim U = \dim V \), есть ещё один тип преобразований, сохраняющих ранг элементов \( U \otimes V \). Возьмём произвольный изоморфизм \( \varphi: U \to V \) и зададим отображение \( S: U \otimes V \to U \otimes V \) формулой \( S(u \otimes v) = \varphi^{-1}v \otimes \varphi u \). Тогда любое преобразование вида \( TS \), где \( T = A \otimes B \) — преобразование первого типа, сохраняет ранг элементов \( U \otimes V \).

Замечание. Легко проверить, что \( S \) — инволюция.

В матричном виде преобразование первого типа запишется как \( X \mapsto AXB \), а преобразование второго типа как \( X \mapsto AX^T B \). Преобразование второго типа не сводится к преобразованию первого типа (см. задачу 34.1).

Теорема 34.1.1. Пусть линейное отображение \( T: U \otimes V \to U \otimes V \) переводит любой элемент ранга 1 в элемент ранга 1. Тогда \( T = A \otimes B \) или \( T = (A \otimes B)S \), причём второй случай возможен, только если \( \dim U = \dim V \).

Доказательство [ГЗ]. Нам потребуется следующее утверждение.

Лемма. Пусть элементы \( \alpha_1, \alpha_2 \in U \otimes V \) таковы, что \( \operatorname{rk}(t_1\alpha_1 + t_2\alpha_2) \leq 1 \) для любых чисел \( t_1 \) и \( t_2 \). Тогда \( \alpha_i \) можно представить в виде \( \alpha_i = u_i \otimes v_i \), где \( u_1 = u_2 \) или \( v_1 = v_2 \).

Доказательство. Предположим, что \( \alpha_i = u_i \otimes v_i \), \( \alpha_1 + \alpha_2 = u \otimes v \) и \( \langle u_1 \rangle \neq \langle u_2 \rangle \), \( \langle v_1 \rangle \neq \langle v_2 \rangle \). Тогда можно считать, что \( \langle u \rangle \neq \langle u_1 \rangle \). С одной стороны, \( (f \otimes g)(u \otimes v) = f(u)g(v) \). С другой стороны,

\[
(f \otimes g)(u \otimes v) = (f \otimes g)(u_1 \otimes v_1 + u_2 \otimes v_2) = f(u_1)g(v_1) + f(u_2)g(u_2).
\]

Поэтому, выбрав \( f \in U^* \) и \( g \in V^* \) так, что \( f(u) = 0, f(u_1) \neq 0 \) и \( g(u_2) = 0, g(u_1) \neq 0 \), приходим к противоречию. \( \square \)

В дальнейшем будем считать, что \( \dim V \geq \dim U \geq 2 \). Кроме того, для удобства фиксированные векторы будем обозначать \( a \) и \( b \), а векторы, в качестве которых можно взять любые векторы пространств \( U \) и \( V \), будем обозначать \( u \) и \( v \). Применив лемму к \( T(a \otimes b_1) \) и \( T(a \otimes b_2) \), где \( \langle b_1 \rangle \neq \langle b_2 \rangle \), получим, что \( T(a \otimes b_i) = a' \otimes b'_i \) или \( T(a \otimes b_i) = a'_i \otimes b' \). Так как \( T(a \otimes (\lambda b_1 - \mu b_2)) = 0 \) только при \( \lambda = \mu = 0 \), то \( \langle b'_1 \rangle \neq \langle b'_2 \rangle \) (соответственно \( \langle a'_1 \rangle \neq \langle a'_2 \rangle \)).