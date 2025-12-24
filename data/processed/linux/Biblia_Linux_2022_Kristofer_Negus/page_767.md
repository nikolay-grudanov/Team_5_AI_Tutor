---
source_image: page_767.png
page_number: 767
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.45
tokens: 7487
characters: 1864
timestamp: 2025-12-24T05:06:41.021201
finish_reason: stop
---

5. Запустите контейнер, чтобы проверить, работает ли он. Для этого можно использовать либо имя контейнера (myproject), либо идентификатор его образа (6837ec3a37a241):

# podman run 6837ec3a37a241
The Container Works!

Создание FTP-контейнера из веб-сервиса GitHub

Следующие шаги позволяют загрузить программное обеспечение, необходимое для создания службы vsftpd, в контейнер из веб-сервиса GitHub. Затем мы рассмотрим, как настроить и запустить этот контейнер.

1. Если у вас еще нет пакета git, установите его в своей локальной системе:

# yum install git -y

2. Начнем с проекта vsftpd container-images на GitHub. Создайте копию этого программного обеспечения в локальном каталоге следующим образом:

# git clone https://github.com/container-images/vsftpd.git
# cd vsftpd
# ls
default-conf/    Dockerfile    LICENSE    Makefile    README.md
root/             s2i/         tests/

3. Изменяйте файлы по мере необходимости. В частности, перейдите в Dockerfile и используйте последний доступный образ Fedora. Опуская :tag в конце имени изображения, следует искать версию этого изображения, которая включает в себя тег :latest — специальный тег, идентифицирующий последнюю доступную версию этого образа. Например, измените строку FROM в начале так, чтобы она выглядела следующим образом:

FROM registry.fedoraproject.org/fedora

4. Из каталога vsftpd используйте команду docker или podman для создания образа контейнера, например:

# podman build -t vsftpd .
STEP 1: FROM registry.fedoraproject.org/fedora:31
Getting image source signatures
Copying blob c0a89efa8873 done
Copying config aaaa3e1d6a done
Writing manifest to image destination
Storing signatures
STEP 2: ENV SUMMARY="Very Secure Ftp Daemon" ...
STEP 3: LABEL maintainer="Dominika Hodovska <dhodovsk@redhat.com>"
...
STEP 4: RUN dnf install -y vsftpd && dnf clean all
        && mkdir /home/vsftpd
...