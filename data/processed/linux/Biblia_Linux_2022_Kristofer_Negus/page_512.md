---
source_image: page_512.png
page_number: 512
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.05
tokens: 7604
characters: 2154
timestamp: 2025-12-24T04:59:47.606156
finish_reason: stop
---

Если хотите получить более подробную информацию о пакете vsftpd, перейдите на сайт security.appspot.com/vsftpd.html. Здесь есть также дополнительная документация и информация о последних версиях vsftpd.

С помощью команд можно просмотреть полное содержимое пакета vsftpd (rpm-q1 vsftpd), только файлы документации (-qd) или файлы конфигурации (-qc). Для просмотра файлов документации используйте следующую команду:

# rpm -qd vsftpd
/usr/share/doc/vsftpd/EXAMPLE/INTERNET_SITE/README
...
/usr/share/doc/vsftpd/EXAMPLE/PER_IP_CONFIG/README
...
/usr/share/doc/vsftpd/EXAMPLE/VIRTUAL_HOSTS/README
/usr/share/doc/vsftpd/EXAMPLE/VIRTUAL_USERS/README
...
/usr/share/doc/vsftpd/FAQ
...
/usr/share/doc/vsftpd/vsftpd.xinetd
/usr/share/man/man5/vsftpd.conf.5.gz
/usr/share/man/man8/vsftpd.8.gz

В структуру каталогов /usr/share/doc/vsftpd/EXAMPLE включены примеры файлов конфигурации, которые помогут настроить пакет vsftpd способами, подходящими для интернет-сайта, сайта с несколькими IP-адресами и виртуальных хостов. Основной каталог /usr/share/doc/vsftpd содержит FAQ (часто задаваемые вопросы), советы по установке и информацию о версии.

На справочных страницах пакета vsftpd, возможно, найдется самая полезная информация о настройке сервера. Введите команду man vsftpd.conf, чтобы прочитать о файле конфигурации, и man vsftpd, чтобы прочитать о процессе демона и о том, как управлять им в качестве службы systemd.

Чтобы перечислить файлы конфигурации, введите следующее:

# rpm -qc vsftpd
/etc/logrotate.d/vsftpd
/etc/pam.d/vsftpd
/etc/vsftpd/ftpusers
/etc/vsftpd/user_list
/etc/vsftpd/vsftpd.conf

Главный файл конфигурации — это /etc/vsftpd/vsftpd.conf (в RHEL и Fedora) и /etc/vsftpd.conf (в Ubuntu). Файлы ftpusers и user_list (в Fedora и RHEL, но не в Ubuntu) в одном каталоге хранят информацию об учетных записях пользователей, которым ограничен доступ к серверу. Файл /etc/pam.d/vsftpd задает способ аутентификации на FTP-сервере. Файл /etc/logrotate.d/vsftpd настраивает способ ротации файлов журналов с течением времени.

Вы установили пакет vsftpd и быстро ознакомились с его содержимым. Следующий шаг — запустить и протестировать службу vsftpd.