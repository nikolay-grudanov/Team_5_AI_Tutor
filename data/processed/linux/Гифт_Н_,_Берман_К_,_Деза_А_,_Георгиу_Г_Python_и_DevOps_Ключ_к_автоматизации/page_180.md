---
source_image: page_180.png
page_number: 180
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.48
tokens: 7477
characters: 1644
timestamp: 2025-12-24T03:05:37.443360
finish_reason: stop
---

Удаление также проходит без проблем:

$ yum remove hello-world
Loaded plugins: fastestmirror, priorities
Resolving Dependencies
--> Running transaction check
---> Package hello-world.noarch 0:0.0.1-1 will be erased
--> Finished Dependency Resolution

Dependencies Resolved
Removing:
hello-world      noarch      0.0.1-1      @hello-world-noarch

Transaction Summary
Remove  1 Package

Installed size: 1.3 k
Is this ok [y/N]: y
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Erasing    : hello-world-0.0.1-1.noarch
  Verifying  : hello-world-0.0.1-1.noarch
Removed:
  hello-world.noarch 0:0.0.1-1
Complete!

Модуль http.server должен при этом вывести сообщения о каких-то действиях, демонстрирующих, что утилита yum обратилась для получения пакета hello-world:

[18/Apr/2019 03:37:24] "GET /x86_64/repo/data/repomd.xml HTTP/1.1"
[18/Apr/2019 03:37:24] "GET /noarch/repo/data/repomd.xml HTTP/1.1"
[18/Apr/2019 03:37:25] "GET /x86_64/repo/data/primary.sqlite.bz2 HTTP/1.1"
[18/Apr/2019 03:37:25] "GET /noarch/repo/data/primary.sqlite.bz2 HTTP/1.1"
[18/Apr/2019 03:56:49] "GET /noarch/hello-world-0.0.1-1.noarch.rpm HTTP/1.1"

Диспетчеризация с помощью systemd

systemd — диспетчер системы и сервисов (system and service manager) для операционной системы Linux, известный также как подсистема инициализации (init system). Он играет роль подсистемы инициализации по умолчанию во многих дистрибутивах, в частности Debian и Red Hat. Вот лишь некоторые из множества возможностей systemd:

• удобное распараллеливание;
• точки подключения и триггеры для поведения по требованию;