---
source_image: page_231.png
page_number: 231
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.05
tokens: 7390
characters: 1478
timestamp: 2025-12-24T04:38:30.406706
finish_reason: stop
---

тернету путем опроса наличия связи с узлом 8.8.8.8 (публичный DNS-сервер компании Google) при помощи команды ping(1). Нужно отметить, что использование until list do ...; done может быть заменено эквивалентным while ! list do ...; done с указанием признака отрицания !

Листинг 5.50. Цикл «ДО»: ожидание доступности подключения к Интернету

bender@ubuntu:~$ set -x
bender@ubuntu:~$ until ping -c1 -w1 8.8.8.8 ; do sleep 1;date ; done
() + ping -c1 -w1 8.8.8.8
connect: Network is unreachable
+ sleep 1
+ date
Сб. дек. 19 09:11:32 MSK 2015
() + ping -c1 -w1 8.8.8.8
connect: Network is unreachable
+ sleep 1
+ date
Сб. дек. 19 09:11:39 MSK 2015
() + ping -c1 -w1 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_req=1 ttl=56 time=11.6 ms

--- 8.8.8.8 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 11.670/11.670/11.670/0.000 ms

5.6.4. Функции

Как и во многих языках программирования, командный интерпретатор имеет средства структуризации сценариев при помощи функций. Составной именованный список команд, называемый функцией, объявляется при помощи (Bourne- и POSIX-диалекты) конструкций

name() compound-list
или (Korn-диалект)
function name compound-list
с использованием ключевого слова function, где compound-list — это составной список, например if, case, for или while. Сформировать составной список из конвейера, простого или условного списка можно при помощи конструкций { list; },