---
source_image: page_190.png
page_number: 190
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.69
tokens: 7599
characters: 2060
timestamp: 2025-12-24T04:37:24.584729
finish_reason: stop
---

/dev/shm/PostgreSQL.1587464325:

postgres 1023 ...m postgres
postgres 1144 ...m postgres
postgres 1145 ...m postgres
postgres 1146 ...m postgres
postgres 1147 ...m postgres
postgres 1149 ...m postgres

fitz@ubuntu:~$ ps p 1023,1144,1145,1146,1147,1149

PID TTY STAT TIME COMMAND
1023 ? S 0:00 /usr/lib/postgresql/11/bin/postgres ...
1144 ? Ss 0:00 postgres: 11/main: checkpointer
1145 ? Ss 0:01 postgres: 11/main: background writer
1146 ? Ss 0:01 postgres: 11/main: walwriter
1147 ? Ss 0:00 postgres: 11/main: autovacuum launcher
1149 ? Ss 0:00 postgres: 11/main: logical replication launcher

fitz@ubuntu:~$ sudo pmap -p 1023
1023: /usr/lib/postgresql/11/bin/postgres -D /var/lib/postgresql/11/main ...
00007feafa398000 8K rw-s- /dev/shm/PostgreSQL.1587464325

fitz@ubuntu:~$ sudo pmap -p 1145
1145: postgres: 11/main: background writer
00007feafa398000 8K rw-s- /dev/shm/PostgreSQL.1587464325

В примере из листинга 4.58 показано, как разделяемую память POSIX использует SQL-сервер postgres(1) для взаимодействия между своими параллельными процессами.

Семафоры и очереди сообщений

Разделяемая память требует синхронизации действий процессов из-за эффекта гонки (гасе), возникающего между конкурентными, выполняющимися параллельно процессами. Для синхронизации процессов при совместном доступе к разделяемой памяти и прочим разделяемым ресурсам предназначено еще одно специализированное средство их взаимодействия — семафоры. В большинстве случаев семафорами System V или POSIX пользуются многопроцессные сервисы, использующие разделяемую память, такие как, например, postgres(1), проиллюстрированный выше.

Очереди сообщений являются средством взаимодействия между процессами, реализующим еще один интерфейс передачи сообщений (message passing interface), подобно каналам и сокетам. По своей природе они похожи на дейтаграммный SOCK_DGRAM режим передачи поверх именованных локальных сокетов unix(7). Основное отличие очередей сообщений от сокетов заключается в том, что время их жизни не ограничивается временем существования процессов, которые их создали.