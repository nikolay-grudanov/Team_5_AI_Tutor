---
source_image: page_106.png
page_number: 106
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.94
tokens: 7305
characters: 1477
timestamp: 2025-12-24T04:34:47.496438
finish_reason: stop
---

профиль переводится в режим enforce, в результате чего доступ firefox(1) к ключам пользователя оказывается запрещенным.

Листинг 3.49. Мандатные правила профиля firefox

finn@ubuntu:~$ apparmor_parser -p /etc/apparmor.d/usr.bin.firefox
...
audit deny @{HOME}/.ssh/** mrwkl,
...
finn@ubuntu:~$ cat ~/.ssh/id_rsa
-----BEGIN RSA PRIVATE KEY-----
...
-----END RSA PRIVATE KEY-----

finn@ubuntu:~$ firefox ~/.ssh/id_rsa

Окно firefox
file:///home/finn/.ssh/id_rsa
-----BEGIN RSA PRIVATE KEY-----
...
-----END RSA PRIVATE KEY-----

finn@ubuntu:~$ sudo aa-enforce firefox
Profile for /usr/lib/firefox/firefox.sh not found, skipping
finn@ubuntu:~$ pgrep firefox
16392
finn@ubuntu:~$ ps up 16392
USER   PID %CPU %MEM   VSZ   RSS TTY STAT START TIME COMMAND
finn  16392 2.4 5.9 2974256 238292 pts/2 Sl 23:33 0:03 /usr/lib/firefox/firefox
finn@ubuntu:~$ sudo aa-enforce /usr/lib/firefox/firefox
Назначение /usr/lib/firefox/firefox принудительного режима.
Warning: profile /usr/lib/firefox/firefox{,[^s][^h]} represents multiple programs
finn@ubuntu:~$ pkill firefox
...
finn@ubuntu:~$ firefox ~/.ssh/id_rsa

Окно firefox
file:///home/finn/.ssh/id_rsa
В доступе к файлу отказано
файл /home/finn/.ssh/id_rsa не может быть прочитан.
• Возможно, что он был удалён или перемещён, или разрешения на файл не дают получить к нему доступ.

Стоит отметить, что команды aa-enforce(8) и aa-status(8) выполняются от лица суперпользователя, единолично управляющего модулем принудительного контроля дос-