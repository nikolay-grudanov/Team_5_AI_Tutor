---
source_image: page_748.png
page_number: 748
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.52
tokens: 7587
characters: 2130
timestamp: 2025-12-24T05:06:16.683712
finish_reason: stop
---

- j действие. Выполняет действие, если правило подошло, например:
# iptables -A INPUT -s 10.140.67.25 -j DROP

- d IP-адрес. Назначает указанное правило для применения к назначенному IP-адресу, например:
# iptables -A OUTPUT -d 10.140.67.25 -j REJECT

- s IP-адрес. Назначает указанное правило для применения к назначенному IP-адресу, например:
# iptables -A INPUT -s 10.140.67.24 -j ACCEPT

- p протокол. Назначает указанное правило для применения к указанному протоколу. Например, здесь отбрасываются входящие запросы ping (icmp):
# iptables -A INPUT -p icmp -j DROP

--dport port#. Назначает указанное правило для применения к определенным пакетам протокола, поступающим в назначенный параметр port#, например:
# iptables -A INPUT -p tcp --dport 22 -j DROP

--sport port#. Назначает указанное правило для применения к определенным пакетам протокола, выходящим из назначенного параметра port#, например:
# iptables -A OUTPUT -p tcp --sport 22 -j ACCEPT

-m state --state состояние_соединения. Назначает указанное правило для применения к назначенному состоянию (состояниям) соединения, например:
# iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

Чтобы увидеть, как работают параметры iptables, рассмотрим следующий пример. У вас есть сервер Linux (Host-A) по IP-адресу 10.140.67.23. В вашей сети имеется еще два сервера Linux. Один из них — Host-B по IP-адресу 10.140.67.22, а другой — Host-C по IP-адресу 10.140.67.25. Вам необходимо выполнить следующее:

- разрешить полный доступ с сервера Host-C к серверу Host-A;
- блокировать удаленные подключения входа с помощью службы ssh от Host-B к Host-A.

Настройка политики DROP. В следующем коде показаны политики брандмауэра сервера Host-A по умолчанию. Здесь брандмауэр открыт полностью, без каких-либо ограничений. Никаких правил не установлено, и все политики настроены на режим ACCEPT:

# iptables -vnL

Chain INPUT (policy ACCEPT)
target     prot opt source                 destination

Chain FORWARD (policy ACCEPT)
target     prot opt source                 destination

Chain OUTPUT (policy ACCEPT)
target     prot opt source                 destination