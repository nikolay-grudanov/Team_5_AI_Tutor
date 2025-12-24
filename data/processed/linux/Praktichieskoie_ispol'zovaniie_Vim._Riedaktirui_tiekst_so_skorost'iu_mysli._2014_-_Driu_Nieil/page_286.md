---
source_image: page_286.png
page_number: 286
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.90
tokens: 5635
characters: 1702
timestamp: 2025-12-24T04:15:35.808556
finish_reason: stop
---

Команда :&& требует дополнительных пояснений, поскольку первый и второй символы & в ней имеют разное значение. Первый из них образует команду Ex :&, которая повторяет последнюю команду :substitute (см. :h :& http://vimdoc.sourceforge.net/htmldoc/change.html#%3A%26), а второй указывает, что должны использоваться флаги из предыдущей команды :s.

Обсуждение

Мы всегда можем указать новый диапазон и повторить подстановку командой :&&. Не важно, какой диапазон использовался в последний раз. Сама команда :&& воздействует на текущую строку, команда :'<,'>&& воздействует на визуальное выделение, и команда :%&& воздействует на весь файл. Как мы уже видели, команда g& является удобным сокращением для команды :%&&.

Таблица 14.2. Изменение диапазона для команды подстановки

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>u</td>
    <td>mixin = {
      applyName: function(config) {
        return Factory(config, this.getName());
      },
      applyName: function(config) {
        return Factory(config, this.getName());
      }
    }</td>
  </tr>
  <tr>
    <td>gv</td>
    <td>mixin = {
      applyName: function(config) {
        return Factory(config, this.getName());
      },
      <span style="background-color:#e0e0e0">applyName: function(config) {</span>
        return Factory(config, this.getName());
      <span style="background-color:#e0e0e0">}</span>,
    }</td>
  </tr>
  <tr>
    <td>:'<,'>&&</td>
    <td>mixin = {
      applyName: function(config) {
        return Factory(config, this.getName());
      },
      applyNumber: function(config) {
        return Factory(config, this.getNumber());
      },
    }</td>
  </tr>
</table>