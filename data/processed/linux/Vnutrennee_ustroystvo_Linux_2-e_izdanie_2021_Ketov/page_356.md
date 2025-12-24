---
source_image: page_356.png
page_number: 356
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.67
tokens: 7592
characters: 2097
timestamp: 2025-12-24T04:42:27.886021
finish_reason: stop
---

rick@ubuntu:~ $ id
uid=1000(rick) gid=1000(rick) groups=1000(rick),4(adm),...,27(sudo),...,132(docker)
rick@ubuntu:~ $ docker image ls
REPOSITORY      TAG      IMAGE ID      CREATED      SIZE
rick@ubuntu:~ $ docker image pull ubuntu:16.04
16.04: Pulling from library/ubuntu
3386e6af03b0: Downloading [====================>        ] 41.38MB/44.12MB
49ac0bbe6c8e: Download complete
d1983a67e104: Download complete
1a0f3a523f04: Download complete
Digest: sha256:181800dada370557133a502977d0e3f7abda0c25b9bbb035f199f5eb6082a114
Status: Downloaded newer image for ubuntu:16.04
docker.io/library/ubuntu:16.04
rick@ubuntu:~ $ docker image ls
REPOSITORY      TAG      IMAGE ID      CREATED      SIZE
ubuntu         16.04    c6a43cd4801e   3 weeks ago  123MB
rick@ubuntu:~ $ docker run -ti -h c-123 -n c-123 ubuntu:16.04
root@c-123:#

В листинге 9.10 показана процедура запуска Docker-контейнера при помощи утилиты docker(1). В реальности эта утилита является всего лишь пользовательским интерфейсом к Docker-службе dockerd, которая использует, в свою очередь, службу управления контейнерами containerd, запускающую контейнеры при помощи все той же runc(1), эксплуатирующей механизмы изоляции ядра¹.

Обращаться к службе dockerd посредством файлового сокета /var/run/docker.sock, оказывается, можно только членам группы docker ①, поэтому после добавления пользователя rick в эту группу ② у непривилегированного пользователя появляется право ③ управлять контейнерами. Для запуска контейнера, как обычно, требуется иметь его образ, но при использовании Docker его можно скачать ④ из централизованного «хаба» docker.io, куда публикуются как официальные образы от поставщиков программного обеспечения, так и образы контейнеров, от всех желающих поделиться. Запуск контейнера производится одной командой ⑤, но сам контейнер гораздо более подготовлен к конечному использованию (листинг 9.11).

Листинг 9.11. Анализ Docker-контейнера

root@c-123:# ps o pid,netns,mntns,pidns,comm p $$
PID   NETNS   MNTNS   PIDNS   COMMAND

¹ В доме, который построил Джек. Ну, в смысле в ядре, которое написал W:[Linus Torvalds].