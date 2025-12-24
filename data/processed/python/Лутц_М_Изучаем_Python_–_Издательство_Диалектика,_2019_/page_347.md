---
source_image: page_347.png
page_number: 347
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.69
tokens: 7946
characters: 2666
timestamp: 2025-12-24T01:18:13.059761
finish_reason: stop
---

<table>
  <tr>
    <th>Оператор</th>
    <th>Роль</th>
    <th>Пример</th>
  </tr>
  <tr>
    <td>global</td>
    <td>Пространства имен</td>
    <td>x = 'old'<br>def function():<br>    global x, y; x = 'new'</td>
  </tr>
  <tr>
    <td>nonlocal</td>
    <td>Пространства имен (Python 3.x)</td>
    <td>def outer():<br>    x = 'old'<br>    def function():<br>        nonlocal x; x = 'new'</td>
  </tr>
  <tr>
    <td>import</td>
    <td>Доступ к модулям</td>
    <td>import sys</td>
  </tr>
  <tr>
    <td>from</td>
    <td>Доступ к атрибутам</td>
    <td>from sys import stdin</td>
  </tr>
  <tr>
    <td>class</td>
    <td>Построение объектов</td>
    <td>class Subclass(Superclass):<br>    staticData = []<br>    def method(self): pass</td>
  </tr>
  <tr>
    <td>try/except/finally</td>
    <td>Перехват исключений</td>
    <td>try:<br>    action()<br>except:<br>    print('action error')</td>
  </tr>
  <tr>
    <td>raise</td>
    <td>Генерация исключений</td>
    <td>raise EndSearch(location)</td>
  </tr>
  <tr>
    <td>assert</td>
    <td>Отладочные проверки</td>
    <td>assert X > Y, 'X too small'</td>
  </tr>
  <tr>
    <td>with/as</td>
    <td>Диспетчеры контекста (Python 3.x, 2.6+)</td>
    <td>with open('data') as myfile:<br>    process(myfile)</td>
  </tr>
  <tr>
    <td>del</td>
    <td>Удаление ссылок</td>
    <td>del data[k]<br>    del data[i:j]<br>    del obj.attr<br>    del variable</td>
  </tr>
</table>

Формально в табл. 10.1 воспроизведены операторы Python 3.x. Хотя этого перечня операторов достаточно для обзора и справочных целей, в том виде, как есть, он не совсем полон. Ниже описано несколько тонкостей относительно его содержимого.

• Операторы присваивания имеют различные синтаксические формы, описанные в главе 11: базовая, последовательности, дополненная и др.
• Формально print в Python 3.x не является ни зарезервированным словом, ни оператором, а вызовом встроенной функции; но поскольку print почти всегда будет выполняться в виде оператора с выражением (и часто занимать отдельную строку), такой вызов в общем случае трактуется как разновидность оператора. Операции вывода рассматриваются в главе 11.
• Начиная с Python 2.5, yield — также выражение, а не оператор; подобно print оно обычно используется как оператор с выражением и потому включено в табл. 10.1, но в главе 20 мы увидим, что сценарии иногда присваивают или по-другому применяют его результат. Будучи выражением, yield также является ключевым словом в отличие от print.

Большая часть табл. 10.1 применима и к Python 2.x за исключением случаев, когда это не так — если вы используете Python 2.x, то ниже приведено несколько замечаний, которые его касаются.