---
source_image: page_172.png
page_number: 172
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.83
tokens: 12369
characters: 2691
timestamp: 2025-12-23T23:42:17.592676
finish_reason: stop
---

Наименование и распределение уровней безопасности

<table>
  <tr>
    <th>Устройство</th>
    <th>Имя интерфейса</th>
    <th>Уровень безопасности</th>
    <th>IP-адрес</th>
  </tr>
  <tr>
    <td rowspan="7">PIX1</td>
    <td>AdminDMZ</td>
    <td>0</td>
    <td>172.16.1.1/28</td>
  </tr>
  <tr>
    <td>WebDMZ</td>
    <td>10</td>
    <td>172.16.3.1/24</td>
  </tr>
  <tr>
    <td>ServiceDMZ</td>
    <td>20</td>
    <td>172.16.4.1/24</td>
  </tr>
  <tr>
    <td>SecureData</td>
    <td>60</td>
    <td>172.16.5.1/24</td>
  </tr>
  <tr>
    <td>Management</td>
    <td>80</td>
    <td>172.16.6.1/24</td>
  </tr>
  <tr>
    <td>Internal</td>
    <td>100</td>
    <td>172.16.9.1/28</td>
  </tr>
  <tr>
    <td>State</td>
    <td>40</td>
    <td>172.16.1.65/30</td>
  </tr>
  <tr>
    <td rowspan="7">PIX2</td>
    <td>AdminDMZ</td>
    <td>0</td>
    <td>172.16.1.2/28</td>
  </tr>
  <tr>
    <td>WebDMZ</td>
    <td>10</td>
    <td>172.16.3.2/24</td>
  </tr>
  <tr>
    <td>ServiceDMZ</td>
    <td>20</td>
    <td>172.16.4.2/24</td>
  </tr>
  <tr>
    <td>SecureData</td>
    <td>60</td>
    <td>172.16.5.2/24</td>
  </tr>
  <tr>
    <td>Management</td>
    <td>80</td>
    <td>172.16.6.2/24</td>
  </tr>
  <tr>
    <td>Internal</td>
    <td>100</td>
    <td>172.16.9.2/28</td>
  </tr>
  <tr>
    <td>State</td>
    <td>40</td>
    <td>172.16.1.65/30</td>
  </tr>
</table>

Конфигурирование уровней безопасности и имен на каждом интерфейсе:

...
nameif ethernet0 AdminDmz security0
nameif ethernet1 WebDMZ security10
nameif ethernet2 ServiceDMZ security20
nameif ethernet3 SecureData security60
nameif ethernet4 Management security80
nameif ethernet5 Internal security 100
nameif ethernet6 State security40

Интерфейс State используется только для обеспечения режима failover. Команды настройки маршрутизации здесь не показаны. Пароли:

...
enable password GHjiiuUIIH67JH encrypted
passwd Huhu&*8h9h encrypted

Конфигурирование NAT. Внутренние межсетевые экраны не используют трансляцию адресов, но таблица трансляции адресов NAT все же требуется для организации доступа в подсети с разными уровнями безопасности. Команда global не используется, так как реальной трансляции не происходит. Для разрешения доступа через интерфейс с низким уровнем безопасности со стороны интерфейсов с более высоким уровнем безопасности используется команда nat. Эта команда применяется только на тех интерфейсах, компьютерам которых требуется доступ к компьютерам, находящимся за интерфейсами с меньшим уровнем безопасности:

...
nat (internal) 0 172.16.16.0. 255.255.248.0
nat (internal) 0 172.16.32.0. 255.255.224.0
nat (Management) 0 172.16.6.0. 255.255.255.0
nat (SecureData) 0 172.16.5.0. 255.255.255.0