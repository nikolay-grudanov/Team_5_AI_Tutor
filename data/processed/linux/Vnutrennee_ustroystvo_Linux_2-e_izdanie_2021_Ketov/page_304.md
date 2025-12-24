---
source_image: page_304.png
page_number: 304
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.31
tokens: 7552
characters: 1628
timestamp: 2025-12-24T04:40:55.812589
finish_reason: stop
---

homer@ubuntu:~$ DISPLAY=:1 dbus-launch --exit-with-session gnome-session &
[2] 26024
homer@ubuntu:~$ pstree -Tp 26024

gnome-session-b(26024) — evolution-alarm(26347)
    |—— gnome-shell(26062) — ibus-daemon(26172) — ibus-dconf(26178)
    |                |—— ibus-engine-sim(26309)
    |                |—— ibus-extension-(26179)
    |—— polkit-agent-he(26409)
    |—— gsd-a11y-settin(26220)
    |—— gsd-color(26229)
    |—— gsd-xsettings(26226)
    |—— tracker-extract(26349)
    |—— tracker-miner-f(26361)

Стоит отметить, что в листинге 7.13 менеджер сеансов gnome-session(1) запускается через посредника — dbus-launch(1), который запустит новую шину для взаимодействия компонент сеанса так, чтобы предыдущий сеанс, работающий с «аппаратным» X-сервером, не пересекался с новым сеанском, запускаемым для «виртуального» Xephyr(1).

Среда KDE, представленная в листинге 7.14 и на рис. 7.8, запускается при помощи специального сценария startkde(1) и тоже состоит из отдельных компонент (1), среди которых неизменно присутствуют менеджер сеансов ksmserver (2) и композитный (см. разд. 7.6.1) оконный менеджер kwin (3).

Листинг 7.14. Настольное окружение KDE

homer@ubuntu:~$ DISPLAY=:0 Xephyr :1 -listen tcp & 
[1] 6215
homer@ubuntu:~$ DISPLAY=:1 startkde >& /dev/null
[1] 6236
homer@ubuntu:~$ pstree -Tp 6236
startkde(6236)——kwrapper5(6291)
homer@ubuntu:~$ pgrep -l ^kde*
21 kdevtmpfs
6270 kdeinit5
(1) 6274 kded5
(1) 6345 kdeconnectd
homer@ubuntu:~$ pstree -Tp 6270
kdeinit5(6270)——file.so(6618)
    |—— kaccess(6289)
    |—— kded5(6274)
    |—— klauncher(6271)
    |—— korgac(6358)
    |—— ksmserver(6293)——kwin_x11(6311) (3)