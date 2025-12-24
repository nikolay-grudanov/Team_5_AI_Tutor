---
source_image: page_172.png
page_number: 172
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.17
tokens: 7510
characters: 1935
timestamp: 2025-12-24T03:05:30.229660
finish_reason: stop
---

понадобится файл distributions с описанием содержимого репозитория, который выглядит вот так:

Codename: sid
Origin: example.com
Label: example.com
Architectures: amd64 source
DscIndices: Sources Release .gz .bz2
DebIndices: Packages Release . .gz .bz2
Components: main
Suite: stable
Description: example repo for hello-world package
Contents: .gz .bz2

Сохраните этот файл по адресу /opt/repo/conf/distributions. Создайте еще один каталог, в котором будет располагаться сам репозиторий:

$ mkdir /opt/repo/debian/sid

Для создания репозитория необходимо указать утилите reprepro, что нужно использовать созданный нами файл distributions, а роль базового каталога должен играть /opt/repo/debian/sid. Наконец, укажите ранее созданный бинарный файл в качестве целевого для дистрибутива sid Debian:

$ reprepro --confdir /opt/repo/conf/distributions -b /opt/repo/debian/sid \
    -C main includedeb sid /opt/binaries/python3-hello-world_0.0.1_all.deb
Exporting indices...

Эта команда создает репозиторий для дистрибутива sid Debian. Ее можно при-способить для различных дистрибутивов на основе Debian, например Ubuntu Bionic. Для этого достаточно заменить sid на bionic.

Следующий шаг после создания репозитория — добиться, чтобы он работал так, как нужно. Для промышленной эксплуатации подойдет надежный веб-сервер, например Apache или Nginx, но для тестирования примера мы воспользуемся модулем http.server Python. Перейдите в каталог, содержащий репозиторий, и запустите веб-сервер:

$ cd /opt/repo/debian/sid
$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

Необходимо указать системе управления пакетами Debian apt (Aptitude) на новое местоположение пакетов. Соответствующая конфигурация представляет собой простой файл, содержащий всего одну строку со ссылкой на URL и компоненты нашего репозитория. Создайте файл /etc/apt/sources.list.d/hello-world.list. Его содержимое должно выглядеть так: