---
source_image: page_221.png
page_number: 221
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.54
tokens: 7401
characters: 1779
timestamp: 2025-12-24T04:38:07.797150
finish_reason: stop
---

будет найдена очередная команда для выполнения, она будет выполнена и начнется анализ ее статуса выполнения по условиям списка, следующим за ней.

Так, например, в листинге 5.39 комбинированный список «ИЛИ-И» всегда приводит к выводу списка файлов из каталога, куда смонтирован ISO-образ, вне зависимости от того, был ли он туда смонтирован до запуска списка или был смонтирован командами при его выполнении.

Листинг 5.39. Комбинация списков «И» и «ИЛИ»

bender@ubuntu:~$ set -x
bender@ubuntu:~$ findmnt ~/.dvd || fuseiso dvd.iso ~/.dvd && ls -a ~/.dvd

1 + findmnt /home/bender/.dvd
2 + fuseiso dvd.iso /home/bender/.dvd
3 + ls --color=auto -a /home/bender/.dvd

acme bootdisk.img env LICENSE.afpl mips pbsraw sparc
.. adm cfg fd LICENSE.gpl mnt power sys
386 amd64 cron lib lp n power64 tmp
9load arm dist LICENSE mail NOTICE rc usr

bender@ubuntu:~$ findmnt ~/.dvd || fuseiso dvd.iso ~/.dvd && ls -a ~/.dvd

1 + findmnt /home/bender/.dvd
TARGET SOURCE FSTYPE OPTIONS
/home/bender/.dvd fuseiso fuse.fuseiso rw,nosuid,nodev,relatime,user_id=1008,...
3 + ls --color=auto -a /home/bender/.dvd

acme bootdisk.img env LICENSE.afpl mips pbsraw sparc
.. adm cfg fd LICENSE.gpl mnt power sys
386 amd64 cron lib lp n power64 tmp
9load arm dist LICENSE mail NOTICE rc usr

5.6.2. Составные списки: ветвление

Условные списки «И» и «ИЛИ» являются простейшей формой ветвления хода выполнения сценария в зависимости от успеха или неудачи выполнения той или иной команды. При помощи специальной команды¹ test(1), позволяющей выполнять проверки логических выражений, можно осуществлять ветвление сценария, например, в зависимости от определенных условий или значений тех или иных параметров.

¹ Аналогично специальной команде expr(1), предназначенной для вычисления арифметических выражений.