---
source_image: page_035.png
page_number: 35
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.60
tokens: 7562
characters: 2014
timestamp: 2025-12-24T04:32:54.170136
finish_reason: stop
---

Реакция драйвера терминала на получаемые управляющие символы и предпринимаемые им управляющие действия (а точнее, наоборот — управляющие символы, закрепленные за управляющими действиями) стандартно предопределена, но почти все эти соответствия могут быть просмотрены и изменены командой stty(1), что иллюстрируется в листинге 2.6.

Листинг 2.6. Утилита stty

finn@ubuntu:~$ stty -a
speed 38400 baud; rows 38; columns 136; line = 0;
intr = ^C; quit = ^\; erase = ^?; kill = ^U ^\; eof = ^D; eol = <undef>; eol2 = <undef>;
swtch = <undef>; start = ^Q; stop = ^S; susp = ^Z;
rprnt = ^R; werase = ^W; lnext = ^V; flush = ^O; min = 1; time = 0;
-parenb -parodd cs8 hupcl -cstopb cread -clocal -crtscs
-ignbrk brkint -ignpar -parmrk -inpck -istrip -inlcr -igncr icrnl ixon -ixoff -iuclc -ixany imaxbel iutf8
opost -olcuc -ocrnl onlcr -onocr -onlret -ofill -ofdel nl0 cr0 tab0 bs0 vt0 ff0
isig icanon iexten echo echoe echok -echonl -noflsh -xcase -tostop -echoprt echoctl echoke

Кроме того, команда stty(1) позволяет получить (а также задать) и другие настройки драйвера терминала:

♦ скорость приемопередатчика последовательного интерфейса терминала (speed 38400 baud);
♦ количество изображаемых терминалом строк и столбцов (rows 33; columns 119);
♦ флаги режимов работы приемопередатчика интерфейса (-parenb...hupcl -cstopb...-inpck);
♦ флаги режимов обработки вводимых из терминала символов (-istrip...-igncr icrnl...iutf8);
♦ флаги режимов обработки выводимых на терминал символов (opost...-ofdel) и пр.

Так, например, флаг icanon включает или выключает (-icanon) «канонический» (canonical) режим обработки вводимых (input) символов, т. е. возможности редактирования вводимой строки при помощи управляющих символов ^? и ^U, а также сигнализацию завершения ввода при помощи ^D.

Флаг iexten включает «расширения» канонического режима стандарта POSIX, т. е. удаление последнего введенного слова при помощи ^W, перерисовку введенной строки при помощи ^R и ввод литеральных значений управляющих символов при помощи ^V.