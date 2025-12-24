---
source_image: page_345.png
page_number: 345
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.63
tokens: 7588
characters: 2177
timestamp: 2025-12-24T04:42:06.824526
finish_reason: stop
---

Используя чрутизацию, уже можно организовать протоконтейнеры при помощи одноименной утилиты chroot(1), которая при запуске назначает своему процессу указанный корневой каталог, а затем замещает себя при помощи системного вызова exec(2) на указанную программу. В результате программа оказывается изолированной в определенной части дерева каталогов. Естественно, при таком поведении утилиты chroot(1) в изолированном окружении можно запускать только программы, сами там расположенные. Более того, не стоит забывать, что программы при запуске компонуются с библиотеками, от которых зависят, поэтому и библиотеки, и сам компоновщик тоже должны располагаться в том же окружении.

В листинге 9.2 показано создание протоконтейнера c-137, в который помещаются командный интерпретатор sh и все необходимые компоненты для его работы, а затем он запускается в этом изолированном окружении.

Листинг 9.2. Протоконтейнер, созданный при помощи chroot

rick@ubuntu:~$ mkdir c-137
rick@ubuntu:~$ chroot c-137 sh
chroot: cannot change root directory to 'c-137': Operation not permitted
rick@ubuntu:~$ sudo chroot c-137 sh
? chroot: failed to run command 'sh': No such file or directory
rick@ubuntu:~$ sudo strace -fe chroot,chdir,execve chroot c-137 sh
execve("/usr/sbin/chroot", ["chroot", "c-137", "sh"], ...) = 0
chroot("c-137")                = 0
chdir("/")                      = 0
execve("/usr/bin/sh", ["sh"], ...) = -1 ENOENT (No such file or directory)
execve("/sbin/sh", ["sh"], ...) = -1 ENOENT (No such file or directory)
execve("/bin/sh", ["sh"], ...) = -1 ENOENT (No such file or directory)
chroot: failed to run command 'sh': No such file or directory
+++ exited with 127 +++
rick@ubuntu:~$ mkdir c-137/bin
rick@ubuntu:~$ cp /bin/sh c-137/bin
rick@ubuntu:~$ sudo chroot c-137 sh
? chroot: failed to run command 'sh': No such file or directory
rick@ubuntu:~$ ldd /bin/sh
    linux-vdso.so.1 (0x00007ffe64cdd000)
    libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fb508897000)
    /lib64/ld-linux-x86-64.so.2 (0x00007fb508abf000)
rick@ubuntu:~$ tar ch /lib/x86_64-linux-gnu/libc.so.6 /lib64/ld-linux-x86-64.so.2 | 
> tar x -C c-137
tar: Removing leading '/' from member names