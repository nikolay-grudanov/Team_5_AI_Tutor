---
source_image: page_210.png
page_number: 210
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.96
tokens: 7168
characters: 1074
timestamp: 2025-12-24T04:37:37.597874
finish_reason: stop
---

На рис. 5.4 показана широко распространенная подстановка результата работы команды command2 в качестве аргументов1 команды command1, используемая в виде command1 $(command2). Так, например, можно, зная полный путь (который можно получить при помощи which(1)) к определенной утилите, выяснить при помощи dpkg(1) пакет программного обеспечения, которому он принадлежит, что показано в примере из листинга 5.25 в режиме трассировки.

Листинг 5.25. В каком пакете утилита?

bender@ubuntu:~$ which lspci
/usr/bin/lspci
bender@ubuntu:~$ set -x
1 bender@ubuntu:~$ dpkg -S `which lspci`
++ which lspci
+ dpkg -S /usr/bin/lspci
pciutils: /usr/bin/lspci
2 bender@ubuntu:~$ dpkg -S $(which lspci) | cut -f 1 -d : | xargs dpkg -s
+ xargs dpkg -s
+ cut -f 1 -d :
++ which lspci
+ dpkg -S /usr/bin/lspci
Package: pciutils
Description: PCI utilities
This package contains various utilities for inspecting and setting of devices connected to the PCI bus.

1 Для сравнения: при конвейерной обработке результаты выполнения одной команды передаются в качестве исходных данных другой программе.