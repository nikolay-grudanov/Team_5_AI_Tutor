---
source_image: page_035.png
page_number: 35
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.52
tokens: 7457
characters: 1422
timestamp: 2025-12-24T09:21:36.681001
finish_reason: stop
---

Выберите первый столбец с помощью селектора table td:first-child:

<table>
  <tr>
    <th>1</th>
    <th>2</th>
    <th>3</th>
  </tr>
  <tr>
    <td>1</td>
    <td>2</td>
    <td>3</td>
  </tr>
</table>

Обратите внимание: между td и :first-child нет пробела. Это важно, поскольку td :first-child (с пробелом) — совершенно другой селектор. Изменение несущественно, однако результаты разные, так как ваш результат будет эквивалентен td *:first-child.

Помните, что символ пробела является селектором иерархии элементов? Примеры ниже комбинируют псевдоселекторы с tr и td для выбора определенного столбца или строки.

table tr td:nth-child(2)

<table>
  <tr>
    <th>1</th>
    <th>2</th>
    <th>3</th>
  </tr>
  <tr>
    <td>1</td>
    <td style="background-color:#cccccc">2</td>
    <td>3</td>
  </tr>
</table>

table tr:nth-child(2) td:nth-child(2)

<table>
  <tr>
    <th>1</th>
    <th>2</th>
    <th>3</th>
  </tr>
  <tr>
    <td>1</td>
    <td style="background-color:#cccccc">2</td>
    <td>3</td>
  </tr>
</table>

table tr:nth-child(2)

<table>
  <tr>
    <th>1</th>
    <th>2</th>
    <th>3</th>
  </tr>
  <tr>
    <td style="background-color:#cccccc">1</td>
    <td>2</td>
    <td>3</td>
  </tr>
</table>

table tr:last-child td:last-child

<table>
  <tr>
    <th>1</th>
    <th>2</th>
    <th>3</th>
  </tr>
  <tr>
    <td>1</td>
    <td>2</td>
    <td style="background-color:#cccccc">3</td>
  </tr>
</table>