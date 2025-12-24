---
source_image: page_175.png
page_number: 175
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 60.99
tokens: 12920
characters: 3098
timestamp: 2025-12-23T23:42:50.208967
finish_reason: stop
---

<table>
  <tr>
    <th>Источник</th>
    <th>IP-источника</th>
    <th>Получатель</th>
    <th>IP-получателя</th>
    <th>Сервис</th>
  </tr>
  <tr>
    <td>Удаленные пользователи VPN</td>
    <td>172.16.61.0/24</td>
    <td></td>
    <td>172.16.17.32/29</td>
    <td>HTTPS (TCP 443)</td>
  </tr>
  <tr>
    <td>Удаленные администраторы VPN</td>
    <td>172.16.62.0/29</td>
    <td>Терминальный сервер</td>
    <td>172.16.6.45/32</td>
    <td>SSH (TCP 22)</td>
  </tr>
  <tr>
    <td>Удаленные администраторы VPN</td>
    <td>172.16.62.0/29</td>
    <td>Консоль Check Point</td>
    <td>172.16.6.13/32</td>
    <td>CPMI (TCP 18190)</td>
  </tr>
  <tr>
    <td>Удаленные администраторы VPN</td>
    <td>172.16.62.0/29</td>
    <td>Сервер управления</td>
    <td>172.16.6.0/24</td>
    <td>MS-RDP (TCP 3389)</td>
  </tr>
  <tr>
    <td>Шлюзы VPN</td>
    <td>172.16.4.117/32</td>
    <td>Центр сертификатов</td>
    <td>172.16.6.17/32</td>
    <td>LDAP (TCP 389)</td>
  </tr>
  <tr>
    <td>Шлюзы VPN</td>
    <td>172.16.4.117/32</td>
    <td>Сервер Cisco ACS</td>
    <td>172.16.6.21/32</td>
    <td>RADIUS (UDP 1645 и 1646)</td>
  </tr>
  <tr>
    <td>Шлюзы VPN</td>
    <td>172.16.4.117/32</td>
    <td>Zone Labs Integrity</td>
    <td>172.16.6.29/32</td>
    <td>Tcp 5054</td>
  </tr>
  <tr>
    <td>Компьютеры</td>
    <td>172.16.4.0/24</td>
    <td>HPCN</td>
    <td>172.16.6.33/32</td>
    <td>SNMP-Trap (UDP 162)</td>
  </tr>
  <tr>
    <td>Компьютеры</td>
    <td>172.16.4.0/24</td>
    <td>Сервер времени</td>
    <td>172.16.6.41/32</td>
    <td>NTP (UDP 132)</td>
  </tr>
  <tr>
    <th colspan="5">SecureData</th>
  </tr>
  <tr>
    <td>Контроллеры домена</td>
    <td>172.16.5.48/30</td>
    <td>Серверы промежуточного уровня</td>
    <td>172.16.3.64/29</td>
    <td>IKE (UDP 500)</td>
  </tr>
  <tr>
    <td>Контроллеры домена</td>
    <td>172.16.5.48/30</td>
    <td>Серверы промежуточного уровня</td>
    <td>172.16.3.64/29</td>
    <td>AH (IP 51)</td>
  </tr>
  <tr>
    <td>Контроллеры домена</td>
    <td>172.16.5.48/30</td>
    <td>Web-ферма 1</td>
    <td>172.16.3.16/29</td>
    <td>IKE (UDP 500)</td>
  </tr>
  <tr>
    <td>Контроллеры домена</td>
    <td>172.16.5.48/30</td>
    <td>Web-ферма 1</td>
    <td>172.16.3.16/29</td>
    <td>AH (IP 51)</td>
  </tr>
  <tr>
    <td>Контроллеры домена</td>
    <td>172.16.5.48/30</td>
    <td>Web-ферма 2</td>
    <td>172.16.3.24/29</td>
    <td>IKE (UDP 500)</td>
  </tr>
  <tr>
    <td>Контроллеры домена</td>
    <td>172.16.5.48/30</td>
    <td>Web-ферма 2</td>
    <td>172.16.3.24/29</td>
    <td>AH (IP 51)</td>
  </tr>
  <tr>
    <td>Контроллеры домена</td>
    <td>172.16.5.48/30</td>
    <td>Сервер времени</td>
    <td>172.16.6.41/32</td>
    <td>NTP (UDP 132)</td>
  </tr>
  <tr>
    <td>DNS-серверы</td>
    <td>172.16.5.52/30</td>
    <td>Шлюзы DNS демилитаризованной зоны</td>
    <td>172.16.4.112/30</td>
    <td>DNS (TCP/UDP 53)</td>
  </tr>
  <tr>
    <td>Сеть данных</td>
    <td>172.16.5.0/24</td>
    <td>HPCN</td>
    <td>172.16.6.33/32</td>
    <td>SNMP-Trap (UDP 162)</td>
  </tr>
</table>

Продолжение табл. 4.6