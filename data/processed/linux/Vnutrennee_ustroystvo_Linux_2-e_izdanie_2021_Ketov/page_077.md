---
source_image: page_077.png
page_number: 77
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.39
tokens: 7538
characters: 2033
timestamp: 2025-12-24T04:34:02.074891
finish_reason: stop
---

unix с именем /run/systemd/journal/dev-log (файловый дескриптор 2 номер 6 на чтение и запись u) и обычный файл REG с именем /var/log/syslog (файловый дескриптор 3 номер 8 на запись w).

Пронаблюдать за использованием системных вызовов файлового программного интерфейса в момент выполнения программам позволяет системный трассировщик strace(1) (листинг 3.19).

Листинг 3.19. Трассировка файлового программного интерфейса

finn@ubuntu:~$ date
Пн ноя 18 00:13:53 MSK -> 2019
finn@ubuntu:~$ strace -fe open,openat,close,read,write,ioctl date
openat(AT_FDCWD, "/etc/localtime", O_RDONLY|O_CLOEXEC) = 3
finn@ubuntu:~$ file /etc/localtime
/etc/localtime: symbolic link to /usr/share/zoneinfo/Europe/Moscow
finn@ubuntu:~$ file /usr/share/zoneinfo/Europe/Moscow
/usr/share/zoneinfo/Europe/Moscow: timezone data, version 2, 17 gmt time flags, 17 std time flags, no leap seconds, 78 transition times, 17 abbreviation chars

finn@ubuntu:~$ ls -la /dev/dvd
lrwxrwxrwx 1 root root 3 ноя 17 22:35 /dev/dvd -> sr0
finn@ubuntu:~$ strace -fe open,openat,close,read,write,ioctl eject
openat(AT_FDCWD, "/dev/sr0", O_RDWR|O_NONBLOCK) = 3
ioctl(3, CDROMEJECT, 0x01)                = 0
close(3)                                 = 0

finn@ubuntu:~$ strace -fe open,openat,read,write,close,ioctl setleds -L +num +scroll
ioctl(0, KDGKBLED, 0x7ffc1ced3d27)         = 0
ioctl(0, KDGTLLED, 0x7ffc1ced3d26)         = 0
ioctl(0, KDSETLED, 0x3)                   = 0

Предположив, что программа date(1) показывает правильное московское время, потому что узнаёт заданную временную зону MSK из некоего конфигурационного файла операционной системы, при трассировке ее работы можно установить его точное имя — /etc/localtime (оказавшимся символической ссылкой на /usr/share/zoneinfo/Europe/Moscow). Аналогично предположив, что программа eject(1) открывает лоток привода CD/DVD при помощи специального файла устройства, при трассировке можно узнать имя файла — /dev/sr0, номер файлового дескриптора при работе с файлом — 3 и команду CDROMEJECT соответствующего устройству