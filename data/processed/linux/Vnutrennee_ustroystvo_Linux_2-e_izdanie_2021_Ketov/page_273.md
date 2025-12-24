---
source_image: page_273.png
page_number: 273
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.32
tokens: 7646
characters: 2141
timestamp: 2025-12-24T04:39:48.783221
finish_reason: stop
---

Листинг 6.23. Терминальные браузеры lynx, links и w3m

lumpy@ubuntu:~$ lynx http://www.kernel.org

#The Linux Kernel Archives Atom Feed Latest Linux Kernel Releases

The Linux Kernel Archives

* About
* Contact us
* FAQ
* Releases
* Signatures
* Site news

Protocol        Location
HTTP           https://www.kernel.org/pub/
GIT            https://git.kernel.org/
RSYNC          rsync://rsync.kernel.org/pub/

Latest Stable Kernel:
Download 5.3.12

mainline:      5.4-rc8   2019-11-17 [tarball] [patch] [inc. patch] [view diff] [browse]
stable:        5.3.12    2019-11-20 [tarball] [pgp] [patch] [inc. patch] [view diff] [browse] [changelog]
longterm:      4.19.85   2019-11-20 [tarball] [pgp] [patch] [inc. patch] [view diff] [browse] [changelog]
longterm:      4.14.155  2019-11-20 [tarball] [pgp] [patch] [inc. patch] [view diff] [browse] [changelog]
longterm:      4.9.102   2019-11-16 [tarball] [pgp] [patch] [inc. patch] [view diff] [browse] [changelog]
longterm:      4.4.202   2019-11-16 [tarball] [pgp] [patch] [inc. patch] [view diff] [browse] [changelog]

Стрелки: Вверх, Вниз - перемещение. Вправо - переход по ссылке; Влево - возврат.
Help Options Print Go Menu Exit /- поиск [delete]-список истории

Кроме Web-браузеров, предназначенных для интерактивной работы пользователей, в сценариях на языке командного интерпретатора зачастую используются неинтерактивные пользовательские агенты wget(1) и curl(1), позволяющие автоматизировать Web-взаимодействие. Так, например, в листинге 6.24 при помощи wget(1) показано скачивание файла в режиме «с докачкой» (-c, continue), а curl(1) применяется для обращения к Google Geocoding API.

Листинг 6.24. Пользовательские агенты wget и curl

lumpy@ubuntu:~$ wget -c http://www.brendangregg.com/Perf/linuxperftools.png
--2019-11-24 00:54:08--  http://www.brendangregg.com/Perf/linuxperftools.png
Распознаётся www.brendangregg.com (www.brendangregg.com)... 184.168.188.1
Подключение к www.brendangregg.com (www.brendangregg.com)|184.168.188.1|:80... соединение установлено.
НПТР-запрос отправлен. Ожидание ответа... 200 OK
Длина: 523561 (511K) [image/png]
Сохранение в: «linuxperftools.png»