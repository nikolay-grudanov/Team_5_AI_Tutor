---
source_image: page_679.png
page_number: 679
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 71.57
tokens: 12260
characters: 2662
timestamp: 2025-12-24T03:46:33.707484
finish_reason: stop
---

<table>
  <tr>
    <th>Команда</th>
    <th>Действие</th>
  </tr>
  <tr>
    <td>:n!</td>
    <td>Принудительное редактирование следующего файла в текущем буфере (не сохраняя изменения в текущем файле)</td>
  </tr>
  <tr>
    <td>:n files</td>
    <td>Задать новый список файлов для редактирования (<i>files</i>)</td>
  </tr>
  <tr>
    <td>:args</td>
    <td>Отобразить список файлов для редактирования</td>
  </tr>
  <tr>
    <td>:rew</td>
    <td>Перейти к началу списка файлов для редактирования</td>
  </tr>
</table>

Взаимодействие с интерпретатором

<table>
  <tr>
    <th>Команда</th>
    <th>Действие</th>
  </tr>
  <tr>
    <td>:r file</td>
    <td>Вставить содержимое файла <i>file</i> после курсора</td>
  </tr>
  <tr>
    <td>:r !command</td>
    <td>Вставить вывод команды <i>command</i> после текущей строки</td>
  </tr>
  <tr>
    <td>:nr !command</td>
    <td>То же, но вставить после строки <i>n</i> (строка 0 является первой строкой файла)</td>
  </tr>
  <tr>
    <td>!command</td>
    <td>Выполнить команду <i>command</i> и вернуться в vi</td>
  </tr>
  <tr>
    <td>!object command</td>
    <td>Послать содержимое объекта <i>object</i> в качестве ввода команде <i>command</i>; заменить объект <i>object</i> выводом команды</td>
  </tr>
  <tr>
    <td>:n1,n2! command</td>
    <td>Послать строки с <i>n1</i> по <i>n2</i> на ввод команды <i>command</i>; заменить строки выводом команды</td>
  </tr>
  <tr>
    <td>n!!command</td>
    <td>Послать <i>n</i> строк на ввод команды <i>command</i>; заменить их выводом команды</td>
  </tr>
  <tr>
    <td>!!</td>
    <td>Повторить последнюю команду интерпретатора</td>
  </tr>
  <tr>
    <td>!!command</td>
    <td>Заменить текущую строку выводом команды <i>command</i></td>
  </tr>
  <tr>
    <td>:sh</td>
    <td>Вызвать субинтерпретатор; вернуться к редактированию по символу <i>EOF</i></td>
  </tr>
  <tr>
    <td>Ctrl-Z</td>
    <td>Приостановить работу редактора, продолжить с помощью команды <i>fg</i></td>
  </tr>
  <tr>
    <td>:so file</td>
    <td>Прочитать и выполнить команды <i>ex</i> из файла <i>file</i></td>
  </tr>
</table>

Макрокоманды

<table>
  <tr>
    <th>Команда</th>
    <th>Действие</th>
  </tr>
  <tr>
    <td>:ab in out</td>
    <td>Использовать <i>in</i> в качестве сокращения <i>out</i></td>
  </tr>
  <tr>
    <td>:unab in</td>
    <td>Удалить сокращение <i>in</i></td>
  </tr>
  <tr>
    <td>:ab</td>
    <td>Перечислить сокращения</td>
  </tr>
  <tr>
    <td>:map c sequence</td>
    <td>Связать символ <i>c</i> с последовательностью команд <i>sequence</i></td>
  </tr>
  <tr>
    <td>:unmap c</td>
    <td>Отменить связку для символа <i>c</i></td>
  </tr>
</table>