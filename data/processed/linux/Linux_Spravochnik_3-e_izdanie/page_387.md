---
source_image: page_387.png
page_number: 387
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.50
tokens: 11852
characters: 1633
timestamp: 2025-12-24T03:32:34.879460
finish_reason: stop
---

<table>
  <tr>
    <th>stty</th>
    <th>Настройки флагов</th>
    <th>Режим управления данными</th>
  </tr>
  <tr>
    <td></td>
    <td><i>ortsfl rtsflow ctsflow</i></td>
    <td>Включить однонаправленное управление данными</td>
  </tr>
  <tr>
    <td></td>
    <td><i>ortsfl rtsflow -ctsflow</i></td>
    <td>Послать сигнал RTS при готовности к посылке данных</td>
  </tr>
  <tr>
    <td></td>
    <td><i>ortsfl -rtsflow ctsflow</i></td>
    <td>Режим не имеет влияния</td>
  </tr>
  <tr>
    <td></td>
    <td><i>ortsfl -rtsflow -ctsflow</i></td>
    <td>Включить двунаправленное управление данными</td>
  </tr>
  <tr>
    <td></td>
    <td><i>-ortsfl rtsflow ctsflow</i></td>
    <td>Включить двунаправленное управление данными</td>
  </tr>
  <tr>
    <td></td>
    <td><i>-ortsfl rtsflow -ctsflow</i></td>
    <td>Режим не имеет влияния</td>
  </tr>
  <tr>
    <td></td>
    <td><i>-ortsfl -rtsflow ctsflow</i></td>
    <td>Прекращать передачу при сбросе CTS</td>
  </tr>
  <tr>
    <td></td>
    <td><i>-ortsfl -rtsflow -ctsflow</i></td>
    <td>Отключить аппаратный контроль передачи данных</td>
  </tr>
</table>

Режимы ввода

[–]brkint
[Не] выдавать сигнал INTR при прерывании (break).

[–]icrnl
[Не] преобразовывать CR в NL при вводе.

[–]ignbrk
[Не] игнорировать прерывание (break) при вводе.

[–]igncr
[Не] игнорировать CR при вводе.

[–]ignpar
[Не] игнорировать ошибки четности.

[–]inlcr
[Не] преобразовывать NL в CR при вводе.

[–]inpck
[Отключить] включить контроль по четности для ввода.

[–]istrip
[Не] усекать вводимые символы до 7 бит.

[–]iuclc*
[Не] преобразовывать верхний регистр символов в нижний при вводе.