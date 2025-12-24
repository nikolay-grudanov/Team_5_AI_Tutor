---
source_image: page_126.png
page_number: 126
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.87
tokens: 6656
characters: 1665
timestamp: 2025-12-24T03:59:14.626517
finish_reason: stop
---

# Разрешаем трафик через loopback
$ip -A INPUT -p all -i $LO_IFACE -j ACCEPT
$ip -A OUTPUT -p all -o $LO_IFACE -j ACCEPT

# Разрешаем трафик через внутренний адаптер
# Между сервером (шлюзом) и локальной сетью разрешаем все
$ip -A INPUT -p all -i $LAN_IFACE -s $LOCAL_NET --match state --state NEW,ESTABLISHED -j ACCEPT

# Разрешаем исходящие новые и уже установленные соединения
# в внутреннюю сеть с адаптера локальной сети
$ip -A OUTPUT -p all -o $LAN_IFACE -d $LOCAL_NET --match state --state NEW,ESTABLISHED -j ACCEPT

# Разрешаем новые и уже установленные соединения извне (с внешней сети)
# к портам 80 (веб-сервер) и 22 (ssh):
$ip -A INPUT -p tcp -i $WAN_IFACE1 -m multiport --dports 80,22,25,110 --match state --state NEW,ESTABLISHED -j ACCEPT
$ip -A OUTPUT -p tcp -o $WAN_IFACE1 -m multiport --sports 80,22,25,110 --match state --state ESTABLISHED,RELATED -j ACCEPT

# Разрешаем выход с сервера во внешнюю сеть, но только на определенные порты
# Разрешаем порты 80 (HTTP), 443 (SSL) и 53 (DNS)
$ip -A INPUT -i $WAN_IFACE1 -p tcp -m multiport --sports 80,53,443 -j ACCEPT
$ip -A OUTPUT -o $WAN_IFACE1 -p tcp -m multiport --dports 80,53,443 -j ACCEPT
$ip -A INPUT -i $WAN_IFACE1 -p udp -m multiport --sports 53 -j ACCEPT
$ip -A OUTPUT -o $WAN_IFACE1 -p udp -m multiport --dports 53 -j ACCEPT

# Открываем админу (192.168.1.10) доступ ко всему, что будет нужно
# Просмотрите список портов и откройте то, что вам будет нужно
# tcp
$ip -A FORWARD -p tcp -s 192.168.1.10 ! -d $LOCAL_NET -m multiport --dports 80,53,443,22,25,110,5190 -j ACCEPT
$ip -A FORWARD -p tcp -d 192.168.1.10 ! -s $LOCAL_NET -m multiport --sports 80,53,443,22,25,110,5190 -j ACCEPT

# udp