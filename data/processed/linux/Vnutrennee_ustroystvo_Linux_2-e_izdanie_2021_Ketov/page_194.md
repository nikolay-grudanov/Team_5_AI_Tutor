---
source_image: page_194.png
page_number: 194
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.26
tokens: 7273
characters: 1322
timestamp: 2025-12-24T04:37:13.728990
finish_reason: stop
---

bender@ubuntu:$ head -1 /bin/which
#!/bin/sh

bender@ubuntu:~$ file /bin/gunzip
/bin/gunzip: Bourne-Again shell script, ASCII text executable

bender@ubuntu:~$ head -1 /bin/gunzip
#!/bin/bash

bender@ubuntu:~$ file /usr/sbin/iotop
/usr/sbin/iotop: Python script, ASCII text executable

bender@ubuntu:~$ head -1 /usr/sbin/iotop
#!/usr/bin/python3

bender@ubuntu:~$ file /usr/bin/lsdev
/usr/bin/lsdev: Perl script text executable

bender@ubuntu:~$ head -1 /usr/bin/lsdev
#!/usr/bin/perl

bender@ubuntu:~$ file /usr/bin/netwag
/usr/bin/netwag: a /usr/bin/wish script, ASCII text executable, with very long lines, with CRLF, LF line terminators, with overstriking

bender@ubuntu:~$ head -1 /usr/bin/netwag
#!/usr/bin/wish

Сами сценарии представляют собой обычные текстовые файлы, подготавливаемые в любом текстовом редакторе, однако размещаются в каталогах и имеют права (см. ① и ②, листинг 5.2) подобно «обычным» исполняемым W:[ELF]-программам.

Листинг 5.2. Сценарии интерпретаторов

Сессия работы
bender@ubuntu:~$ cat hello.sh
#!/bin/sh

echo "Hello, World!"

bender@ubuntu:~$ hello.sh
hello.sh: команда не найдена

bender@ubuntu:~$ printenv PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:...:/snap/bin

bender@ubuntu:~$ pwd
/home/bender

bender@ubuntu:~$ mkdir /home/bender/bin

bender@ubuntu:~$ logout