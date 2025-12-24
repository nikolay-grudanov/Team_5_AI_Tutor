---
source_image: page_077.png
page_number: 77
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 11.72
tokens: 7604
characters: 2070
timestamp: 2025-12-23T23:04:33.854097
finish_reason: stop
---

<table>
  <tr>
    <th>Команда Linux</th>
    <th>Эквивалент Windows Git Bash</th>
    <th>Назначение</th>
  </tr>
  <tr>
    <td>route</td>
    <td>route print</td>
    <td>Показать таблицу маршрутизации</td>
  </tr>
  <tr>
    <td>arp -a</td>
    <td>arp -a</td>
    <td>Вывести таблицу ARP (протокол определения адреса)</td>
  </tr>
  <tr>
    <td>netstat -a</td>
    <td>netstat -a</td>
    <td>Отобразить сетевые подключения</td>
  </tr>
  <tr>
    <td>mount</td>
    <td>net share</td>
    <td>Вывести информацию о файловых системах</td>
  </tr>
  <tr>
    <td>ps -e</td>
    <td>tasklist</td>
    <td>Отобразить запущенные процессы</td>
  </tr>
</table>

Сценарий getlocal.sh, показанный в примере 5.3, предназначен для определения типа операционной системы, запуска различных команд, соответствующих типу ОС, и записи результатов в файл. Вывод каждой команды хранится в формате XML, то есть для упрощения последующей обработки ограничен тегами XML. Вызовите скрипт следующим образом: bash getlocal.sh < cmds.txt, где файл cmds.txt содержит список команд, аналогичных приведенным в табл. 5.3. Ожидаемый формат — это поля, разделенные вертикальными линиями, плюс дополнительное поле — тег XML, с помощью которого можно пометить вывод команды (кроме того, строки, начинающиеся с #, считаются комментариями и будут игнорироваться).

Вот как может выглядеть файл cmds.txt:

# Linux Command | MSWin Bash | XML tag | Purpose
uname -a | uname -a | uname | O.S. version etc
cat /proc/cpuinfo | systeminfo | sysinfo | system hardware and related info
ifconfig | ipconfig | nwinterface | Network interface information
route | route print | nwroute | routing table
arp -a | arp -a | nwarp | ARP table
netstat -a | netstat -a | netstat | network connections
mount | net share | diskinfo | mounted disks
ps -e | tasklist | processes | running processes

Пример 5.3 показывает исходный код для скрипта.

Пример 5.3. getlocal.sh

#!/bin/bash -
#
# Bash и кибербезопасность
# getlocal.sh
#
# Описание:
# Собираем основную информацию о системе и сбрасываем в файл
# Использование: