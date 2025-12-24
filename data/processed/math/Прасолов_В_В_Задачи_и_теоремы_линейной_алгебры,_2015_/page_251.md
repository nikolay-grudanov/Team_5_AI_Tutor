---
source_image: page_251.png
page_number: 251
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.49
tokens: 6637
characters: 2578
timestamp: 2025-12-24T08:14:22.100085
finish_reason: stop
---

Теперь решение находится следующим образом. Прежде всего заметим, что \( b' = \begin{pmatrix} 1 & 0 \\ -7 & 1 \end{pmatrix} \begin{pmatrix} 8 \\ 2 \end{pmatrix} = \begin{pmatrix} 8 \\ -54 \end{pmatrix} \). Поэтому \( x' = (8, -54/3, t)^T \) и

\[
x = \begin{pmatrix} 1 & -10 & 33 \\ 0 & -1 & 3 \\ 0 & 5 & -16 \end{pmatrix} \begin{pmatrix} 8 \\ -18 \\ t \end{pmatrix} = \begin{pmatrix} 188 + 33t \\ 18 + 3t \\ -90 - 16t \end{pmatrix}.
\]

Положив \( 18 + 3t = 3s \), т. е. \( t = s - 6 \), можно несколько упростить полученное решение: \( x_1 = -10 + 33s, x_2 = 3s, x_3 = 6 - 16s \).

**20.4. Классификация абелевых групп**

**Теорема 20.4.1.** *Любая конечно порождённая абелева группа имеет вид \( \mathbb{Z}^r \oplus \mathbb{Z}_{g_1} \oplus \ldots \oplus \mathbb{Z}_{g_p} \), где \( g_{i+1} \) делится на \( g_i \).*

**Доказательство.** Пусть абелева группа \( G \) порождена элементами \( a_1, \ldots, a_n \). Возьмём свободную абелеву группу \( \mathbb{Z}^n \) с базисом \( e_1, \ldots, e_n \) и рассмотрим гомоморфизм \( f : \mathbb{Z}^n \to G \), заданный формулой \( f(\bullet\ k_i e_i) = \bullet\ k_i a_i \). Ясно, что \( f \) — эпиморфизм, поэтому \( G \cong \mathbb{Z}^n / \mathrm{Ker}\ f \).

Группа \( \mathrm{Ker}\ f \) является свободной абелевой группой (теорема 7.4.1). Пусть \( \varepsilon_1, \ldots, \varepsilon_m \) — её базис, \( \varepsilon \) — столбец векторов \( \varepsilon_1, \ldots, \varepsilon_m \), а \( e \) — столбец векторов \( e_1, \ldots, e_n \). Тогда \( \varepsilon = A e \), где \( A \) — матрица размером \( m \times n \), элементами которой являются целые числа. Выберем матрицы-единицы \( B \) и \( C \) так, что \( BAC = A' \), где

\[
A' = \mathrm{diag}(g_1, \ldots, g_p, 0, \ldots, 0).
\]

Тогда \( \varepsilon' = A'e' \), где \( \varepsilon' = Be \) и \( e' = C^{-1}e \) — базисы групп \( \mathrm{Ker}\ f \) и \( \mathbb{Z}^n \). Таким образом, в группе \( \mathbb{Z}^n \) можно выбрать базис \( e'_1, \ldots, e'_n \) так, что базис группы \( \mathrm{Ker}\ f \) имеет вид \( \varepsilon'_1 = g_1 e'_1, \ldots, \varepsilon'_p = g_p e'_p \). При таком выборе базисов ясно, что \( \mathbb{Z}^n / \mathrm{Ker}\ f \cong \mathbb{Z}^r \oplus \mathbb{Z}_{g_1} \oplus \ldots \oplus \mathbb{Z}_{g_p} \). \( \square \)

**Задачи**

**20.1.** Вычислите инвариантные множители жордановой клетки и циклической клетки.

**20.2.** Пусть \( A \) — матрица порядка \( n \), \( f_{n-1} \) — наибольший общий делитель миноров порядка \( n-1 \) матрицы \( A - xI \). Докажите, что минимальный многочлен матрицы \( A \) равен \( \pm |A - xI| / f_{n-1} \).