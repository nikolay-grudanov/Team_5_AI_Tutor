---
source_image: page_174.png
page_number: 174
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 60.50
tokens: 12882
characters: 3035
timestamp: 2025-12-23T23:42:44.894282
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
    <th colspan="5">WebDMZ</th>
  </tr>
  <tr>
    <td>Серверы промежуточного уровня</td>
    <td>172.16.3.64/29</td>
    <td>файл-серверы</td>
    <td>172.16.5.32/30</td>
    <td>CIFS (TCP 445)</td>
  </tr>
  <tr>
    <td>Серверы промежуточного уровня</td>
    <td>172.16.3.64/29</td>
    <td>DNS-серверы</td>
    <td>172.16.5.52/30</td>
    <td>DNS (TCP/UDP 53)</td>
  </tr>
  <tr>
    <td>Серверы промежуточного уровня</td>
    <td>172.16.3.64/29</td>
    <td>Контроллеры домена</td>
    <td>172.16.5.48/30</td>
    <td>IKE (UDP 500)</td>
  </tr>
  <tr>
    <td>Серверы промежуточного уровня</td>
    <td>172.16.3.64/29</td>
    <td>Контроллеры домена</td>
    <td>172.16.5.48/30</td>
    <td>AH (IP 51)</td>
  </tr>
  <tr>
    <td>Web-ферма 1</td>
    <td>172.16.3.16/29</td>
    <td>DNS-серверы</td>
    <td>172.16.5.52/30</td>
    <td>DNS (TCP/UDP 53)</td>
  </tr>
  <tr>
    <td>Web-ферма 1</td>
    <td>172.16.3.16/29</td>
    <td>Контроллеры домена</td>
    <td>172.16.5.48/30</td>
    <td>IKE (UDP 500)</td>
  </tr>
  <tr>
    <td>Web-ферма 1</td>
    <td>172.16.3.16/29</td>
    <td>Контроллеры домена</td>
    <td>172.16.5.48/30</td>
    <td>AH (IP 51)</td>
  </tr>
  <tr>
    <td>Web-ферма 2</td>
    <td>172.16.3.24/29</td>
    <td>DNS-серверы</td>
    <td>172.16.5.52/30</td>
    <td>DNS (TCP/UDP 53)</td>
  </tr>
  <tr>
    <td>Web-ферма 2</td>
    <td>172.16.3.24/29</td>
    <td>Контроллеры домена</td>
    <td>172.16.5.48/30</td>
    <td>IKE (UDP 500)</td>
  </tr>
  <tr>
    <td>Web-ферма 2</td>
    <td>172.16.3.24/29</td>
    <td>Контроллеры домена</td>
    <td>172.16.5.48/30</td>
    <td>AH (IP 51)</td>
  </tr>
  <tr>
    <td>Web-серверы демилитаризованной зоны</td>
    <td>172.16.3.0/24</td>
    <td>HPON</td>
    <td>172.16.6.33/32</td>
    <td>SNMP-Trap (UDP 162)</td>
  </tr>
  <tr>
    <td>Web-серверы демилитаризованной зоны</td>
    <td>172.16.3.0/24</td>
    <td>Cisco VMS 2.2</td>
    <td>172.16.6.9/32</td>
    <td>SSL (TCP 443)</td>
  </tr>
  <tr>
    <td>Web-серверы демилитаризованной зоны</td>
    <td>172.16.3.0/24</td>
    <td>Сеть данных</td>
    <td>172.16.5.0/24</td>
    <td>ICMP source-quench</td>
  </tr>
  <tr>
    <th colspan="5">ServiceDMZ</th>
  </tr>
  <tr>
    <td>Прокс-серверы</td>
    <td>172.16.4.104/30</td>
    <td>SIMS</td>
    <td>172.16.6.25/32</td>
    <td>Syslog (UDP 514)</td>
  </tr>
  <tr>
    <td>Шлюзы VPN</td>
    <td>172.16.4.117/32</td>
    <td>SIMS</td>
    <td>172.16.6.25/32</td>
    <td>Syslog (UDP 514)</td>
  </tr>
  <tr>
    <td>Удаленные пользователи VPN</td>
    <td>172.16.61.0/24</td>
    <td>Внутренний сервер ОМА</td>
    <td>172.16.17.54/32</td>
    <td>HTTPS (TCP 443)</td>
  </tr>
  <tr>
    <td>Удаленные пользователи VPN</td>
    <td>172.16.61.0/24</td>
    <td>Внутренние файл- и принт-серверы</td>
    <td>172.16.17.32/29</td>
    <td>HTTP (TCP 80)</td>
  </tr>
</table>

Продолжение табл. 4.6