---
source_image: page_171.png
page_number: 171
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.03
tokens: 7563
characters: 2172
timestamp: 2025-12-24T03:05:29.848316
finish_reason: stop
---

Генерация двоичного файла

Для генерации двоичного файла используйте утилиту командной строки debuild. В своем примере проекта мы не станем подписывать пакет (для создания цифровой подписи требуется GPG-ключ), а в документации debuild есть пример, позволяющий пропустить этап подписывания. Сценарий запускается изнутри дерева каталогов исходного кода для сборки только двоичного пакета. Вот команда, подходящая для проекта hello-world:

$ debuild -i -us -uc -b
...
dpkg-deb: building package 'python3-hello-world' in '../python3-hello-world_0.0.1_all.deb'.
...
 dpkg-genbuildinfo --build=binary
 dpkg-genchanges --build=binary >../hello-world_0.0.1_amd64.changes
dpkg-genchanges: info: binary-only upload (no source code included)
 dpkg-source -i --after-build hello-world-debian
dpkg-buildpackage: info: binary-only upload (no source code included)
Now running lintian hello-world_0.0.1_amd64.changes ...
E: hello-world changes: bad-distribution-in-changes-file stable
Finished running lintian.

Теперь в верхнем каталоге должен появиться файл python3-hello-world_0.0.1_all.deb. При вызове lintian (линтера Debian для создания пакетов) в самом конце возникает сообщение о некорректном дистрибутиве. Об этом волноваться не стоит, ведь мы и не ориентировались на какой-то конкретный дистрибутив (например, Debian Buster), а собирали пакет, который можно было бы установить в любом дистрибутиве на основе Debian, совместимом со всеми зависимостями (в данном случае только Python 3).

Репозитории Debian

Существует множество утилит для автоматизации работы с репозиториями Debian, но совсем не помешает разобраться в схеме их создания (Альфредо даже помогал разрабатывать один репозиторий (https://oreil.ly/hJMgY), предназначенный как для RPM, так и для Debian). Убедитесь, что созданный нами ранее бинарный пакет находится в нужном месте:

$ mkdir /opt/binaries
$ cp python3-hello-world_0.0.1_all.deb /opt/binaries/

Для этого раздела необходимо, чтобы была установлена утилита reprepro:

$ sudo apt-get install reprepro

Создайте новый каталог где-нибудь в системе для хранения пакетов. В данном примере его роль играет каталог /opt/repo. Для основных настроек репозитория