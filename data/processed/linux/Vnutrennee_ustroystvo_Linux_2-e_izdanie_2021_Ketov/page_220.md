---
source_image: page_220.png
page_number: 220
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.65
tokens: 7478
characters: 2004
timestamp: 2025-12-24T04:38:07.592581
finish_reason: stop
---

В примере из листинга 5.37 безусловная попытка ① смонтировать ISO-образ диска неуспешна, потому что эта операция уже была выполнена ранее. Условный список «ИЛИ» ② организует проверку «смонтированности» файловой системы в указанный каталог. Если первая команда списка findmnt(1) завершится неуспехом (если никакая файловая система в указанный каталог не смонтирована), то в этом случае будет запущена команда монтирования fuseiso(1). В противном случае результатом успешно выполнившейся команды findmnt(1) будет вывод информации о файловой системе, уже смонтированной в целевой каталог.

Листинг 5.37. Список «ИЛИ»

bender@ubuntu:~$ fuseiso dvd.iso ~/.dvd
① bender@ubuntu:~$ fuseiso dvd.iso ~/.dvd
fuse: mountpoint is not empty
fuse: if you are sure this is safe, use the 'nonempty' mount option
② bender@ubuntu:~$ set -x
bender@ubuntu:~$ findmnt ~/.dvd || fuseiso dvd.iso ~/.dvd
+ findmnt /home/bender/.dvd
TARGET      SOURCE   FSTYPE   OPTIONS
/home/bender/.dvd fuseiso fuse,fuseiso rw,nosuid,nodev,relatime,user_id=1008,group_id=1010

Условный список «И» в примере из листинга 5.38, наоборот, пытается размонтировать файловую систему, только если она была смонтирована ранее.

Листинг 5.38. Список «И»

bender@ubuntu:~$ fusermount -u ~/.dvd
fusermount: entry for /home/bender/.dvd not found in /etc/mtab
bender@ubuntu:~$ set -x
bender@ubuntu:~$ findmnt ~/.dvd && fusermount -u ~/.dvd
+ findmnt /home/bender/.dvd

Условные списки можно комбинировать, например, в виде command₁ && command₂ || command₃ ... или command₁ || command₂ && command₃. Сначала будет выполнена первая команда, и начнется анализ ее статуса завершения по условиям списка. Если после команды указано условие «И» &&, то при ее успешном завершении будет выполнена следующая команда, а при неуспешном анализ продолжится на следующем условии и т. д. И наоборот, если после команды указано условие «ИЛИ», то при ее неуспешном завершении будет выполнена следующая команда, а при успешном анализ продолжится на следующем условии. Как только