---
source_image: page_347.png
page_number: 347
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.46
tokens: 8319
characters: 2649
timestamp: 2025-12-24T04:28:57.174079
finish_reason: stop
---

может открываться несколько раз каждым из них. Это касается в основном системных конфигурационных файлов.

12.5.2. Системные текстовые журналы

Следующие журналы — это текстовые файлы. Их можно без проблем просматривать такими командами, как cat, или любыми текстовыми редакторами.

В файле /var/log/messages находится основная информация о заходах пользователей, о неверных авторизациях, остановках и запусках сервисов и многое другое. В один документ все подобные события поместиться не могут, иначе он будет непрочитаемым, поэтому в папке /var/log/ могут находиться файлы с именами messages.X, где X — это число.

Журнал messages — один из самых главных для любого администратора. Если взломщик пытается подобрать пароль, то вы сможете заметить быстрый рост этого файла и появление большого количества записей о неверной авторизации. На рис. 12.1 показан пример содержимого файла.

Dec 5 13:45:55 FlenouM syslogd 1.4.1: restart.
Dec 5 13:55:28 FlenouM ftpd[1414]: wu-ftpd - TLS settings: control allow, client_cert allow, data allow
Dec 5 13:55:28 FlenouM ftp(pam_unix)[1414]: session opened for user flenou by (uid=0)
Dec 5 13:55:28 FlenouM ftpd: 192.168.77.10: flenou[1414]: FTP LOGIN FROM 192.168.77.10 [192.168.77.10], flenou
Dec 5 13:55:29 FlenouM ftpd: 192.168.77.10: flenou: USER flenou[1414]: FTP LOGIN REFUSED (already logged in as flenou) FROM 192.168.77.10 [192.168.77.10], flenou
Dec 5 13:55:31 FlenouM ftp(pam_unix)[1414]: session closed for user flenou
Dec 5 13:55:31 FlenouM ftpd: 192.168.77.10: flenou: QUIT[1414]: FTP session closed
Dec 5 13:55:50 FlenouM ftpd[1415]: wu-ftpd - TLS settings: control allow, client_cert allow, data allow
Dec 5 13:55:51 FlenouM ftp(pam_unix)[1415]: session opened for user flenou by (uid=0)
Dec 5 13:55:51 FlenouM ftpd: 192.168.77.10: flenou[1415]: FTP LOGIN FROM 192.168.77.10 [192.168.77.10], flenou
Dec 5 13:56:08 FlenouM ftp(pam_unix)[1415]: session closed for user flenou
Dec 5 13:56:08 FlenouM ftpd: 192.168.77.10: flenou: QUIT[1415]: FTP session closed
Dec 5 14:50:19 FlenouM /sbin/mingetty[1008]: tty2: invalid character ^I in logi

Рис. 12.1. Снимок экрана с выведенным на него файлом /var/log/messages

Следующий журнал расположен в файле /var/log/secure. Что в нем особенного? Это самый основной журнал, который нужно проверять максимально часто, и каждой записи следует уделять особое внимание. В этом файле отображается, под каким именем и с какого адреса пользователь вошел в систему. Например, на сервис FTP может подключаться главный бухгалтер. Если вы увидели, что он пользуется сервисом, но при этом журнал показывает чужой IP-адрес, то это должно стать поводом для беспокойства.