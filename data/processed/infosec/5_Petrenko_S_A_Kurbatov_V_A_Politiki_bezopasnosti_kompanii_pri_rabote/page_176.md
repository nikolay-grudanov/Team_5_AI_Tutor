---
source_image: page_176.png
page_number: 176
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 63.79
tokens: 12985
characters: 3516
timestamp: 2025-12-23T23:42:53.081450
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
    <td>Сеть данных</td>
    <td>172.16.5.0/24</td>
    <td>Web-серверы демилитаризованной зоны</td>
    <td>172.16.2.0/24</td>
    <td>ICMP source-quench</td>
  </tr>
  <tr>
    <th colspan="5">Management</th>
  </tr>
  <tr>
    <td>HPOV</td>
    <td>172.16.6.33/32</td>
    <td>Внутренняя сеть</td>
    <td>172.16.0.0/16</td>
    <td>SNMP (UDP 161)</td>
  </tr>
  <tr>
    <td>HPOV</td>
    <td>172.16.6.33/32</td>
    <td>Пограничные маршрутизаторы</td>
    <td>70.70.70.16/30</td>
    <td>SNMP (UDP 161)</td>
  </tr>
  <tr>
    <td>Сеть управления</td>
    <td>172.16.6.0/24</td>
    <td>Балансировщики нагрузки, proxy-серверы</td>
    <td>172.16.1.8/22</td>
    <td>SSH (TCP 22)</td>
  </tr>
  <tr>
    <td>Сеть управления</td>
    <td>172.16.6.0/24</td>
    <td>Компьютеры зоны ServiceDMZ</td>
    <td>172.6.4.96/27</td>
    <td>SSH (TCP 22)</td>
  </tr>
  <tr>
    <td>Сеть управления</td>
    <td>172.16.6.0/24</td>
    <td>Web-серверы демилитаризованной зоны</td>
    <td>172.16.3.0/24</td>
    <td>MS-RDP (TCP 3389)</td>
  </tr>
  <tr>
    <td>Сеть управления</td>
    <td>172.16.6.0/24</td>
    <td>DNS-серверы зоны ServiceDMZ</td>
    <td>172.16.4.112/30</td>
    <td>MS-RDP (TCP 3389)</td>
  </tr>
  <tr>
    <td>Сеть управления</td>
    <td>172.16.6.0/24</td>
    <td>Компьютеры зоны данных</td>
    <td>172.16.5.0/24</td>
    <td>MS-RDP (TCP 3389)</td>
  </tr>
  <tr>
    <td>Сеть управления</td>
    <td>172.16.6.0/24</td>
    <td>Внутренние серверы</td>
    <td>172.16.16.16/21</td>
    <td>MS-RDP (TCP 3389)</td>
  </tr>
  <tr>
    <td>Консоль Check Point</td>
    <td>172.16.6.13/32</td>
    <td>Внешние межсетевые экраны</td>
    <td>172.16.1.4/30</td>
    <td>RW1-In (UDP 259)</td>
  </tr>
  <tr>
    <th colspan="5">Internal</th>
  </tr>
  <tr>
    <td>Клиентские подсети</td>
    <td>172.16.32.0/19</td>
    <td>Proxy-серверы DMZ</td>
    <td>172.16.4.104/30</td>
    <td>TCP 8080</td>
  </tr>
  <tr>
    <td>Exchange Cluster IP</td>
    <td>172.16.17.46/32</td>
    <td>SMTP-шлюзы</td>
    <td>172.16.4.108/30</td>
    <td>SMTP (TCP 25)</td>
  </tr>
  <tr>
    <td>Внутренние DNS</td>
    <td>172.16.17.20/30</td>
    <td>DNS-форвардеры</td>
    <td>172.16.4.112/30</td>
    <td>DNS (TCP/UDP 53)</td>
  </tr>
  <tr>
    <td>Серверы управления контентом</td>
    <td>172.16.16.16/21</td>
    <td>HPOV</td>
    <td>172.16.6.33/32</td>
    <td>SNMP-Trap (UDP 162)</td>
  </tr>
  <tr>
    <td>Внутренние контроллеры домена</td>
    <td>172.16.17.16/30</td>
    <td>Сервер времени</td>
    <td>172.16.6.41/32</td>
    <td>NTP (UDP 123)</td>
  </tr>
</table>

Окончание табл. 4.6

Turbo ACL. Для ускорения обработки списков контроля доступа используется возможность PIX по компилированию списков контроля доступа. Включается эта возможность следующей командой: access-list compiled

Группирование объектов. Возможность группирования объектов PIX позволяет улучшить читабельность списков контроля доступа, ускорить создание похожих записей в списках контроля доступа:

object-group network WebDMZServers
network-object 172.16.3.16 255.255.255.248
network-object 172.16.3.24 255.255.255.248
network-object 172.16.3.64 255.255.255.248
object-group network AdminDMZNet
network-object 70.70.70.16 255.255.255.252
network-object 172.16.1.8 255.255.255.248
object-group network AdminDMZAll network-object 172.16.1.4 255.255.255.252
group-object AdminDMZNet