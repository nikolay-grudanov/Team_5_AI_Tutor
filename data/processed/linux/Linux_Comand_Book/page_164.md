---
source_image: page_164.png
page_number: 164
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.49
tokens: 6044
characters: 1162
timestamp: 2025-12-24T04:08:14.302153
finish_reason: stop
---

Она может узнать намного больше.

$ host -a www.redhat.com Trying "www.redhat.com"
->>HEADER<<- opcode: QUERY, status: NOERROR, id: 50419
    flags: gr rd ra,- QUERY: 1, ANSWER: 1,
AUTHORITY: 3, ADDITIONAL: 3
; QUESTION SECTION:
www.redhat.com.   IN ANY
; ANSWER SECTION: www.redhat.com.      196   IN A 66.187.232.50
AUTHORITY SECTION: redhat.com. 90535 IN NS ns2.redhat.com. redhat.com. 9053 5 IN NS ns3.redhat.com. redhat.com. 9053 5 IN NS nsl.redhat.com.
;; ADDITIONAL SECTION:
ns2.redhat.com. 143358 IN A 66.187.224.210 ns3.redhat.com. 143358 IN A 66.187.229.10 nsl.redhat.com. 143358 IN A 66.187.233.210

Полное обсуждение серверов имен выходит за рамки данной книги. Последний, необязательный, параметр "сервер" позволяет задавать конкретный

DNS-сервер для запроса. Вот пример запроса сервера comcast.net.
$ host www.redhat.com ns01.jdc01.pa.comcast.net
Using domain server:
Name: ns01.jdc01.pa.comcast.net
Address: 66.45.25.71#53
Aliases:
www.redhat.com has address 66.187.232.50
Чтобы вывести список всех опций, наберите просто команду host.

Полезные опции
- a    Вывести всю доступную информацию
-1    Выбрать тип запроса: A, AXFR, CNAME, HINFO, KEY,