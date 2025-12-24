---
source_image: page_411.png
page_number: 411
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.46
tokens: 6477
characters: 2431
timestamp: 2025-12-24T08:18:49.373236
finish_reason: stop
---

43.8. Докажите, что если \( A \) — диагонализируемая матрица и \( \operatorname{ad}_A^n X = 0 \), то \( \operatorname{ad}_A X = 0 \).

43.9. а) Докажите, что если \( \operatorname{tr}(AXY) = \operatorname{tr}(AYX) \) для любых матриц \( X \) и \( Y \), то \( A = \lambda I \).
    б) Пусть \( f \) — линейная функция на пространстве матриц порядка \( n \). Докажите, что если \( f(XY) = f(YX) \) для любых матриц \( X \) и \( Y \), то \( f(X) = \lambda \operatorname{tr} X \).

§ 44. Теория реплик

44.1. Определение и основные свойства

Любому линейному оператору \( A : V \to V \) можно сопоставить линейный оператор \( A_{p,q} : T_q^p(V) \to T_q^p(V) \), заданный следующим образом:

\[
A_{p,q}(v_1 \otimes \ldots \otimes v_p \otimes f_1 \otimes \ldots \otimes f_q) =
\]
\[
= A(v_1) \otimes v_2 \otimes \ldots \otimes v_p \otimes f_1 \otimes \ldots \otimes f_q +
\]
\[
+ v_1 \otimes A(v_2) \otimes \ldots \otimes v_p \otimes f_1 \otimes \ldots \otimes f_q + \ldots
\]
\[
\ldots - v_1 \otimes \ldots \otimes v_p \otimes A^*(f_1) \otimes \ldots \otimes f_q - \ldots
\]
\[
\ldots - v_1 \otimes \ldots \otimes v_p \otimes f_1 \otimes \ldots \otimes A^*(f_q).
\]

Например, если мы отождествим пространства \( T_1^1(V) \) и \( \operatorname{Hom}(V, V) \), то для \( X \in \operatorname{Hom}(V, V) \) получаем \( A_{1,1}(X) = AX - XA = [A, X] \).

Линейный оператор \( B : V \to V \) называют репликой \( A \), если \( \operatorname{Ker} A_{p,q} \subset \operatorname{Ker} B_{p,q} \) для всех \( p, q \). Это понятие ввёл Шевалле [Ch1]. То, что \( B \) — реплика \( A \), мы будем обозначать \( A \twoheadrightarrow B \).

Теорема 44.1.1. Если \( A \twoheadrightarrow B \), то \( B \) можно представить в виде многочлена от \( A \) без свободного члена.

Доказательство. Условие \( \operatorname{Ker} A_{1,1} \subset \operatorname{Ker} B_{1,1} \) означает, что любой оператор \( X \), коммутирующий с \( A \), коммутирует также и с \( B \). Поэтому согласно теореме 42.3.1 \( B = g(A) \), где \( g \) — некоторый многочлен. Остаётся доказать, что \( g \) можно выбрать так, что \( g(0) = 0 \). Рассмотрим для этого два случая.

Случай 1. \( \det A \neq 0 \).
В этом случае минимальный многочлен матрицы \( A \) имеет ненулевой свободный член, поэтому для любого \( \lambda \) матрицу \( \lambda I \) можно представить как многочлен от \( A \) без свободного члена. Этот многочлен можно подставить в \( g(A) \) вместо свободного члена.