---
source_image: page_160.png
page_number: 160
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 55.82
tokens: 12701
characters: 3543
timestamp: 2025-12-23T23:42:02.015320
finish_reason: stop
---

<table>
  <tr>
    <th>Сервис</th>
    <th>Протокол</th>
    <th>Порт получателя</th>
    <th>Комментарии</th>
  </tr>
  <tr>
    <td>CPD</td>
    <td>TCP</td>
    <td>18191</td>
    <td>Check Point Daemon Protocol</td>
  </tr>
  <tr>
    <td>CPD_amon</td>
    <td>TCP</td>
    <td>18192</td>
    <td>Check Point Internal Application Monitoring</td>
  </tr>
  <tr>
    <td>RDP</td>
    <td>UDP</td>
    <td>259</td>
    <td>Check Point Reliable Datagram Protocol</td>
  </tr>
  <tr>
    <td>PW1</td>
    <td>TCP</td>
    <td>256</td>
    <td>Check Point VPN-1 & Firewall-1 Service</td>
  </tr>
  <tr>
    <td>PW1_log</td>
    <td>TCP</td>
    <td>257</td>
    <td>Check Point Logs</td>
  </tr>
  <tr>
    <td>PW1_mgmt</td>
    <td>TCP</td>
    <td>258</td>
    <td>Check Point Management</td>
  </tr>
  <tr>
    <td>PW1_ica_pull</td>
    <td>TCP</td>
    <td>18210</td>
    <td>Check Point Internal CA Pull Certificate Service</td>
  </tr>
  <tr>
    <td>PW1_ica_push</td>
    <td>TCP</td>
    <td>18211</td>
    <td>Check Point Internal CA Push Certificate Service</td>
  </tr>
  <tr>
    <td>PW1-inc</td>
    <td>Group</td>
    <td></td>
    <td>CPD, CPD_amon, RDP, PW1_mgmt, PW1_ica_push, FW1</td>
  </tr>
  <tr>
    <td>PW1-Out</td>
    <td>Group</td>
    <td></td>
    <td>CPD, RDP, PW1_ica_pull, FW1</td>
  </tr>
  <tr>
    <td>VRRP</td>
    <td>IP type 112</td>
    <td>n/a</td>
    <td></td>
  </tr>
  <tr>
    <td>IGMP</td>
    <td>IP type 2</td>
    <td>n/a</td>
    <td></td>
  </tr>
  <tr>
    <td>HTTP</td>
    <td>TCP</td>
    <td>80</td>
    <td></td>
  </tr>
  <tr>
    <td>HTTPS</td>
    <td>TCP</td>
    <td>443</td>
    <td></td>
  </tr>
  <tr>
    <td>FTP</td>
    <td>TCP</td>
    <td>21</td>
    <td></td>
  </tr>
  <tr>
    <td>domain-udp</td>
    <td>UDP</td>
    <td>53</td>
    <td></td>
  </tr>
  <tr>
    <td>domain-tcp</td>
    <td>TCP</td>
    <td>53</td>
    <td></td>
  </tr>
  <tr>
    <td>DNS</td>
    <td>Group</td>
    <td></td>
    <td>domain-udp, domain-tcp</td>
  </tr>
  <tr>
    <td>SMTP</td>
    <td>TCP</td>
    <td>25</td>
    <td></td>
  </tr>
  <tr>
    <td>NTP</td>
    <td>UDP</td>
    <td>123</td>
    <td></td>
  </tr>
  <tr>
    <td>SSH</td>
    <td>TCP</td>
    <td>22</td>
    <td></td>
  </tr>
  <tr>
    <td>IKE</td>
    <td>UDP</td>
    <td>500</td>
    <td></td>
  </tr>
  <tr>
    <td>ESP</td>
    <td>IP type 50</td>
    <td>n/a</td>
    <td></td>
  </tr>
  <tr>
    <td>TCP7456</td>
    <td>TCP</td>
    <td>7456</td>
    <td>For Cisco VPN 3030 IPSec tunnelling over TCP</td>
  </tr>
  <tr>
    <td>IPSec</td>
    <td>Group</td>
    <td></td>
    <td>IKE, ESP, TCP7456</td>
  </tr>
  <tr>
    <td>SNMP-read</td>
    <td>UDP</td>
    <td>161</td>
    <td></td>
  </tr>
  <tr>
    <td>SNMP-trap</td>
    <td>UDP</td>
    <td>162</td>
    <td></td>
  </tr>
  <tr>
    <td>source-quench</td>
    <td>ICMP</td>
    <td>Type 4</td>
    <td></td>
  </tr>
</table>

Был задан следующий порядок обработки трафика Firewall-1:
• anti-spoofing;
• свойства, маркированные как «First» в Global Properties;
• все правила по порядку, за исключением последнего;
• свойства, отмеченные как «Before Last» в Global Properties;
    • последнее правило;
• свойства, маркированные «Last» в Global Properties;
    • неявно заданное правило «Drop».

На рис. 4.7 представлена реализованная политика межсетевого экрана. Как будет показано далее, все неявные правила межсетевого экрана были отключены на закладке Global Properties и созданы явные правила. Это позволило повысить защищенность межсетевого экрана.