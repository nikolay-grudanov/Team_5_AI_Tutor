---
source_image: page_125.png
page_number: 125
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 50.17
tokens: 11742
characters: 1633
timestamp: 2025-12-24T03:21:00.280352
finish_reason: stop
---

<table>
  <tr>
    <th>dip</th>
    <td>
      <b>help</b><br>
      Перечислить доступные команды.<br>
      <b>if expr goto label</b><br>
      Переход к секции с меткой <i>label</i>, если выражение <i>expr</i> истинно. В выражении происходит сравнение переменных и констант при помощи одного из операторов: =, !=, <, >, <= или >=.<br>
      <b>inc $variable [value]</b><br>
      Увеличить значение переменной <i>variable</i> на <i>value</i>. По умолчанию — на 1.<br>
      <b>init string</b><br>
      Задание строки, используемой для инициализации модема. По умолчанию это строка ATE0 Q0 V1 X1.<br>
      <b>mode protocol</b><br>
      Задание протокола соединения. Допустимые значения: SLIP, CSLIP, PPP и TERM. По умолчанию — SLIP.<br>
      <b>netmask mask</b><br>
      Задание маски подсети.<br>
      <b>parity E|O|N</b><br>
      Установка контроля четности линии: по четности (even), по нечетности (odd) или отсутствие контроля (none).<br>
      <b>password</b><br>
      Запросить пароль у пользователя.<br>
      <b>proxyarp</b><br>
      Добавить запись для ARP-прокси в локальную таблицу ARP.<br>
      <b>print $variable</b><br>
      Отобразить значение переменной <i>variable</i>.<br>
      <b>psend command</b><br>
      Выполнить команду в интерпретаторе и направить вывод команды в последовательное устройство. Команды выполняются с реальным идентификатором пользователя.<br>
      <b>port device</b><br>
      Указать последовательное устройство, к которому подключен modem.<br>
      <b>quit</b><br>
      Завершить работу с ненулевым кодом завершения. Происходит разрыв соединения.
    </td>
  </tr>
</table>