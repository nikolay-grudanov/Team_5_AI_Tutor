---
source_image: page_175.png
page_number: 175
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.57
tokens: 7607
characters: 1663
timestamp: 2025-12-24T04:36:57.277823
finish_reason: stop
---

Диспозицию сигналов, т. е. информацию об игнорировании (IGNORED), перехвате (CAUGHT), временной блокировке (BLOCKED) или ожидании доставки (PENDING) сигналов процессов можно получить при помощи команды ps(1), как показано в листинге 4.47. Диспозиция изображается битовой маской, где каждый N-й бит маски (нумерация от младших к старшим) соответствует сигналу N. Например, командный интерпретатор игнорирует сигналы, представленные (шестнадцатеричной) маской 00384004_{16}, что в двоичном представлении составляет 11100001000000000000100_{2} и указывает на игнорируемые 3-й, 15-й, 20-й, 21-й и 22-й сигналы, т. е. SIGQUIT, SIGTERM, SIGTSTP, SIGTTIN и SIGTTOU. Для перевода из шестнадцатеричного в двоичное представление использован стековый калькулятор dc(1), которому было велено из входной i (input) системы счисления по основанию 16 в выходную o (output) систему счисления по основанию 2 напечатать p (print) число 00384004, а для просмотра имен сигналов по их номерам использована встроенная команда kill.

Листинг 4.47. Диспозиция сигналов

fitz@ubuntu:~$ ps s
UID PID PENDING BLOCKED IGNORED CAUGHT STAT TTY TIME COMMAND
1006 23025 00000000 00010000 00380004 4b813efb Ss pts/5 0:00 -bash
1006 23773 00000000 00000000 00000000 <f3d1fef9 R+ pts/5 0:00 ps s

fitz@ubuntu:~$ dc -e 16i2000380004p
1110000000000000000000100
222120- - - - - - - - - - - 87654321

fitz@ubuntu:~$ kill -l
1) SIGHUP   2) SIGINT   3) SIGQUIT   4) SIGILL   5) SIGTRAP
11) SIGSEGV  12) SIGUSR2  13) SIGPIPE  14) SIGALRM  15) SIGTERM
16) SIGSTKFLT 17) SIGCHLD  18) SIGCONT  19) SIGSTOP  20) SIGTSTP
21) SIGTTIN  22) SIGTTOU  23) SIGURG   24) SIGXCPU  25) SIGXFSZ
63) SIGRTMAX-164) SIGRTMAX