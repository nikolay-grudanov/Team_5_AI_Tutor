---
source_image: page_079.png
page_number: 79
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 11.36
tokens: 7200
characters: 1029
timestamp: 2025-12-24T04:33:47.357623
finish_reason: stop
---

3 sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
4 /dev/sdb1 on /media/flash type vfat (rw,...)
5 /dev/sr0 on /media/cdrom type iso9660 (ro,...)

![Рис. 3.3. Монтирование файловых систем](../images/chapter3_3.png)

Рис. 3.3. Монтирование файловых систем

Несмотря на то, что в современных дистрибутивах Linux обнаружение и процедуры монтирования файловых систем автоматизированы, операции монтирования/размонтирования могут быть произведены вручную (листинг 3.31).

Листинг 3.21. Процедуры монтирования/размонтирования файловых систем

finn@ubuntu:~$ mount /dev/dvd /media/cdrom
mount: только root может сделать это
finn@ubuntu:~$ sudo mount /dev/dvd /media/cdrom
mount: /media/cdrom: ВНИМАНИЕ: устройство защищено от записи, смонтировано только для чтения.
finn@ubuntu:~$ mount
/dev/dvd on /media/cdrom type iso9660 (ro,...)
finn@ubuntu:~$ cat /media/cdrom/.disk/info
Ubuntu 19.10 "Eoan Ermine" - Release amd64 (20191017)
finn@ubuntu:~$ umount /media/cdrom
umount: /media/cdrom: umount failed: Операция не позволена.