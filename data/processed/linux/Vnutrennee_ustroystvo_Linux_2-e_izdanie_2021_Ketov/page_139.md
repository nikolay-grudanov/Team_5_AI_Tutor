---
source_image: page_139.png
page_number: 139
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.50
tokens: 7495
characters: 1858
timestamp: 2025-12-24T04:35:47.132921
finish_reason: stop
---

По отношению к объектам, доступ к которым ограничивается при помощи мандатных механизмов (см. разд. 3.6), возможности процесса определяются значениями его MAC-маркера доступа, а именно — атрибутом мандатной метки LABEL. Как и RUID/EUID/RGID/EGID, атрибут LABEL назначается первому процессу сеанса пользователя явным образом, а затем наследуется при клонировании процессами-потомками от процессов-родителей. В примере из листинга 4.22 при помощи команды id(1) показан атрибут LABEL сеанса пользователя, а при помощи команды ps(1) — его явное наследование от процесса-родителя. Аналогично изменениям EUID/EGID процесса, происходящим при запуске SUID-ной/SGID-ной программы, изменение метки LABEL процесса происходит (согласно мандатным правилам ①) в системном вызове exec(3) при запуске программы, помеченной соответствующей мандатной меткой файла. Так, например, при запуске программы /usr/sbin/dhclient с типом dhcpc_exec_t ее мандатной метки ③ процесс приобретает тип dhcpc_t своей мандатной метки ④, в результате чего существенно ограничивается в правах доступа к различным объектам операционной системы.

Листинг 4.22. MAC-маркер доступа процесса — мандатная метка selinux

fitz@ubuntu:~$ ssh lich@fedora
lich@fedora's password:
Last login: Sat Nov 21 14:25:16 2015

[lich@centos ~]$ id -Z
staff_u:staff_r:staff_t:s0-s0:c0.c1023

[lich@centos ~]$ ps Zf
LABEL PID TTY STAT TIME COMMAND
staff_u:staff_r:staff_t:s0-s0:c0.c1023 31396 pts/0 Ss 0:00 -bash
staff_u:staff_r:staff_t:s0-s0:c0.c1023 31835 pts/0 R+ 0:00 \_ ps Zf
staff_u:staff_r:staff_t:s0-s0:c0.c1023 31334 tty2 Ss+ 0:00 -bash

[lich@centos ~]$ sesearch -T -t dhcpc_exec_t -c process
Found 19 semantic te rules:

① type_transition NetworkManager_t dhcpc_exec_t : process dhcpc_t;

[lich@centos ~]$ ls -Z /usr/sbin/dhclient
② -rwxr-xr-x. root root system_u:object_r:dhcpc_exec_t:s0 /usr/sbin/dhclient