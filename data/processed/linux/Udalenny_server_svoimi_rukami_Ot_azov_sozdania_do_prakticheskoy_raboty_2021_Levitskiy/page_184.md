---
source_image: page_184.png
page_number: 184
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.66
tokens: 6400
characters: 1151
timestamp: 2025-12-24T04:00:17.036690
finish_reason: stop
---

Проверим, работает ли наш DNS-сервер. В /etc/resolv.conf на DNS-сервере добавьте строку:

nameserver 127.0.0.1

Если вы по каким-то причинам не отключили NetworkManager, то он при следующей перезагрузке перезапишет этот файл. Понятно, что NetworkManager получит IP-адрес DNS-сервера от DHCP-сервера, но пока вы еще не настроили DHCP-сервер, тогда можете запретить изменение файла /etc/resolv.conf:

# chattr +i /etc/resolv.conf

После этого перезапустите сеть или компьютер. После этого введите команду:

nslookup mail.ru

Вывод будет таким:

Server: 127.0.0.1
Address: 127.0.0.1#53

Non-authoritative answer:
Name: mail.ru
Address: 217.69.139.202
Name: mail.ru
Address: 217.69.139.200
Name: mail.ru
Address: 94.100.180.201
Name: mail.ru
Address: 94.100.180.200

Как видите, ответ пришел от нашего сервера 127.0.0.1. Мы убедились, что наш DNS-сервер работает, значит, можно настроить DHCP-сервер, чтобы он «раздавал» всем вашим клиентам IP-адрес только что настроенного DNS-сервера. Конечно, прописывать в настройках DHCP-сервера нужно не IP-адрес 127.0.0.1, а IP-адрес сервера, который вы можете получить командой ifconfig, запущенной на DNS-сервере.