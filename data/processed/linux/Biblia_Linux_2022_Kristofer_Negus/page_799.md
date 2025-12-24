---
source_image: page_799.png
page_number: 799
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.54
tokens: 7432
characters: 1707
timestamp: 2025-12-24T05:07:40.342267
finish_reason: stop
---

$ sudo cat /var/lib/cloud/instances/FedoraWS01/user-data.txt
#cloud-config
password: cloudpass
chpasswd: {expire: False}

Базовая настройка облака выполняется в файле /etc/cloud/cloud.cfg. В примере видно, что учетная запись суперпользователя по умолчанию отключена. В нижней части файла вы видите, что пользователь с именем fedora — это пользователь по умолчанию, он имеет права sudo, и не требует вводить пароль:

$ sudo cat /etc/cloud/cloud.cfg
users:
  - default
disable_root: 1
...
system_info:
  default_user:
    name: fedora0
    lock_passwd: true
    gecos: Fedora Cloud User
    groups: [wheel, adm, systemd-journal]
    sudo: ["ALL=(ALL) NOPASSWD:ALL"]
    shell: /bin/bash
distro: fedora
paths:
  cloud_dir: /var/lib/cloud
  templates_dir: /etc/cloud/templates
ssh_svcname: sshd

# vim:syntax=yaml

В файле cloud.cfg вы можете увидеть и другую информацию. Например, какие модули cloud_init_module запускаются во время инициализации (те, которые устанавливают имя хоста или запускают ведение журнала rsyslog). Вы увидите модули cloud_config_modules, которые устанавливают локальный и часовой пояс и запускают дополнительные инструменты настройки, такие как Chef и Puppet.

Поскольку репозитории yum подключены, вы можете установить любые пакеты, доступные из репозиториев Fedora, при условии, что у вас есть доступное сетевое подключение (DHCP должен был назначить адреса виртуальной машине по умолчанию).

Копирование облачного образа

Если вас устраивает созданный облачный образ, сохраните его копию для последующего запуска, сделав клон из двух образов — облака и образа данных. Чтобы создать клон запущенного облачного экземпляра с помощью утилиты virt-manager, выполните следующие действия.