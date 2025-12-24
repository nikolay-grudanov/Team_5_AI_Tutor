---
source_image: page_021.png
page_number: 21
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.46
tokens: 7267
characters: 1370
timestamp: 2025-12-24T04:32:16.080973
finish_reason: stop
---

граммы. В листинге 1.1 представлена трассировка программ whoami(1), hostname(1) и pwd(1) относительно системных вызовов geteuid(2), uname(2), getcwd(2) и sethostname(2), где оказывается, что для получения и установки значения (сетевого) имени системы программа hostname(1) использует разные системные вызовы uname(2) и sethostname(2), при этом один из системных вызовов является привилегированным и доступен только суперпользователю root (см. разд. 2.7).

Листинг 1.1. Трассировщик системных вызовов strace

bart@ubuntu:~$ whoami
bart

bart@ubuntu:~$ hostname
ubuntu

bart@ubuntu:~$ pwd
/home/bart

bart@ubuntu:~$ strace -fe uname,getcwd,geteuid,sethostname whoami
geteuid() = 1000
bart
+++ exited with 0 +++

bart@ubuntu:~$ strace -fe uname,getcwd,geteuid,sethostname hostname
uname({sysname="Linux", nodename="ubuntu", ...}) = 0
ubuntu
+++ exited with 0 +++

bart@ubuntu:~$ strace -fe uname,getcwd,geteuid,sethostname pwd
getcwd("/home/bart", 4096) = 11
/home/bart
+++ exited with 0 +++

bart@ubuntu:~$ strace -fe uname,getcwd,geteuid,sethostname hostname springfield
sethostname("springfield", 11) = -1 EPERM (Операция не позволена)
hostname: you must be root to change the host name
+++ exited with 1 +++

В листинге 1.2 показана трассировка программы date(1) относительно библиотечных вызовов fwrite(2) или таких, в имени которых встречается строка time. Оказывает-