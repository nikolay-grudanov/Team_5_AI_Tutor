---
source_image: page_056.png
page_number: 56
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 241.23
tokens: 12695
characters: 14901
timestamp: 2025-12-24T07:22:08.673770
finish_reason: length
---

знаком равенства; поэтому можно записать \( \psi_{14}(x_1, x_2) = \overline{x}_1 \lor \overline{x}_2 = \overline{x}_1 \overline{x}_2 \). Как для двух данных формул выяснить, эквивалентны они или нет? Существует стандартный метод, всегда приводящий к ответу: по каждой формуле восстанавливается таблица* функции, а затем полученные две таблицы сравниваются. Иначе говоря, для каждого набора значений переменных проверяется, равны ли на нем значения формул. Этот метод требует \( 2 \cdot 2^n \) вычислений (если считать, что обе формулы зависят от \( n \) переменных) и на практике оказывается слишком громоздким. Существуют и другие методы установления эквивалентности формул и получения новых формул, эквивалентных исходной. К этим методам, называемым эквивалентными преобразованиями формул, мы еще вернемся.

3.2.
БУЛЕВА АЛГЕБРА

В этом параграфе будут рассмотрены представления логических функций в виде суперпозиций дизъюнкций, конъюнкций и отрицаний.

Разложение функций по переменным. Совершенная дизъюнктивная нормальная форма. Введем обозначение \( x^0 = x, \ x^1 = x \). Пусть \( \alpha \) — параметр, равный 0 или 1. Тогда \( x^\alpha = 1 \), если \( x = \alpha \), и \( x^\alpha = 0 \), если \( x \neq \alpha \).

Теорема 3.1. Всякая логическая функция \( f(x_1, ..., x_n) \) может быть представлена в следующем виде:

\[
f(x_1, ..., x_m, x_{m+1}, ..., x_n) =
\]
\[
= \bigwedge_{\alpha_1, ..., \alpha_m} x_1^{\alpha_1} ... x_m^{\alpha_m} f(\alpha_1, ..., \alpha_m, x_{m+1}, ..., x_n),
\]

где \( m \leq n \), а дизъюнкция берется по всем \( 2^m \) наборам значений переменных \( x_1, ..., x_m \).

Это равенство называется разложением по переменным \( x_1, ..., x_m \). Например, при \( n = 4, m = 2 \) разложение (3.4) имеет вид:
\[
f(x_1, x_2, x_3, x_4) = \overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4) \lor \overline{x}_1 x_2 f(0, 1, x_3, x_4) \lor
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2, x_3, x_4)} \phantom{\overline{x}_1 \overline{x}_2 f(0, 0, x_3, x_4)} \phantom{\overline{x}_1 x_2 f(0, 1, x_3, x_4)}
\]
\[
\phantom{f(x_1, x_2