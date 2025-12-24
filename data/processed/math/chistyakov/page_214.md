---
source_image: page_214.png
page_number: 214
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.98
tokens: 5513
characters: 2136
timestamp: 2025-12-24T07:31:11.778149
finish_reason: stop
---

Таблица 5

<table>
  <tr>
    <th rowspan="2">n</th>
    <th colspan="4">α</th>
  </tr>
  <tr>
    <th>0,10</th>
    <th>0,05</th>
    <th>0,02</th>
    <th>0,01</th>
  </tr>
  <tr>
    <td>5</td>
    <td>2,015</td>
    <td>2,571</td>
    <td>3,365</td>
    <td>4,032</td>
  </tr>
  <tr>
    <td>6</td>
    <td>1,943</td>
    <td>2,447</td>
    <td>3,143</td>
    <td>3,707</td>
  </tr>
  <tr>
    <td>7</td>
    <td>1,895</td>
    <td>2,365</td>
    <td>2,998</td>
    <td>3,499</td>
  </tr>
  <tr>
    <td>8</td>
    <td>1,860</td>
    <td>2,306</td>
    <td>2,896</td>
    <td>3,355</td>
  </tr>
  <tr>
    <td>9</td>
    <td>1,833</td>
    <td>2,262</td>
    <td>2,821</td>
    <td>3,250</td>
  </tr>
  <tr>
    <td>10</td>
    <td>1,812</td>
    <td>2,228</td>
    <td>2,764</td>
    <td>3,169</td>
  </tr>
  <tr>
    <td>12</td>
    <td>1,782</td>
    <td>2,179</td>
    <td>2,681</td>
    <td>3,055</td>
  </tr>
  <tr>
    <td>14</td>
    <td>1,761</td>
    <td>2,145</td>
    <td>2,624</td>
    <td>2,977</td>
  </tr>
  <tr>
    <td>16</td>
    <td>1,746</td>
    <td>2,120</td>
    <td>2,583</td>
    <td>2,921</td>
  </tr>
  <tr>
    <td>18</td>
    <td>1,734</td>
    <td>2,101</td>
    <td>2,552</td>
    <td>2,878</td>
  </tr>
  <tr>
    <td>20</td>
    <td>1,725</td>
    <td>2,086</td>
    <td>2,528</td>
    <td>2,845</td>
  </tr>
  <tr>
    <td>22</td>
    <td>1,717</td>
    <td>2,074</td>
    <td>2,508</td>
    <td>2,819</td>
  </tr>
  <tr>
    <td>30</td>
    <td>1,697</td>
    <td>2,042</td>
    <td>2,457</td>
    <td>2,750</td>
  </tr>
  <tr>
    <td>∞</td>
    <td>1,645</td>
    <td>1,960</td>
    <td>2,326</td>
    <td>2,576</td>
  </tr>
</table>

Распределение Стьюдента

Значения функции \( t_{\alpha, n} \)

Функция \( t_{\alpha, n} \) определяется равенством \( P(|t_n| < t_{\alpha, n}) = 1 - \alpha \), где случайная величина \( t_n \) имеет распределение Стьюдента с \( n \) степенями свободы. Плотность распределения \( t_n \) равна

\[
p_{t_n}(x) = \frac{\Gamma \left( \frac{n+1}{2} \right)}{\Gamma \left( \frac{n}{2} \right) \sqrt{\pi n}} \cdot \left( 1 + \frac{x^2}{n} \right)^{-\frac{n+1}{2}}.
\]