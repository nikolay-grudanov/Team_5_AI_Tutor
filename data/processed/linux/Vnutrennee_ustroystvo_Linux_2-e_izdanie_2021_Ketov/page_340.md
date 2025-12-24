---
source_image: page_340.png
page_number: 340
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.40
tokens: 7475
characters: 1783
timestamp: 2025-12-24T04:41:57.783478
finish_reason: stop
---

менной реинкарнаций дисплейного сервера и композитного менеджера окон, тесно интегрированных друг с другом в одной компоненте.

В этом смысле запуск графической среды на основе Wayland мало чем отличается от среды на основе X Window System. В листинге 8.8 показан сеанс работы пользователя, запущенный менеджером gdm3(1).

Листинг 8.8. Графический сеанс Wayland

homer@ubuntu:~$ pgrep gdm3
742
homer@ubuntu:~$ pstree -Tp 742
gdm3(742)—gdm-session-worker(20003)—gdm-wayland-ses(20042)—gnome-session-b(20046)

homer@ubuntu:~$ ps fp 742,20003,20042,20046
PID TTY STAT TIME COMMAND
742 ? Ssl 0:00 /usr/sbin/gdm3
20003 ? Sl 0:00 \_ gdm-session-worker [pam/gdm-launch-environment]
20042 tty1 Ssl+ 0:00 \_ /usr/lib/gdm3/gdm-wayland-session ...
20046 tty1 Sl+ 0:00 \_ /usr/lib/gnome-session/gnome-session-binary --systemd ...

homer@ubuntu:~$ pgrep -l gnome-shell
5628 gnome-shell
5672 gnome-shell-cal

homer@ubuntu:~$ pstree -sTp 5628
systemd(1)—systemd(5527)—gnome-shell(5628)—Xwayland(5641)
    └─ibus-daemon(5721)—ibus-dconf(5726)
        └─ibus-...-sim(5892)
            └─ibus-...-(5727)

Основное наблюдается в том, что в сессии отсутствует дисплейный сервер (Xorg(1)), т. к. его роль выполняет композитор gnome-shell(1), а остальные процессы остались практически без изменения.

8.4. В заключение

Графический интерфейс, с которого начинается первое «визуальное» знакомство любого начинающего пользователя с современной операционной системой Linux, на поверку оказывается самой «сложной» ее подсистемой.

Оконные системы X Window System и Wayland и используют в своей работе практически все1 рассмотренные сущности операционной системы — программы и

1 Даже выход первой версии ядра Linux был практически «приурочен» к моменту успешного запуска и стабильной работы оконной системы X.