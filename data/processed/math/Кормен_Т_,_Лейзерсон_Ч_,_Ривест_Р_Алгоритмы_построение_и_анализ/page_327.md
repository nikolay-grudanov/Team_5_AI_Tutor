---
source_image: page_327.png
page_number: 327
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.82
tokens: 11235
characters: 944
timestamp: 2025-12-24T06:35:18.202174
finish_reason: stop
---

<table>
  <tr>
    <th>i</th>
    <th>s_i</th>
    <th>f_i</th>
  </tr>
  <tr><td>1</td><td>1</td><td>4</td></tr>
  <tr><td>2</td><td>3</td><td>5</td></tr>
  <tr><td>3</td><td>0</td><td>6</td></tr>
  <tr><td>4</td><td>5</td><td>7</td></tr>
  <tr><td>5</td><td>3</td><td>8</td></tr>
  <tr><td>6</td><td>5</td><td>9</td></tr>
  <tr><td>7</td><td>6</td><td>10</td></tr>
  <tr><td>8</td><td>8</td><td>11</td></tr>
  <tr><td>9</td><td>8</td><td>12</td></tr>
  <tr><td>10</td><td>2</td><td>13</td></tr>
  <tr><td>11</td><td>12</td><td>14</td></tr>
</table>

Рисунок 17.1 Работа алгоритма Greedy-Activity-Selector для 11 заявок (таблица слева). Каждая строка на рисунке соответствует одному проходу цикла в строках 4–7. Серые заявки уже включены в \( A \), белая сейчас рассматривается. Если левый конец белого прямоугольника левее правого конца правого серого (стрелка идёт влево), то заявка отвергается. В противном случае она добавляется к \( A \).