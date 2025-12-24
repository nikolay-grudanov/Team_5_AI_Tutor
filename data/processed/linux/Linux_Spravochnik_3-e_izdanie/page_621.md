---
source_image: page_621.png
page_number: 621
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.17
tokens: 11682
characters: 1402
timestamp: 2025-12-24T03:43:22.694016
finish_reason: stop
---

<table>
  <tr>
    <th>fg</th>
    <td>% %<br>% fg<br>% fg %<br>% fg %vi <i>По имени задачи (поиск)</i></td>
  </tr>
  <tr>
    <th>filetest</th>
    <td><b>filetest -op files</b><br>Только для <b>tcsh</b>. Применить оператор проверки (<i>op</i>) к перечисленным файлам. Выдать результаты в виде списка. В разделе «Операторы опроса файлов» перечислены допустимые операторы.</td>
  </tr>
  <tr>
    <th>foreach</th>
    <td><b>foreach name (wordlist)<br>commands<br>end</b><br>Присваивать переменной <i>name</i> последовательно значения из списка <i>wordlist</i> и выполнять команды <i>commands</i> на каждой итерации. <b>foreach</b> можно использовать в качестве многострочной команды, набираемой в приглашении интерпретатора C shell (см. первый пример ниже) либо в сценарии (второй пример).<br><b>Примеры</b><br>Переименовать все файлы, имена которых начинаются с заглавной буквы:<br><pre>% foreach i ([A-Z]*)
? mv $i $i.new
? end</pre><br>Проверить, является ли параметром каждый из аргументов командной строки:<br><pre>foreach arg ($argv)
# начинается ли с символа - ?
if ("$arg" =~ -*) then
    echo "Аргумент является параметром"
else
    echo "Аргумент является именем файла"
endif
end</pre></td>
  </tr>
  <tr>
    <th>glob</th>
    <td><b>glob wordlist</b><br>Выполнить подстановку переменных, команд журнала и расширений имен файлов в список слов <i>wordlist</i>. Символы</td>
  </tr>
</table>