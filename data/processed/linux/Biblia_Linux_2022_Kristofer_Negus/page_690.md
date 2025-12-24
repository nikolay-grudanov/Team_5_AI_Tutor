---
source_image: page_690.png
page_number: 690
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.09
tokens: 7469
characters: 1965
timestamp: 2025-12-24T05:04:40.756741
finish_reason: stop
---

ПРИМЕЧАНИЕ

Файлы конфигурации PAM находятся в каталогах /etc/pam.d и /etc/security.

В следующем примере показан файл /etc/security/limits.conf. Он хорошо закомментирован. Необходимо прочитать содержимое этого файла, где подробно описан формат и приведены примеры ограничений, которые можно установить:

$ cat /etc/security/limits.conf
# /etc/security/limits.conf
#
#This file sets the resource limits for the users logged in via PAM.
#It does not affect resource limits of the system services.
#
#Also note that configuration files in /etc/security/limits.d directory,
#which are read in alphabetical order, override the settings in this #file in case the domain is the same or more specific.
...
#Each line describes a limit for a user in the form:
#
#<domain>    <type>   <item>   <value>
...
#*
soft      core      0
#*
hard      rss       10000
#@student hard      nproc     20
#@faculty soft      nproc     20
#@faculty hard      nproc     50
#ftp       hard      nproc     0
#@student -         maxlogins 4
# End of file

Элементы формата domain (домен) и type (тип) нуждаются в дополнительном объяснении вдобавок к задокументированному в файле конфигурации.

● domain (домен). Ограничение применяется к указанным пользователю или группе, а если в значении домена указан символ *, то ко всем пользователям.
● type (тип). Предел hard не может быть превышен. Предел soft может быть превышен, но только временно.

Посмотрите на настройки файла limits.conf в примере. В списке указана группа преподавателей faculty, однако нужно приглядеться к элементу nproc. Ограничение nproc устанавливает максимальное количество процессов, которые может запустить пользователь. Именно эта настройка предотвращает fork-бомбу. Обратите внимание на то, что тип type установлен в предел hard, таким образом, предел в 50 процессов не может быть превышен. Конечно, это ограничение не применяется, потому что строка закомментирована символом #:

#@faculty    hard      nproc     50