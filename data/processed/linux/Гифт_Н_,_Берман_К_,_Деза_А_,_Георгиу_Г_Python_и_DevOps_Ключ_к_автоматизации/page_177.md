---
source_image: page_177.png
page_number: 177
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.83
tokens: 7543
characters: 1750
timestamp: 2025-12-24T03:05:37.444359
finish_reason: stop
---

running install_scripts
writing list of installed files to 'INSTALLED_FILES'
Processing files: hello-world-0.0.1-1.noarch
Provides: hello-world = 0.0.1-1
Wrote: /opt/repo/centos/SRPMS/hello-world-0.0.1-1.src.rpm
Wrote: /opt/repo/centos/RPMS/noarch/hello-world-0.0.1-1.noarch.rpm
Executing(%clean): /bin/sh -e /var/tmp/rpm-tmp.gcIJgT
+ umask 022
+ cd /opt/repo/centos//BUILD
+ cd hello-world-0.0.1
+ rm -rf /opt/repo/centos/BUILDROOT/hello-world-0.0.1-1.x86_64
+ exit 0

В структуре каталогов в /opt/repo/centos появится множество новых файлов, но нас интересует только один, с расширением noarch.rpm:

$ tree /opt/repo/centos/RPMS
/opt/repo/centos/RPMS
└── noarch
    └── hello-world-0.0.1-1.noarch.rpm

1 directory, 1 file

Этот файл представляет собой подходящий для установки пакет RPM! Утилита сгенерировала и другие полезные пакеты, которые также можно опубликовать (загляните, например, в /opt/repo/centos/SRPMS).

Репозитории RPM

Для создания репозитория RPM мы возьмем утилиту командной строки createrepo. Она создает метаданные репозитория (метаданные RPM в формате XML) из бинарных файлов, найденных в указанном каталоге. В этом разделе мы создадим (и разместим в репозитории) бинарный файл типа noarch:

$ sudo yum install createrepo

Можете создать репозиторий там же, где мы генерировали пакет noarch, или воспользоваться новым (пустым) каталогом. При необходимости создайте новые бинарные файлы. А затем скопируйте пакет:

$ mkdir -p /var/www/repos/centos
$ cp -r /opt/repo/centos/RPMS/noarch /var/www/repos/centos

Запустите утилиту createrepo для создания метаданных:

$ createrepo -v /var/www/repos/centos/noarch
Spawning worker 0 with 1 pkgs
Worker 0: reading hello-world-0.0.1-1.noarch.rpm
Workers Finished
Saving Primary metadata