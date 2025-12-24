---
source_image: page_762.png
page_number: 762
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.26
tokens: 7688
characters: 2132
timestamp: 2025-12-24T05:06:51.407298
finish_reason: stop
---

проверяете файл os-release, чтобы увидеть операционную систему, на которой основан контейнер:

[root@e9086da6ed70 /]# ls /
bin dev home lib64 media opt root sbin sys usr
boot etc lib lost+found mnt proc run srv tmp var
[root@e9086da6ed70 /]# cat /etc/os-release | grep ^NAME
NAME="Red Hat Enterprise Linux"

Поскольку контейнеры предназначены для хранения минимального объема содержимого, необходимого для запуска предполагаемого приложения, многих стандартных инструментов в контейнере может не быть. Вы можете установить программное обеспечение в работающий контейнер. Однако имейте в виду, что контейнеры — вещь непостоянная. Поэтому, если хотите добавить программное обеспечение на постоянной основе, необходимо создать новый образ, чтобы включить в него нужное ПО.

Вот пример добавления программного обеспечения в работающий контейнер:

[root@e9086da6ed70 /]# yum install procps iproute -y

Теперь можно запускать команды как ps и ip внутри контейнера.

[root@e9086da6ed70 /]# ps -ef
UID     PID  PPID  C STIME TTY      TIME CMD
root     1    0   0 17:44 pts/0    00:00:00 bash
root    40    1   0 17:45 pts/0    00:00:00 ps -ef
[root@e9086da6ed70 /]# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 ...
    inet 127.0.0.1/8 scope host lo
    ...
3: eth0@if11: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 ...
    inet 10.88.0.6/16 brd 10.88.255.255 scope global eth0
    ...

Обратите внимание на то, что внутри контейнера запущены только два процесса — оболочка и команда ps. PID 1 — это оболочка bash. Часть вывода из команды ip a показывает, что существует только один внешний сетевой интерфейс из контейнера (eth0@if11) и ему присвоен IP-адрес 10.88.0.6/16.

Закончив, введите команду exit, чтобы выйти из оболочки и остановить контейнер:

[root@e9086da6ed70 /]# exit

Хотя оболочка и контейнер больше не работают, контейнер по-прежнему доступен в вашей системе в остановленном состоянии. Обратите внимание, что просто команда podman ps не отображает контейнер — нужно добавить параметр --all:

[root@e9086da6ed70 /]# podman ps
CONTAINER ID  IMAGE  COMMAND  CREATED  STATUS  PORTS  NAMES
[root@e9086da6ed70 /]# podman ps --all