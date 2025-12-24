---
source_image: page_604.png
page_number: 604
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 56.56
tokens: 12103
characters: 2082
timestamp: 2025-12-24T03:42:48.136646
finish_reason: stop
---

<table>
  <tr>
    <th>Спецификатор</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>:n-m</td>
    <td>Аргументы из диапазона от n до m</td>
  </tr>
  <tr>
    <td>-m</td>
    <td>Слова с 0 по m; идентично :0-m</td>
  </tr>
  <tr>
    <td>:n-</td>
    <td>Слова с n до предпоследнего</td>
  </tr>
  <tr>
    <td>:n*</td>
    <td>Аргументы от n до последнего; идентично n-$</td>
  </tr>
  <tr>
    <td>*</td>
    <td>Все аргументы; идентично ^-$ или 1-$</td>
  </tr>
  <tr>
    <td>#</td>
    <td>Текущая командная строка до текущей позиции; практически бесполезный спецификатор</td>
  </tr>
</table>

Примеры подстановки слов

Рассматривается команда

%13 cat ch01 ch02 ch03 biblio back

<table>
  <tr>
    <th>Номер события</th>
    <th>Введенная команда</th>
    <th>Выполняемая команда</th>
  </tr>
  <tr>
    <td>14</td>
    <td>ls !13^</td>
    <td>ls ch01</td>
  </tr>
  <tr>
    <td>15</td>
    <td>sort !13:*</td>
    <td>sort ch01 ch02 ch03 biblio back</td>
  </tr>
  <tr>
    <td>16</td>
    <td>more !cat:3*</td>
    <td>more ch03 biblio back</td>
  </tr>
  <tr>
    <td>17</td>
    <td>!cat:0-3</td>
    <td>cat ch01 ch02 ch03</td>
  </tr>
  <tr>
    <td>18</td>
    <td>vi !-5:4</td>
    <td>vi biblio</td>
  </tr>
</table>

Модификаторы команд журнала

Подстановки команд и слов могут модифицироваться следующим образом:

Отображение, замена и экранирование

<table>
  <tr>
    <th>Модификатор</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>:p</td>
    <td>Отобразить команду, но не выполнять ее</td>
  </tr>
  <tr>
    <td>s/old/new</td>
    <td>Заменить первое вхождение подстроки old на new</td>
  </tr>
  <tr>
    <td>gs/old/new</td>
    <td>Заменить все вхождения подстроки old на new</td>
  </tr>
  <tr>
    <td>&</td>
    <td>Повторить предыдущую замену (команда :s или ^) первого вхождения</td>
  </tr>
  <tr>
    <td>g&</td>
    <td>Повторить предыдущую замену для всех вхождений</td>
  </tr>
  <tr>
    <td>q</td>
    <td>Заключить список слов в кавычки</td>
  </tr>
  <tr>
    <td>x</td>
    <td>Заключить в кавычки отдельные слова</td>
  </tr>
</table>