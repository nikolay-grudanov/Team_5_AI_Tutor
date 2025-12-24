---
source_image: page_092.png
page_number: 92
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 90.90
tokens: 13073
characters: 4085
timestamp: 2025-12-24T05:32:16.082398
finish_reason: stop
---

Вот вычисление строки 7:

\[
\forall x \left[ P(f(x)) \lor \exists y x = f(f(y)) \right]
\]

(i)
\[
\forall x \left[ I_2(f_3(x)) \lor \exists y x = f_3(f_3(y)) \right]
\]
(ii) \( t \)

При получении (ii) нужна следующая вспомогательная таблица:

(a)
\[
x \mid I_2(f_3(x)) \lor \exists y \quad x = f_3(f_3(y))
\]
\[
\begin{array}{c|c}
1 & t \\
2 & t
\end{array}
\]

вычисление которой осуществляется следующим образом (объяснения ниже):

\[
I_2(f_3(1)) \lor \exists y 1 = f_3(f_3(y)) \qquad I_2(f_3(2)) \lor \exists y 2 = f_3(f_3(y))
\]
\[
\begin{array}{c|c}
I_2(2) & t \\
f & t \\
V & t \\
t & t
\end{array}
\]
\[
\begin{array}{c|c}
I_2(1) & t \\
t & V t \\
t & t
\end{array}
\]

Для нахождения \( t \) во второй строке под \( \exists y \) нужны еще две вспомогательные таблицы:

\[
y \mid 1 = f_3(f_3(y)) \qquad y \mid 2 = f_3(f_3(y))
\]
\[
(b_1) \begin{array}{c|c}
1 & t \\
2 & f
\end{array} \qquad (b_2) \begin{array}{c|c}
1 & f \\
2 & t
\end{array}
\]

которые вычисляются так:

\[
\begin{array}{c|c}
1 = f_3(f_3(1)) & 1 = f_3(f_3(2)) \\
1 = 1 & 1 = 2 \\
t & f \\
t & f
\end{array}
\]
\[
\begin{array}{c|c}
2 = f_3(f_3(1)) & 2 = f_3(f_3(2)) \\
2 = 1 & 2 = 2 \\
f & f \\
t & t
\end{array}
\]

На последнем шаге каждого из этих четырех вычислений применяется правило вычисления \( = \). Так как каждая из таблиц \((b_1)\) и \((b_2)\) дает \( t \), мы получаем \( t \) при вычислении каждой строки таблицы (a) в силу правила вычисления \( \exists \). Затем по правилу вычисления \( \forall \) получаем \( t \) в строке (ii) той таблицы, которую мы построили для вычисления искомой строки 7.

Пример 3. Построим таблицы для \( \exists x \forall y (P(y) \supset x = y) \) и \( \exists x [P(x) \& \forall y (P(y) \supset x = y)] \) при \( D = \{1, 2, 3\} \). Начнем со списка возможных значений \( P(x) \), как в примере 4 § 17.

\[
\begin{array}{c|cccccccc}
x & I_1(x) & I_2(x) & I_3(x) & I_4(x) & I_5(x) & I_6(x) & I_7(x) & I_8(x) \\
\hline
1 & t & t & t & t & f & f & f & f \\
2 & t & t & f & f & t & t & f & f \\
3 & t & f & t & f & t & f & t & f
\end{array}
\]

(a)
\[
\forall x \left[ \exists x \forall y (P(y) \supset x = y) \right] \quad \exists x [P(x) \& \forall y (P(y) \supset x = y)]
\]
\[
\begin{array}{c|c}
I_1(x) & f \\
I_2(x) & f \\
I_3(x) & f \\
I_4(x) & t \\
I_5(x) & f \\
I_6(x) & t \\
I_7(x) & t \\
I_8(x) & f
\end{array}
\]

(b)
\[
\forall x \left[ \exists x \forall y (P(y) \supset x = y) \right] \quad \exists x [P(x) \& \forall y (P(y) \supset x = y)]
\]
\[
\begin{array}{c|c}
I_1(x) & f \\
I_2(x) & f \\
I_3(x) & f \\
I_4(x) & t \\
I_5(x) & f \\
I_6(x) & t \\
I_7(x) & t \\
I_8(x) & f
\end{array}
\]

Вычислим строку 6 в (a) и (b). Вот вспомогательные таблицы:

(a')
\[
x \quad \forall y (I_6(y) \supset x = y) \quad I_6(x) \& \forall y (I_6(y) \supset x = y)
\]
\[
\begin{array}{c|c}
1 & f \\
2 & t \\
3 & f
\end{array}
\]

(b')
\[
x \quad \forall y (I_6(y) \supset x = y) \quad I_6(x) \& \forall y (I_6(y) \supset x = y)
\]
\[
\begin{array}{c|c}
1 & f \\
2 & t \\
3 & f
\end{array}
\]

Чтобы вычислить их, нужны новые вспомогательные таблицы:

(a'')
\[
y \quad I_6(y) \supset 1 = y \quad I_6(y) \supset 2 = y \quad I_6(y) \supset 3 = y
\]
\[
\begin{array}{c|ccc}
1 & t & t & t \\
2 & f & t & f \\
3 & t & t & t
\end{array}
\]

Подробности вычислений \((a''_1)\), \((a''_2)\) и \((a''_3)\) почти одинаковы:

\[
I_6(1) \supset 1 = 1 \quad I_6(2) \supset 1 = 2 \quad I_6(3) \supset 1 = 3
\]
\[
\begin{array}{c|c}
f & t \\
t & f \\
t & t
\end{array}
\]

Правило вычисления \( \forall \), примененное к таблицам \((a''_1)-(a''_3)\), дает в качестве значений для \((a')\) те, которые мы привели выше в этой таблице; значения \((b')\) те же самые, ибо

\[
I_6(1) \& \forall y (I_6(y) \supset 1 = y) \quad I_6(2) \& \forall y (I_6(y) \supset 2 = y)
\]
\[
\begin{array}{c|c}
f & f \\
t & t
\end{array}
\]
\[
I_6(3) \& \forall y (I_6(y) \supset 3 = y)
\]
\[
\begin{array}{c|c}
f & f
\end{array}
\]

Поскольку и \((a')\), и \((b')\) содержат \( t \), то по правилу вычисления \( \exists \) столбцы (a) и (b) истинностной таблицы исходной формулы дают \( t \) в строке 6.