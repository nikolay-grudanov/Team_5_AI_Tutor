---
source_image: page_588.png
page_number: 588
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.63
tokens: 11706
characters: 1523
timestamp: 2025-12-24T03:41:38.444715
finish_reason: stop
---

% set a="[a-z]*" A="[A-Z]*"
% echo "$a" "$A"
[a-z]* [A-Z]*
% echo $a $A
at cc m4 Book Doc

%echo $a:x $A
[a-z]* Book Doc

% set d=($a:q $A:q)
% echo $d
at cc m4 Book Doc

% echo $d:q
[a-z]* [A-Z]*
% echo $d[1] +++ $d[2]
at cc m4 +++ Book Doc

% echo $d[1]:q
[a-z]*

Предопределенные переменные интерпретатора

Переменные могут устанавливаться двумя способами. Присваиванием значения:

set var=value

или простым включением:

set var

Ниже перечислены переменные. Те из них, которые могут содержать значения, отмечены знаком равенства и типом принимаемого значения, за которыми следует описание переменной. (Имейте в виду, что некоторым переменным, например argv, cwd или status, значения никогда не присваиваются явным образом.) Для переменных, которые могут быть включены или выключены, описан только эффект включенного состояния. Интерпретатор tcsh автоматически устанавливает (и в некоторых случаях обновляет) значения следующих переменных: addsuffix, argv, autologout, cwd, dirstack, echo-style, edit, gid, home, loginsh, logout, oid, owd, path, prompt, prompt2, prompt3, shell, shlvl, status, tcsh, term, tty, uid, user и version. Переменные, выделенные курсивом, являются особенностью tcsh.

<table>
  <tr>
    <th>Переменная</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td><i>addsuffix</i></td>
    <td>Добавлять символ / к именам каталогов и пробел к именам файлов при дополнении до уникального имени</td>
  </tr>
  <tr>
    <td><i>amrt</i></td>
    <td>Отображать время в 12-часовом формате</td>
  </tr>
</table>