---
source_image: page_405.png
page_number: 405
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.91
tokens: 7524
characters: 1923
timestamp: 2025-12-24T04:56:40.469225
finish_reason: stop
---

Перейдите к кнопке OK с помощью клавиши Tab и нажмите клавишу Пробел. Затем нажмите кнопку Quit (Выйти), чтобы выйти из утилиты.

Сетевые файлы конфигурации

Вне зависимости от того, что применяется для изменения сетевых настроек — NetworkManager или nmtui, большинство одинаковых файлов конфигурации обновляется. В системах Fedora и RHEL сетевые интерфейсы и пользовательские маршруты задаются в файлах каталога /etc/sysconfig/network-scripts.

Откройте файл /usr/share/doc/initscripts/sysconfig.txt, чтобы увидеть описания сетевых конфигурационных файлов (доступны в пакете initscripts).

Необходимо быть осторожными, так как программа NetworkManager считает, что она контролирует файлы в каталоге сетевых скриптов. Поэтому имейте в виду: если вы вручную зададите адреса в интерфейсе, который программа NetworkManager использует для службы DHCP, она может перезаписать изменения, внесенные вручную в файл.

Файлы сетевого интерфейса

Файлы конфигурации для каждого проводного, беспроводного, ISDN, коммутируемого или другого типа сетевого интерфейса представлены файлами в каталоге /etc/sysconfig/network-scripts, которые начинаются с ifcfg-interface. Обратите внимание на то, что слово interface заменяется именем сетевого интерфейса.

Если установить сетевой интерфейс проводной карты NIC как enp4s0, то вот так будет выглядеть пример файла ifcfg-enp4s0 для этого интерфейса, настроенного на использование службы DHCP:

DEVICE=enp4s0
TYPE=Ethernet
BOOTPROTO=dhcp
ONBOOT=yes
DEFROUTE=yes
UUID=f16259c2-f350-4d78-a539-604c3f95998c
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
NAME="System enp4s0"
PEERDNS=yes
PEERROUTES=yes
IPV6_PEERDNS=yes
IPV6_PEERROUTES=yes

В этом примере файла ifcfg-enp4s0 первые две строчки устанавливают имя устройства и тип интерфейса для подключения к сетям Ethernet. Переменная BOOTPROTO имеет значение dhcp, что заставляет ее запрашивать адреса