---
source_image: page_635.png
page_number: 635
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.90
tokens: 11610
characters: 1187
timestamp: 2025-12-24T03:43:52.506750
finish_reason: stop
---

<table>
  <tr>
    <th>where</th>
    <td><b>where command</b><br>Только для <b>tcsh</b>. Отобразить все псевдонимы, встроенные команды и программы с именем <i>command</i>.</td>
  </tr>
  <tr>
    <th>which</th>
    <td><b>which command</b><br>Только для <b>tcsh</b>. Отображение номера версии команды, которая будет выполнена. Идентично исполняемой программе <b>which</b>, но работает быстрее и учитывает встроенные команды <b>tcsh</b>.</td>
  </tr>
  <tr>
    <th>while</th>
    <td><b>while (expression)<br>commands<br>end</b><br>До тех пор пока истинно выражение <i>expression</i> (т. е. его значение не равно нулю), выполнять команды (<i>commands</i>) из тела цикла (между <b>while</b> и <b>end</b>). Для выхода из цикла и перехода к следующей итерации могут использоваться операторы <b>break</b> и <b>continue</b>. См. также пример в описании команды <b>shift</b>.

<b>Пример</b>

set user = (alice bob carol ted)
while ($argv[1] != $user[1])    <i>Перебирать пользователей в поисках совпадения</i>
    shift user
    if (#user == 0) then
        echo "$argv[1] нет в списке пользователей"
        exit 1
    endif
end    <i>Если пользователь не найден...</i></td>
  </tr>
</table>