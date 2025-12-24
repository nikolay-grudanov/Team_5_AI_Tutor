---
source_image: page_226.png
page_number: 226
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.59
tokens: 7292
characters: 1245
timestamp: 2025-12-24T04:38:14.898932
finish_reason: stop
---

**Листинг 5.44. Множественное ветвление**

bender@ubuntu:~$ PROMPT_COMMAND=\
> case $? in \
>   0|127) PROMPT_COLOR=`tput sgr0`;; \
>   13[01]) PROMPT_COLOR=`tput rev`;; \
>   1) PROMPT_COLOR=`tput bold`;; \
>   *) echo "exit code = $?"; PROMPT_COLOR=`tput bold`;; \
> esac

bender@ubuntu:~$ PS1='echo $PROMPT_COLOR\u@\h \w\$ `tput sgr0`'

bender@ubuntu ~$ dd
^C0+0 записей получено
0+0 записей отправлено
скопировано 0 байт (0 B), 0,900673 c, 0,0 kB/c

bender@ubuntu ~$

1 bender@ubuntu ~$ date
Сб ноя 23 15:55:19 MSK 2019
bender@ubuntu ~$

bender@ubuntu ~$ grep bender /etc/shadow
grep: /etc/shadow: Отказано в доступе
exit code = 2

2 bender@ubuntu ~$

**5.6.3. Составные списки: циклы**

Последний важный вид составных списков предназначен для многократного циклического выполнения команд в сценариях командного интерпретатора. Различают цикл с параметром, реализуемый конструкцией

for name in [words ...]; do list; done.

и циклы с условием «ПОКА»

while [!] list; do list; done

и «ДО»

until [!] list do list; done

с ключевыми словами for, in, while, until, do, done соответственно.

В примере из листинга 5.45 цикл с параметром используется для создания галереи миниатюр фотографий при помощи составного списка for и подстановки вывода