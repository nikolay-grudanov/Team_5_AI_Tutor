---
source_image: page_316.png
page_number: 316
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.17
tokens: 7645
characters: 1920
timestamp: 2025-12-24T04:41:13.083328
finish_reason: stop
---

[lich@centos ~]$ xauth list
2 centos/unix:10 MIT-MAGIC-COOKIE-1 80c749073282be2001c33bd43e577aa4

[lich@centos ~]$ strace -fe connect xeyes
connect(3, {sa_family=AF_INET, sin_port=htons(6010), sin_addr=inet_addr("127.0.0.1")}, 16) = 0
+++ exited with 0 +++

[lich@centos ~]$ sudo lsof -nP -i 4:6010
COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
sshd 14221 lich 10u IPv4 44578 0t0 TCP 127.0.0.1:6010 (LISTEN)

[lich@centos ~]$ logout
Connection to centos closed.

Листинг 7.28 иллюстрирует поведение SSH-клиента в режиме (-X) X-туннелирования, при котором он эмулирует «X-клиента» и соединяется с аппаратным (!) X-сервером через локальный сокет /tmp/.X11-unix/X0. При получении от SSH-сервера перенаправленных соединений X-протокола они ретранслируются SSH-эмулятором «X-клиента» локальному X-серверу, тем самым вывод дистанционных X-клиентов изображается в окнах локального X-сервера.

Листинг 7.28. SSH-туннелирование X-протокола (SSH-клиент)

homer@ubuntu:~$ strace -fe connect ssh -f -X lich@centos xeyes
connect(3, {sa_family=AF_INET, sin_port=htons(22), sin_addr=inet_addr("10.0.0.99")}, 16) = 0
connect(7, {sa_family=AF_FILE, path="/tmp/.X11-unix/X0"}, 110) = 0

Так как SSH-туннелирование X-протокола позволяет перенаправлять любое количество X-соединений внутри одного SSH-соединения, то дистанционно можно запускать целые сеансы пользовательских сред, таких как GNOME (листинг 7.29), с использованием xinit(1) и виртуального X-сервера Xnest(1).

Листинг 7.29. Запуск дистанционного сеанса GNOME с отображением на локальном сервере Xnest

homer@ubuntu:~$ xinit /usr/bin/ssh -X lich@centos gnome-session -- /usr/bin/Xnest :4 &
homer@ubuntu:~$ ps f
PID TTY STAT TIME COMMAND
27759 pts/0 Ss 0:00 bash
27829 pts/0 S 0:00 \_ xinit /usr/bin/ssh -X lich@centos gnome-session -- ...
27830 pts/0 sl 0:00 \_ /usr/bin/Xnest :4
27837 pts/0 S 0:00 \_ /usr/bin/ssh -X lich@centos gnome-session
27928 pts/0 R+ 0:00 \_ ps f