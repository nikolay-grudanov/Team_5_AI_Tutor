---
source_image: page_247.png
page_number: 247
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.79
tokens: 6405
characters: 1322
timestamp: 2025-12-24T04:01:44.573008
finish_reason: stop
---

Удаленный сервер своими руками

Раскомментируйте строчку:

net.ipv4.ip_forward=1

Чтобы изменения вступили в силу, введите команду:

sudo sysctl -p

Нам осталось только настроить брандмауэр и можно запускать VPN-сервер.
Будем считать, что используется брандмауэр UFW (в современных дистри-
бутивах используется вместо iptables). Вы должны знать имя публичного
интерфейса, пусть это будет ens33 - для примера, в вашем случае имя пу-
бличного интерфейса будет отличаться. Выяснить чего можно командой:

ip route | grep default

Данное название нужно добавить в файл /etc/ufw/before.rules. В самое на-
чало этого файла нужно добавить строки (также укажите IP-адрес и маску
вашей подсети):

# START OPENVPN RULES
# NAT table rules
*nat
:POSTROUTING ACCEPT [0:0]
# Allow traffic from OpenVPN client to ens33
-A POSTROUTING -s 192.168.0.0/24 -o ens33 -j MASQUERADE
COMMIT
# END OPENVPN RULES

Вместо ens33 нужно указать имя вашего публичного интерфейса. Теперь от-
кройте файл nano /etc/default/ufw и найдите директиву DEFAULT_FORWARD_POLICY:

DEFAULT_FORWARD_POLICY="ACCEPT"

Откроем порт для OpenVPN:

sudo ufw allow 443/tcp

или

sudo ufw allow 1194/udp

Первую команду нужно вводить, если вы используете протокол TCP, вто-
рую, если используется протокол UDP. Чтобы изменения вступили в силу,
брандмауэр нужно перезапустить: