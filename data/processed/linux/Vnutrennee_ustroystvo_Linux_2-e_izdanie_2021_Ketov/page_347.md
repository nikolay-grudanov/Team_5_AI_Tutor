---
source_image: page_347.png
page_number: 347
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.71
tokens: 7301
characters: 1542
timestamp: 2025-12-24T04:41:58.224326
finish_reason: stop
---

mktemp modinfo modprobe more mount mt mv nameif nc netstat nl
paste patch pidof ping ping6 pivot_root poweroff printf ps pwd
whoami xargs xxd xz xzcat yes zcat

/ # ps
PID   USER   COMMAND
ps: can't open '/proc': No such file or directory

/ # lsmod
lsmod: /proc/modules: No such file or directory
Module    Size Used by Not tainted

/ # lsscsi
lsscsi: can't change directory to '/sys/bus/scsi/devices': No such file or directory

Однако многие утилиты, например ps(1), отказываются работать в таком изолированном окружении в силу изоляции от той части дерева каталогов (каталоги /proc и /sys), где при помощи псевдофайловой системы proc или sysfs (см. разд. 3.4.4) ядром экспортируется информация о процессах и устройствах. Это в принципе и есть ожидаемый результат изоляции в случаях, когда она используется для предотвращения утечки информации третьим лицам, однако для организации работы хостинга это не тот результат, который требуется получить. Естественным решением в таком случае является повторное монтирование файловых систем proc и/или sysfs внутрь окружения.

Листинг 9.4. Протоконтейнер, созданный при помощи chroot, busybox, proc и sysfs

rick@ubuntu:~$ sudo chroot c-137/ busybox sh
/ # ps
PID   USER   COMMAND
ps: can't open '/proc': No such file or directory
/ # mount
? sh: mount: not found
! / # ln -s /bin/busybox /bin/mount
/ # mount
mount: no /proc/mounts
/ # mkdir /proc
1 / # mount -t proc none /proc
2 / # mount
1 none on /proc type proc (rw,relatime)
3 / # ps
PID   USER   COMMAND
1   0   {systemd} /sbin/init splash