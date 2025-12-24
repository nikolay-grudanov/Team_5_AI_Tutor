---
source_image: page_163.png
page_number: 163
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.64
tokens: 6037
characters: 1243
timestamp: 2025-12-24T04:08:14.303344
finish_reason: stop
---

carrier:O
collisions:0 txqueuelen:10 0
RX bytes:2320504831 (2213.0 Mb)
TX bytes: 152785756 (145.7 Mb)
Interrupt:11 Base address:0x6000
Выходные данные включают в себя ваш МАС-адрес (00:50:BA:48:4F:BA), ваш IP-адрес (192.168.0. 10), вашу сетевую маску (255.255.255.0) и различную другую информацию. Для того чтобы вывести список всех существующих интерфейсов, выполните следующую команду.

$ ifconfig -a

Если у вас есть опыт работы с сетевыми службами, изучите man-страницу команды ifconfig для того, чтобы узнать детали.

Поиск хоста
host        Исказать имена хостов, IP-адреса и информацию DNS
whois       Исказать владельцев Интернет-доменов
ping        Проверить, доступен ли удаленный хост
traceroute  Вывести сетевой путь к удаленному хосту

При работе с удаленными компьютерами вы, возможно, захотите узнать о них больше. Кто является их владельцем? Какие у них IP-адреса? Где они расположены в сети?

host [опции] имя [сервер]    bind-utils
/usr/bin    stdin stdout -file --opt --help -version

Команда host осуществляет поиск имени хоста или IP-адреса удаленной машины, запрашивая DNS.

$ host www.redhat.com
www.redhat.com has address 66.187.232.50
$ host 66.187.232.50
50.232.187.66.in-addr.arpa domain name pointer www.redhat.com.