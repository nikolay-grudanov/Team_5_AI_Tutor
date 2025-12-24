---
source_image: page_354.png
page_number: 354
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.69
tokens: 7496
characters: 1906
timestamp: 2025-12-24T04:42:20.964281
finish_reason: stop
---

ко прямое использование механизмов и базовых утилит, как это иллюстрируется в предыдущем разделе, требует выполнения колоссального количества типовых действий для организации каждого контейнера, что и привело к созданию специализированных систем управления контейнерами, таких как W:[Docker (software)] или W:[LXC] (в том числе W:[OpenVZ], хотя она использует свои механизмы изоляции и поэтому требует специально модифицированного ядра).

Более того, изначальная разрозненность систем контейнеризации привела в конце концов к созданию инициативы OCI (W:[Open Container Initiative]), под эгидой которой была согласована спецификация «исполнителя» контейнеров (runtime) и спецификация формата образов (image) контейнеров, которые должен понимать это «исполнитель». В Linux обе OCI-спецификации реализуются утилитой runc(8), которая, в свою очередь, основывается на сервисах ядра Linux, включая механизмы изоляции, рассмотренные выше. Сами же системы контейнеризации, например Docker, используют утилиту runc(8) для непосредственного запуска контейнеров.

Дистриб 9.9. OCI исполнитель runc и запуск OCI-контейнера:

1 rick@ubuntu:~$ runc spec
rick@ubuntu:~$ ls
config.json
rick@ubuntu:~$ sed -n '/root.*{/,/}/p' config.json
    "root": {
        "path": "rootfs",
        "readonly": true
    },
2 rick@ubuntu:~$ sudo debootstrap --variant=minbase xential rootfs
I: Retrieving InRelease
I: Checking Release signature
I: Valid Release signature (key id 790BC7277767219C42C86F933B4FE6ACC0B21F32)
I: Retrieving Packages
I: Validating Packages
I: Base system installed successfully.
rick@ubuntu:~$ ps o pid,netns,mntns,pidns,comm p $$
    PID   NETNS   MNTNS   PIDNS COMMAND
10149 4026531992 4026531840 4026531836 bash

1 rick@ubuntu:~ $ sudo runc run c-132
# ps o pid,netns,mntns,pidns,comm p $$
    PID   NETNS   MNTNS   PIDNS COMMAND
1 4026532375 4026532251 4026532373 sh
# ps axf
    PID TTY STAT TIME COMMAND