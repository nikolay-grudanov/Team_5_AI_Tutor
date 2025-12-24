---
source_image: page_089.png
page_number: 89
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.89
tokens: 6639
characters: 1749
timestamp: 2025-12-24T03:58:23.684121
finish_reason: stop
---

<table>
  <tr>
    <th>lsmod</th>
    <td>Выводит список загруженных модулей ядра</td>
  </tr>
  <tr>
    <th>dmidecode</th>
    <td>Отображает информацию о BIOS компьютера</td>
  </tr>
  <tr>
    <th>cat /proc/cupinfo</th>
    <td>Выводит информацию о процессоре</td>
  </tr>
  <tr>
    <th>cat /proc/meminfo</th>
    <td>Отображает информацию о памяти</td>
  </tr>
  <tr>
    <th>cat /proc/mounts</th>
    <td>Показывает точки монтирования</td>
  </tr>
  <tr>
    <th>cat /proc/net/dev</th>
    <td>Выводит сетевые интерфейсы и статистику по ним</td>
  </tr>
  <tr>
    <th>cat /proc/version</th>
    <td>Похожа на uname, выводит версию ядра</td>
  </tr>
  <tr>
    <th>cat /proc/interrupts</th>
    <td>Отображает информацию по прерываниям</td>
  </tr>
  <tr>
    <th>cat /proc/swaps</th>
    <td>Выводит информацию о файлах подкачки</td>
  </tr>
</table>

4.6.2. Команды настройки сетевых интерфейсов

Подробно настройка сети будет рассматриваться в следующей главе, а пока рассмотрим таблицу 4.5, в которой представлен короткий список команд, которые вам могут пригодиться при настройке сети.

Таблица 4.5. Некоторые команды настройки сети

<table>
  <tr>
    <th>Команда</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>route</td>
    <td>Просмотр и изменение таблицы маршрутизации</td>
  </tr>
  <tr>
    <td>dmesg | less</td>
    <td>Просмотр сообщений ядра, которые выводятся ядром при загрузке системы</td>
  </tr>
  <tr>
    <td>iwconfig</td>
    <td>Выводит информацию обо всех беспроводных интерфейсах</td>
  </tr>
  <tr>
    <td>iwlist scan</td>
    <td>Поиск беспроводных сетей</td>
  </tr>
  <tr>
    <td>dhclient wlan0</td>
    <td>Обновляет IP-адрес и другую сетьную информацию беспроводного интерфейса wlan0</td>
  </tr>
</table>