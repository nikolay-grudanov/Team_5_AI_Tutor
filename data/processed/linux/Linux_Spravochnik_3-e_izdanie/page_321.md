---
source_image: page_321.png
page_number: 321
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 46.48
tokens: 11753
characters: 1552
timestamp: 2025-12-24T03:29:48.252506
finish_reason: stop
---

<table>
  <tr>
    <th>passwd</th>
    <td><b>passwd [user]</b><br>Создать или изменить пароль для пользователя <i>user</i>. Только владелец пароля или привилегированный пользователь могут изменять его. Владельцу не надо указывать свое имя.</td>
  </tr>
  <tr>
    <th>paste</th>
    <td><b>paste [options] files</b><br>Объединить соответствующие строки из одного или нескольких файлов (<i>files</i>) в вертикальные колонки, разделяемые табуляцией. См. также <b>cut</b>, <b>join</b> и <b>pr</b>.

<b>Параметры</b><br>
- Взять имена файлов со стандартного ввода.<br>
--d<em>char</em>, --delimiters=<em>char</em><br>
Разделять колонки символом <i>char</i>, а не символом табуляции. Примечание: колонки могут разделяться различными символами, перечисленными в параметре <b>-d</b>.<br>
--help<br>
Отобразить справку по использованию и завершить работу.<br>
--version<br>
Вывести информацию о номере версии и завершить работу.<br>
-s, --serial<br>
Объединить последовательные строки из одного файла.

<b>Примеры</b><br>
Создать трехколоночный файл <i>file</i> из файлов <i>x</i>, <i>y</i> и <i>z</i>:
<paste x y z > file</paste>
Перечислить пользователей в две колонки:
<who | paste - -></who>
Объединить строки попарно:
<paste -s -d"\t\n" list</paste>
</td>
  </tr>
  <tr>
    <th>patch</th>
    <td><b>patch [options][original [patchfile]]</b><br>Наложение «заплаты» <i>patchfile</i> на файл <i>original</i>. Исходный файл заменяется более новой исправленной версией и переименовывается в <i>original.orig</i> или в <i>original~</i>.</td>
  </tr>
</table>