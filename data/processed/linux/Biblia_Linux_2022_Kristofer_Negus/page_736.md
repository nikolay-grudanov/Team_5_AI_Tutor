---
source_image: page_736.png
page_number: 736
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.22
tokens: 7707
characters: 2117
timestamp: 2025-12-24T05:06:08.935636
finish_reason: stop
---

Затем с помощью IP-адреса Host-A сканирование nmap TCP Connect выполняется с Host-A. Сканирование nmap переходит в сеть для продолжения работы. У всех портов статус closed:

# nmap -sT 10.140.67.23
Starting Nmap 7.80 ( https://nmap.org ) at 2020-1-31 11:53 EDT

Nmap scan report for rhel8 (10.140.67.23)

Host is up (0.010s latency).
All 1000 scanned ports on 10.140.67.23 are closed

Nmap done: 1 IP address (1 host up) scanned in 1.48 seconds

Сканирование nmap перемещается с Host-A на Host-B. Теперь сканирование TCP Connect выполняется на портах Host-A из командной строки Host-B:

$ nmap -sT 10.140.67.23
Starting Nmap 7.80 ( https://nmap.org ) at 2020-1-31 11:57 EDT

Note: Host seems down. If it is really up,
but blocking our ping probes, try -PN

Nmap done: 1 IP address (0 hosts up) scanned in 0.11 seconds

В рассмотренном примере утилита nmap дает полезную подсказку. Host-A, похоже, не работает или просто блокирует попытки подключения. Поэтому предпринимается еще одна попытка сканирования nmap с хоста Host-B, причем nmap приказано отключить пинг с помощью параметра -PN:

$ nmap -sT -PN 10.140.67.23
Starting Nmap 7.80 ( https://nmap.org ) at 2020-1-31 11:58 EDT
Nmap scan report for rhel8 (10.140.67.23)

Host is up (0.0015s latency).
All 1000 scanned ports on 10.140.67.23 are filtered

Nmap done: 1 IP address (1 host up) scanned in 5.54 seconds

В примере видно, что Host-A (10.140.67.23) запущен и работает и все его порты имеют статус filtered. Это означает, что на Host-A установлен брандмауэр. Сканирование с Host-B позволяет лучше понять, что может увидеть вредоносный сканер при сканировании Linux-сервера. Здесь вредоносный сканер почти ничего не увидит.

ПРИМЕЧАНИЕ
Если вам известна утилита nmap, то вы знаете, что сканирование TCP SYN — это реализуемое ею сканирование по умолчанию. TCP SYN scan отлично справляется с исследованием удаленной системы в скрытом режиме. Поскольку вы изучаете собственную систему в целях аудита безопасности, имеет смысл использовать более тяжеловесные утилиты сканирования nmap. Для сканирования TCP SYN scan необходимо ввести команду nmap -SS ip_address.