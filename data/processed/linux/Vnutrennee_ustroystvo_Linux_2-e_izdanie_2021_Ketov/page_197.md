---
source_image: page_197.png
page_number: 197
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.42
tokens: 7422
characters: 1762
timestamp: 2025-12-24T04:37:29.899212
finish_reason: stop
---

Листинг 5.4. Перенаправление стандартного потока вывода

bender@ubuntu:~$ sed -n 5,8p /etc/passwd
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
lp:x:7:7:lp:/var/spool/lpd:/bin/sh
bender@ubuntu:~$ cut -f 1 -d : /etc/passwd 1> users
bender@ubuntu:~$ sed -n 5,8p users
sync
games
man
lp

При выполнении некоторых команд, например как в листинге 5.5, при поиске файлов посредством find(1) может выводиться достаточное количество сообщений об «ошибках» доступа в тот или иной каталог, которые мешают анализировать результаты поиска. В этом случае их удобно убрать с терминала путем перенаправления потока № 2, stderr(3), например в файл eaccess. В результате на терминале будут отражены только имена (-name) файлов, соответствующие критерию имени *.xml, найденные в каталоге /etc и всех его подкаталогах.

Листинг 5.5. Перенаправление стандартного потока ошибок

bender@ubuntu:~$ find /etc -name '*.xml'
/etc/cupshelpers/preferreddrivers.xml
...
...
...
?
find: '/etc/cups/ssl': Отказано в доступе
find: '/etc/polkit-1/localauthority': Отказано в доступе
find: '/etc/ssl/private': Отказано в доступе
...
...
...
/etc/thermal/thermal-cpu-cdev-order.xml
bender@ubuntu:~$ find /etc -name '*.xml' 2>eaccess
/etc/cupshelpers/preferreddrivers.xml
...
...
...
/etc/ImageMagick-6/log.xml
/etc/thermal/thermal-cpu-cdev-order.xml

На практике часто оказывается, что мешающий вывод сообщений об «ошибках» доступа, как в листинге 5.6, оказывается ненужным вовсе, тогда его подавляют при помощи перенаправления потока STDERR в файл /dev/null специального всепожирающего псевдоустройства null(4). Подсчитав количество строк (-l) в результирующем файле empty и зная, что одна строка в нем соответствует одному найден-