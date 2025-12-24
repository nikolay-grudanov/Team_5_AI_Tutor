---
source_image: page_125.png
page_number: 125
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.36
tokens: 6372
characters: 1014
timestamp: 2025-12-24T03:58:59.459784
finish_reason: stop
---

# Внешний IP-адрес и внешний интерфейс
WAN_IP1=88.99.88.99
WAN_IFACE1=eth0

# Внутренний адрес сервера и внутренний интерфейс
LAN_IP=192.168.1.1
LAN_IFACE=eth1

# Внутренняя сеть
LOCAL_NET=192.168.1.0/24

# loopback
LO_IFACE=lo
LO_IP=127.0.0.1

# Путь к iptables
ip=/sbin/iptables

# Черный список
blacklist=( $(cat "/etc/firewall/black.txt") )
admins=( $(cat "/etc/firewall/admins.txt") )

# Очищаем все таблицы iptables
$ip -F -t filter
$ip -F -t nat
$ip -F -t mangle
$ip -F

# Правила по умолчанию: запрещаем все, что явно не разрешено
$ip -P INPUT DROP
$ip -P OUTPUT DROP
$ip -P FORWARD DROP

# Превращаем компьютер в шлюз, на всякий случай, если мы забыли сделать это раньше
echo 1 > /proc/sys/net/ipv4/ip_forward

# Включаем NAT, чтобы локальные узлы могли получать доступ к Интернету
$ip -t nat -A POSTROUTING -o $WAN_IFACE1 -s $LOCAL_NET ! -d $LOCAL_NET -j SNAT --to-source $WAN_IP1

# Отбрасываем INVALID-пакеты
$ip -A INPUT -m state --state INVALID -j DROP
$ip -A FORWARD -m state --state INVALID -j DROP