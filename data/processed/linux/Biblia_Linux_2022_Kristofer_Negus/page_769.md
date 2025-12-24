---
source_image: page_769.png
page_number: 769
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.22
tokens: 7637
characters: 2371
timestamp: 2025-12-24T05:07:00.443111
finish_reason: stop
---

Дополнительные сведения о создании и использовании Dockerfile для создания образов контейнеров см. в справочнике Dockerfile (docs.docker.com/engine/reference/builder/). Чтобы узнать больше о вариантах построения образов контейнеров, обратитесь к справочным страницам команды podman (man podman build).

Добавление тегов и загрузка образа в реестр

До сих пор я показывал, как создавать образ контейнера и запускать его в вашей локальной системе. Чтобы сделать образ доступным для других пользователей в других системах, необходимо добавить его в реестр контейнеров.

Следуйте дальнейшим инструкциям, чтобы пометить образ в локальной системе и отправить его в удаленный реестр контейнеров.

Чтобы опробовать простой реестр в локальной системе, установите дистрибутив docker в систему Fedora или RHEL 7. Можете также завести учетные записи в публичных реестрах контейнеров, например в Quay.io и Docker Hub. Как бесплатные пробные версии, так и подписки доступны на странице Quay.io (quay.io/plans/). Вдобавок можете настроить и запустить собственный поддерживаемый реестр контейнеров, например Red Hat Quay (www.openshift.com/products/quay).

Чтобы начать работу, установите пакет docker-distribution в локальную систему, а затем пометьте и вставьте в него образ.

1. Установите дистрибутив docker. В системах RHEL 7 или Fedora последней версии установите и запустите дистрибутив docker:

# yum install docker-distribution -y
# systemctl start docker-distribution
# systemctl enable docker-distribution
# systemctl status docker-distribution
• docker-distribution.service-v2 Registry server for Docker
Loaded: loaded (/usr/lib/systemd/system/docker-distribution.service; enabled; vendor pres>
Active: active (running) since Wed 2020-01-01...

2. Откройте порт реестра. Чтобы иметь возможность загружать и устанавливать образы контейнеров из других хост-систем, необходимо открыть TCP-порт 5000 на брандмауэре:

# firewall-cmd --zone=public --add-port=5000/tcp --permanent

3. Установите тег к образу. Пометив локальный образ, определите местоположение реестра, в котором образ будет храниться. Замените идентификатор образа и host.example.com идентификатором образа и именем хоста или IP-адресом, чтобы пометить изображение:

# podman images | grep vsftpd
localhost/vsftpd latest aa0274872f23 2 hours ago 607 MB
# podman tag aa0274872f23
host.example.com:5000/myvsftpd:v1.0