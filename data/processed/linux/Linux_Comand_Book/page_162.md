---
source_image: page_162.png
page_number: 162
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.41
tokens: 6025
characters: 1256
timestamp: 2025-12-24T04:08:14.045702
finish_reason: stop
---

$ hostname
myhost

Также вы можете задать имя вашего хоста, работая в режиме суперпользователя.
Однако имена хостов и имена серверов - это сложные темы, рассмотрение которых выходит за рамки этой книги. И не нужно сразу бросаться изменять имена хостов!

Полезные опции
- i    Вывести IP-адрес вашего хоста
-а    Вывести псевдоним вашего хоста
-s    Вывести короткое имя вашего хоста
-f    Вывести полностью определенное имя вашего хоста
-d    Вывести DNS-домен вашего хоста
-y    Вывести имя NIS- или YP-домена вашего хоста
-F файл    Установить имя вашего хоста, считав имя из файла файла
ifconfig интерфейс net-tools
/sbin stdin stdout -file —opt -help —version

Команда ifconfig выводит и устанавливает различные атрибуты сетевого интерфейса вашего компьютера. Эта тема выходит за рамки данной книги, но мы покажем вам несколько приемов.

Для того чтобы вывести информацию о стандартном сетевом интерфейсе (который обычно называется eth0), выполните следующую команду.

$ ifconfig eth0
eth0 Link encap:Ethernet HWaddr 00:50:BA:48:4F:BA
inet addr:192.168.0.10 Bcast:192.168.0.255 Mask:255.255.255.0
UP BROADCAST RUNNING MULTICAST MTU:1500
Metric:1
RX packets:1955231 errors:0 droppediO overruns:0 frame: 0
TX packets:1314765 errors:0 dropped:0 overruns:0