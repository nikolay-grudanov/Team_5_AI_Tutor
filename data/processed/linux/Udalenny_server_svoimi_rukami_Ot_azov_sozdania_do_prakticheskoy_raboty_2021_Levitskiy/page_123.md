---
source_image: page_123.png
page_number: 123
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.51
tokens: 6382
characters: 1379
timestamp: 2025-12-24T03:58:49.535047
finish_reason: stop
---

• Администратору (его IP-адрес 192.168.1.10) открываем все, что ему будет нужно.

Создайте каталог /etc/firewall, в котором мы будем хранить все необходимое для организации нашего шлюза. Сейчас создайте в ней два файла - admins.txt и black.txt. В первый нужно внести IP-адреса администрации (по одному IP-адресу в одной строке) - им будут доступны все сайты. Это может быть сотрудники IT-отдела, директор, его зам и т.д. - в общем, все вышестоящее начальство. В файл black.txt нужно внести сайты, доступ к которым нужно ограничить (тоже по одному сайту в одной строке).

# mkdir /etc/firewall
# touch /etc/firewall/admins.txt
# touch /etc/firewall/black.txt

После этого можно приступить, собственно, к настройке шлюза. Первым делом нам нужно отключить Network Manager и настроить наши интерфейсы статически. На сервере (шлюзе) Network Manager не нужен, а сетевые интерфейсы можно легко настроить с помощью /etc/network/interfaces.

Сначала введите команду:

# runlevel

Вы узнаете текущий уровень запуска:

# runlevel
N 2

Далее переходим в каталог /etc/rcX.d, где X - это уровень запуска и удаляем ссылку на network-manager. Можно также использовать команду:

# update-rc.d -f network-manager remove

Далее остановите Network Manager:

# /etc/init.d/network-manager stop

После этого отредактируйте файл /etc/network/interfaces и сконфигурируйте сетевые интерфейсы (лист. 6.2).