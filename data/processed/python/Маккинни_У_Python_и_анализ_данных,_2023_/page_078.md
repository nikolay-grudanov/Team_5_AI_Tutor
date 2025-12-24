---
source_image: page_078.png
page_number: 78
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.35
tokens: 7939
characters: 2402
timestamp: 2025-12-24T02:42:12.686389
finish_reason: stop
---

Пересечение множеств содержит элементы, встречающиеся в обоих множествах. Вычислить его можно с помощью метода intersection или бинарного оператора &:

In [130]: a.intersection(b)
Out[130]: {3, 4, 5}

In [131]: a & b
Out[131]: {3, 4, 5}

Наиболее употребительные методы множеств перечислены в табл. 3.1.

Таблица 3.1. Операции над множествами в Python

<table>
  <tr>
    <th>Функция</th>
    <th>Альтернативный синтаксис</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>a.add(x)</td>
    <td>Нет</td>
    <td>Добавить элемент x в множество a</td>
  </tr>
  <tr>
    <td>a.clear()</td>
    <td>Нет</td>
    <td>Опустошить множество, удалив из него все элементы</td>
  </tr>
  <tr>
    <td>a.remove(x)</td>
    <td>Нет</td>
    <td>Удалить элемент x из множества a</td>
  </tr>
  <tr>
    <td>a.pop()</td>
    <td>Нет</td>
    <td>Удалить какой-то элемент x из множества a и возбудить исключение KeyError, если множество пусто</td>
  </tr>
  <tr>
    <td>a.union(b)</td>
    <td>a | b</td>
    <td>Найти все уникальные элементы, входящие либо в a, либо в b</td>
  </tr>
  <tr>
    <td>a.update(b)</td>
    <td>a |= b</td>
    <td>Присвоить a объединение элементов a и b</td>
  </tr>
  <tr>
    <td>a.intersection(b)</td>
    <td>a & b</td>
    <td>Найти все элементы, входящие и в a, и в b</td>
  </tr>
  <tr>
    <td>a.intersection_update(b)</td>
    <td>a &= b</td>
    <td>Присвоить a пересечение элементов a и b</td>
  </tr>
  <tr>
    <td>a.difference(b)</td>
    <td>a - b</td>
    <td>Найти элементы, входящие в a, но не входящие в b</td>
  </tr>
  <tr>
    <td>a.difference_update(b)</td>
    <td>a -= b</td>
    <td>Записать в a элементы, которые входят в a, но не входят в b</td>
  </tr>
  <tr>
    <td>a.symmetric_difference(b)</td>
    <td>a ^ b</td>
    <td>Найти элементы, входящие либо в a, либо в b, но не в a и b одновременно</td>
  </tr>
  <tr>
    <td>a.symmetric_difference_update(b)</td>
    <td>a ^= b</td>
    <td>Записать в a элементы, которые входят либо в a, либо в b, но не в a и b одновременно</td>
  </tr>
  <tr>
    <td>a.issubset(b)</td>
    <td>Нет</td>
    <td>True, если все элементы a входят также и в b</td>
  </tr>
  <tr>
    <td>a.issuperset(b)</td>
    <td>Нет</td>
    <td>True, если все элементы b входят также и в a</td>
  </tr>
  <tr>
    <td>a.isdisjoint(b)</td>
    <td>Нет</td>
    <td>True, если у a и b нет ни одного общего элемента</td>
  </tr>
</table>