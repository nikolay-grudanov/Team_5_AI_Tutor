---
source_image: page_407.png
page_number: 407
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.54
tokens: 11650
characters: 1421
timestamp: 2025-12-24T03:33:21.910983
finish_reason: stop
---

<table>
  <tr>
    <th>telnet</th>
    <th>Команды</th>
  </tr>
  <tr>
    <td></td>
    <td><b>CTRL-Z</b><br>Приостановить выполнение telnet.<br><b>![command]</b><br>Выполнить одну команду в интерпретаторе локальной системы. Если команда опущена, вызывается диалоговый интерпретатор.<br><b>?[command]</b><br>Получение справки о команде. «?» без аргументов приводит к выдаче конспекта справки. Если команда задана, отображается справка только по этой команде.</td>
  </tr>
  <tr>
    <td></td>
    <td><b>close</b><br>Завершить сеанс Telnet и вернуться в командный режим.<br><b>display argument ...</b><br>Отобразить значения всех или некоторых переменных set и toggle.<br><b>environ [arguments [...] ]</b><br>Управление переменными, значения которых могут быть посланы с параметром TELNET ENVIRON. Допустимые аргументы environ:<br>? Получение справки по команде environ.<br><b>define variable value</b><br>Определить переменную и ее значение.<br><b>undefine variable</b><br>Удалить определение переменной из списка переменных окружения.<br><b>export variable</b><br>Сделать значение переменной видимым для удаленной системы.<br><b>unexport variable</b><br>Сделать значение переменной невидимым для удаленной системы без специального запроса.<br><b>list</b><br>Перечислить значения существующих переменных.<br><b>logout</b><br>Если удаленный узел поддерживает команду logout, завершить сеанс telnet.</td>
  </tr>
</table>