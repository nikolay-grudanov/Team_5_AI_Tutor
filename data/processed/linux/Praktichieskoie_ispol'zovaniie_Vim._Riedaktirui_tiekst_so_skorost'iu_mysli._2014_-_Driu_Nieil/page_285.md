---
source_image: page_285.png
page_number: 285
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.62
tokens: 5680
characters: 1822
timestamp: 2025-12-24T04:15:34.003920
finish_reason: stop
---

Новая функция практически идентична прежней. Поэтому начнем с того, что создадим копию функции applyName, а затем с помощью команды подстановки заменим вхождения слова «Name» на «Number». Весь процесс показан в табл. 14.1.

Сможете ли вы найти здесь ошибку? Мы использовали диапазон %, из-за чего команда заменила все вхождения «Name» на «Number», тогда как нам следовало ограничить область действия команды второй функцией (копией).

Не волнуйтесь. Мы легко можем отменить изменения и исправить ошибку (как показано в табл. 14.2).

Команда gv выполняет переход в визуальный режим и восстанавливает последнее выделение (об этом рассказывалось в рецепте 21 в главе 4). Затем мы нажимаем : в визуальном режиме, и командная строка заполняется диапазоном :'<,'>, который ограничит область действия следующей за ним команды Ex выделенными строками.

Таблица 14.1. Ошибка при использовании команды подстановки

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>{start}</td>
    <td>mixin = {
      applyName: function(config) {
        return Factory(config, this.getName());
      },
    }</td>
  </tr>
  <tr>
    <td>Vjj</td>
    <td>mixin = {
      applyName: function(config) {
        return Factory(config, this.getName());
      },
    }</td>
  </tr>
  <tr>
    <td>yP</td>
    <td>mixin = {
      applyName: function(config) {
        return Factory(config, this.getName());
      },
      applyName: function(config) {
        return Factory(config, this.getName());
      },
    }</td>
  </tr>
  <tr>
    <td>:%s/Name/Number/g</td>
    <td>mixin = {
      applyNumber: function(config) {
        return Factory(config, this.getNumber());
      },
      applyNumber: function(config) {
        return Factory(config, this.getNumber());
      },
    }</td>
  </tr>
</table>