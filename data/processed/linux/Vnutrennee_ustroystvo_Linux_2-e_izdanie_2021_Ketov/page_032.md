---
source_image: page_032.png
page_number: 32
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.87
tokens: 7806
characters: 2163
timestamp: 2025-12-24T04:33:00.784150
finish_reason: stop
---

Таблица 2.1. (окончание)

<table>
  <tr>
    <th>Управляющий символ</th>
    <th colspan="2">Стандартное действие драйвера</th>
    <th>Клавиши</th>
    <th>Код символа</th>
  </tr>
  <tr>
    <th>Нотация</th>
    <th>ввод символа</th>
    <th>выход символа</th>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td>^U</td>
    <td>kill</td>
    <td>—</td>
    <td>CTRL U</td>
    <td>0x15 NAK</td>
  </tr>
  <tr>
    <td>^I или \t</td>
    <td>—</td>
    <td>tab</td>
    <td>TAB или CTRL I</td>
    <td>0x09 HT</td>
  </tr>
  <tr>
    <td>^M или \r</td>
    <td>eol</td>
    <td>cr</td>
    <td>ENTER или CTRL M</td>
    <td>0x0D CR</td>
  </tr>
  <tr>
    <td>^J или \n</td>
    <td>eol</td>
    <td>nl</td>
    <td>CTRL J</td>
    <td>0x0A LF</td>
  </tr>
  <tr>
    <td>^S</td>
    <td>stop</td>
    <td>—</td>
    <td>CTRL S</td>
    <td>0x13 DC3</td>
  </tr>
  <tr>
    <td>^Q</td>
    <td>start</td>
    <td>—</td>
    <td>CTRL Q</td>
    <td>0x11 DC1</td>
  </tr>
  <tr>
    <td>^R</td>
    <td>rprnt</td>
    <td>—</td>
    <td>CTRL R</td>
    <td>0x12 DC2</td>
  </tr>
  <tr>
    <td>^V</td>
    <td>lnext</td>
    <td>—</td>
    <td>CTRL V</td>
    <td>0x16 SYN</td>
  </tr>
  <tr>
    <td>^N</td>
    <td>—</td>
    <td>so</td>
    <td>CTRL N</td>
    <td>0x0E SO</td>
  </tr>
  <tr>
    <td>^O</td>
    <td>—</td>
    <td>si</td>
    <td>CTRL O</td>
    <td>0x0F SI</td>
  </tr>
  <tr>
    <td>^[ или \e</td>
    <td>esc</td>
    <td>esc</td>
    <td>ESC или CTRL [ или CTRL 3</td>
    <td>0x1B ESC</td>
  </tr>
</table>

Так, например, нажатие клавиши ENTER или эквивалентное сочетание CTRL J, записывающееся как ^J, генерирует управляющий символ LF (таким же действием обладает символ CR, ^M), который сигнализирует драйверу терминала о завершении ввода строки (eol, end of line) и необходимости «отдать команду на выполнение» (листинг 2.2).

Листинг 2.2. Управляющие символы ^J и ^M

finn@ubuntu:~$ date
Вс. февр. 1 22:39:00 MSK 2015
finn@ubuntu:~$ hostname
ubuntu
finn@ubuntu:~$ whoami ^J
finn

Нажатие клавиши BACKSPACE или сочетания клавиш CTRL ? приводит к генерации управляющего символа DEL, что заставляет драйвер выполнить управляющее дейст-