---
source_image: page_532.png
page_number: 532
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.25
tokens: 7648
characters: 2189
timestamp: 2025-12-24T05:00:25.442647
finish_reason: stop
---

Чтобы установить все только что упомянутые пакеты (samba-common устанавливается как зависимый пакет общего пакета samba, так что не нужно делать это отдельно), как суперпользователь введите из командной строки в дистрибутиве Fedora или RHEL следующее:

# yum install samba samba-client samba-winbind
...
Last metadata expiration check: 0:01:44 ago on Sun 24 Jan 2020
11:35:37 AM EST.
Dependencies resolved.
===============================================================================
Package           Architecture      Version   Repository         Size
===============================================================================
Installing:
  samba            x86_64           4.10.4-101.el8_1  rhel-8-for-x86_64-baseosrpms-739 k
  samba-winbind    x86_64           4.10.4-101.el8_1  rhel-8-for-x86_64-baseosrpms-570 k
Installing dependencies:
  samba-common-tools
    x86_64         4.10.4-101.el8_1  rhel-8-for-x86_64-baseosrpms-469 k
  samba-libs       x86_64           4.10.4-101.el8_1  rhel-8-for-x86_64-baseosrpms-185 k
  samba-winbind-modules
    x86_64         4.10.4-101.el8_1  rhel-8-for-x86_64-baseosrpms-122 k
  samba-client     x86_64           4.10.4-101.el8_1  rhel-8-for-x86_64-baseosrpms-658 k

Transaction Summary
===============================================================================
Install  6 Packages

Total download size: 2.5 M
Installed size: 6.8 M
Is this ok [y/d/N]: y

Чтобы просмотреть файлы конфигурации после того, как вы установили пакеты Samba, введите:

# rpm -qc samba-common
/etc/logrotate.d/samba
/etc/samba/lmhosts
/etc/samba/smb.conf
/etc/sysconfig/samba

Файлы /etc/logrotate.d/samba и /etc/sysconfig/samba обычно не изменяются. Первый устанавливает, как файлы в каталоге /var/log/samba обрабатываются (копируются в другие файлы и удаляются) с течением времени. Второй — это файл, в который можно поместить параметры, передаваемые демону smbd, nmbd или winbindd, чтобы отключить различные функции, например отладку.

Большинство файлов конфигурации, которые можно изменить для сервера Samba, находятся в каталоге /etc/samba. Файл smb.conf — это основной файл конфигурации, в котором содержатся основные настройки сервера, а также ин-