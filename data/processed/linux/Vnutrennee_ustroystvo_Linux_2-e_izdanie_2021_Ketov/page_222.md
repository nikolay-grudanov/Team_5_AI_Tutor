---
source_image: page_222.png
page_number: 222
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.01
tokens: 7304
characters: 1428
timestamp: 2025-12-24T04:38:05.310514
finish_reason: stop
---

В листинге 5.40 показано, что команда test(1) и ее «красивая» форма [ изначально являются внешними командами, что также влечет за собой накладные расходы на системные вызовы fork(2) и execve(2). Поэтому в большинстве интерпретаторов обе формы команды test(1) реализованы еще и как встроенные команды.

Листинг 5.40. Команды test и [
bender@ubuntu:~$ which test
/usr/bin/test
bender@ubuntu:~$ which [
/usr/bin/[

bender@ubuntu:~$ type -a test
test — это встроенная команда bash
test является /usr/bin/test
test является /bin/test
bender@ubuntu:~$ type -a [
[ — это встроенная команда bash
[ является /usr/bin/[

[ является /bin/[

bender@ubuntu:~$ test -f /etc/passwd
bender@ubuntu:~$ echo $?
0
bender@ubuntu:~$ [ -w /etc/passwd
-bash: [: отсутствует символ «]»
bender@ubuntu:~$ [ -w /etc/passwd ] -
bender@ubuntu:~$ echo $?
1

Команда test(1) выполняет проверку логических выражений и заканчивается успехом, если проверяемое выражение истинно, и неуспехом, если проверяемое выражение ложно. Именно это ее свойство используется для реализации ветвления. Например, во втором примере из листинга 5.41 проверяется наличие блочного (-b) файла устройства /dev/cdrom и при наличии запускается команда eject(1), предписывающая драйверу устройства открыть лоток привода CD/DVD.

Листинг 5.41. Ветвление при помощи условных списков
bender@ubuntu:~$ which clear && clear || tput clear
bender@ubuntu:~$ [ -b /dev/cdrom ] && eject /dev/cdrom