---
source_image: page_151.png
page_number: 151
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.58
tokens: 7761
characters: 2473
timestamp: 2025-12-24T03:04:58.010224
finish_reason: stop
---

что у ссылки на каталог был установлен sticky bit, предотвращавший изменение пути другими ссылками, включая устройство блочного ввода/вывода. У утилиты chown есть специальный флаг (-h или --no-dereference), указывающий, что смена владельца должна влиять и на ссылки.

Выполнять подобную отладку без чего-то наподобие утилиты strace очень сложно, а то и вовсе невозможно. Попробуйте ее сами, для чего создайте файл follow.py со следующим содержимым:

import subprocess

subprocess.call(['ls', '-alh'])

Он импортирует модуль subprocess для выполнения системных вызовов, после чего выводит результаты системного вызова ls. Вместо вызова напрямую с помощью Python укажите перед командой strace и посмотрите, что произойдет:

$ strace python follow.py

Терминал сразу заполнится огромным количеством информации, большая часть которой, вероятно, покажется вам тарабарщиной. Заставьте себя просмотреть каждую строку вне зависимости от того, понятно ли ее содержание. Некоторые строки легче отделить от прочих. Например, сразу заметно множество вызовов read и fstat, вы увидите непосредственно системные вызовы, выполняемые процессом на каждом шаге. Над некоторыми файлами также производятся операции open и close, кроме того, в отдельном разделе можно видеть несколько вызовов stat:

stat("/home/alfredo/go/bin/python", 0x7ff) = -1 ENOENT (No such file)
stat("/usr/local/go/bin/python", 0x7ff) = -1 ENOENT (No such file)
stat("/usr/local/bin/python", 0x7ff) = -1 ENOENT (No such file)
stat("/home/alfredo/bin/python", 0x7ff) = -1 ENOENT (No such file)
stat("/usr/local/sbin/python", 0x7ff) = -1 ENOENT (No such file)
stat("/usr/local/bin/python", 0x7ff) = -1 ENOENT (No such file)
stat("/usr/sbin/python", 0x7ff) = -1 ENOENT (No such file)
stat("/usr/bin/python", {st_mode=S_IFREG|0755, st_size=3691008, ...}) = 0
readlink("/usr/bin/python", "python2", 4096) = 7
readlink("/usr/bin/python2", "python2.7", 4096) = 9
readlink("/usr/bin/python2.7", 0x7ff, 4096) = -1 EINVAL (Invalid argument)
stat("/usr/bin/Modules/Setup", 0x7ff) = -1 ENOENT (No such file)
stat("/usr/bin/lib/python2.7/os.py", 0x7ffd) = -1 ENOENT (No such file)
stat("/usr/bin/lib/python2.7/os.pyc", 0x7ff) = -1 ENOENT (No such file)
stat("/usr/lib/python2.7/os.py", {st_mode=S_IFREG|0644, ...}) = 0
stat("/usr/bin/pybuilddir.txt", 0x7ff) = -1 ENOENT (No such file)
stat("/usr/bin/lib/python2.7/lib-dynload", 0x7ff) = -1 ENOENT (No such file)
stat("/usr/lib/python2.7/lib-dynload", {st_mode=S_IFDIR|0755, ...}) = 0