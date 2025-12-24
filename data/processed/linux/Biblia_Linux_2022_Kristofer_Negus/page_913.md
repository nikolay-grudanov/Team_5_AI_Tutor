---
source_image: page_913.png
page_number: 913
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.91
tokens: 7474
characters: 1672
timestamp: 2025-12-24T05:10:45.916250
finish_reason: stop
---

# restorecon /etc/test.txt
# ls -Z /etc/test.txt
-rw-r--r--. root root unconfined_u:object_r:etc_t:s0    /etc/test.txt
# rm /etc/test.txt
rm: remove regular empty file `/etc/test.txt'? y

8. Чтобы определить, какие логические типы разрешают анонимную запись и доступ к домашнему каталогу службы tftp, а затем включить эти логические типы навсегда, введите следующие команды:

# getsebool -a | grep tftp
tftp_home_dir --> off
tftpd_anon_write --> off
...
# setsebool -P tftp_home_dir=on
# setsebool -P tftp_anon_write=on
# getsebool tftp_home_dir tftp_anon_write
tftp_home_dir --> on
tftp_anon_write --> on

9. Чтобы перечислить все модули политики SELinux в своей системе вместе с их номерами версий, введите команду semodule -l.

ПРИМЕЧАНИЕ
Команда ls /etc/selinux/targeted/modules/active/modules/*.pp подходит в качестве ответа, однако она не дает вам номера версий модулей политики. Только команда semodule -l выводит номера версий.

10. Чтобы разрешить доступ к службе sshd через TCP-порт 54 903 в SELinux, введите следующее:

# semanage port -a -t ssh_port_t -p tcp 54903
# semanage port -l | grep ssh
ssh_port_t        tcp        54903, 22

Глава 25. Защита Linux в сети

1. Чтобы установить утилиту Network Mapper (она же nmap) в локальную систему Linux, выполните следующие действия:
   а) в системе Fedora или RHEL введите команду yum install nmap в командной строке;
   б) в системе Ubuntu пакет nmap может быть предустановлен заранее. Если его нет, введите команду sudo apt-get install nmap в командной строке.
2. Чтобы запустить сканирование TCP Connect на локальном адресе интернет-протокола loopback, введите в командной строке nmap-sT 27.0.0. Порты, которые