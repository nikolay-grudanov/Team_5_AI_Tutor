---
source_image: page_129.png
page_number: 129
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.70
tokens: 7557
characters: 1943
timestamp: 2025-12-24T04:35:32.352120
finish_reason: stop
---

4.3.1. Параллельные многопроцессные программы

Как указывалось ранее, параллельные программы зачастую используют процессы для выполнения отдельных ветвей. В эту категорию часто попадают программы сетевых служб, например сервер баз данных W:[PostgreSQL], служба удаленного доступа W:[SSH] и подобные. Листинг 4.13 иллюстрирует программу postgres(1), выполняющуюся в шести параллельных процессах, один из которых — диспетчер ①, четыре служебных ② и еще один ③ вызван подключением пользователя fitz к одноименной базе данных fitz. При последующих подключениях пользователей к серверу будут порождены дополнительные дочерние процессы для обслуживания их запросов — по одному на каждое подключение.

Листинг 4.13. Параллельные многопроцессные сервисы

fitz@ubuntu:~$ ps f -C postgres
PID TTY STAT TIME COMMAND
① 6711 ? S 0:00 /usr/lib/postgresql/11/bin/postgres -D /var/lib/postgresql...
② 6713 ? Ss 0:00 \_ postgres: 11/main: checkpointer
| 6714 ? Ss 0:00 \_ postgres: 11/main: background writer
| 6715 ? Ss 0:00 \_ postgres: 11/main: walwriter
| 6716 ? Ss 0:00 \_ postgres: 11/main: autovacuum launcher
| 6717 ? Ss 0:00 \_ postgres: 11/main: stats collector
| 6718 ? Ss 0:00 \_ postgres: 11/main: logical replication launcher
③ 9443 ? Ss 0:00 \_ postgres: 11/main: fitz * fitz [local] idle

fitz@ubuntu:~$ ssh ubuntu
fitz@ubuntu's password:
Last login: Sat Nov 21 13:29:33 2015 from localhost
fitz@ubuntu:~$ ps f -C sshd
PID TTY STAT TIME COMMAND
① 655 ? Ss 0:00 /usr/sbin/sshd -D
② 21975 ? Ss 0:00 \_ sshd: fitz [priv]
③ 22086 ? S 0:00 \_ sshd: * fitz@pts/1

fitz@ubuntu:~$ ^Дыход
Connection to ubuntu closed.

Аналогично, при удаленном доступе по протоколу SSH программа sshd(8), работая в качестве диспетчера ① в одном процессе, на каждое подключение порождает один свой клон ②, который, выполнив аутентификацию и авторизацию пользователя в системе, порождает еще один свой клон ③, имперсонирующийся в пользователя и обслуживающий его запросы.