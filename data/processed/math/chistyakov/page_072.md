---
source_image: page_072.png
page_number: 72
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.21
tokens: 7762
characters: 1697
timestamp: 2025-12-24T07:27:34.498582
finish_reason: stop
---

chinami. Если много раз бросать иглу, как описано в задаче Бюффона (см. § 6, гл. I), то частота \( \mu_n / n \) будет мало отличаться от вероятности \( p \) пересечения иглой какой-либо линии. Зная величину отклонения \( \mu_n / n \) от \( p \), можно оценить ошибку в определении числа \( \pi \). В таких задачах естественно считать \( p \) неизвестным. Тогда, чтобы подобрать наименьшее \( n \), при котором вероятность отклонения будет равна \( 1 - 2\alpha \), нужно согласно (3.14) решить уравнение

\[
2 \Phi_0 \left( \Delta \sqrt{\frac{n}{pq}} \right) = 1 - 2\alpha.
\]

Решение будет зависеть от неизвестного \( p \). От этой зависимости можно избавиться, если потребовать, чтобы

\[
P \left( \left| \frac{\mu_n}{n} - p \right| < \Delta \right) \geqslant 1 - 2\alpha.
\]

Тогда из (3.14), используя неравенство \( pq \leqslant 1/4 \), получим

\[
P \left( \left| \frac{\mu_n}{n} - p \right| < \Delta \right) \approx 2 \Phi_0 \left( \Delta \sqrt{\frac{n}{pq}} \right) \geqslant 
\]
\[
\geqslant 2 \Phi_0 (2 \Delta \sqrt{n}) = 1 - 2\alpha
\]

и для определения \( n \) имеем уравнение \( \Phi_0 (2 \Delta \sqrt{n}) = \frac{1 - 2\alpha}{2} \). По таблице можно найти \( u_\alpha \), для которых \( \Phi_0 (u_\alpha) = \frac{1 - 2\alpha}{2} \). Тогда \( 2 \Delta \sqrt{n} = u_\alpha \) и

\[
n \geqslant \frac{u_\alpha^2}{4 \Delta^2}.
\]

Довольно часто используются значения \( 2\alpha \), равные 0,05 и 0,01. Для этих значений имеем

<table>
  <tr>
    <th>2\alpha</th>
    <th>0,01</th>
    <th>0,05</th>
  </tr>
  <tr>
    <th>u_\alpha</th>
    <th>2,58</th>
    <th>1,96</th>
  </tr>
</table>

В задаче с иглой вовсе не обязательно проводить реальные подбрасывания иглы. Можно этот процесс