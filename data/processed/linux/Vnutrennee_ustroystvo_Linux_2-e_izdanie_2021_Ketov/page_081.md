---
source_image: page_081.png
page_number: 81
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.61
tokens: 7623
characters: 1850
timestamp: 2025-12-24T04:34:12.219216
finish_reason: stop
---

System или Server Message Block, W:[Server_Message_Block]) или им подобным. Одноименные файловые системы nfs и cifs/smb используются для монтирования файлов сервера в дерево каталогов клиента. Таким образом, обычные (ничего не знающие ни про какие сетевые протоколы) программы, запускаемые в операционной системе клиента, используют файлы сетевого сервера точно так, как если бы они были размещены на локальных дисках, под управлением дисковых файловых систем.

В примере из листинга 3.22 программы avconv(1) и avprobe(1), предназначенные для работы с «обычными» видеофайлами, используются для обработки записей сетевого видеорегистратора, видеофайлы которого доступны по протоколу NFS. Смонтированные при помощи сетевой файловой системы nfs в дерево каталогов файлы сетевого регистратора становятся никак неотличимы от файлов локальных дисковых файловых систем.

Листинг 3.22. Сетевая файловая система NFS

finn@ubuntu:~$ mount -t nfs 182.168.1.10:/share/video /mnt/nas/video
finn@ubuntu:~$ mount
182.168.1.10:/share/video on /mnt/nas/video type nfs (rw,...)
finn@ubuntu:~$ cd /mnt/nas/video/screencasts
finn@ubuntu:~$ ls
20140523142626.mp4

finn@ubuntu:~$ file 20140523142626.mp4
20140523142626.mp4: ISO Media, MPEG v4 system, version 2

finn@ubuntu:~$ avprobe 20140523142626.mp4
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from '20140523142626.mp4':
    Duration: 00:00:07.94, start: 0.000000, bitrate: 11020 kb/s
    Stream #0.0(eng): Video: h264 (High), yuv420p, 1920x1080 [PAR 1:1 DAR 16:9], 10843 kb/s, 50 fps, 50 tbr, 50k tbn, 100 tbc

finn@ubuntu:~$ avconv -i 20140523142626.mp4 20140523142626.mkv
Output #0, matroska, to '20140523142626.mkv':
    Stream #0.0(eng): Video: mpeg4, yuv420p, 1920x1080 [PAR 1:1 DAR 16:9], q=2-31, 200 kb/s, 1k tbn, 50 tbc
Stream mapping:
    Stream #0:0 -> #0:0 (h264 -> mpeg4)
    Stream #0:1 -> #0:1 (aac -> libvorbis)