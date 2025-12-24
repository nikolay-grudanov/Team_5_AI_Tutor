---
source_image: page_603.png
page_number: 603
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 63.41
tokens: 12174
characters: 2238
timestamp: 2025-12-24T03:42:48.139145
finish_reason: stop
---

<table>
  <tr>
    <th>Команда</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>!?string?</td>
    <td>Самая недавняя команда, содержащая строку string</td>
  </tr>
  <tr>
    <td>!?string?%</td>
    <td>Аргумент самой недавней команды, содержащий строку string</td>
  </tr>
  <tr>
    <td>!$</td>
    <td>Последний аргумент предыдущей команды</td>
  </tr>
  <tr>
    <td>!!string</td>
    <td>Выполнить предыдущую команду с добавлением строки string</td>
  </tr>
  <tr>
    <td>!N string</td>
    <td>Выполнить команду с номером N с добавлением строки string</td>
  </tr>
  <tr>
    <td>!{s1}s2</td>
    <td>Самая недавняя команда, начинающаяся со строки s1; выполнить с добавлением строки s2</td>
  </tr>
  <tr>
    <td>^old^new^</td>
    <td>Быстрая подстановка; в последней команде заменить строку old на строку new и выполнить измененную команду</td>
  </tr>
</table>

Примеры подстановки команд

Рассматривается следующая команда:

%3 vi cprogs/01.c ch002 ch03

<table>
  <tr>
    <th>Номер события</th>
    <th>Введенная команда</th>
    <th>Выполняемая команда</th>
  </tr>
  <tr>
    <td>4</td>
    <td>^00^0</td>
    <td>vi cprogs/01.c ch02 ch03</td>
  </tr>
  <tr>
    <td>5</td>
    <td>nroff !*</td>
    <td>nroff cprogs/01.c ch02 ch03</td>
  </tr>
  <tr>
    <td>6</td>
    <td>nroff !$</td>
    <td>nroff ch03</td>
  </tr>
  <tr>
    <td>7</td>
    <td>!vi</td>
    <td>vi cprogs/01.c ch02 ch03</td>
  </tr>
  <tr>
    <td>8</td>
    <td>!6</td>
    <td>nroff ch03</td>
  </tr>
  <tr>
    <td>9</td>
    <td>!?01</td>
    <td>vi cprogs/01.c ch02 ch03</td>
  </tr>
  <tr>
    <td>10</td>
    <td>!{nr}.new</td>
    <td>nroff ch03.new</td>
  </tr>
  <tr>
    <td>11</td>
    <td>!!!lp</td>
    <td>nroff ch03.new | lp</td>
  </tr>
  <tr>
    <td>12</td>
    <td>more !?pr?%</td>
    <td>more cprogs/01.c</td>
  </tr>
</table>

Подстановка слов

Двоеточие может предварять любой из спецификаторов слов:

<table>
  <tr>
    <th>Спецификатор</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>:0</td>
    <td>Имя команды</td>
  </tr>
  <tr>
    <td>:n</td>
    <td>Аргумент с номером n</td>
  </tr>
  <tr>
    <td>~</td>
    <td>Первый аргумент</td>
  </tr>
  <tr>
    <td>$</td>
    <td>Последний аргумент</td>
  </tr>
</table>