---
source_image: page_526.png
page_number: 526
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.68
tokens: 7641
characters: 2052
timestamp: 2025-12-24T05:00:15.528637
finish_reason: stop
---

Доступ к FTP-серверу с помощью команды lftp

Для проверки своего FTP-сервера из командной строки примените команду lftp. Чтобы установить команду lftp в системах Fedora или RHEL, введите в командной строке следующее:

# yum install lftp

Если вы применяете команду lftp только с именем FTP-сервера, к которому хотите получить доступ, команда пытается подключиться к FTP-серверу как анонимный пользователь. Добавив параметр и имя_пользователя, можете ввести пароль пользователя при появлении запроса и получить доступ к FTP-серверу от имени пользователя, под которым вошли в систему.

После ввода информации о пользователе и пароле вы получите приглашение lftp, готовое к вводу команд. При вводе первой команды устанавливается соединение с сервером. Вы можете задействовать команды для перемещения по FTP-серверу, а затем команды get и put для загрузки и выгрузки файлов.

В следующем примере показано, как применять команды подобным образом. Предполагается, что FTP-сервер (и связанные с ним меры безопасности) был настроен таким образом, чтобы позволить локальным пользователям подключаться, а также читать и записывать файлы:

# lftp -u chris localhost
Password:
*******
lftp chris@localhost:~> pwd
ftp://chris@localhost/%2Fhome/chris
lftp chris@localhost:~> cd stuff/state/
lftp chris@localhost:~/stuff/state> ls
-rw-r--r--   1 13597    13597      1394 Oct 23 2014 enrolled-20141012
-rw-r--r--   1 13597    13597      514 Oct 23 2014 enrolled-20141013
lftp chris@localhost:~/stuff/state> !pwd
/root
lftp chris@localhost:~/stuff/state> get survey-20141023.txt
3108 bytes transferred
lftp chris@localhost:~/stuff/state> put /etc/hosts
201 bytes transferred
lftp chris@localhost:~/stuff/state> ls
-rw-r--r--   1 13597    13597      1394 Oct 23 2014 enrolled-20141012
-rw-r--r--   1 13597    13597      514 Oct 23 2014 enrolled-20141013
-rw-r--r--   1 0        0           201 May 03 20:22 hosts
lftp chris@localhost:~/stuff/state> !ls
anaconda-ks.cfg    bin
dog                Pictures
Downloads          Public
lftp chris@localhost:~/stuff/state> quit