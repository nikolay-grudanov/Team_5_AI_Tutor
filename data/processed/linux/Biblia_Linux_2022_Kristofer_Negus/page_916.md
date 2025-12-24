---
source_image: page_916.png
page_number: 916
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.18
tokens: 7439
characters: 1536
timestamp: 2025-12-24T05:10:46.325567
finish_reason: stop
---

3. Чтобы запустить образ ubi7/ubi, откройте оболочку bash:

# podman run -it ubi7/ubi bash

ИЛИ

# docker run -it ubi7/ubi bash

4. Чтобы выполнить команды для просмотра операционной системы, на которой основан контейнер, установите пакет proc-ps и выполните команду для просмотра процессов, запущенных внутри контейнера:

bash-4.4# cat /etc/os-release | grep ^NAME
NAME="Red Hat Enterprise Linux"
bash-4.4# yum install procps -y
bash-4.4# ps -ef
UID     PID  PPID  C STIME TTY      TIME CMD
root     1    0  0 03:37 pts/0   00:00:00 bash
root    20    1  0 03:43 pts/0   00:00:00 ps -ef
bash-4.4# exit

5. Чтобы перезапустить контейнер, который вы только что закрыли с помощью интерактивной оболочки, и подключиться к нему, введите следующее:

# podman ps -a
CONTAINER ID   IMAGE           COMMAND   CREATED   STATUS    PORTS     NAMES
eabf1fb57a3a   ...ubi8/ubi:latest bash     7 minutes ago   Exited (0) 4 seconds ago compassionate_hawking
# podman start -a eabf1fb57a3a
bash-4.4# exit

6. Чтобы создать простой файл Dockerfile из базового образа ubi7/ubi, включите скрипт cworks.sh, который повторяет фразу The Container Works!, и добавьте его к образу:

а) создайте и измените новый каталог:

# mkdir project
# cd project

б) создайте файл Dockerfile со следующим содержимым:

FROM registry.access.redhat.com/ubi7/ubi-minimal
COPY ./cworks.sh /usr/local/bin/
CMD ["/usr/local/bin/cworks.sh"]

в) создайте файл cworks.sh со следующим содержимым:

#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail
echo "The Container Works!"