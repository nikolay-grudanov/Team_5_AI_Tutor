---
source_image: page_241.png
page_number: 241
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.86
tokens: 8069
characters: 3151
timestamp: 2025-12-24T01:14:44.091125
finish_reason: stop
---

Если метод вычисляет результат, тогда он также поступает обратно как результат всего выражения вызова метода. Вот более осозаемый пример:

```python
>>> S = 'spam'
>>> result = S.find('pa')    # Вызов метода find для поиска 'pa' в строке S
```

Такое отображение остается справедливым для методов встроенных типов и определяемых пользователем классов, которые мы исследуем позже. В этой части книги вы увидите, что большинство объектов имеют вызываемые методы, и все они доступны с использованием того же самого синтаксиса вызова методов. Как будет показано в последующих разделах, для вызова метода объекта необходим существующий объект; без такого объекта методы не могут быть выполнены (и имеют мало смысла).

Методы строк

В табл. 7.3 приведена сводка по методам и шаблонам вызовов для встроенных строковых объектов в Python 3.3; они часто меняются, поэтому проверяйте руководство по стандартной библиотеке Python на предмет самого актуального списка или запускайте dir или help на любой строке (либо имени типа str) интерактивным образом. Строчные методы Python 2.x слегка варьируются; например, они включают decode из-за их отличающейся обработки данных Unicode (то, что мы обсудим в главе 37). В табл. 7.3 имя S — это строковый объект, а необязательные аргументы помещены в квадратные скобки.

Таблица 7.3. Вызовы строковых методов в Python 3.3

<table>
  <tr>
    <th>S.capitalize()</th>
    <th>S.ljust(width [, fill])</th>
  </tr>
  <tr>
    <td>S.casefold()</td>
    <td>S.lower()</td>
  </tr>
  <tr>
    <td>S.center(width [, fill])</td>
    <td>S.lstrip([chars])</td>
  </tr>
  <tr>
    <td>S.count(sub [, start [, end]])</td>
    <td>S.maketrans(x[, y[, z]])</td>
  </tr>
  <tr>
    <td>S.encode([encoding [,errors]])</td>
    <td>S.partition(sep)</td>
  </tr>
  <tr>
    <td>S.endswith(suffix [, start [, end]])</td>
    <td>S.replace(old, new [, count])</td>
  </tr>
  <tr>
    <td>S.expandtabs([tabsize])</td>
    <td>S.rfind(sub [,start [,end]])</td>
  </tr>
  <tr>
    <td>S.find(sub [, start [, end]])</td>
    <td>S.rindex(sub [, start [, end]])</td>
  </tr>
  <tr>
    <td>S.format(fmtstr, *args, **kwargs)</td>
    <td>S.rjust(width [, fill])</td>
  </tr>
  <tr>
    <td>S.index(sub [, start [, end]])</td>
    <td>S.rpartition(sep)</td>
  </tr>
  <tr>
    <td>S.isalnum()</td>
    <td>S.rsplit([sep[, maxsplit]])</td>
  </tr>
  <tr>
    <td>S.isalpha()</td>
    <td>S.rstrip([chars])</td>
  </tr>
  <tr>
    <td>S.isdecimal()</td>
    <td>S.split([sep [,maxsplit]])</td>
  </tr>
  <tr>
    <td>S.isdigit()</td>
    <td>S.splitlines([keepends])</td>
  </tr>
  <tr>
    <td>S.isidentifier()</td>
    <td>S.startswith(prefix [, start [, end]])</td>
  </tr>
  <tr>
    <td>S.islower()</td>
    <td>S.strip([chars])</td>
  </tr>
  <tr>
    <td>S.isnumeric()</td>
    <td>S.swapcase()</td>
  </tr>
  <tr>
    <td>S.isprintable()</td>
    <td>S.title()</td>
  </tr>
  <tr>
    <td>S.isspace()</td>
    <td>S.translate(map)</td>
  </tr>
  <tr>
    <td>S.istitle()</td>
    <td>S.upper()</td>
  </tr>
  <tr>
    <td>S.isupper()</td>
    <td>S.zfill(width)</td>
  </tr>
  <tr>
    <td>S.join(iterable)</td>
    <td></td>
  </tr>
</table>