---
source_image: page_070.png
page_number: 70
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 56.92
tokens: 11657
characters: 1911
timestamp: 2025-12-24T08:27:44.112130
finish_reason: stop
---

Теорема 26 (Неравенство Йенсена).

Пусть функция \( g : \mathbb{R} \to \mathbb{R} \) выпукла (вниз :-)) ). Тогда для любой случайной величины \( \xi \) с конечным первым моментом

\[
\mathbf{E} g(\xi) \geqslant g(\mathbf{E} \xi).
\]

Нам понадобится следующее свойство выпуклых функций (то есть таких, что для любых \( a < b \) при всяком \( \alpha \in [0, 1] \) верно \( \alpha g(a) + (1 - \alpha)g(b) \geqslant g(\alpha a + (1 - \alpha)b) \)):

Лемма 8. Пусть функция \( g : \mathbb{R} \to \mathbb{R} \) выпукла. Тогда для всякого \( y \) найдется число \( c(y) \) такое, что при всех \( x \)

\[
g(x) \geqslant g(y) + c(y)(x - y).
\]

Доказательство (предложено Дебеловым Алексеем, гр.871).

Положим \( c(y) = \inf_{x > y} \frac{g(x) - g(y)}{x - y} \geqslant -\infty \). Тогда \( g(x) - g(y) \geqslant c(y)(x - y) \) при \( x > y \). Докажем, что это неравенство верно и при \( x < y \), и заодно покажем, что \( c(y) \) конечно.

Пусть \( x_1 < y \). Тогда \( y \) принадлежит отрезку \([x_1; x_2]\) для любого \( x_2 > y \), то есть существует \( \alpha \in [0, 1] \) такое, что

\[
y = \alpha \cdot x_1 + (1 - \alpha) \cdot x_2, \quad \text{или} \quad x_2 = \frac{y - \alpha x_1}{1 - \alpha}.
\]

(14)

Но в силу выпуклости функции \( g \)

\[
g(y) \leqslant \alpha \cdot g(x_1) + (1 - \alpha) \cdot g(x_2), \quad \text{или} \quad g(x_2) \geqslant \frac{g(y) - \alpha \cdot g(x_1)}{1 - \alpha}.
\]

(15)

Вспомним, что \( c(y) = \inf_{x_2 > y} \frac{g(x_2) - g(y)}{x_2 - y} \) и подставим вместо \( g(x_2) \) и \( x_2 \) выражения, стоящие в правой части формул (15) и (14), соответственно:

\[
c(y) = \inf_{x_2 > y} \frac{g(x_2) - g(y)}{x_2 - y} \geqslant \frac{\frac{g(y) - \alpha g(x_1)}{1 - \alpha} - g(y)}{\frac{y - \alpha x_1}{1 - \alpha} - y} = \frac{g(y) - g(x_1)}{y - x_1}.
\]

Последнее выражение заведомо конечно, то есть \( c(y) > -\infty \). Более того, мы получили, что требуемое неравенство