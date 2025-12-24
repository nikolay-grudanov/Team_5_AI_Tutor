---
source_image: page_071.png
page_number: 71
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 79.53
tokens: 12839
characters: 3768
timestamp: 2025-12-24T05:30:30.531748
finish_reason: stop
---

ничиению в \( \forall \)-правиле, переменная \( x \) не входит свободно в \( C \). Значит, \( x \) не входит свободно в \( A_m \& C \). Используем это для обоснования нового применения \( \forall \)-правила на \((k_2 + 1')\)-м шаге:

\[
\begin{array}{ll}
k'_1. & A_m \supset B_g', \text{ т. е. } A_m \supset (C \supset A(x)) \\
k'_2. & A_m \& C \supset A(x) \\
k_2 + 1'. & A'_m \& C \supset \forall xA(x) — \forall\text{-правило}, k'_2 \\
k'_3. & A_m \supset (C \supset \forall xA(x)), \text{ т. е. } A_m \supset B_i
\end{array}
\]

вывод из примера 7 § 10.

из упр. 10.3.

Случай 6. \( B_i \) (\( i > n \)) получается из предшествующей формулы \( B_g' \) (\( g < i \)) применением \( \exists \)-правила. Рассмотрение предоставим читателю (упр. 22.1).

Итак, мы видели, как строить конкретный вывод \( A_m \supset B \) из \( A_1, \ldots, A_{m-1} \). Применения \( \forall \) и \( \exists \)-правил в этом «результатирующем выводе» находятся в соответствии с применением тех же правил в данном выводе: переменные \( x \) соответствующих друг другу применений совпадают, а сами эти применения расположены одинаково по отношению к \( A_1, \ldots, A_{m-1} \). И так как все переменные в данном выводе остаются фиксированными, то все они фиксированы в результирующем выводе. Значит, \( A_1, \ldots, A_{m-1} \vdash \vdash A_m \supset B \), что и требовалось доказать.

Пример 14. Левый столбец показывает, что \( \forall x(P(x) \supset Q(x)), \forall xP(x) \vdash \forall xQ(x) \). Согласно теореме, отсюда следует \( \forall x(P(x) \supset \supset Q(x)) \vdash \forall xP(x) \supset \forall xQ(x) \). Правый столбец и дает вывод \( \forall xP(x) \supset \forall xQ(x) \) из \( \forall x(P(x) \supset Q(x)) \), построенный в соответствии с нашим общим методом из левого столбца. Так как второе допущение появляется только в строке 4, приписывание «\( \forall xP(x) \supset \)» начинается только с этой строки.

1. \( \forall x(P(x) \supset Q(x)) — 1\)-е доп.
2. \( \forall x(P(x) \supset Q(x)) \supset (P(x) \supset \supset Q(x)) — \forall\text{-схема}.
3. \( P(x) \supset Q(x) — MP, 1, 2.
4. \( \forall xP(x) — 2\)-е доп.
5. \( \forall xP(x) \supset P(x) — \forall\text{-схема}.
6. \( P(x) — MP, 4, 5.
7. \( Q(x) — MP, 6, 3.
8. \( Q(x) \supset ((P \supset PVP) \supset Q(x)) — схема аксиом 1a.
9. \( (P \supset PVP) \supset Q(x) — MP, 7, 8.
10. \( (P \supset PVP) \supset \forall xQ(x) — \forall\text{-правило, 9.
11. \( P \supset PVP — схема аксиом 5a.
12. \( \forall xQ(x) — MP, 11, 10.

13'. \( \{ \forall xP(x) \supset (\forall xP(x) \supset \supset P(x)) \} \supset \{ \forall xP(x) \supset \supset P(x) \} — MP, 8', 12'.
14'. \( \forall xP(x) \supset P(x) — MP, 11', 13'.
15'. \( \{ P(x) \supset Q(x) \} \supset \{ \forall xP(x) \supset \supset (P(x) \supset Q(x)) \} — схема аксиом 1a.
16'. \( \forall xP(x) \supset (P(x) \supset Q(x)) — MP, 3', 15'.
17'. \( \{ \forall xP(x) \supset P(x) \} \supset \{ \{ \forall xP(x) \supset (P(x) \supset \supset Q(x)) \} \supset \{ \forall xP(x) \supset \supset Q(x) \} \} — схема аксиом 1b.
18'. \( \{ \forall xP(x) \supset (P(x) \supset Q(x)) \} \supset \{ \forall xP(x) \supset Q(x) \} — MP, 14, 17.
19'. \( \forall xP(x) \supset Q(x) — MP, 16', 18'.
22'. \( \forall xP(x) \supset \{ Q(x) \supset ((P \supset PVP) \supset Q(x)) \} — аналогично 9' — 11'.
25'. \( \forall xP(x) \supset \{ (P \supset PVP) \supset Q(x) \} — аналогично 12' — 14'.
k'_1. \( \forall xP(x) \& \& (P \supset PVP) \supset Q(x) — пример 7 § 10.
k_1 + 1'. \( \forall xP(x) \& \& (P \supset PVP) \supset Q(x) — \forall\text{-правило, } k'_1 — упр. 10.3.
k'_2. \( \forall xP(x) \supset \{ (P \supset PVP) \supset \forall xQ(x) \} — аналогично 9' — 11'.
k_2 + 3'. \( \forall xP(x) \supset \{ (P \supset PVP) \supset \forall xQ(x) \} — аналогично 12' — 14'.