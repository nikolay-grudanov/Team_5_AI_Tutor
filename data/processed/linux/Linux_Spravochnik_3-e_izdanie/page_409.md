---
source_image: page_409.png
page_number: 409
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 56.94
tokens: 11770
characters: 1775
timestamp: 2025-12-24T03:33:43.908464
finish_reason: stop
---

<table>
  <tr>
    <th>telnet</th>
    <td>
      <b>ao</b><br>
      Послать последовательность Telnet AO, предписывающую удаленной системе сбросить весь вывод на терминал пользователя.<br>
      <b>ayt</b><br>
      Послать последовательность Telnet AYT (Are You There).<br>
      <b>brk</b><br>
      Послать последовательность Telnet BRK (Break).<br>
      <i>do cmd</i><br>
      <i>dont cmd</i><br>
      <i>will cmd</i><br>
      <i>wont cmd</i><br>
      Послать предписание Telnet DO <i>cmd</i>, где <i>cmd</i> является числом от 0 до 255 или именем определенной команды telnet. Если аргумент <i>cmd</i> имеет значение ? или help, отображается справка (включающая список имен команд).<br>
      <b>ec</b><br>
      Послать Telnet EC (Erase Character) — предписание удаленной системе стереть последний введенный символ.<br>
      <b>el</b><br>
      Послать Telnet EL (Erase Line) — предписание удаленной системе стереть последнюю введенную строку.<br>
      <b>eof</b><br>
      Послать предписание Telnet EOF (End Of File).<br>
      <b>eor</b><br>
      Послать предписание Telnet EOR (End Of Record).<br>
      <b>escape</b><br>
      Послать текущий escape-символ Telnet (изначально — ^).<br>
      <b>ga</b><br>
      Послать предписание Telnet GA (Go Ahead).<br>
      <b>getstatus</b><br>
      Если удаленная система поддерживает команду Telnet STATUS, getstatus посылает запрос на получение текущего состояния параметров сервера.<br>
      <b>ip</b><br>
      Послать Telnet IP (Interrupt Process) — предписание удаленной системе прекратить выполнение текущего задания.<br>
      <b>nop</b><br>
      Послать предписание Telnet NOP (No OPeration).<br>
      <b>susp</b><br>
      Послать предписание Telnet SUSP (SUSpend Process).
    </td>
  </tr>
</table>