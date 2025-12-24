---
source_image: page_802.png
page_number: 802
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.12
tokens: 7750
characters: 2356
timestamp: 2025-12-24T05:08:00.761119
finish_reason: stop
---

ZBb3S1j7vK2WymOcwEoWekhbZHBAyYeqXKYQQjUB2E2Mr6qMkmrjQBx6ypxbz+VwADNCwegY5RCUoNjrN43GVu6nSOxhFf7hv6dtCjvos0vtt0979YS3UcEyrobpNzreGSJ8FMPMRFMWwg68Jz5hOMCIE1Illdhp0DvQVbTNsn/STx07ZwSYV6kfDj0szvdoDDCyh8mPNC1kIDhf/qu/Zn1kxQ9xfecQ+SUi+2IwN69o1fNpexJPFr+Bwjkwcrk58C6uowG5eNSgnuu7GMUkT root@host2.example.com

Из примера видно, что wsmith — это пользователь по умолчанию. Запись gecos обычно является полным именем пользователя, применяемым в пятом поле файла /etc/passwd. Пароль для этого пользователя заблокирован. Но, поскольку запись ssh-rsa из моей учетной записи суперпользователя на host2.example.com предоставляет ssh-authorized-keys для пользователя, я могу войти в облачный образ как пользователь wsmith, применив ключи ssh без ввода пароля (при условии, что мой закрытый ключ связан с этим открытым ключом).

Добавление программного обеспечения с помощью службы cloud-init

Вы не ограничены программным обеспечением, которое имеется в вашем облачном образе. В файле пользовательских данных вы можете определить репозитории YUM (в Fedora и RHEL) или apt (в Ubuntu или Debian), а затем выделить любые пакеты, которые хотите установить при запуске облачного образа.

В следующем примере показано, как могут выглядеть записи в файле user-data при добавлении репозитория YUM (для систем Fedora или RHEL) в облачный образ и последующей установке пакетов из этого или любого другого подключенного репозитория:

myownrepo:
    baseurl: http://myrepo.example.com/pub/myrepo/
    enabled: true
    gpgcheck: true
    gpgkey: file:///etc/pki/rpm-gpg/RPM-GPG-KEY-MYREPO
    name: My personal software repository
packages:
    - nmap
    - mycoolcmd
    - [libmystuff, 3.10.1-2.fc21.noarch]

Здесь новый репозиторий yum создается в файле /etc/yum.repos.d/myownrepo.repo. Для проверки правильности установленных пакетов используется служба gpgkey и включается проверка GPG. После этого устанавливаются пакет nmap (который находится в стандартном yum-репозитории Fedora), затем пакет mycoolcmd (из моего частного репозитория) и конкретная версия пакета libmystuff.

Настройка репозиториев программного обеспечения apt для Ubuntu выполняется немного иначе. Отказоустойчивые первичные и защитные зеркала пакетов apt настраиваются по умолчанию (в файле cloud.cfg на образе) вместе с параметрами, позволяющими образу при запуске в облаке Amazon EC2 искать пакеты в ближай-