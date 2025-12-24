---
source_image: page_587.png
page_number: 587
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 61.73
tokens: 12085
characters: 2223
timestamp: 2025-12-24T03:42:02.791312
finish_reason: stop
---

:е Вернуть расширение переменной.
:h Вернуть заголовок переменной (имя каталога в полном имени файла).
:t Вернуть хвост переменной (за последним символом /).
:gr Вернуть все корни.
:ge Вернуть все расширения.
:gh Вернуть все заголовки.
:gt Вернуть все хвосты.
:q Заключить переменную (список слов) в кавычки, сохраняя разделение элементов. Модификатор полезен, если необходимо хранить имена файлов, содержащие специальные символы, которые не следует расширять.
:x Заключить шаблон в кавычки, расширяя его в список слов.

Примеры использования модификаторов путей

В следующей таблице приведены примеры использования модификаторов путей для переменной:

set aa=(/progs/num.c /book/chap.ps)

<table>
  <tr>
    <th>Часть переменной</th>
    <th>Запись</th>
    <th>Результат</th>
  </tr>
  <tr>
    <td>Обычная переменная</td>
    <td>echo $aa</td>
    <td>/progs/num.c /book/chap.ps</td>
  </tr>
  <tr>
    <td>Второй корень</td>
    <td>echo $aa[2]:r</td>
    <td>/book/chap</td>
  </tr>
  <tr>
    <td>Второй заголовок</td>
    <td>echo $aa[2]:h</td>
    <td>/book</td>
  </tr>
  <tr>
    <td>Второй хвост</td>
    <td>echo $aa[2]:t</td>
    <td><i>chap.ps</i></td>
  </tr>
  <tr>
    <td>Второе расширение</td>
    <td>echo $aa[2]:e</td>
    <td><i>ps</i></td>
  </tr>
  <tr>
    <td>Корень</td>
    <td>echo $aa:r</td>
    <td>/progs/num /book/chap.ps</td>
  </tr>
  <tr>
    <td>Все корни</td>
    <td>echo $aa:gr</td>
    <td>/progs/num /book/chap</td>
  </tr>
  <tr>
    <td>Заголовок</td>
    <td>echo $aa:h</td>
    <td>/progs /book/chap.ps</td>
  </tr>
  <tr>
    <td>Все заголовки</td>
    <td>echo $aa:gh</td>
    <td>/progs /book</td>
  </tr>
  <tr>
    <td>Хвост</td>
    <td>echo $aa:t</td>
    <td><i>num.c /book/chap.ps</i></td>
  </tr>
  <tr>
    <td>Все хвосты</td>
    <td>echo $aa:gt</td>
    <td><i>num.c chap.ps</i></td>
  </tr>
  <tr>
    <td>Расширение</td>
    <td>echo $aa:e</td>
    <td><i>c /book/chap.ps</i></td>
  </tr>
  <tr>
    <td>Все расширения</td>
    <td>echo $aa:ge</td>
    <td><i>c ps</i></td>
  </tr>
</table>

Примеры использования экранирующих модификаторов

Без экранирования интерпретатор расширяет специальные символы в именах файлов, представляя содержимое текущего каталога: