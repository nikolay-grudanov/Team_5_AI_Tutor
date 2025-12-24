---
source_image: page_786.png
page_number: 786
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.32
tokens: 7613
characters: 2049
timestamp: 2025-12-24T05:07:24.195180
finish_reason: stop
---

за основу второй вариант и создадим виртуальную машину из установочного ISO-образа Fedora 30 Workstation.

Предположим, что вы вошли в один из гипервизоров как суперпользователь и нашли ISO в текущем каталоге. Скопируйте образ ISO в каталог по умолчанию, применяемый командой virt-manager для хранения (/var/lib/libvirt/images):

# cp Fedora-Workstation-Live-x86_64-30-1.2.iso /var/lib/libvirt/images/

Поскольку этот каталог общий для обоих гипервизоров, можете перейти к любому из них, чтобы использовать этот образ.

Шаг 2. Проверить сетевой мост

На каждом гипервизоре должен быть сетевой мост по умолчанию с именем virbr0. Все виртуальные машины будут добавлены в этот сетевой интерфейс и автоматически присвоены IP-адресу. Данный мост по умолчанию существует благодаря виртуальной сети libvirtd. Гипервизор использует диапазон адресов от 192.168.122.2 до 192.168.122.254 для назначения виртуальным машинам. Преобразуя сетевые адреса (NAT), хост может маршрутизировать пакеты от виртуальных машин, применяющих эти частные адреса, к внешним сетевым интерфейсам.

Выполните на каждом гипервизоре следующие действия, чтобы проверить мосты:

# brctl show virbr0

bridge name     bridge id            STP enabled   interfaces
virbr0          8000.001aa0d7483e    yes           vnet0

# ip addr show virbr0

5: virbr0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue
    state UP group default
    link/ether fe:54:00:57:71:67 brd ff:ff:ff:ff:ff:ff
    inet 192.168.122.1 brd 192.168.122.255 scope global dynamic virbr0

Шаг 3. Запустить программу Virtual Machine Manager (virt-manager)

Чтобы открыть программу Virtual Machine Manager и подключить ее к гипервизору, на рабочем столе любого из гипервизоров выполните следующие действия.

1. Запустите команду virt-manager. Перейдите на экран Activities (Приложения), введите Virtual Machine Manager в поле поиска и нажмите клавишу Enter или введите команду virt-manager из командной консоли. При появлении запроса введите пароль суперпользователя. Появится программа Virtual Machine Manager.