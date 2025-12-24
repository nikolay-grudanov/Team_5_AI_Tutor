---
source_image: page_763.png
page_number: 763
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.51
tokens: 7445
characters: 1671
timestamp: 2025-12-24T05:06:38.005260
finish_reason: stop
---

CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
437ec53386ca ...ubi:latest bash 1 hour ago Up 1 minute ago go_ein

Позже вы узнаете, как удалить и перезапустить остановленный контейнер.

Запуск FTP-сервера из контейнера

Всегда должна быть возможность удалить контейнер, закончив работу с ним, но при этом сохранять любые изменяемые данные вне контейнера. Далее приведен простой пример запуска FTP-сервера (vsftpd) из контейнера. Если хотите решить этот пример самостоятельно, рекомендую перейти к подразделу «Создание образа контейнера» далее в этом разделе, чтобы узнать, как самостоятельно создать образ контейнера vsftpd.

Для этого вам понадобятся файл конфигурации (vsftpd.conf) и каталог FTP, содержащий один или два файла для совместного использования (/var/ftp/pub) в хост-системе. Когда контейнер vsftpd запускается, он связывает эти элементы в контейнер в виде томов.

1. Создайте файл vsftpd.conf. Создайте файл vsftpd.conf в папке по умолчанию /etc/vsftpd/vsftpd.conf (дополнительные сведения см. на справочной странице vsftpd.conf), например:

anonymous_enable=YES
local_enable=YES
write_enable=YES
local_umask=022
dirmessage_enable=YES
xferlog_enable=NO
connect_from_port_20=YES
listen=NO
listen_ipv6=YES
pam_service_name=vsftpd
userlist_enable=YES
tcp_wrappers=NO
vsftpd_log_file=/dev/stdout
syslog_enable=NO
background=NO
pasv_enable=Yes
pasv_max_port=21100
pasv_min_port=21110

2. Создайте каталог ftp. Создайте анонимный FTP-каталог службы vsftpd для совместного использования в месте стандартного расположения на хосте (/var/ftp/pub) и скопируйте в него несколько файлов:

# mkdir -p /var/ftp/pub
# cp /etc/services /etc/login.defs /var/ftp/pub/