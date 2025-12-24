---
source_image: page_228.png
page_number: 228
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 8.55
tokens: 7068
characters: 698
timestamp: 2025-12-24T04:38:07.821638
finish_reason: stop
---

В примере из листинга 5.47 на основе составного списка while организован «индикатор прогресса» процесса фонового сжатия ISO-образа диска при помощи опроса его состояния. Цикл выполняется, пока успешно команда ps(1), опрашивающая процесс, PID которого передан при помощи подстановки специального параметра $!. При каждой итерации цикла (1) команда ls(1) выводит размер выходного файла dvd.iso.bz2, а команда sleep(1) приостанавливает выполнение на 1 секунду.

Листинг 5.47. Цикл «ПОКА»: ожидание завершения процесса

bender@ubuntu:~$ bzip2 -kf dvd.iso &
[1] 5773
bender@ubuntu:~$ set -x
bender@ubuntu:~$ while ps p $! ; do ls -lh dvd.iso.bz2; sleep 1 ; done
(1) + ps p 5773
PID TTY STAT TIME COMMAND