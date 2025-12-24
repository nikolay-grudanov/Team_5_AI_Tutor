---
source_image: page_136.png
page_number: 136
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 94.47
tokens: 9211
characters: 4991
timestamp: 2025-12-24T04:36:51.843461
finish_reason: stop
---

Демоны (daemons) выполняют системные программы, реализующие те или иные службы операционной системы. Например, cron(8) реализует службу периодического выполнения заданий, atd(8) — службу отложенного выполнения заданий, rsyslogd(8) — службу централизованной журнализации событий, sshd(8) — службу дистанционного доступа, systemd-udevd(8) — службу «регистрации» подключаемых устройств, и т. д. Демоны запускаются на ранних стадиях загрузки операционной системы и взаимодействуют с пользователем не интерактивно при помощи терминала, а опосредованно — при помощи своих утилит. Таким образом, отсутствие управляющего терминала в столбце TTY отличает их от прикладных процессов.

Листинг 4.19. Процессы ядра, демоны, прикладные процессы

fitz@ubuntu:~$ ps faxu

<table>
  <tr>
    <th>USER</th>
    <th>PID</th>
    <th>%CPU</th>
    <th>%MEM</th>
    <th>VSZ</th>
    <th>RSS</th>
    <th>TTY</th>
    <th>STAT</th>
    <th>START</th>
    <th>TIME</th>
    <th>COMMAND</th>
  </tr>
  <tr>
    <td>root</td>
    <td>2</td>
    <td>0.0</td>
    <td>0.0</td>
    <td>0</td>
    <td>0</td>
    <td>?</td>
    <td>S</td>
    <td>ноя18</td>
    <td>0:00</td>
    <td>[kthreadd]</td>
  </tr>
  <tr>
    <td>root</td>
    <td>3</td>
    <td>0.0</td>
    <td>0.0</td>
    <td>0</td>
    <td>0</td>
    <td>?</td>
    <td>I&lt;</td>
    <td>ноя18</td>
    <td>0:00</td>
    <td>\_ [rcu_gp]</td>
  </tr>
  <tr>
    <td>root</td>
    <td>4</td>
    <td>0.0</td>
    <td>0.0</td>
    <td>0</td>
    <td>0</td>
    <td>?</td>
    <td>I&lt;</td>
    <td>ноя18</td>
    <td>0:00</td>
    <td>\_ [rcu_par_gp]</td>
  </tr>
  <tr>
    <td>root</td>
    <td>6</td>
    <td>0.0</td>
    <td>0.0</td>
    <td>0</td>
    <td>0</td>
    <td>?</td>
    <td>I&lt;</td>
    <td>ноя18</td>
    <td>0:00</td>
    <td>\_ [kworker/0:0H...]</td>
  </tr>
  <tr>
    <td>root</td>
    <td>8</td>
    <td>0.0</td>
    <td>0.0</td>
    <td>0</td>
    <td>0</td>
    <td>?</td>
    <td>I&lt;</td>
    <td>ноя18</td>
    <td>0:00</td>
    <td>\_ [mm_percpu_wq]</td>
  </tr>
  <tr>
    <td>root</td>
    <td>9</td>
    <td>0.0</td>
    <td>0.0</td>
    <td>0</td>
    <td>0</td>
    <td>?</td>
    <td>S</td>
    <td>ноя18</td>
    <td>0:09</td>
    <td>\_ [ksoftirqd/0]</td>
  </tr>
  <tr>
    <td>root</td>
    <td>1</td>
    <td>0.0</td>
    <td>0.2</td>
    <td>168400</td>
    <td>11684</td>
    <td>?</td>
    <td>Ss</td>
    <td>ноя18</td>
    <td>0:12</td>
    <td>/sbin/init splash</td>
  </tr>
  <tr>
    <td>root</td>
    <td>333</td>
    <td>0.0</td>
    <td>0.1</td>
    <td>21844</td>
    <td>5348</td>
    <td>?</td>
    <td>Ss</td>
    <td>ноя18</td>
    <td>0:07</td>
    <td>/lib/systemd/systemd-udevd</td>
  </tr>
  <tr>
    <td>syslog</td>
    <td>606</td>
    <td>0.0</td>
    <td>0.1</td>
    <td>224360</td>
    <td>4244</td>
    <td>?</td>
    <td>Ssl</td>
    <td>ноя18</td>
    <td>0:01</td>
    <td>/usr/sbin/rsyslogd -n -i...</td>
  </tr>
  <tr>
    <td>root</td>
    <td>649</td>
    <td>0.0</td>
    <td>0.0</td>
    <td>20320</td>
    <td>3036</td>
    <td>?</td>
    <td>Ss</td>
    <td>ноя18</td>
    <td>0:00</td>
    <td>/usr/sbin/cron -f</td>
  </tr>
  <tr>
    <td>daemon</td>
    <td>675</td>
    <td>0.0</td>
    <td>0.0</td>
    <td>3736</td>
    <td>2184</td>
    <td>?</td>
    <td>Ss</td>
    <td>ноя18</td>
    <td>0:00</td>
    <td>/usr/sbin/atd -f</td>
  </tr>
  <tr>
    <td>root</td>
    <td>21545</td>
    <td>0.0</td>
    <td>0.0</td>
    <td>5560</td>
    <td>3420</td>
    <td>tty4</td>
    <td>Ss</td>
    <td>ноя18</td>
    <td>0:00</td>
    <td>/bin/login -p --</td>
  </tr>
  <tr>
    <td>fitz</td>
    <td>28152</td>
    <td>0.0</td>
    <td>0.0</td>
    <td>2600</td>
    <td>1784</td>
    <td>tty4</td>
    <td>S</td>
    <td>01:38</td>
    <td>0:00</td>
    <td>\_ -sh</td>
  </tr>
  <tr>
    <td>fitz</td>
    <td>28162</td>
    <td>0.0</td>
    <td>0.0</td>
    <td>12948</td>
    <td>3584</td>
    <td>tty4</td>
    <td>S+</td>
    <td>01:38</td>
    <td>0:00</td>
    <td>\_ bash</td>
  </tr>
  <tr>
    <td>finn</td>
    <td>12989</td>
    <td>0.2</td>
    <td>0.0</td>
    <td>12092</td>
    <td>3988</td>
    <td>tty4</td>
    <td>S+</td>
    <td>13:47</td>
    <td>0:00</td>
    <td>\_ man ps</td>
  </tr>
  <tr>
    <td>finn</td>
    <td>13000</td>
    <td>0.0</td>
    <td>0.0</td>
    <td>10764</td>
    <td>2544</td>
    <td>tty4</td>
    <td>S+</td>
    <td>13:47</td>
    <td>0:00</td>
    <td>\_ pager</td>
  </tr>
</table>

Системные (ядерные) процессы выполняют параллельные части ядра операционной системы, поэтому не обладают ни индивидуальной виртуальной памятью VSZ, ни управляющим терминалом TTY. Более того, ядерные процессы не выполняют отдельную программу, загружаемую из ELF-файла, поэтому их имена COMMAND яв-

1 Зачастую демоны имеют суффикс d в конце названия, например sshd — это secure shell daemon, а rsyslogd — rocket system logging daemon, и т. д.
2 Правильнее — ядерные нити, т. к. выполняются они в общей памяти ядра операционной системы.