---
source_image: page_039.png
page_number: 39
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.19
tokens: 7457
characters: 1502
timestamp: 2025-12-24T04:33:00.338323
finish_reason: stop
---

Многие «дополнительные» клавиши современных терминалов, такие как функциональные F1...F12, клавиши управления курсором ↓↑←→, скроллингом PGUP PGDN HOME END и пр., генерируют (листинг 2.10) управляющие последовательности, которые обрабатываются, например, библиотекой readline(3) и используются для редактирования командной строки.

Листинг 2.10. Управляющие последовательности клавиатуры

finn@ubuntu:~$ od -a
F1
0000000 esc  O  Q  nl
0000004
finn@ubuntu:~$ od -a
END
0000000 esc  O  F  nl
0000004

Несмотря на стандартизацию управляющих последовательностей, разные терминалы все же имеют различия, поэтому в операционной системе появились базы данных с описанием свойств и управляющих последовательностей терминалов termcap(5) и terminfo(5) (листинг 2.11). Узнать ESC-последовательности можно при помощи команды infocmp(1), а вывести их на терминал — включить соответствующий режим — при помощи команды tput(1).

Листинг 2.11. База данных управляющих последовательностей termcap(5)

finn@ubuntu:~$ infocmp
# Reconstructed via infocmp from file: /lib/terminfo/l/linux
linux|linux console,
    am, bce, ccc, eo, mir, msgr, xenl, xon,
colors#8, it#8, ncv#18, pairs#64,
    op=\E[39;49m, rc=\E8, rev=\E[7m ^, ri=\EM, rmacs=\E[10m,
    sgr0=\E[0;10m ^, smacs=\E[11m, smam=\E[?7h, smir=\E[4h,
    smpch=\E[11m, smso=\E[7m, smul=\E[4m ^, tbc=\E[3g,
finn@ubuntu:~$ tput smul
finn@ubuntu:~$ tput rev
finn@ubuntu:~$ tput sgr0
finn@ubuntu:~$ tput smul | od -ac
0000000 esc   [   4   m
    033   [   4   m
0000004