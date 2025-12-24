---
source_image: page_158.png
page_number: 158
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 90.96
tokens: 13587
characters: 5166
timestamp: 2025-12-23T23:42:28.718993
finish_reason: stop
---

Вот таблицы, приведенные в изображении:

Таблица 1:
<table>
  <tr>
    <th>Имя</th>
    <th>Описание</th>
    <th>IP-адрес</th>
    <th>Тип объекта</th>
  </tr>
  <tr>
    <td>FWAdmin</td>
    <td>Консоль управления Firewall-1</td>
    <td>172.16.6.13</td>
    <td>Check Point Host</td>
  </tr>
  <tr>
    <td>PW-Front1</td>
    <td>Внешний межсетевой экран № 1</td>
    <td>70.70.70.28</td>
    <td>Gateway</td>
  </tr>
  <tr>
    <td>PW-Front2</td>
    <td>Внешний межсетевой экран № 2</td>
    <td>70.70.70.29</td>
    <td>Gateway</td>
  </tr>
  <tr>
    <td>FW-Front</td>
    <td>Объект Gateway Cluster: cp-front1, cp-front2</td>
    <td></td>
    <td>Gateway Cluster</td>
  </tr>
  <tr>
    <td>VRRPMulticast</td>
    <td>VRRP Multicast-адрес</td>
    <td>224.0.0.18</td>
    <td>Workstation</td>
  </tr>
  <tr>
    <td>VRRP-Front-Ext</td>
    <td>VRRP-адрес на внешних интерфейсах</td>
    <td>70.70.70.30</td>
    <td>Workstation</td>
  </tr>
  <tr>
    <td>VRRP-Front-DMZ1</td>
    <td>VRRP-адрес на внутренних интерфейсах DMZ1</td>
    <td>70.70.70.65</td>
    <td>Workstation</td>
  </tr>
  <tr>
    <td>VRRP-Front-DMZ2</td>
    <td>VRRP-адрес на внутренних интерфейсах DMZ2</td>
    <td>70.70.70.97</td>
    <td>Workstation</td>
  </tr>
  <tr>
    <td>VRRP-FW</td>
    <td>Требуется для функционирования VRRP, включает: VRRP-Front-Ext, VRRP-Front-DMZ1, VRRP-Front-DMZ2</td>
    <td></td>
    <td>Group</td>
  </tr>
  <tr>
    <td>Broadcast255</td>
    <td>Все широковещательные адреса</td>
    <td>255.255.255.255</td>
    <td>Workstation</td>
  </tr>
  <tr>
    <td>Broadcast0</td>
    <td>Старые широковещательные адреса Broadcast0</td>
    <td>0.0.0.0</td>
    <td>Workstation</td>
  </tr>
  <tr>
    <td>Broadcast</td>
    <td>Группа, включающая: Broadcast255, Broadcast0</td>
    <td></td>
    <td>Group</td>
  </tr>
</table>

