---
source_image: page_377.png
page_number: 377
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.35
tokens: 7428
characters: 1598
timestamp: 2025-12-24T04:43:08.396174
finish_reason: stop
---

Листинг 10.11. Служба Web-сервера на основе systemd: запуск

(1) morty@ubuntu:~$ systemctl --user start peerweb.socket
(2) morty@ubuntu:~$ systemctl --user status peerweb.socket
● peerweb.socket
① Loaded: loaded (/home/morty/.config/systemd/user/peerweb.socket; static; ...)
Active: active (listening) since Tue 2020-01-14 03:28:47 MSK; 8s ago
Listen: 0.0.0.0:8080 (Stream)
Accepted: 0; Connected: 0;
CGroup: /user.slice/user-1000.slice/user@1000.service/peerweb.socket

② янв 14 03:28:47 ubuntu systemd[18739]: Listening on peerweb.socket.

После запуска (1) сокет-юнита в работу (листинг 10.11) можно узнать его состояние (2) и расположение самих юнит-файлов (1) и журнальные записи (2) о последних событиях. Работу службы можно протестировать, разместив в каталоге ~/Public какой-либо файл и запросив его получение при помощи Web-браузера или простейшего Web-клиента curl(1), как проиллюстрировано в листинге 10.12.

Листинг 10.12. Служба Web-сервера на основе systemd: использование

morty@ubuntu:~$ cat ~/Public/README
:)
morty@ubuntu:~$ curl -v http://ubuntu.local:8080/README
* Trying 172.17.0.1:8080...
* TCP_NODELAY set
* Connected to ubuntu-2.local (172.17.0.1) port 8080 (#0)
> GET /README HTTP/1.1
> Host: ubuntu-2.local:8080
> User-Agent: curl/7.65.3
> Accept: */*
>
* Mark bundle as not supporting multiuse
* HTTP 1.0, assume close after body
< HTTP/1.0 200 Ok
< Content-Type: text/plain; charset=us-ascii
< Content-Size: 3
<

1 Необходимо убедиться, что служба MDNS (см. avahi в главе 6) исправно функционирует, иначе придется воспользоваться IP-адресами вместо имен в домене .local.