---
source_image: page_088.png
page_number: 88
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 74.05
tokens: 8541
characters: 3275
timestamp: 2025-12-24T04:35:09.493246
finish_reason: stop
---

Дискреционные механизмы разграничения доступа используются для разграничения прав доступа процессов (см. разд. 4.5.1) как обычных пользователей ①, так и для ограничения прав системных программ ② (например, служб операционной системы), которые работают от лица псевдопользовательских учетных записей (см. разд. 2.7).

В примере из листинга 3.30 при помощи команды ps(1) проиллюстрированы процессы операционной системы, выполняющиеся от лица разных учетных записей.

Листинг 3.30. Субъекты разграничения прав доступа: пользователи и псевдопользователи

<table>
  <tr>
    <th>USER</th>
    <th>PID %CPU %MEM</th>
    <th>VSZ RSS TTY</th>
    <th>STAT START TIME COMMAND</th>
  </tr>
  <tr><td>root</td><td>2 0.0 0.0</td><td>0 0 ?</td><td>S ноя17 0:00 [kthreadd]</td></tr>
  <tr><td>root</td><td>3 0.0 0.0</td><td>0 0 ?</td><td>I<sup>&lt;</sup> ноя17 0:00 \_ [rcu_gp]</td></tr>
  <tr><td>root</td><td>4 0.0 0.0</td><td>0 0 ?</td><td>I<sup>&lt;</sup> ноя17 0:00 \_ [rcu_par_gp]</td></tr>
  <tr><td>root</td><td>1 0.0 0.2</td><td>167164 10936 ?</td><td>Ss ноя17 0:06 /sbin/init splash</td></tr>
  <tr><td>systemd+</td><td>577 0.0 0.2</td><td>20784 9836 ?</td><td>Ss ноя17 0:01 /lib/systemd/systemd-resolved</td></tr>
  <tr><td>syslog</td><td>606 0.0 0.1</td><td>224360 4584 ?</td><td>Ssl ноя17 0:01 /usr/sbin/rsyslogd -n -i NONE</td></tr>
  <tr><td>message+</td><td>617 0.0 0.1</td><td>9808 6448 ?</td><td>Ss ноя17 0:18 /usr/bin/dbus-daemon --system ...</td></tr>
  <tr><td>avahi</td><td>628 0.0 0.0</td><td>8532 3648 ?</td><td>Ss ноя17 0:00 avahi-daemon: running ...</td></tr>
  <tr><td>daemon</td><td>675 0.0 0.0</td><td>3736 2232 ?</td><td>Ss ноя17 0:00 /usr/sbin/atd -f</td></tr>
  <tr><td>whoopsie</td><td>812 0.0 0.3</td><td>330936 15844 ?</td><td>Ssl ноя17 0:00 /usr/bin/whoopsie -f</td></tr>
  <tr><td>root</td><td>1145 0.0 0.1</td><td>37168 4040 ?</td><td>Ss ноя17 0:00 /usr/lib/postfix/sbin/master -w</td></tr>
  <tr><td>postfix</td><td>1150 0.0 0.1</td><td>37556 5520 ?</td><td>S ноя17 0:00 \_ qmgr -l -t unix -u</td></tr>
  <tr><td>postfix</td><td>21924 0.0 0.1</td><td>37504 5400 ?</td><td>S 00:39 0:00 \_ pickup -l -t unix -u -c</td></tr>
  <tr><td>root</td><td>2539 0.0 0.2</td><td>251392 9792 ?</td><td>Ssl ноя17 0:00 /usr/sbin/gdm3</td></tr>
  <tr><td>root</td><td>17750 0.0 0.2</td><td>316608 9932 ?</td><td>Sl ноя17 0:00 \_ gdm-session-worker [pam/gdm-...</td></tr>
  <tr><td>finn</td><td>17764 0.0 0.1</td><td>166540 6908 tty3</td><td>Ssl+ ноя17 0:00 \_ /usr/lib/gdm3/gdm-x- ...</td></tr>
  <tr><td>finn</td><td>17766 0.1 1.8</td><td>237008 75900 tty3</td><td>Sl+ ноя17 0:23 \_ /usr/lib/xorg/Xorg ...</td></tr>
  <tr><td>finn</td><td>17774 0.0 0.3</td><td>194680 15940 tty3</td><td>Sl+ ноя17 0:00 \_ /usr/lib/gnome-sessi...</td></tr>
  <tr><td>finn</td><td>2987 0.0 0.3</td><td>21112 12356 ?</td><td>Ss ноя17 0:03 /lib/systemd/systemd --user</td></tr>
  <tr><td>finn</td><td>2992 0.0 0.0</td><td>168572 3124 ?</td><td>S ноя17 0:00 \_ (sd-pam)</td></tr>
  <tr><td>finn</td><td>17921 0.7 8.2</td><td>2641464 331536 ?</td><td>Ssl ноя17 2:01 \_ /usr/bin/gnome-shell</td></tr>
</table>

3.5.1. Владельцы и режим доступа к файлам

В рамках дискреционного разграничения доступа каждому файлу назначены пользователь-владелец ① и группа-владелец ② файла (листинг 3.31).