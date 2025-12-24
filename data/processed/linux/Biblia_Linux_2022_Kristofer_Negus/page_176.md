---
source_image: page_176.png
page_number: 176
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 87.04
tokens: 9066
characters: 5029
timestamp: 2025-12-24T04:50:59.203155
finish_reason: stop
---

Обычно команда top применяется для поиска процессов, которые потребляют слишком много памяти или вычислительной мощности, и взаимодействия с ними. У процесса, потребляющего слишком много ресурсов ЦП, можно сменить приоритет. Или полностью завершить его (убить). Пример использования top.

● Смена приоритета. Запомните идентификатор процесса, для которого нужно сменить приоритет, и, когда появится сообщение PID to renice, введите номер. При появлении запроса Renice PID to value на изменение значения PID введите число от –20 до 19. (См. подраздел «Настройка приоритета с помощью команд nice и renice» далее в этой главе, чтобы узнать о значениях для renice.)

● Убийство процесса. Запомните идентификатор процесса и нажмите клавишу k. Введите 15, чтобы процесс завершил работу, или 9, чтобы остановить его сразу. (Дополнительную информацию о различных сигналах, которые можно посылать процессам, см. в подразделе «Завершение процессов с помощью команд kill и killall» далее в этой главе.)

Перечисление процессов с помощью программы «Системный монитор»

Если у вас рабочий стол GNOME, то вы можете воспользоваться программой «Системный монитор» (System Monitor), которая отображает все процессы в системе в графическом представлении. Процессы сортируются щелчками кнопкой мыши на столбцах. Можно также щелкнуть правой кнопкой мыши на процессе, чтобы заморозить или завершить его либо изменить его приоритет.

Чтобы запустить программу System Monitor в GNOME, нажмите клавишу Windows, а затем введите System Monitor и нажмите клавишу Enter. Затем выберите вкладку Processes (Процессы). На рис. 6.2 показано окно System Monitor (Системный монитор) с процессами текущего пользователя, отсортированными по степени использования памяти.

<table>
  <tr>
    <th>Process Name</th>
    <th>User</th>
    <th>% CPU</th>
    <th>ID</th>
    <th>Memory</th>
    <th>Disk read tota</th>
    <th>Disk write tot</th>
    <th>Disk read</th>
    <th>Disk write</th>
    <th>Priority</th>
  </tr>
  <tr>
    <td>gnome-shell</td>
    <td>chris</td>
    <td>1</td>
    <td>2366</td>
    <td>276.8 MiB</td>
    <td>11.4 MiB</td>
    <td>952.0 KiB</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Normal</td>
  </tr>
  <tr>
    <td>Web Content</td>
    <td>chris</td>
    <td>1</td>
    <td>3233</td>
    <td>198.6 MiB</td>
    <td>16.5 MiB</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Normal</td>
  </tr>
  <tr>
    <td>firefox</td>
    <td>chris</td>
    <td>0</td>
    <td>3030</td>
    <td>141.2 MiB</td>
    <td>220.8 MiB</td>
    <td>128.2 MiB</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Normal</td>
  </tr>
  <tr>
    <td>gnome-software</td>
    <td>chris</td>
    <td>0</td>
    <td>2644</td>
    <td>51.8 MiB</td>
    <td>9.7 MiB</td>
    <td>2.1 MiB</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Normal</td>
  </tr>
  <tr>
    <td>Web Content</td>
    <td>chris</td>
    <td>0</td>
    <td>16945</td>
    <td>19.6 MiB</td>
    <td>10.6 MiB</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Normal</td>
  </tr>
  <tr>
    <td>gnome-system-monitor</td>
    <td>chris</td>
    <td>0</td>
    <td>16924</td>
    <td>16.9 MiB</td>
    <td>10.3 MiB</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Normal</td>
  </tr>
  <tr>
    <td>seapplet</td>
    <td>chris</td>
    <td>0</td>
    <td>2687</td>
    <td>15.2 MiB</td>
    <td>612.0 KiB</td>
    <td>12.0 KiB</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Normal</td>
  </tr>
  <tr>
    <td>evolution-alarm-notify</td>
    <td>chris</td>
    <td>0</td>
    <td>2690</td>
    <td>12.8 MiB</td>
    <td>996.0 KiB</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Normal</td>
  </tr>
  <tr>
    <td>gnome-terminal-server</td>
    <td>chris</td>
    <td>0</td>
    <td>3467</td>
    <td>12.5 MiB</td>
    <td>15.3 MiB</td>
    <td>20.0 KiB</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Normal</td>
  </tr>
  <tr>
    <td>tracker-store</td>
    <td>chris</td>
    <td>0</td>
    <td>2677</td>
    <td>11.4 MiB</td>
    <td>5.4 MiB</td>
    <td>312.0 KiB</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Normal</td>
  </tr>
  <tr>
    <td>Xwayland</td>
    <td>chris</td>
    <td>0</td>
    <td>2392</td>
    <td>10.8 MiB</td>
    <td>244.0 KiB</td>
    <td>24.0 KiB</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Normal</td>
  </tr>
  <tr>
    <td>evolution-source-registry</td>
    <td>chris</td>
    <td>0</td>
    <td>2458</td>
    <td>9.8 MiB</td>
    <td>23.5 MiB</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Normal</td>
  </tr>
  <tr>
    <td>evolution-calendar-factory-subf chris</td>
    <td>chris</td>
    <td>0</td>
    <td>2715</td>
    <td>9.8 MiB</td>
    <td>624.0 KiB</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Normal</td>
  </tr>
  <tr>
    <td>ibus-x11</td>
    <td>chris</td>
    <td>0</td>
    <td>2434</td>
    <td>9.6 MiB</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Normal</td>
  </tr>
</table>

Рис. 6.2. Окно программы System Monitor