---
source_image: page_047.png
page_number: 47
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.67
tokens: 5925
characters: 1119
timestamp: 2025-12-24T04:05:44.054326
finish_reason: stop
---

*.rpm-файлы.

Файлы Red Hat Package Manager (RPM) устанавливаются и управляются программами rpm (вручную) и up2date (автоматически).

файлы *.tar.gz, *.tar.Z, *.tar.bz2

Упакованные tar-файлы - упакованы с помощью программы tar и сжаты с помощью архиваторов gzip (.gz), compress (.Z) или bzip2 (.bz2).
Большая часть программного обеспечения должна устанавливаться суперпользователем, поэтому вам нужно выполнить команду su (или ее эквивалент) перед установкой. Например:

$ su -1
Password: **********
# rpm -ivh mypackage.rpm
...etc...

Для поиска нового программного обеспечения изучите компакт-диски вашего Linux-дистрибутива или зайдите, например, на следующие сайты.
http://freshmeat.net/ http://freshrpms.net/ http://rpmfmd.net/ http.V/sourceforge.net/

up2date [опции] [файл\] up2date /usr/bin stdin stdout -file --opt --help -version

up2date - это самый простой способ обновления вашей системы Fedora. В режиме суперпользователя просто выполните команду:

#up2date
и следуйте инструкциям. Эта команда вызывает графический пользовательский интерфейс. Также вы можете запустить команду up2date в командном режиме: