---
source_image: page_392.png
page_number: 392
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 62.70
tokens: 11960
characters: 2100
timestamp: 2025-12-24T03:33:04.994954
finish_reason: stop
---

<table>
  <tr>
    <th>rows rows*</th>
    <td>Задать количество строк.</td>
    <th>stty</th>
  </tr>
  <tr>
    <th>cols columns, columns columns*</th>
    <td>Задать количество колонок.</td>
    <th></th>
  </tr>
  <tr>
    <th>size*</th>
    <td>Отобразить текущие настройки строк и колонок.</td>
    <th></th>
  </tr>
  <tr>
    <th>line discipline*</th>
    <td>Установить режим работы линии.</td>
    <th></th>
  </tr>
  <tr>
    <th>speed</th>
    <td>Отобразить скорость терминала.</td>
    <th></th>
  </tr>
  <tr>
    <th>su [options] [user] [shell_args]</th>
    <td colspan="2">Создать интерпретатор с эффективным идентификатором другого пользователя (<i>user</i>). Если имя пользователя не указано, создается интерпретатор привилегированного пользователя (т. е. происходит превращение в суперпользователя). Сеанс завершается символом <i>EOF</i>. Можно запускать интерпретатор с различными параметрами (<i>shell_args</i>), т. е. если выполняется <b>sh</b>, то можно задать <b>-c command</b> для выполнения команды <i>command</i> в <b>sh</b> или <b>-r</b> для создания ограниченного интерпретатора.</td>
    <th>su</th>
  </tr>
  <tr>
    <th>Параметры</th>
    <td colspan="2"></td>
    <th></th>
  </tr>
  <tr>
    <th>–, –l, —login</th>
    <td>Выполнить полную регистрацию в системе (т. е. переход в окружение пользователя <i>user</i>).</td>
    <th></th>
  </tr>
  <tr>
    <th>–c <i>command</i>, —command=<i>command</i></th>
    <td>Выполнить команду в интерпретаторе и немедленно завершить работу в нем. Если команда состоит более чем из одного слова, ее необходимо заключить в кавычки:</td>
    <th></th>
  </tr>
  <tr>
    <td colspan="3">su -c 'find / -name \*.c -print' nobody</td>
    <th></th>
  </tr>
  <tr>
    <th>–f, —fast</th>
    <td>Выполнить интерпретатор с параметром –f. В <b>csh</b> и <b>tcsh</b> этот параметр подавляет чтение файла <i>.cshrc</i>. В <b>bash</b> параметр подавляет расширение имен по маске.</td>
    <th></th>
  </tr>
  <tr>
    <th>–m, –p, —preserve-environment</th>
    <td>Не сбрасывать переменные окружения.</td>
    <th></th>
  </tr>
</table>