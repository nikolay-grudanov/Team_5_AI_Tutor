---
source_image: page_192.png
page_number: 192
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.71
tokens: 5378
characters: 1831
timestamp: 2025-12-24T07:21:28.256792
finish_reason: stop
---

Пример 5.10. Примитивно-рекурсивными являются следующие функции:

1) \( f(x) = x \div 1 \), определяемая схемой:
\[
f(0) = 0 \div 1 = 0;
\]
\[
f(y + 1) = y;
\]

2) \( f(x, y) = x \div y \), определяемая схемой:
\[
f(x, 0) = x;
\]
\[
f(x, y + 1) = x \div (y + 1) = (x \div y) \div 1 = f(x, y) \div 1
\]
(для определения функции из п. 2 использована функция из п. 1);

3) \( f(x, y) = |x - y| = (x \div y) + (y \div x); \)

4) \( \operatorname{sg}(x) = \begin{cases} 0, & \text{если } x = 0; \\ 1, & \text{если } x \neq 0; \end{cases} \)
ее схема имеет вид:
\[
\operatorname{sg}(0) = 0;
\]
\[
\operatorname{sg}(x + 1) = 1;
\]
5) \( \min(x, y) = x \div (x \div y); \)
6) \( \max(x, y) = y + (x \div y). \)

С помощью функции \( \operatorname{sg} \) (сигнум) из примера 5.10, г и ее отрицания \( \overline{\operatorname{sg}}(x) = 1 \div \operatorname{sg}x \) построим примитивно-рекурсивное описание функций, связанных с делением.

Пример 5.11 (деление). а. Функция \( r(x, y) \) — остаток от деления \( y \) на \( x \):
\[
r(x, 0) = 0;
\]
\[
r(x, y + 1) = (r(x, y) + 1)\operatorname{sg}(|x - (r(x, y) + 1)|).
\]
Смысл второй строки определения в следующем: если \( y + 1 \) не делится на \( x \), то \( \operatorname{sg}(|x \div (r(x, y) + 1)|) = 1 \) и \( r(x, y + 1) = r(x, y) + 1 \); если же \( y + 1 \) делится на \( x \), то \( r(x, y, + 1) = \operatorname{sg}(|x - r(x, y) + 1|)) = 0 \).

б. Функция \( g(x, y) = [y/x] \) — частное от деления \( y \) на \( x \), т. е. целая часть дроби \( y/x \):
\[
q(x, 0) = 0;
\]
\[
q(x, y + 1) = q(x, y) + \overline{\operatorname{sg}}(|x - (r(x, y) + 1)|).
\]
Второе слагаемое, как и в случае \( r(x, y) \), зависит от делимости \( y + 1 \) на \( x \). Если \( y + 1 \) делится на \( x \), то \( q(x, y + 1) \) на единицу больше, чем \( q(x, y) \); если нет, то \( q(x, y + 1) = q(x, y) \).