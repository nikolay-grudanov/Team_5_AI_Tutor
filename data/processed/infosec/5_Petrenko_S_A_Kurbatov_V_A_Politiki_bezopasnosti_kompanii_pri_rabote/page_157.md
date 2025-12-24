---
source_image: page_157.png
page_number: 157
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.61
tokens: 11839
characters: 1744
timestamp: 2025-12-23T23:41:32.118432
finish_reason: stop
---

permit tcp host 90.90.1.2 host 90.90.1.1 eq 79
deny ip any 70.70.70.16 0.0.0.15
permit tcp any 70.70.70.0 0.0.0.255 established
permit udp any 70.70.70.0 0.0.0.255
permit icmp any 70.70.70.0 0.0.0.255 source-quench
deny ip any any

Список контроля доступа для исходящего трафика. Для предупреждения организации атак типа «отказ в обслуживании» с подменой адресов разрешен доступ в Интернет только с IP-адресов компании. Весь трафик, направленный на «опасные» порты — NetBIOS, SNMP, TFTP, syslog, тоже удаляется:

no ip access-list extended Egress
ip access-list extended Egress
deny udp any any range 161 162
deny udp any any eq 69
deny tcp any any range 135 139
deny udp any any range 135 139
deny tcp any any eq 445
deny udp any any eq 514
permit tcp 70.70.70.0 0.0.0.255 any
permit udp 70.70.70.0 0.0.0.255 any
permit icmp any 70.70.70.0 0.0.0.255 source-quench
deny ip any any

Применение списков контроля доступа:

interface hssi2/0
ip access-group Ingress in
no ip proxy-arp
ip accounting access-violations
interface Fa0/0
ip access-group Egress in
no cdp enable
no ip proxy-arp
ip accounting access-violations

4.3.3. Настройки внешних межсетевых экранов
Внешние межсетевые экраны позволяют построить эффективный периметр защиты компании от угроз из Интернета. Политика безопасности внешних межсетевых экранов основана на бизнес-требованиях и согласована с общей политикой информационной безопасности компании. В качестве внешнего межсетевого экрана выбран Check Point Firewall-1 NG FP3, выполняющийся на аппаратной платформе Nokia IP530 с операционной системой IPSO v.3.6. В табл. 4.2 описаны все важные компоненты сети компании, подлежащие защите с помощью указанного межсетевого экрана.
Таблица 4.2. Компоненты сети, подлежащие защите