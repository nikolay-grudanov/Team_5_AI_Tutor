---
source_image: page_694.png
page_number: 694
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 56.93
tokens: 11906
characters: 1745
timestamp: 2025-12-24T03:47:02.177725
finish_reason: stop
---

<table>
  <tr>
    <th>Alфавитный перечень команд ex</th>
    <th></th>
  </tr>
  <tr>
    <td>tagn[!]</td>
    <td>tagnext</td>
  </tr>
  <tr>
    <td>Найти следующее вхождение текущего тега.</td>
    <td></td>
  </tr>
  <tr>
    <td>tagp[!]</td>
    <td>tagpop</td>
  </tr>
  <tr>
    <td>Вернуться к последнему вхождению предыдущего тега.</td>
    <td></td>
  </tr>
  <tr>
    <td>tagpr[!]</td>
    <td>tagprev</td>
  </tr>
  <tr>
    <td>Вернуться к предыдущему вхождению текущего тега.</td>
    <td></td>
  </tr>
  <tr>
    <td>tagt[!]</td>
    <td>tagtop</td>
  </tr>
  <tr>
    <td>Вернуться к работе с первым из тегов.</td>
    <td></td>
  </tr>
  <tr>
    <td>una word</td>
    <td>unabbreviate</td>
  </tr>
  <tr>
    <td>Удалить слово <i>word</i> из списка сокращений.</td>
    <td></td>
  </tr>
  <tr>
    <td>u</td>
    <td>undo</td>
  </tr>
  <tr>
    <td>Обратить изменения, внесенные последней командой редактирования.</td>
    <td></td>
  </tr>
  <tr>
    <td>unm[!] char</td>
    <td>unmap</td>
  </tr>
  <tr>
    <td>Удалить символ <i>char</i> из списка макросов. Используйте символ ! для удаления макросов режима ввода.</td>
    <td></td>
  </tr>
  <tr>
    <td>[address] v/pattern/[commands]</td>
    <td>v</td>
  </tr>
  <tr>
    <td>Применить команды <i>commands</i> ко всем строкам, не содержащим соответствия шаблону <i>pattern</i>. Если команды не заданы, отобразить все соответствующие строки. Команда v эквивалентна g!. См. global.</td>
    <td></td>
  </tr>
  <tr>
    <td><b>Пример</b><br>:v/#include/d Удалить все строки, кроме содержащих «#include»</td>
    <td></td>
  </tr>
  <tr>
    <td>ve</td>
    <td>version</td>
  </tr>
  <tr>
    <td>Отобразить номер версии редактора.</td>
    <td></td>
  </tr>
</table>