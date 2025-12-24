---
source_image: page_207.png
page_number: 207
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.28
tokens: 7397
characters: 1557
timestamp: 2025-12-24T04:37:43.892089
finish_reason: stop
---

+ file /bin/bash

/bin/bash: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=0xf199a4a89ac968c2e0e99f2410600b9d7e995187, stripped

bender@ubuntu:/tmp$ ps p $SSH_AGENT_PID

+ ps p 3260

PID TTY STAT TIME COMMAND
3260 ? Ss 0:00 /usr/bin/ssh-agent /usr/bin/im-launch env GNOME_SHELL

bender@ubuntu:/tmp$ cd $HOME

+ cd /home/bender

bender@ubuntu:~$

Позиционные параметры

Позиционные параметры используются сценариями командного интерпретатора для передачи их фактических параметров и идентифицируются номерами, нумерующими аргументы сценария, указанные при его запуске. Например, в листинге 5.21 показан достаточно простой сценарий tgz(1), применяемый для создания .tgz-архивов. В тексте сценария используются подстановки $1 и $0, символизирующие первый формальный аргумент ①, переданный в сценарий при его запуске, и нулевой формальный аргумент ② — имя самого сценария. При последующем запуске сценария в режиме трассировки (явно указывая интерпретатор sh с опцией -x) ему передаются фактические аргументы ① и ①, которые соответствующим образом подставляются в командах, выполняемых интерпретатором согласно тексту сценария.

Листинг 5.21. Подстановка значений позиционных параметров

bender@ubuntu:~$ which tgz
/usr/bin/tgz

bender@ubuntu:~$ file /usr/bin/tgz
/usr/bin/gunzip: POSIX shell script, ASCII text executable

bender@ubuntu:~$ less /usr/bin/gunzip
#!/bin/sh
...
Error ()
{
    echo "Error: $0: ${@-}." >&2 ①
    exit 1
}

if [ $# = 0 ]; then
else
    dest=$1 ①