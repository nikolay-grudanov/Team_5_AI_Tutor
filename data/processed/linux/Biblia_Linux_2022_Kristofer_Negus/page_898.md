---
source_image: page_898.png
page_number: 898
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.68
tokens: 7344
characters: 1509
timestamp: 2025-12-24T05:10:14.720388
finish_reason: stop
---

Глава 18. Настройка FTP-сервера

ВНИМАНИЕ!
Не выполняйте описанные здесь действия на активном общедоступном FTP-сервере, так как они помешают его работе. (Однако можно с их помощью настроить новый FTP-сервер.)

1. Чтобы определить, какой пакет предоставляет службу Very Secure FTP Daemon, от имени суперпользователя введите следующую строку:

# yum search "Very Secure FTP"
...
==================== N/S Matched: Very Secure FTP =================
vsftpd.i686 : Very Secure Ftp Daemon

Поиск отобразит пакет vsftpd.

2. Чтобы установить службу Very Secure FTP Daemon в системе и выполнить поиск файлов конфигурации в пакете vsftpd, введите следующее:

# yum install vsftpd
# rpm -qc vsftpd | less

3. Чтобы включить анонимный FTP и отключить локальный вход пользователя для службы Very Secure FTP Daemon, установите в файле /etc/vsftpd/vsftpd.conf следующее:

anonymous_enable=YES
write_enable=YES
anon_upload_enable=YES
local_enable=NO

4. Чтобы запустить службу Very Secure FTP Daemon и настроить ее запуск при загрузке системы, введите в актуальной версии системы Fedora или Red Hat Enterprise Linux следующее:

# systemctl start vsftpd.service
# systemctl enable vsftpd.service

В системе Red Hat Enterprise Linux 6 введите:

# service vsftpd start
# chkconfig vsftpd on

5. В системе, на которой работает FTP-сервер, введите следующую команду, чтобы создать файл с именем test в анонимном каталоге FTP, содержащем слова Welcome to your vsftpd server:

# echo "Welcome to your vsftpd server" > /var/ftp/test