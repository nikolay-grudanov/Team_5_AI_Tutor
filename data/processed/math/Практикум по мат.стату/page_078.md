---
source_image: page_078.png
page_number: 78
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.59
tokens: 6660
characters: 3221
timestamp: 2025-12-24T07:39:51.971254
finish_reason: stop
---

7. Примеры

Решение в Excel.

<table>
  <tr>
    <th>A</th>
    <th>B</th>
    <th>C</th>
    <th>D</th>
    <th>E</th>
    <th>F</th>
    <th>G</th>
    <th>H</th>
  </tr>
  <tr>
    <td>1</td>
    <td></td>
    <td></td>
    <td>n =</td>
    <td>200</td>
    <td></td>
    <td>λ̂ =</td>
    <td>1,03</td>
  </tr>
  <tr>
    <td>3</td>
    <td>i</td>
    <td>x<sub>i</sub></td>
    <td>n<sub>i</sub></td>
    <td>p<sub>i</sub></td>
    <td>n*p<sub>i</sub></td>
    <td>n<sub>i</sub> - n*p<sub>i</sub></td>
    <td>(n<sub>i</sub> - n*p<sub>i</sub>)<sup>2</sup></td>
    <td>(n<sub>i</sub> - n*p<sub>i</sub>)<sup>2</sup>/n*p<sub>i</sub></td>
  </tr>
  <tr>
    <td>4</td>
    <td>1</td>
    <td>0</td>
    <td>70</td>
    <td>0,35701</td>
    <td>71,40139</td>
    <td>-1,40139</td>
    <td>1,96390</td>
    <td>0,02751</td>
  </tr>
  <tr>
    <td>5</td>
    <td>2</td>
    <td>1</td>
    <td>78</td>
    <td>0,36772</td>
    <td>73,54343</td>
    <td>4,45657</td>
    <td>19,86098</td>
    <td>0,27006</td>
  </tr>
  <tr>
    <td>6</td>
    <td>3</td>
    <td>2</td>
    <td>34</td>
    <td>0,18937</td>
    <td>37,87487</td>
    <td>-3,87487</td>
    <td>15,01461</td>
    <td>0,39643</td>
  </tr>
  <tr>
    <td>7</td>
    <td>4</td>
    <td>3</td>
    <td>13</td>
    <td>0,06502</td>
    <td>13,00370</td>
    <td>-0,00370</td>
    <td>0,00001</td>
    <td>0,00000</td>
  </tr>
  <tr>
    <td>8</td>
    <td>5</td>
    <td>4</td>
    <td>4</td>
    <td>0,01674</td>
    <td>3,34845</td>
    <td>0,65155</td>
    <td>0,42451</td>
    <td>0,12678</td>
  </tr>
  <tr>
    <td>9</td>
    <td>6</td>
    <td>5</td>
    <td>1</td>
    <td>0,00414</td>
    <td>0,82815</td>
    <td>0,17185</td>
    <td>0,02953</td>
    <td>0,03566</td>
  </tr>
  <tr>
    <td>10</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>11</td>
    <td></td>
    <td></td>
    <td>200</td>
    <td>1</td>
    <td>200</td>
    <td>1,288E-14</td>
    <td>0,8564</td>
    <td></td>
  </tr>
  <tr>
    <td>12</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>13</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>P-value =</td>
    <td>0,9307</td>
    <td></td>
    <td></td>
  </tr>
</table>

Оценка параметра распределения Пуассона в ячейке H1 (λ̂ = 1,03) вычисляется по формуле
\[
\hat{\lambda} = \text{СУММПРОИЗВ}(B4:B9; C4:C9)/E1
\]
Теоретические вероятности p<sub>i</sub> в ячейках D4:D8 вычисляются с использованием функции ПУАССОН.РАСП. В ячейке D4 стоит команда
\[
=\text{ПУАССОН.РАСП} (B4;$H$1;0)
\]
Так как случайная величина, распределенная по закону Пуассона, может принимать любые целые значения, то последний интервал ее значений должен быть расширен до бесконечного. По этой причине последняя вероятность p<sub>6</sub> вычисляется как дополнение до 1 суммы остальных вероятностей. В ячейке D9 команда:
\[
=1 - \text{СУММ}(D4:D8)
\]
Сумма значений по строкам столбца Н дает наблюдаемое значение статистики \( \chi^2_{\text{набл}} = 0,8564 \).
P-значение в ячейке G13 вычисляется по формуле
\[
\text{P-value} = \text{ХИ2.РАСП.ПХ}(H11; 4)
\]