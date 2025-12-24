---
source_image: page_234.png
page_number: 234
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.20
tokens: 6405
characters: 1282
timestamp: 2025-12-24T04:01:16.785333
finish_reason: stop
---

### 7: Удаляем фрагментированные пакеты ###
/sbin/iptables -t mangle -A PREROUTING -f -j DROP

### 8: Ограничиваем соединения по IP ###
/sbin/iptables -A INPUT -p tcp -m connlimit --connlimit-above 111 -j REJECT --reject-with tcp-reset

### 9: Ограничиваем RST-пакеты ###
/sbin/iptables -A INPUT -p tcp --tcp-flags RST RST -m limit --limit 2/s --limit-burst 2 -j ACCEPT
/sbin/iptables -A INPUT -p tcp --tcp-flags RST RST -j DROP

### 10: Ограничиваем число TCP-соединений в секунду с одного IP ###
/sbin/iptables -A INPUT -p tcp -m conntrack --ctstate NEW -m limit --limit 60/s --limit-burst 20 -j ACCEPT
/sbin/iptables -A INPUT -p tcp -m conntrack --ctstate NEW -j DROP

14.2.8. Защита от брутфорса SSH

С помощью правил iptables можно защититься от брутфорса (перебора пароля) SSH:

/sbin/iptables -A INPUT -p tcp --dport ssh -m conntrack --ctstate NEW -m recent --set
/sbin/iptables -A INPUT -p tcp --dport ssh -m conntrack --ctstate NEW -m recent --update --seconds 60 --hitcount 10 -j DROP

14.2.9. Запрет сканирования портов

Также iptables позволяет защититься от сканирования портов:

/sbin/iptables -N port-scanning
/sbin/iptables -A port-scanning -p tcp --tcp-flags SYN,ACK,FIN,RST RST -m limit --limit 1/s --limit-burst 2 -j RETURN
/sbin/iptables -A port-scanning -j DROP