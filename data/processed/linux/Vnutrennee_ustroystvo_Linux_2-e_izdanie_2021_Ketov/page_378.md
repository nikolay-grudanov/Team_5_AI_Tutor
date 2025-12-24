---
source_image: page_378.png
page_number: 378
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.32
tokens: 7603
characters: 1838
timestamp: 2025-12-24T04:43:13.479402
finish_reason: stop
---

* Recv failure: Connection reset by peer
* Closing connection 0
curl: (56) Recv failure: Connection reset by peer

Листинг 10.13 иллюстрирует, что «шаблонные» сервис-юниты не имеют собственных состояний ①, но порождают при запуске свои конкретные ② экземпляры, что отмечается ③ в журнале ④ событий.

Листинг 10.13. Служба Web-сервера на основе systemd: диагностика

① morty@ubuntu:~$ systemctl --user status peerweb@.service
? Failed to get properties: Unit name peerweb@.service is neither a valid invocation ID nor unit name.
② morty@ubuntu:~$ journalctl --user -e
янв 14 03:50:44 ubuntu systemd[18739]: Started 192.168.0.103:46930.
③ янв 14 03:50:44 ubuntu systemd[18739]: peerweb@27-172.17.0.1:8888-192.168.0.103:46930.service: Succeeded.
④ morty@ubuntu:~$ systemctl --user status peerweb@*.service
peerweb@27-172.17.0.1:8888-192.168.0.103:46930.service - 192.168.0.103:46930
Loaded: loaded (/home/morty/.config/systemd/user/peerweb@.service; static; ...)
Active: active (running) since Tue 2020-01-14 03:53:06 MSK; 10s ago
Main PID: 20563 (peerweb)
CGroup: /user.slice/user-1000.slice/user@1000.service
    /peerweb.slice/peerweb@27-172.17.0.1:8888-192.168.0.103:46930.service
        └─20563 /bin/bash /home/morty/bin/peerweb /home/morty/Public
янв 14 03:53:06 ubuntu systemd[18739]: Started 192.168.0.103:46930.

Остается только привязать ⑤ активацию сокет-юнита к входу пользователя в систему (листинг 10.14), иначе каждый раз придется активировать его вручную (см. ⑥ в листинге 10.11).

Листинг 10.14. Встраивание юнита в дерево зависимостей

morty@ubuntu:~$ systemctl --user list-dependencies
default.target
├──pulseaudio.service
├──ubuntu-report.path
├──basic.target
│   ├──paths.target
│   ├──sockets.target
│   │   ├──dbus.socket
│   │   │   ├──pulseaudio.socket
│   │   │   └──snapd.session-agent.socket
│   └──timers.target