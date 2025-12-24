---
source_image: page_178.png
page_number: 178
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.06
tokens: 7513
characters: 1719
timestamp: 2025-12-24T03:05:37.052335
finish_reason: stop
---

Saving file lists metadata
Saving other metadata
Generating sqlite DBs
Starting other db creation: Thu Apr 18 09:13:35 2019
Ending other db creation: Thu Apr 18 09:13:35 2019
Starting filelists db creation: Thu Apr 18 09:13:35 2019
Ending filelists db creation: Thu Apr 18 09:13:35 2019
Starting primary db creation: Thu Apr 18 09:13:35 2019
Ending primary db creation: Thu Apr 18 09:13:35 2019
Sqlite DBs complete

И хотя пакета x86_64 не существует, повторите вызов утилиты createrepo для нового каталога, чтобы не получать предупреждений yum в дальнейшем:

$ mkdir /var/www/repos/centos/x86_64
$ createrepo -v /var/www/repos/centos/x86_64

Для выдачи данных из этого каталога по HTTP давайте воспользуемся модулем http.server:

$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

Для доступа к этому репозиторию yum понадобятся настройки в файле repo. Создайте его — /etc/yum.repos.d/hello-world.repo. Он должен выглядеть вот так:

[hello-world]
name=hello-world example repo for noarch packages
baseurl=http://0.0.0.0:8000/$basearch
enabled=1
gpgcheck=0
type=rpm-md
priority=1

[hello-world-noarch]
name=hello-world example repo for noarch packages
baseurl=http://0.0.0.0:8000/noarch
enabled=1
gpgcheck=0
type=rpm-md
priority=1

Обратите внимание на то, что значение gpgcheck равно 0. Это значит, что мы не подписывали никаких пакетов и утилита yum не должна пытаться проверить подписи, из-за чего в этом примере могла бы возникнуть ошибка. Теперь можно выполнить поиск пакета, в ходе которого мы получим описание в виде части выводимых данных:

$ yum --enablerepo=hello-world search hello-world
Loaded plugins: fastestmirror, priorities
Loading mirror speeds from cached hostfile