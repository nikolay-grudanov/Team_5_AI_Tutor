---
source_image: page_260.png
page_number: 260
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 71.25
tokens: 11681
characters: 1949
timestamp: 2025-12-24T06:32:43.771591
finish_reason: stop
---

<table>
  <tr>
    <th>ключи</th>
    <th>21</th>
    <th>9</th>
    <th>4</th>
    <th>25</th>
    <th>7</th>
    <th>12</th>
    <th>3</th>
    <th>10</th>
    <th>19</th>
    <th>29</th>
    <th>17</th>
    <th>6</th>
    <th>26</th>
    <th>18</th>
  </tr>
  <tr>
    <th>G'_j</th>
    <td>21</td>
    <td></td>
    <td></td>
    <td>25</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>19</td>
    <td>29</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <th>G_j</th>
    <td>21</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>19</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <th>L'_j</th>
    <td>9</td>
    <td>4</td>
    <td></td>
    <td>7</td>
    <td>12</td>
    <td>3</td>
    <td>10</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <th>L_j</th>
    <td>9</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>12</td>
  </tr>
</table>

(б)

Рисунок 13.5 Множества G_j и L_j, составляющие множество ключей на пути к ключу k_j = 17. (а) Чёрные вершины содержат ключи из G_j, белые из L_j, остальные вершины — серые. Выделен путь к ключу k_j. Ключи левее пунктирной линии меньше k_j, ключи правее — больше. (б) Множество G'_j = {21, 25, 19, 29} состоит из ключей, добавленных раньше ключа 17 и больших 17. Множество G_j = {21, 19} содержит ключи, бывшие ближайшими справа к ключу 17, то есть бывшие минимальными в уже появившейся части G'_j. Ключ 21 был добавлен первым к G'_j и попал в G_j; ключ 25 не попал (он больше текущего минимума, равного 21). Ключ 19 попадает в G_j, потому что он меньше 21, а 29 — нет, так как 29 > 19. Множества L'_j и L_j строятся аналогичным образом.