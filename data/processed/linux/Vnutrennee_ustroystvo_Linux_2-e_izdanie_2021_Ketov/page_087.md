---
source_image: page_087.png
page_number: 87
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.32
tokens: 7440
characters: 1865
timestamp: 2025-12-24T04:34:16.887911
finish_reason: stop
---

В примере из листинга 3.29 показано, как можно монтировать файловые системы fuse друг поверх друга в стек — смонтировать содержимое дерева каталогов FTP-сервера mirror.yandex.ru, далее смонтировать содержимое ISO-образа FreeBSD-12.1-RELEASE-amd64-dvd1.iso, а затем смонтировать архив исходных текстов src.txz. При чтении файла страницы руководства ls.1 файловые системы будут прозрачно и на лету (!) извлекать файл из архива, архив из образа и образ с сервера без предварительных скачиваний и распаковываний.

Листинг 3.29. Внеядерные файловые системы «fuse.curlftpfs», «fuse.fuseiso» и стекирование файловых систем

finn@ubuntu:~$ curlftpfs mirror.yandex.ru ~/mnt/net

finn@ubuntu:~$ fuseiso ~/mnt/net/freebsd/releases/ISO-IMAGES/12.1/FreeBSD-12.1-RELEASE-amd64-dvd1.iso ~/mnt/cd

finn@ubuntu:~$ archivemount ~/mnt/cd/usr/freebsd-dist/src.txz ~/mnt/archive

finn@ubuntu:~$ mount
curlftpfs#ftp://mirror.yandex.ru/ on /home/finn/mnt/net type fuse (rw,...)
fuseiso on /home/finn/mnt/cd type fuse.fuseiso (rw,...)
archivemount on /home/finn/mnt/archive type fuse.archivemount (rw,...)

finn@ubuntu:~$ man ~/mnt/archive/usr/src/bin/ls/ls.1
LS(1)           BSD General Commands Manual

NAME
    ls - list directory contents

finn@ubuntu:~$ fusermount -u ~/mnt/archive
finn@ubuntu:~$ fusermount -u ~/mnt/cd
finn@ubuntu:~$ fusermount -u ~/mnt/net

3.5. Дискреционное разграничение доступа

В Linux, как и в любой многопользовательской системе, абсолютно естественным образом возникает задача разграничения доступа субъектов — пользователей к объектам — файлам дерева каталогов. Один из подходов к разграничению доступа — так называемый дискреционный (от англ. discretion — чье-либо усмотрение) — предполагает назначение владельцев объектов, которые по собственному усмотрению определяют права доступа субъектов (других пользователей) к объектам (файлам), которыми владеют.