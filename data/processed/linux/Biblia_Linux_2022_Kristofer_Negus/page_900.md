---
source_image: page_900.png
page_number: 900
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.10
tokens: 7584
characters: 2036
timestamp: 2025-12-24T05:10:30.254477
finish_reason: stop
---

добавив в файл /etc/sysconfig/iptables перед окончательным правилом DROP или REJECT следующее правило:

-A INPUT -m state --state NEW -m tcp -p tcp --dport 21 -j ACCEPT

в) настройте брандмауэр iptables для отслеживания подключений, загрузив соответствующий модуль в файл /etc/sysconfig/iptables-config:
IPTABLES_MODULES="nf_conntrack_ftp"

г) чтобы SELinux разрешил загрузку в каталог, сначала правильно установите контексты файлов:
# semanage fcontext -a -t public_content_rw_t "/var/ftp/in(/.*)?"
# restorecon -F -R -v /var/ftp/in

д) затем установите логический тип SELinux, чтобы разрешить загрузку:
# setsebool -P allow_ftpd_anon_write on

е) перезапустите службу vsftpd (service vsftpd restart systemctl restart vsftpd.service).

9. Установите FTP-клиент lftp (если у вас нет второй системы Linux, установите lftp на тот же хост, на котором работает FTP-сервер). При необходимости загрузите файл /etc/hosts в каталог in на сервере, чтобы убедиться, что он доступен. Выполните от имени суперпользователя следующие команды:
# yum install lftp
# lftp localhost
lftp localhost:/> cd in
lftp localhost:/in> put /etc/hosts
89 bytes transferred
lftp localhost:/in> quit

Вы не сможете увидеть, что скопировали файл hosts во входящий каталог. Однако введите следующую команду из оболочки на хосте, на котором запущен FTP-сервер, чтобы убедиться, что файл hosts находится в этом каталоге:
# ls /var/ftp/in/hosts

Если не можете загрузить файл, устраните проблему, как описано в упражнении 7, перепроверьте настройки файла vsftpd.conf и проверьте все права в каталоге /var/ftp/in.

10. Используя любой FTP-клиент, перейдите в каталог /pub/debian-meetings на сайте ftp://ftp.gnome.org и перечислите содержимое этого каталога. Вот как это можно сделать с помощью клиента lftp:
# lftp ftp://ftp.gnome.org/pub/debian-meetings/
cd ok, cwd=/pub/debian-meetings
lftp ftp.gnome.org:/pub/debian-meetings>> ls
drwxr-xr-x   3 ftp ftp    3 Jan 13 2 014 2004
drwxr-xr-x   6 ftp ftp    6 Jan 13 2014 2005
drwxr-xr-x   8 ftp ftp    8 Dec 20 2006 2006
...