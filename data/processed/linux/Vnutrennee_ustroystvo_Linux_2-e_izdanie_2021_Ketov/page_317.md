---
source_image: page_317.png
page_number: 317
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.76
tokens: 7595
characters: 1826
timestamp: 2025-12-24T04:41:13.018627
finish_reason: stop
---

7.7.3. Управление X-дисплеями: XDMCP-менеджер и протокол

В большинстве современных инсталляций Linux работа пользователей в системе осуществляется сразу с использованием оконной системы X и какой-либо пользовательской среды, например GNOME. Если при работе в (автоматически запущенной) оконной системе (листинг 7.30) проследить дерево процессов от аппаратного X-сервера Xorg(1) до прадодителя процессов init(1), то обнаружится менеджер дисплеев ① (например, gdm3(1)), осуществивший запуск ② X-сервера. Более того, пользовательский сеанс ③ (gnome-session(1)) тоже окажется запущенным этим менеджером.

Листинг 7.30. Локальный графический вход

homer@ubuntu:~$ pgrep Xorg
21261

homer@ubuntu:~$ pstree -sTp 21261
systemd(1)—gdm3(742)—gdm-session-worker(21227)—gdm-x-session(21259)—Xorg(21261)

①                ②

homer@ubuntu:~$ pstree -Tp 742
gdm3(742)—gdm-session-worker(21227)—gdm-x-session(21259)—Xorg(21261)
    └─gnome-session-b(21267)

①                ②                ③

homer@ubuntu:~$ ps fp 742,21227,21259,21261,21267
   PID TTY STAT TIME COMMAND
   742 ? Ssl 0:00 /usr/sbin/gdm3
21227 ? Sl 0:00 \_ gdm-session-worker [pam/gdm-password] ②
21259 tty7 Ssl+ 0:00 \_ /usr/lib/gdm3/gdm-x-session ...
21261 tty7 Sl+ 0:00 \_ /usr/lib/xorg/Xorg vt7 -displayfd 3 ... ①
21267 tty7 Sl+ 0:00 \_ /usr/lib/gnome-session/gnome-session-binary --systemd... ③

homer@ubuntu:~$ pgrep -l gnome-shell
21604 gnome-shell
21655 gnome-shell-cal

homer@ubuntu:~$ pstree -sTp 21604
systemd(1)—systemd(5527)—gnome-shell(21604)—ibus-daemon(21707)—ibus-dconf(21714)
    └─ibus—...—sim(21922)
        └─ibus—...—(21716)

Менеджер дисплеев является специальной компонентой оконной системы, управляющей автоматическим запуском ее X-серверов и X-сеансов. Именно он запускает аппаратные X-серверы для обслуживания дисплеев в указанном количестве (по