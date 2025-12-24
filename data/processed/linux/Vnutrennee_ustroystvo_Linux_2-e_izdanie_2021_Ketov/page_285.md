---
source_image: page_285.png
page_number: 285
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.18
tokens: 7512
characters: 1616
timestamp: 2025-12-24T04:40:15.012597
finish_reason: stop
---

x-cloud-trace-context: 8fa4d5d63ef04865-6a136652cac2f6b/7935058721407822980\r\n
Access-Control-Allow-Origin: *\r\n
X-Frame-Options: DENY\r\n
X-XSS-Protection: 1; mode=block\r\n
X-Content-Type-Options: nosniff\r\n
Referrer-Policy: strict-origin-when-cross-origin\r\n
Via: 1.1 google\r\n
\r\n
[HTTP response 1/1]
[Time since request: 0.145039080 seconds]
[Request in frame: 4]
[Request URI: http://ipinfo.io/city]
File Data: 7 bytes
Line-based text data: text/html (1 lines)
Saint Petersburg\r\n

^C2 packets captured

6.5.2. Сетевой сканер nmap

Сетевой сканер W:[nmap] предназначен для поиска служб по их открытым портам на указанных узлах сети. В примере из листинга 6.37 показан процесс и результаты сканирования узла 192.168.0.1 (беспроводной маршрутизатор, арендованный у провайдера Интернета).

Сканирование выполнялось способом TCP connect scan ①, т. е. предпринималась попытка установить соединение TCP с каждым из 1000 «популярных» портов. В результате оказывается, что на узле открыты 4 порта, доступные ② для присоединения.

Листинг 6.37. Сетевой сканер nmap

lumpy@ubuntu:~$ nmap -n -vvv --reason 192.168.0.1
Starting Nmap 7.80 ( https://nmap.org ) at 2019-11-24 11:46 MSK
Initiating Ping Scan at 11:46
Scanning 192.168.0.1 [2 ports]
Completed Ping Scan at 11:46, 0.01s elapsed (1 total hosts)
① Initiating Connect Scan at 11:46
Scanning 192.168.0.1 [1000 ports]
Discovered open port 80/tcp on 192.168.0.1
Discovered open port 22/tcp on 192.168.0.1
Discovered open port 1900/tcp on 192.168.0.1
Discovered open port 49152/tcp on 192.168.0.1
Completed Connect Scan at 11:46, 0.57s elapsed (1000 total ports)