---
source_image: page_260.png
page_number: 260
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 8.56
tokens: 7369
characters: 1275
timestamp: 2025-12-23T23:11:36.442992
finish_reason: stop
---

Общие параметры команды

-с (Linux) — количество отправляемых в удаленную систему запросов ping.
-n (Windows) — количество отправляемых в удаленную систему запросов ping.
-w (Linux) — время ожидания ответа в секундах.
-w (Windows) — время ожидания ответа в миллисекундах.

Пример команды

Для однократной проверки связи узла 192.168.0.11 нужно выполнить следующее:

$ ping -n 1 192.168.0.11

Pinging 192.168.0.11 with 32 bytes of data:
Reply from 192.168.0.11: bytes=32 time<1ms TTL=128

Ping statistics for 192.168.0.11:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

Реализация

В примере 19.1 подробно описано, как можно использовать bash и команду ping для создания постоянно обновляемой панели мониторинга, которая предупредит вас, если система перестанет быть доступной.

Пример 19.1. pingmonitor.sh

#!/bin/bash -
#
# Bash и кибербезопасность
# pingmonitor.sh
#
# Описание:
# Проверка связи для мониторинга доступности хоста
#
# Использование:
# pingmonitor.sh <file> <seconds>
#   <file> Файл, содержащий список хостов
#   <seconds> Количество секунд между пингами
#

while true
do
  clear
  echo 'Cybersecurity Ops System Monitor'
  echo 'Status: Scanning ...'