---
source_image: page_265.png
page_number: 265
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.22
tokens: 7485
characters: 1752
timestamp: 2025-12-24T04:39:31.429350
finish_reason: stop
---

Сетевая подсистема

mattias  pq 81.233.210.67   180ct19   θ /suid/bin/party
pbbl     ps 24.59.50.208      7:17PM    41 alpine
jake     p8 93.100.207.82     8:44PM    θ w
lerxst   pG 47.50.84.206      03Nov1920days screen -RDD
grex$ tty
/dev/ttypB ③
grex$ logout ←
Connection to grex.org closed.
lumpy@ubuntu:~$

После успешного установления соединения SSH пользовательский сеанс аутентифицируется одним из способов, например с помощью пароля ②, а затем в интерактивном режиме запускается начальный командный интерпретатор аутентифицированного пользователя. При этом на стороне сервера используется псевдотерминал ③ и эмулируется терминальный вход в систему (см. разд. 2.2.1), считающийся сетевым ①.

Листинг 6.15. Выполнение отдельной команды

lumpy@ubuntu:~$ ssh jake@grex.org uptime
← jake@grex.org's password: PassWord ←
8:47PM up 41 days, 3:17, 7 users, load averages: 2.34, 1.65, 1.64
← lumpy@ubuntu:~$

Кроме интерактивного сетевого входа, SSH позволяет удаленно выполнять отдельные команды (см. листинг 6.15), при этом псевдотерминал не используется, а терминальный вход не эмулируется. Вместо этого стандартные потоки ввода-вывода STDIN, STDOUT и STDERR выполняемой команды просто перенаправляются через сетевое соединение ssh-клиенту. Это зачастую используется для удаленного копирования файлов. Например, в листинге 6.16 при помощи архиватора tar(1) создается сжатый архив каталога /usr/src/sys на удаленном узле grex.org, а результат перенаправляется в локальный файл openbsd-kernel-source.tgz.

Листинг 6.16. Копирование при помощи ssh

lumpy@ubuntu:~$ ssh jake@grex.org tar czf - /usr/src/sys > openbsd-kernel-source.tgz
← jake@grex.org's password: PassWord ←
tar: Removing leading / from absolute path names in the archive
lumpy@ubuntu:~$