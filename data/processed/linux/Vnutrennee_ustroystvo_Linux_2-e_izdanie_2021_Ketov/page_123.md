---
source_image: page_123.png
page_number: 123
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.09
tokens: 7698
characters: 2302
timestamp: 2025-12-24T04:35:29.343187
finish_reason: stop
---

Управление процессами и памятью

17764 tty3 Ssl+ 0:00 /usr/lib/gdm3/gdm-x-session --run-script ...
17766 tty3 Sl+ 3:09 \_ /usr/lib/xorg/Xorg vt3 -displayfd 3 ...
17774 tty3 Sl+ 0:00 \_ /usr/lib/gnome-session/gnome-session-binary ...
2987 ? Ss 0:04 /lib/systemd/systemd --user
2992 ? S 0:00 \_ (sd-pam)
17373 ? Ssl 0:08 \_ /usr/bin/pulseaudio --daemonize=no
17444 ? Ss 0:02 \_ /usr/bin/dbus-daemon --session --address=systemd: ...
17921 ? Ssl 10:04 \_ /usr/bin/gnome-shell
0 30192 ? Ssl 0:00 \_ /usr/libexec/gnome-terminal-server
1 30202 pts/1 Ss 0:00 \_ bash
0 30226 pts/1 S+ 0:00 | \_ man ps
30236 pts/1 S+ 0:00 | \_ pager
1 30245 pts/3 Ss 0:00 \_ bash
0 30251 pts/3 R+ 0:00 \_ ps fx
0 30315 ? Sl 0:04 \_ /usr/lib/firefox/firefox -new-window
30352 ? Sl 0:02 \_ /usr/lib/firefox/firefox -contentproc -childID 1 ...
30396 ? Sl 0:00 \_ /usr/lib/firefox/firefox -contentproc -childID 2 ...
30442 ? Sl 0:00 \_ /usr/lib/firefox/firefox -contentproc -childID 3 ...

Управляющий терминал процесса, показанный в столбце TTY, используется для доставки ему интерактивных сигналов (см. разд. 4.8), при вводе управляющих символов (см. разд. 2.3) intr ^C, quit ^\ и пр. У части процессов 0, 0 управляющий терминал отсутствует, потому что они выполняют приложения, взаимодействующие с пользователем не посредством терминалов, а через графическую систему (см. главу 7).

Процесс по своему определению изолирует свою программу от других выполняющихся программ, что затрудняет использование процессов для выполнения таких параллельных программ, ветви которых не являются полностью независимыми друг от друга и должны обмениваться данными. Использование предназначенных для этого средств межпроцессного взаимодействия (см. разд. 4.9) при интенсивном обмене приводит к обременению неоправданными накладными расходами, поэтому для эффективного выполнения таких параллельных программ используются легковесные процессы (LWP, light-weight processes), они же 'нити' (threads). Механизм

Существует еще один (неудачный, на мой взгляд) перевод понятия thread на русский язык — поток. Во-первых, он конфликтует с переводом понятия stream — поток, а во-вторых, в отличие от stream, thread никуда не течет. А вот процесс (process) содержит в себе нити (thread) абсолютно таким же образом, как и обычная веревка состоит из... нитей.