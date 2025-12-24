---
source_image: page_178.png
page_number: 178
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.67
tokens: 7458
characters: 1736
timestamp: 2025-12-24T04:36:55.155108
finish_reason: stop
---

«одновременном» вводе информации с одного терминала несколькими процессами результат оказывается непредсказуем, т. к. нет возможности предугадать порядок и объемы считываемой информации. Поэтому ввод (input) разрешен только процессам группы «переднего» фона, а группа формируется так, что только один из них в реальности будет производить чтение. Процессам группы «заднего» фона ввод запрещен, а любые попытки подавляются при помощи сигнала SIGTTIN (terminal stop on input signal), доставка которого приводит к приостановке процесса.

В примере из листинга 4.49 при составлении текста письма посредством команды mail(1) ее процесс был временно приостановлен ① при помощи ^Z и SIGTSTP для получения доступа к командному интерпретатору. Попытка продолжить ② выполнение задания mail на «заднем» фоне не увенчалась успехом, т. к. была подавлена ③ за чтение терминала. Продолжение задания на «переднем» фоне ④ дает возможность закончить ввод текста письма и завершить ввод управляющим символом ^Z (EOT).

Листинг 4.49. Приостановка при вводе из заднего фона (SIGTTIN)

fitz@ubuntu:~$ mail dketov@gmail.com
Subject: schedtool(1) вместо taskset, chrt и nice/renice
^Z
① [2]+ Остановлен mail dketov@gmail.com
fitz@ubuntu:~$ which schedtool
/usr/bin/schedtool
fitz@ubuntu:~$ dpkg -S /usr/bin/schedtool
schedtool: /usr/bin/schedtool
② fitz@ubuntu:~$ bg
? [1]+ mail dketov@gmail.com &
? (continue)
? fitz@ubuntu:~$ jobs -l
③ [1]+ 12025 Остановлено (вывод на терминал) mail dketov@gmail.com
fitz@ubuntu:~$ ps f
   PID TTY      STAT   TIME COMMAND
8992 pts/2    Ss     0:00 bash
12025 pts/2   T      0:00  \_ mail dketov@gmail.com
12063 pts/2   R+     0:00  \_ ps f
8897 pts/0    Ss+    0:00 bash
④ fitz@ubuntu:~$ fg
mail dketov@gmail.com
(continue)