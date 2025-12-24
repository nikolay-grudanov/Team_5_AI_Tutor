---
source_image: page_206.png
page_number: 206
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.16
tokens: 7399
characters: 1474
timestamp: 2025-12-24T04:37:42.406944
finish_reason: stop
---

-rw-r--r-- 1 bender bender 114650029 мс 23 10:36 dvd.iso.gz
-rw-r--r-- 1 bender bender 113666114 мс 23 00:02 plan9.iso.gz
bender@ubuntu:~$ TZ=Europe/Helsinki ls -l
итого 222976
-rw-r--r-- 1 bender bender 114650029 marras 23 09:36 dvd.iso.gz
-rw-r--r-- 1 bender bender 113666114 marras 22 23:02 plan9.iso.gz
bender@ubuntu:~$ typeset -p LC_TIME TZ
declare -x LC_TIME="ru_RU.UTF-8"
-bash: typeset: TZ: не найден
bender@ubuntu:~$ ls -l
итого 222976
-rw-r--r-- 1 bender bender 114650029 ноя 23 10:36 dvd.iso.gz
-rw-r--r-- 1 bender bender 113666114 ноя 23 00:02 plan9.iso.gz

Для подстановки значения параметров при выполнении команд используется конструкция $parameter, где символ $ является требованием подстановки, а parameter — идентификатором параметра, например именем переменной, номером позиционного параметра или символом специального параметра.

В режиме трассировки команд интерпретатора из листинга 5.20 видно, что командный интерпретатор вместо указанной переменной подставляет ее значение до выполнения команды, после чего команда выполняется так, как будто ее аргументы были заданы непосредственно подставленными значениями.

Листинг 5.20. Подстановка значений переменных

bender@ubuntu:/tmp$ env
SSH_AGENT_PID=3260
SHELL=/bin/bash
USER=bender
USERNAME=bender
MAIL=/var/mail/bender
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
PWD=/tmp
LANG=ru_RU.UTF-8
HOME=/home/bender
LOGNAME=bender
bender@ubuntu:/tmp$ set -x
bender@ubuntu:/tmp$ file $SHELL