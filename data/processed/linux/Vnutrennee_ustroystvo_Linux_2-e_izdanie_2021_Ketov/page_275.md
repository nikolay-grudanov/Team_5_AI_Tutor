---
source_image: page_275.png
page_number: 275
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.07
tokens: 7666
characters: 1902
timestamp: 2025-12-24T04:39:57.712406
finish_reason: stop
---

Листинг 6.25. FTP-клиент lftp

lumpy@ubuntu $ lftp cdimage.debian.org
lftp cdimage.debian.org:~> cd /cdimage/ports/latest/hurd-i386/current
cd ok, каталог=/cdimage/ports/latest/hurd-i386/current
lftp cdimage.debian.org:/../hurd-i386/current> ls *.iso
-rw-r--r--   1 ftp ftp  670121984 Feb 20 2019 debian-sid-hurd-i386-CD-1.iso
-rw-r--r--   1 ftp ftp  1764358144 Feb 20 2019 debian-sid-hurd-i386-DVD-1.iso
-rw-r--r--   1 ftp ftp  174952448 Feb 20 2019 debian-sid-hurd-i386-NETINST-1.iso
-rw-r--r--   1 ftp ftp  30199808 Feb 20 2019 mini.iso
lftp cdimage.debian.org:/../hurd-i386/current> get debian-sid-hurd-i386-DVD-1.iso &

[0] get debian-sid-hurd-i386-DVD-1.iso &
    'debian-sid-hurd-i386-DVD-1.iso' в позиции 0
lftp cdimage.debian.org:/../hurd-i386/current> get mini.iso &

[1] get mini.iso &
    'mini.iso' в позиции 0
lftp cdimage.debian.org:/../hurd-i386/current> jobs
[1] get mini.iso -- 907.5 Киб/с
    'mini.iso' в позиции 1573976 (5%) 907.5Кб/с овп:31с [Получение данных]
[0] get debian-sid-hurd-i386-DVD-1.iso -- 2.95 Миб/с
    'debian-sid-hurd-i386-DVD-1.iso' в позиции 18610948 (1%) 2.95Мб/с овп:9м [Получение данных]
lftp cdimage.debian.org:/../hurd-i386/current> quit

[12334] Переход в фоновый режим для завершения работы заданий...

lumpy@ubuntu $ lftp -c attach 12334
[12334] Присоединился к терминалу.
lftp cdimage.debian.org:/cdimage/ports/latest/hurd-i386/current> jobs
[0] get debian-sid-hurd-i386-DVD-1.iso -- 498.6 Киб/с
    'debian-sid-hurd-i386-DVD-1.iso' в позиции 718802944 (40%) овп:6м [Получение данных]
lftp cdimage.debian.org:/cdimage/ports/latest/hurd-i386/current> quit
[12334] Переход в фоновый режим для завершения работы заданий...

Кроме массы специализированных FTP-клиентов ftp(1), lftp(1), ncftp(1), gftp(1), протокол FTP поддерживается и другими программными средствами, скажем различными файловыми менеджерами, что иллюстрирует листинг 6.26 на примере mc(1).