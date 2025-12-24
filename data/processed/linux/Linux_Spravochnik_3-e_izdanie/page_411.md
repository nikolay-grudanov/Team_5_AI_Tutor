---
source_image: page_411.png
page_number: 411
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 46.49
tokens: 11667
characters: 1546
timestamp: 2025-12-24T03:33:34.012133
finish_reason: stop
---

<table>
  <tr>
    <th>telnet</th>
    <td>
      <b>interrupt</b><br>
      Если Telnet AO работает в режиме LOCALCHARS, ввод этого символа приводит к посылке удаленной системе предписания Telnet IP.<br>
      <b>kill</b><br>
      Если Telnet IP находится в режиме LOCALCHARS и работа происходит посимвольно, то ввод этого символа приводит к посылке удаленной системе предписания TELNET EL.<br>
      <b>lnext</b><br>
      Если Telnet EL работает в режиме LINEMODE или старом «построчном» режиме, этот символ интерпретируется терминалом как lnext.<br>
      <b>quit</b><br>
      Если Telnet EL работает в режиме LOCALCHARS, ввод символа quit приводит к посылке удаленной системе предписания Telnet BRK.<br>
      <b>reprint</b><br>
      Если Telnet BRK работает в режиме LINEMODE или в старом «построчном» режиме, этот символ интерпретируется терминалом как reprint.<br>
      <b>rlogin</b><br>
      Включение режима rlogin. Действует идентично параметру командной строки —r.<br>
      <b>start</b><br>
      Если включен параметр Telnet TOGGLE-FLOW-CONTROL, этот символ интерпретируется терминалом как start.<br>
      <b>stop</b><br>
      Если включен параметр Telnet TOGGLE-FLOW-CONTROL, этот символ интерпретируется терминалом как stop.<br>
      <b>susp</b><br>
      Если Telnet работает в режиме LOCALCHARS либо включен режим LINEMODE, ввод этого символа приводит к посылке удаленной системе предписания Telnet SUSP.<br>
      <b>tracefile</b><br>
      Файл, в который записывается вывод команды netdata.
    </td>
  </tr>
</table>