Таблица 2:
<table>
  <tr>
    <th>Имя</th>
    <th>Описание</th>
    <th>IP-адрес</th>
    <th>Тип объекта</th>
  </tr>
  <tr>
    <td>Net-Mgmt</td>
    <td>Подсеть управления, необходима для включения функции antispoofing на административном интерфейсе межсетевых экранов</td>
    <td>172.16.6.0/24</td>
    <td>Network</td>
  </tr>
  <tr>
    <td>Net-Admin</td>
    <td>Подсеть, соединяющая внутренние и внешние межсетевые экраны, выделенная для управления</td>
    <td>172.16.1.0/28</td>
    <td>Network</td>
  </tr>
  <tr>
    <td>Spoof-Admin</td>
    <td>Группа, включающая: Net-Mgmt, Net-Admin</td>
    <td></td>
    <td>Group</td>
  </tr>
  <tr>
    <td>Web-VIP1</td>
    <td>Виртуальный IP-адрес для клиентской Web-фермы</td>
    <td>70.70.70.81</td>
    <td>Workstation</td>
  </tr>
  <tr>
    <td>Web-VIP2</td>
    <td>Виртуальный IP-адрес для партнерской Web-фермы</td>
    <td>70.70.70.82</td>
    <td>Workstation</td>
  </tr>
  <tr>
    <td>Web-Incoming</td>
    <td>Группа, включающая: Web-VIP1, Web-VIP2</td>
    <td></td>
    <td>Group</td>
  </tr>
  <tr>
    <td>Proxy-GW1</td>
    <td>Публичный адрес proxy-сервера № 1</td>
    <td>70.70.70.105</td>
    <td>Workstation</td>
  </tr>
  <tr>
    <td>Proxy-GW2</td>
    <td>Публичный адрес proxy-сервера № 2</td>
    <td>70.70.70.106</td>
    <td>Workstation</td>
  </tr>
  <tr>
    <td>Proxy-GW</td>
    <td>Группа, включающая: Proxy-GW1, Proxy-GW2</td>
    <td></td>
    <td>Group</td>
  </tr>
  <tr>
    <td>SMTP-GW1</td>
    <td>Публичный адрес SMTP-шлюза № 1</td>
    <td>70.70.70.109</td>
    <td>Workstation</td>
  </tr>
  <tr>
    <td>SMTP-GW2</td>
    <td>Публичный адрес SMTP-шлюза № 2</td>
    <td>70.70.70.110</td>
    <td>Workstation</td>
  </tr>
  <tr>
    <td>SMTP-GW</td>
    <td>Группа, включающая: SMTP-GW1, SMTP-GW2</td>
    <td></td>
    <td>Group</td>
  </tr>
  <tr>
    <td>DNS-GW1</td>
    <td>Публичный адрес DNS-сервера № 1</td>
    <td>70.70.70.113</td>
    <td>Workstation</td>
  </tr>
  <tr>
    <td>DNS-GW2</td>
    <td>Публичный адрес DNS-сервера № 2</td>
    <td>70.70.70.114</td>
    <td>Workstation</td>
  </tr>
  <tr>
    <td>DNS-GW</td>
    <td>Группа, включающая: DNS-GW1, DNS-GW2</td>
    <td></td>
    <td>Group</td>
  </tr>
  <tr>
    <td>DNS-ISP1-1</td>
    <td>DNS-сервер № 1 провайдера ISP1</td>
    <td>12.x.x.x</td>
    <td>Workstation</td>
  </tr>
  <tr>
    <td>DNS-ISP1-2</td>
    <td>DNS-сервер № 2 провайдера ISP1</td>
    <td>12.x.x.x</td>
    <td>Workstation</td>
  </tr>
  <tr>
    <td>DNS-ISP2-1</td>
    <td>DNS-сервер № 1 провайдера ISP2</td>
    <td>207.x.x.x</td>
    <td>Workstation</td>
  </tr>
  <tr>
    <td>DNS-ISP2-2</td>
    <td>DNS-сервер № 2 провайдера ISP2</td>
    <td>204.x.x.x</td>
    <td>Workstation</td>
  </tr>
  <tr>
    <td>DNS-ISP</td>
    <td>Группа, включающая: DNS-ISP1-1, DNS-ISP1-2, DNS-ISP2-1, DNS-ISP2-2</td>
    <td></td>
    <td>Group</td>
  </tr>
  <tr>
    <td>VPN-GW1</td>
    <td>Публичный адрес VPN-концентратора</td>
    <td>70.70.70.117</td>
    <td>Workstation</td>
  </tr>
  <tr>
    <td>VPN-GW</td>
    <td>Группа, включающая: VPNGW1</td>
    <td></td>
    <td>Group</td>
  </tr>
  <tr>
    <td>Router-GW1</td>
    <td>Внутренний адрес пограничного маршрутизатора № 1</td>
    <td>70.70.70.18</td>
    <td>Workstation</td>
  </tr>
</table>

Продолжение табл. 4.2