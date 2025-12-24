---
source_image: page_070.png
page_number: 70
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.90
tokens: 8434
characters: 1491
timestamp: 2025-12-24T02:17:54.283773
finish_reason: stop
---

Todo count: {{ todos | length }}
Todo count: 4

Примечание
Полный список фильтров и дополнительные сведения о фильтрах в Jinja см. на странице https://jinja.palletsprojects.com/en/3.0.x/templates/#builtin-filters.

Использование операторов if
Использование операторов if в Jinja аналогично их использованию в Python. if операторы используются в блоках управления {% %}. Давайте посмотрим на пример:

{% if todo | length < 5 %}
    You don't have much items on your todo list!
{% else %}
    You have a busy day it seems!
{% endif %}

Циклы
Мы также можем перебирать переменные в Jinja. Это может быть список или общая функция, например, следующая:

{% for todo in todos %}
    <b> {{ todo.item }} </b>
{% endfor %}

Вы можете получить доступ к специальным переменным внутри цикла for, таким как loop.index, который дает индекс текущей итерации. Ниже приведен список специальных переменных и их описания:

<table>
  <tr>
    <th>Variable</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>loop.index</td>
    <td>The current iteration of the loop (1 indexed)</td>
  </tr>
  <tr>
    <td>loop.index0</td>
    <td>The current iteration of the loop (0 indexed)</td>
  </tr>
  <tr>
    <td>loop.revindex</td>
    <td>The number of iterations from the end of the loop (1 indexed)</td>
  </tr>
  <tr>
    <td>loop.revindex0</td>
    <td>The number of iterations from the end of the loop (0 indexed)</td>
  </tr>
  <tr>
    <td>loop.first</td>
    <td>True if first iteration</td>
  </tr>
</table>