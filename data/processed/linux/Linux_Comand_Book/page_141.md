---
source_image: page_141.png
page_number: 141
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.50
tokens: 6071
characters: 1183
timestamp: 2025-12-24T04:07:48.840669
finish_reason: stop
---

top [опции] procps
/usr/bin    stdin stdout -file --opt --help --version

Команда top позволяет следить за наиболее активными процессами, обновляя данные через определенные интервалы времени (скажем, каждую секунду). Это консольная программа, которая обновляет данные интерактивно.

$ top
116 processes: 104 sleeping, 1 running,
0 zombie, 11 stopped
CPU states: 1.1% user, 0.5% system,
0.0% nice, 4.5% idle
Mem: 523812K av, 502328K used, 21484K free,
OK shrd, 160436K buff
Swap: 530104K av, OK used, 530104K free
115300K cached
PID USER PRI   N1 SIZE RSS SHARE STAT
%CPU %MEM TIME COMMAND
26265 smith 10   0 1092 1092 840 R
4.7 0.2 0:00 top
1root 0 0 540 540 472 S
0.0 0.1 0:07 init
2root 0 0 0 0 0 SW
0.0 0.0 0:00 kflushd

Когда выполняется программа top, вы можете нажимать клавиши, чтобы изменять ее поведение, например задавать скорость обновления (s), скрывать бездействующие процессы (i) или убивать процессы (k). Нажмите h, чтобы увидеть полный список, и q, чтобы выйти из программы.

Полезные опции
-nw   Выполнить ^обновлений, а затем завершить работу
-dw   Обновлять данные каждые Л'секунд
-pN -pm ...   Выводить процессы только с идентификаторами N, M,..., до 20 процессов