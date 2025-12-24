---
source_image: page_036.png
page_number: 36
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 96.48
tokens: 12009
characters: 2667
timestamp: 2025-12-24T06:22:21.999100
finish_reason: stop
---

2.2-7 Докажите по индукции формулу (2.15).

2.2-8 Докажите такую оценку для чисел Фибоначчи: \( F_{i+2} \geq \varphi^i \) при \( i \geq 0 \) (здесь \( \varphi \) — отношение золотого сечения).

Задачи

2-1 Асимптотика многочленов
Пусть \( p(n) = a_0 + a_1 n + \ldots + a_d n^d \) — многочлен степени \( d \), причём \( a_d > 0 \). Докажите, что
а. \( p(n) = O(n^k) \) при \( k \geq d \).
б. \( p(n) = \Omega(n^k) \) при \( k \leq d \).
в. \( p(n) = \Theta(n^k) \) при \( k = d \).
г. \( p(n) = o(n^k) \) при \( k > d \).
д. \( p(n) = \omega(n^k) \) при \( k < d \).

2-2 Сравнение асимптотик
Для всех клеток следующей таблицы ответьте "да" или "нет" на вопрос о том, можно ли записать \( A \) как \( O, o, \Omega, \omega \) или \( \Theta \) от \( B \) (\( k \geq 1, \varepsilon > 0, c > 1 \) — некоторые константы).

<table>
  <tr>
    <th>A</th>
    <th>B</th>
    <th>O</th>
    <th>o</th>
    <th>\(\Omega\)</th>
    <th>\(\omega\)</th>
    <th>\(\Theta\)</th>
  </tr>
  <tr>
    <td>a. \( \lg^k n \)</td>
    <td>\( n^\varepsilon \)</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>б. \( n^k \)</td>
    <td>\( c^n \)</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>в. \( \sqrt{n} \)</td>
    <td>\( n^{\sin n} \)</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>г. \( 2^n \)</td>
    <td>\( 2^{n/2} \)</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>д. \( n^{\lg m} \)</td>
    <td>\( m^{\lg n} \)</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>е. \( \lg(n!) \)</td>
    <td>\( \lg(n^n) \)</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

2-3 Сравнение скорости роста
а. Расположите следующие 30 функций в порядке увеличения скорости роста (каждая функция есть \( O \) (следующая)) и отметьте, какие из этих функций на самом деле имеют одинаковую скорость роста (одна есть \( \Theta \) от другой):

\[
\begin{array}{cccccccccc}
\lg(\lg^* n) & 2^{\lg^* n} & (\sqrt{2})^{\lg n} & n^2 & n! & (\lg n)! \\
(3/2)^n & n^3 & \lg^2 n & \lg(n!) & 2^{2^n} & n^{1/\lg n} \\
\ln \ln n & \lg^* n & n \cdot 2^n & n^{\lg \lg n} & \ln n & 1 \\
2^{\lg n} & (\lg n)^{\lg n} & e^n & 4^{\lg n} & (n+1)! & \sqrt{\lg n} \\
\lg^* \lg n & 2^{\sqrt{2 \lg n}} & n & 2^n & n \lg n & 2^{2^{n+1}}
\end{array}
\]

б. Укажите неотрицательную функцию \( f(n) \), которая не сравнима ни с одной из функций \( g_i \) этой таблицы (\( f(n) \) не есть \( O(g_i(n)) \) и \( g_i(n) \) не есть \( O(f(n)) \)).