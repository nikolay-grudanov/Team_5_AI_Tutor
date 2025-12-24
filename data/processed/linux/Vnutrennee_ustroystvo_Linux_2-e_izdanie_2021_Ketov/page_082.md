---
source_image: page_082.png
page_number: 82
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.75
tokens: 7560
characters: 2020
timestamp: 2025-12-24T04:34:14.738206
finish_reason: stop
---

Press ctrl-c to stop encoding

frame= 395 fps= 72 q=31.0 Lsize= 2481kB time=7.94 bitrate=2561.5kbits/s dup=0 drop=1
video:2339kB audio:128kB global headers:4kB muxing overhead 0.457686%

Аналогично, в примере из листинга 3.23 геотеги файлов изображений сетевого видеорегистратора анализируются утилитой exiv2(1), предназначенной для работы с «обычными» изображениями. За счет файловой системы cifs и доступности видеорегистратора по протоколу CIFS его содержимое смонтировано в дерево каталогов так, словно сетевой регистратор является локальным дисковым накопителем.

Листинг 3.23. Сетевая файловая система CIFS/SMB

finn@ubuntu:~$ mount -t cifs -o username=guest //182.168.1.10/share/photos /mnt/nas/photos
Password:
finn@ubuntu:~$ mount
//182.168.1.10/share/photos on /mnt/nas/video type cifs (rw,...)
finn@ubuntu:~$ cd /mnt/nas/photos
finn@ubuntu:~$ ls
DSC_0034.JPG DSC_0043.JPG DSC_0062.JPG DSC_0074.JPG DSC_0100.JPG DSC_0189.JPG

finn@ubuntu:~$ exiv2 -p a DSC_0043.JPG
Exif.GPSInfo.GPSLatitudeRef    Ascii   2 North
Exif.GPSInfo.GPSLatitude       Rational 3 60deg 10' 3.479"
Exif.GPSInfo.GPSLongitudeRef   Ascii   2 East
Exif.GPSInfo.GPSLongitude      Rational 3 24deg 57' 23.294"

3.4.4. Специальные файловые системы

Развитие идеи файла как единицы обеспечения доступа к информации привело к тому, что абстракцию файловой системы перенесли и на другие сущности, доступ к которым стал организовываться в виде иерархии файлов. Например, информацию о процессах, нитях и прочих сущностях ядра операционной системы и используемых ими ресурсах предоставляет программам виде файлов (!) псевдофайловая система proc(5). Таким же образом, информацию об аппаратных устройствах, обнаруженных ядром операционной системы на шинах PCI, USB, SCSI и пр., предоставляет псевдофайловая система sysfs.

Различные утилиты, пользующиеся ядерной информацией, например показывающие нагрузку на операционную систему uptime(1) или списки процессов и загруженных модулей (драйверов) ядра операционной системы — ps(1) и lsmod(8), пользуются