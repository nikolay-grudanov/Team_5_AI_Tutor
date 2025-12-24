---
source_image: page_523.png
page_number: 523
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.69
tokens: 7535
characters: 2126
timestamp: 2025-12-24T05:00:00.731543
finish_reason: stop
---

Ранее мы рассмотрели варианты конфигурации отдельных функций на сервере vsftpd. Некоторые наборы переменных vsftp.conf могут работать вместе с помощью подходящих для определенных типов FTP-сайтов способов. В следующем разделе описан один из этих примеров, представленный файлом конфигурации vsftpd.conf, который входит в пакет vsftpd. Этот файл можно скопировать из каталога с примерами файлов в файл /etc/vsftpd/vsftpd.conf и использовать на FTP-сервере, доступном в Интернете.

Настройка службы vsftpd для Интернета

Чтобы безопасно обмениваться файлами с FTP-сервера в Интернете, можно заблокировать сервер, ограничив его только разрешением на загрузку и только от анонимных пользователей. Чтобы настроить безопасный обмен файлами vsftpd через Интернет, создайте резервную копию текущего файла /etc/vsftpd/vsftpd.conf и скопируйте этот файл, чтобы перезаписать файл vsftpd.conf:

/usr/share/doc/vsftpd/EXAMPLE/INTERNET_SITE/vsftpd.conf

Далее описывается содержание этого файла. Настройки в первом разделе задают права доступа к серверу:

# Access rights
anonymous_enable=YES
local_enable=NO
write_enable=NO
anon_upload_enable=NO
anon_mkdir_write_enable=NO
anon_other_write_enable=NO

Включите параметр anonymous_enable (YES) и отключите параметр local_enable (NO), чтобы никто не мог войти на FTP-сервер с помощью обычной учетной записи пользователя Linux. Все должны входить через анонимный аккаунт. Никто не может загружать файлы (write_enable=NO). Затем установите, что анонимный пользователь не может загружать файлы (anon_upload_enable=NO), создавать каталоги (anon_mkdir_write_enable=NO) или как-то иначе записывать на сервер (anon_other_write_enable=NO). Вот так выглядят настройки безопасности:

# Security
anon_world_readable_only=YES
connect_from_port_20=YES
hide_ids=YES
pasv_min_port=50000
pasv_max_port=60000

Поскольку демон vsftpd может читать файлы, назначенные пользователю и группе ftp, параметр anon_world_readable_only=YES гарантирует, что анонимные пользователи могут видеть файлы, где включен только бит разрешения на чтение для other (------r--). Параметр connect_from_port_20=YES дает демону vsftpd