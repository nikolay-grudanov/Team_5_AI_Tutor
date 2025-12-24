---
source_image: page_187.png
page_number: 187
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.97
tokens: 7651
characters: 1577
timestamp: 2025-12-24T04:37:26.961492
finish_reason: stop
---

creator pid) процессом PID = 3828 программы X-клиента gnome-shell, а последнее обращение к нему (lpid, last operation pid) осуществлялось процессом PID = 3450 программы X-сервера Xorg(1). В данном конкретном случае X-клиент и X-сервер (см. разд. 7.1) для эффективного обмена значительными объемами растровых изображений используют расширение X-протокола W:[MIT-SHM] (см. разд. 7.6), основанное на применении разделяемой памяти.

Листинг 4.56. Разделяемая память (System V IPC)

fitz@ubuntu:~$ ipcs -m -p
------ Shared Memory Creator/Last-op PIDs --------
shmd   владелец   cpid   lpid
23     fitz       3887   5007
26     fitz       3887   5007
38     fitz       3887   3541
40     fitz       3887   3541

fitz@ubuntu:~$ dc -e 16o10i38p
26

fitz@ubuntu:~$ dc -e 16o10i40p
28

fitz@ubuntu:~$ ps up 3887,3541,5007
USER    PID %CPU %MEM   VSZ   RSS TTY STAT START TIME COMMAND
fitz    3541 0.0 1.7 376008 68532 tty2 Sl+ 15:12 0:04 /usr/lib/xorg/Xorg ...
fitz    3887 0.4 7.9 2646616 322356 ? Ssl 15:12 0:50 /usr/bin/gnome-shell
fitz    5007 0.2 7.1 3072068 286592 ? Sl 15:16 0:26 /usr/lib/.../firefox ...

fitz@ubuntu:~$ pmap 3887
3887:   /usr/bin/gnome-shell
00007ff280123000  3952K rw-s- [ shmid=0x1a ]
00007ff2a11d7000  3744K rw-s- [ shmid=0x28 ]
00007ff2a157f000  512K rw-s- [ shmid=0x26 ]
00007ff2c413e000  16K rw-s- [ shmid=0x17 ]

fitz@ubuntu:~$ pmap 3541
3541:   /usr/lib/xorg/Xorg vt2 -displayfd 3 -auth /run/user/1000/gdm/Xauthority ...
00007f70a7c58000  3744K rw-s- [ shmid=0x28 ]
00007f70b4591000  512K rw-s- [ shmid=0x26 ]
00007f70bbe32000  3952K rw-s- [ shmid=0x1a ]