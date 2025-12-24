---
source_image: page_132.png
page_number: 132
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.29
tokens: 7473
characters: 1384
timestamp: 2025-12-24T04:35:35.826456
finish_reason: stop
---

2 fitz@ubuntu:~$ time bzip2 -d plan9.iso.bz2

real 0m20.705s
user 0m19.044s
sys 0m1.168s

1 fitz@ubuntu:~$ time pbzip2 plan9.iso &

[1] 5571

fitz@ubuntu:~$ ps f
PID TTY STAT TIME COMMAND
4637 pts/0 S 0:00 -bash
5571 pts/0 S 0:00 \_ -bash
5572 pts/0 Sl 0:03 \_ pbzip2 plan9.iso
5580 pts/0 R+ 0:00 \_ ps f

fitz@ubuntu:~$ ps -fLp 5572
UID PID PPID LWP C NLWP STIME TTY TIME CMD
fitz 5572 5571 5578 92 8 10:52 pts/0 00:00:43 pbzip2 plan9.iso
fitz 5572 5571 5579 1 8 10:52 pts/0 00:00:00 pbzip2 plan9.iso

fitz@ubuntu:~$ fg
time pbzip2 plan9.iso

real 0m24.259s
user 1m22.940s
sys 0m1.888s

fitz@ubuntu:~$ ls -lh plan9.iso.bz2
-rw-r--r-- 1 fitz fitz 89M нояб. 28 15:47 plan9.iso.bz2

2 fitz@ubuntu:~$ time pbzip2 -d plan9.iso.bz2

real 0m7.384s
user 0m25.972s
sys 0m1.396s

В результате оценки оказывается, что последовательный упаковщик bzip2(1) использует один однотитевой процесс и затрачивает ≈54,7 с реального времени на упаковку, из них ≈51,7 с проводит в пользовательском режиме user и лишь ≈0,4 с в режиме ядра sys (выполняя системные вызовы, например read(2) или write(2)). Соотношение между временем режимов говорит о вычислительном характере программы, т. е. о существенном превалировании времени вычислительных операций упаковки над временем операций ввода-вывода для чтения исходных данных и записи результатов (что подтверждает анализ разд. 4.2). Это означает, что нагрузка