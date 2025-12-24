---
source_image: page_096.png
page_number: 96
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.43
tokens: 7495
characters: 1584
timestamp: 2025-12-24T04:34:28.747093
finish_reason: stop
---

**Листинг 3.40. Дополнительный атрибут SUID**

finn@ubuntu:~$ ls -la /etc/passwd /etc/shadow

1 -rw-r--r-- 1 root root 2867 ноя 17 11:16 /etc/passwd
2 -rw-r----- 1 root shadow 1617 ноя 17 11:17 /etc/shadow

finn@ubuntu:~$ passwd
Смена пароля для finn.
(текущий) пароль UNIX:
Введите новый пароль UNIX:
Повторите ввод нового пароля UNIX:
passwd: пароль успешно обновлён

finn@ubuntu:~$ ls -la /etc/passwd /etc/shadow

1 -rw-r--r-- 1 root root 2867 ноя 17 11:16 /etc/passwd
2 -rw-r----- 1 root shadow 1617 ноя 18 01:46 /etc/shadow

finn@ubuntu:~$ chfn
Пароль:
Изменение информации о пользователе finn
Введите новое значение или нажмите ENTER для выбора значения по умолчанию
Полное имя:
Номер комнаты []:
Рабочий телефон []: +7(812)703-02-02
Домашний телефон []:
finn@ubuntu:~$ ls -l /etc/passwd /etc/shadow

1 -rw-r--r-- 1 root root 2883 ноя 18 01:47 /etc/passwd
2 -rw-r----- 1 root shadow 1617 ноя 18 01:46 /etc/shadow

finn@ubuntu:~$ ls -la /usr/bin/passwd /usr/bin/chfn

3 -rwsr-xr-x 1 root root 84848 авг 29 16:00 /usr/bin/chfn
4 -rwsr-xr-x 1 root root 67992 авг 29 16:00 /usr/bin/passwd

За счет использования атрибута SUID получается, что пользователям, запускающим программы chfn(1), chsh(1) и passwd(1), для их исполнения временно делегируются права владельца этих программ (суперпользователя root) так, как будто сам суперпользователь их запустил.

**Листинг 3.41. Дополнительный атрибут SGID**

Сеанс finn
finn@ubuntu:~$ w
00:03:53 up 12 days, 13:53, 7 users, load average: 0,53, 0,51, 0,91
USER   TTY   FROM           LOGING   IDLE   JCPU   PCPU WHAT
jake   tty2
finn   tty1