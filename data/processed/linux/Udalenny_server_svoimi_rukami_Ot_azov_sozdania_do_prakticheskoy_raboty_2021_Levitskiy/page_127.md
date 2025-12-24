---
source_image: page_127.png
page_number: 127
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.31
tokens: 6457
characters: 1251
timestamp: 2025-12-24T03:59:06.207375
finish_reason: stop
---

Удаленный сервер своими руками

$ip -A FORWARD -p udp -s 192.168.1.10 ! -d $LOCAL_NET -m multiport --dports 53 -j ACCEPT
$ip -A FORWARD -p udp -d 192.168.1.10 ! -s $LOCAL_NET -m multiport --sports 53 -j ACCEPT

# Резрешаем ICQ только администраторам
i=0
for i in "${admins[@]}"
do
    $ip -A FORWARD -p tcp -d $i --sport 5190 -j ACCEPT
    $ip -A FORWARD -p tcp -s $i --dport 5190 -j ACCEPT
done

# Резрешаем избранным (список admins) доступ к сайтам из черного списка
j=0
for j in "${blacklist[@]}"
do
    i=0
    for i in "${admins[@]}"
    do
        $ip -A FORWARD -d $i -s $j -j ACCEPT
    done
done

# Всем остальным запрещаем доступ к сайтам из списка blacklist
i=0
for i in "${blacklist[@]}"
do
    $ip -A FORWARD -s $i -j DROP
done

# Разрешаем транзит некоторых пакетов (80, 443 и 53)
$ip -A FORWARD -p tcp -s $LOCAL_NET ! -d $LOCAL_NET -m multiport --dports 80,53,443 -j ACCEPT
$ip -A FORWARD -p tcp -d $LOCAL_NET ! -s $LOCAL_NET -m multiport --sports 80,53,443 -j ACCEPT
$ip -A FORWARD -p udp -s $LOCAL_NET ! -d $LOCAL_NET -m multiport --dports 53 -j ACCEPT
$ip -A FORWARD -p udp -d $LOCAL_NET ! -s $LOCAL_NET -m multiport --sports 53 -j ACCEPT

После этого нужно обеспечить автоматический запуск нашего сценария /etc/firewall/firewall.sh.