---
source_image: page_057.png
page_number: 57
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 51.37
tokens: 13041
characters: 4056
timestamp: 2025-12-24T07:05:11.923233
finish_reason: stop
---

Критерий согласия \( \chi^2 \) имеет вид:

\[
\delta(\vec{X}) = \begin{cases}
H_1, & \text{если } \rho(\vec{X}) < C \\
H_2, & \text{если } \rho(\vec{X}) \geqslant C.
\end{cases}
\]

Замечание 27. Замечания 24, 25 остаются в силе.

8.6 Проверка гипотезы однородности: критерий Колмогорова - Смирнова

Есть две выборки \( \vec{X} = (X_1, \ldots, X_n) \) и \( \vec{Y} = (Y_1, \ldots, Y_m) \), причем \( X_i \in \mathcal{F}_x, Y_i \in \mathcal{F}_y \), и распределения \( \mathcal{F}_x, \mathcal{F}_y \), вообще говоря, неизвестны. Проверяется сложная гипотеза \( H_1: \mathcal{F}_x = \mathcal{F}_y \) против (еще более сложной) альтернативы \( H_2: H_1 \) не верна.

Если \( \mathcal{F}_x, \mathcal{F}_y \) имеют непрерывные функции распределения, применим критерий Колмогорова - Смирнова.

Пусть \( F_{n,x}^* \) и \( F_{m,y}^* \) — эмпирические функции распределения, построенные по выборкам \( \vec{X} \) и \( \vec{Y} \),

\[
\rho(\vec{X}, \vec{Y}) = \sqrt{\frac{mn}{m+n}} \sup_t |F_{n,x}^*(t) - F_{m,y}^*(t)|.
\]

Теорема 14. Если гипотеза \( H_1 \) верна, то \( \rho(\vec{X}, \vec{Y}) \Rightarrow \xi \in K \) (распределение с ф.р. Колмогорова) при \( n, m \to \infty \).

Упражнение. Доказать, что \( \rho(\vec{X}, \vec{Y}) \xrightarrow{p} \infty \) при \( n, m \to \infty \), если гипотеза \( H_2 \) верна.

И снова: пусть случайная величина \( \xi \) имеет распределение с ф.р. \( K(y) \). По заданному \( \varepsilon \) найдем \( C \) такое, что \( \varepsilon = \mathrm{P}(\xi \geqslant C) \), и построим критерий согласия Колмогорова - Смирнова:

\[
\delta(\vec{X}) = \begin{cases}
H_1, & \text{если } \rho(\vec{X}) < C \\
H_2, & \text{если } \rho(\vec{X}) \geqslant C.
\end{cases}
\]

Замечание 28. Если есть более двух выборок, и требуется проверить гипотезу однородности, часто пользуются одним из вариантов критерия \( \chi^2 \) Пирсона. Этот критерий (и ряд других критериев) рекомендую посмотреть в §3.4.2, с. 124 книги Г. И. Ивченко, Ю. И. Медведев, Математическая статистика. Москва, 1984, 248 с.

8.7 Проверка гипотезы независимости: критерий \( \chi^2 \) Пирсона

Есть выборка \( (\vec{X}, \vec{Y}) = ((X_1, Y_1), \ldots, (X_n, Y_n)) \) значений двух наблюдаемых совместно величин \( \xi \) и \( \eta \) в \( n \) экспериментах. Проверяется гипотеза \( H_1: \xi \) и \( \eta \) независимы.

Введем \( k \) интервалов группировки для значений \( \xi \): \( \Delta_1^x, \ldots, \Delta_k^x \) и \( m \) интервалов группировки для значений \( \eta \): \( \Delta_1^y, \ldots, \Delta_m^y \).

Посчитаем эмпирические частоты: для \( i = 1, \ldots, k, j = 1, \ldots, m \)

\[
\begin{align*}
\nu_{i,j} &= \{ \text{число пар } (X_l, Y_l) \in \Delta_i^x \times \Delta_j^y \}, \\
\nu_{.,j} &= \{ \text{число пар } (X_l, Y_l) : Y_l \in \Delta_j^y \} = \{ \text{число } Y_l \in \Delta_j^y \}, \\
\nu_{i,.} &= \{ \text{число пар } (X_l, Y_l) : X_l \in \Delta_i^x \} = \{ \text{число } X_l \in \Delta_i^x \}.
\end{align*}
\]

<table>
  <tr>
    <th rowspan="2">$\vec{X}$</th>
    <th colspan="m">$\Delta_1^y$</th>
    <th colspan="m">$\Delta_2^y$</th>
    <th colspan="m">$\ldots$</th>
    <th colspan="m">$\Delta_m^y$</th>
    <th rowspan="2">$\Sigma$</th>
  </tr>
  <tr>
    <td>$\nu_{1,1}$</td>
    <td>$\nu_{1,2}$</td>
    <td colspan="m-2">$\ldots$</td>
    <td>$\nu_{1,m}$</td>
    <td>$\nu_{1,.}$</td>
  </tr>
  <tr>
    <td>$\Delta_1^x$</td>
    <td>$\nu_{2,1}$</td>
    <td>$\nu_{2,2}$</td>
    <td colspan="m-2">$\ldots$</td>
    <td>$\nu_{2,m}$</td>
    <td>$\nu_{2,.}$</td>
  </tr>
  <tr>
    <td>$\Delta_2^x$</td>
    <td colspan="m">$\ldots$</td>
    <td colspan="m">$\ldots$</td>
    <td colspan="m">$\ldots$</td>
    <td colspan="m">$\ldots$</td>
    <td colspan="m">$\ldots$</td>
  </tr>
  <tr>
    <td>$\Delta_k^x$</td>
    <td>$\nu_{k,1}$</td>
    <td>$\nu_{k,2}$</td>
    <td colspan="m-2">$\ldots$</td>
    <td>$\nu_{k,m}$</td>
    <td>$\nu_{k,.}$</td>
  </tr>
  <tr>
    <td>$\Sigma$</td>
    <td>$\nu_{.,1}$</td>
    <td>$\nu_{.,2}$</td>
    <td colspan="m-2">$\ldots$</td>
    <td>$\nu_{.,m}$</td>
    <td>$n$</td>
  </tr>
</table>