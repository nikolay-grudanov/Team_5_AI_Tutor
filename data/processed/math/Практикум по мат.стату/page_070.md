---
source_image: page_070.png
page_number: 70
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.14
tokens: 6947
characters: 3235
timestamp: 2025-12-24T07:39:51.567135
finish_reason: stop
---

Наблюдаемое значение статистики:
\[
\chi^2_{\text{набл}} = 518,84.
\]
Критическое значение статистики:
\[
\chi^2_{\text{кр}} = \chi^2_{n-r-1; \alpha} = \chi^2_{7-1-1; 0,05} = 11,07.
\]
Так как \( \chi^2_{\text{набл}} > \chi^2_{\text{кр}} \), то гипотеза \( H_0 \) отклоняется.
Найдем P-значение.
\[
\text{P-value} = P(\chi^2_{\text{кр}} > \chi^2_{\text{набл}}) = P(\chi^2_5 > 514,94) =
= \text{ХИ2.ПАСП.ПХ (514,94; 5)} = 6,8502E-110.
\]
P-значение практически равно 0. Оно меньше значения \( \alpha = 0,05 \), и на этом уровне значимости гипотеза \( H_0 \) отклоняется.

Решение примера в Excel.

<table>
  <tr>
    <th>A</th><th>B</th><th>C</th><th>D</th><th>E</th><th>F</th><th>G</th><th>H</th><th>I</th><th>J</th><th>K</th>
  </tr>
  <tr>
    <td>1</td><td>i</td><td>x_i</td><td>n_i</td><td>p_i</td><td>N*p_i</td><td>n_i - Np_i</td><td>(n_i - Np_i)^2</td><td>(n_i - Np_i)^2/Np_i</td><td>n =</td><td>10</td>
  </tr>
  <tr>
    <td>2</td><td>1</td><td>0</td><td>13</td><td>9,6E-05</td><td>0,02869</td><td>12,97131</td><td>168,254889</td><td>5864,62757</td><td>N =</td><td>300</td>
  </tr>
  <tr>
    <td>3</td><td>2</td><td>1</td><td>17</td><td>0,00146</td><td>0,436982</td><td>16,56302</td><td>274,333555</td><td>627,790995</td><td></td><td></td>
  </tr>
  <tr>
    <td>4</td><td>3</td><td>2</td><td>15</td><td>0,00998</td><td>2,995111</td><td>12,00489</td><td>144,117354</td><td>48,1175294</td><td>p =</td><td>0,60367</td>
  </tr>
  <tr>
    <td>5</td><td>4</td><td>3</td><td>35</td><td>0,04055</td><td>12,16517</td><td>22,83483</td><td>521,429327</td><td>42,8624673</td><td></td><td></td>
  </tr>
  <tr>
    <td>6</td><td>5</td><td>4</td><td>10</td><td>0,10809</td><td>32,42597</td><td>-22,42597</td><td>502,923979</td><td>15,5099147</td><td>q =</td><td>0,39633</td>
  </tr>
  <tr>
    <td>7</td><td>6</td><td>5</td><td>9</td><td>0,19756</td><td>59,2667</td><td>-50,2667</td><td>2526,7415</td><td>42,6334069</td><td></td><td></td>
  </tr>
  <tr>
    <td>8</td><td>7</td><td>6</td><td>40</td><td>0,25075</td><td>75,22568</td><td>-35,22568</td><td>1240,84854</td><td>16,4950125</td><td></td><td></td>
  </tr>
  <tr>
    <td>9</td><td>8</td><td>7</td><td>51</td><td>0,21824</td><td>65,47337</td><td>-14,47337</td><td>209,478328</td><td>3,19944337</td><td></td><td></td>
  </tr>
  <tr>
    <td>10</td><td>9</td><td>8</td><td>45</td><td>0,12466</td><td>37,39664</td><td>7,603364</td><td>57,8111495</td><td>1,54589172</td><td></td><td></td>
  </tr>
  <tr>
    <td>11</td><td>10</td><td>9</td><td>33</td><td>0,04219</td><td>12,65775</td><td>20,34225</td><td>413,807015</td><td>32,6919807</td><td></td><td></td>
  </tr>
  <tr>
    <td>12</td><td>11</td><td>10</td><td>32</td><td>0,00643</td><td>1,927939</td><td>30,07206</td><td>904,328874</td><td>469,065170</td><td></td><td></td>
  </tr>
  <tr>
    <td>13</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
  </tr>
  <tr>
    <td></td><td></td><td>300</td><td>1</td><td>300</td><td>-4,6E-14</td><td></td><td>7164,54</td><td></td><td></td><td></td>
  </tr>
</table>

Вероятности \( p_i = P(X = i) = C_n^i p^i q^{n-i} \) биномиального распределения вычисляются с помощью функции БИНOM.РАСП. В ячейке D2 стоит команда:
БИНом.РАСП (B2;$K$1;$K$4;1)