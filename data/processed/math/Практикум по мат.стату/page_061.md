---
source_image: page_061.png
page_number: 61
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.19
tokens: 6618
characters: 2969
timestamp: 2025-12-24T07:39:46.167140
finish_reason: stop
---

7. Примеры

Пример 6. Сгенерируйте две независимые выборки: \( Y \sim \mathrm{Exp}(1) \), \( Z \sim \mathrm{Exp}(1) \) распределенные по показательному закону с параметром \( \lambda = 1 \).

Объёмы выборок — по 200 элементов.
Сформируйте новую выборку \( X \) по правилу: \( X = Y + Z \).
Проверьте, используя подходящие критерии, гипотезу \( H_0 : X \sim \mathrm{Exp}(0.5) \) о соответствии выборки \( X \) показательному закону распределения с параметром \( \lambda = 0.5 \).
(Принять уровень значимости \( \alpha = 0.05 \)).

Решение. Используем критерий Колмогорова (одновыборочный критерий Колмогорова-Смирнова).

Решение в Excel.

<table>
  <tr>
    <th>A</th><th>B</th><th>C</th><th>D</th><th>E</th><th>F</th><th>G</th><th>H</th><th>I</th><th>J</th><th>K</th><th>L</th>
  </tr>
  <tr>
    <td>i</td><td>u1</td><td>u2</td><td>y</td><td>z</td><td>x</td><td>x<sub>(i)</sub></td><td>F(x)</td><td>i/n</td><td>(i-1)/n</td><td>i/n - F(x)</td><td>F(x) — (i-1)/n</td>
  </tr>
  <tr><td>2</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>3</td><td>1</td><td>0,075</td><td>0,774</td><td>0,078</td><td>1,485</td><td>1,564</td><td>0,089</td><td>0,043</td><td>0,005</td><td>0,000</td><td>-0,038</td><td>0,043</td></tr>
  <tr><td>4</td><td>2</td><td>0,491</td><td>0,740</td><td>0,676</td><td>1,346</td><td>2,022</td><td>0,110</td><td>0,053</td><td>0,010</td><td>0,005</td><td>-0,043</td><td>0,048</td></tr>
  <tr><td>5</td><td>3</td><td>0,622</td><td>0,412</td><td>0,972</td><td>0,531</td><td>1,503</td><td>0,179</td><td>0,085</td><td>0,015</td><td>0,010</td><td>-0,070</td><td>0,075</td></tr>
  <tr><td>6</td><td>4</td><td>0,614</td><td>0,159</td><td>0,951</td><td>0,174</td><td>1,125</td><td>0,213</td><td>0,101</td><td>0,020</td><td>0,015</td><td>-0,081</td><td>0,086</td></tr>
  <tr><td>7</td><td>5</td><td>0,951</td><td>0,970</td><td>3,009</td><td>3,498</td><td>6,506</td><td>0,309</td><td>0,143</td><td>0,025</td><td>0,020</td><td>-0,118</td><td>0,123</td></tr>
  <tr><td>8</td><td>6</td><td>0,856</td><td>0,474</td><td>1,939</td><td>0,643</td><td>2,582</td><td>0,330</td><td>0,152</td><td>0,030</td><td>0,025</td><td>-0,122</td><td>0,127</td></tr>
  <tr><td>9</td><td>7</td><td>0,119</td><td>0,747</td><td>0,126</td><td>1,375</td><td>1,501</td><td>0,354</td><td>0,162</td><td>0,035</td><td>0,030</td><td>-0,127</td><td>0,132</td></tr>
  <tr><td>.</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr>
</table>

1. Формирование массива \( X \).
Генерируем последовательности: \( u_{1i} \sim \mathrm{Unif}(0; 1) \) (столбец B, команда СЛЧИС()), \( u_{2i} \sim \mathrm{Unif}(0; 1) \) (столбец C, команда СЛЧИС()).
Для генерирования экспоненциально распределенных величин используем следующий факт: если \( u \sim \mathrm{Unif}(0; 1) \), то \( -\frac{1}{\lambda} \ln(1-u) \sim \mathrm{Exp}(\lambda) \).