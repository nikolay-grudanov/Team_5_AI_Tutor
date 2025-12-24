---
source_image: page_209.png
page_number: 209
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.47
tokens: 7385
characters: 1484
timestamp: 2025-12-24T04:37:46.708278
finish_reason: stop
---

Листинг 5.22. PID текущего процесса

bender@ubuntu:~$ set -x
bender@ubuntu:~$ ps up $$
+ ps up 32649
USER    PID %CPU %MEM   VSZ   RSS TTY STAT START TIME COMMAND
bender  32649 0.1 0.1 13536 8604 pts/1 Ss 10:28 0:00 -bash

Листинг 5.23. PID последнего дочернего асинхронного процесса

bender@ubuntu:~$ set -x
bender@ubuntu:~$ dd if=/dev/dvd of=dvd.iso &
[1] 399
+ dd if=/dev/dvd of=dvd.iso
bender@ubuntu:~$ ps up $!
+ ps up 399
USER    PID %CPU %MEM   VSZ   RSS TTY STAT START TIME COMMAND
bender  399 14.0 0.0 5604 588 pts/1 D 10:36 0:00 dd if=/dev/dvd ...

Используя специальный параметр ?, можно узнать статус завершения (код возврата) программы, выполнившейся последней. При этом нулевой статус завершения символизирует успешное ее выполнение, а любое другое, отличное от нулевого, значение есть «номер» ошибки. В листинге 5.24 команда which(1) завершилась с успехом при поиске программы, запускающейся по внешней команде ls, и неудачей — при поиске программы, соответствующей встроенной команде cd.

Листинг 5.24. Статус завершения процесса/программы

bender@ubuntu:~$ which ls
/usr/bin/ls
bender@ubuntu:~$ echo $?
0
bender@ubuntu:~$ which cd
bender@ubuntu:~$ echo $?
1

5.4.3. Подстановки вывода команд

Еще одним видом подстановок, выполняемых командным интерпретатором, являются подстановки вывода команд. Конструкции вида $(command) (или ее более старая форма `command`) используются для подстановки результата вывода команды command на поток STDOUT в место ее использования.