---
source_image: page_278.png
page_number: 278
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.41
tokens: 7671
characters: 2051
timestamp: 2025-12-24T04:40:00.037900
finish_reason: stop
---

но выбираемый порт. Вместо этого в SUN RPC закрепляются номера «программ» (program), предоставляющих определенные «услуги» (service), а соответствующий порт регистрируется в служебной RPC-программе portmapper¹, что проиллюстрировано в листинге 6.28 при помощи утилиты rpcinfo(8).

Листинг 6.28. Удаленный вызов процедур RPC: динамические номера портов и portmapper

lumpy@ubuntu:~$ rpcinfo -p NVR.local

<table>
  <tr>
    <th>program</th>
    <th>vers</th>
    <th>proto</th>
    <th>port</th>
    <th>service</th>
  </tr>
  <tr>
    <td>100000</td>
    <td>3</td>
    <td>tcp</td>
    <td>111</td>
    <td>portmapper</td>
  </tr>
  <tr>
    <td>100000</td>
    <td>3</td>
    <td>udp</td>
    <td>111</td>
    <td>portmapper</td>
  </tr>
  <tr>
    <td>100003</td>
    <td>3</td>
    <td>tcp</td>
    <td>2049</td>
    <td>nfs</td>
  </tr>
  <tr>
    <td>100003</td>
    <td>3</td>
    <td>udp</td>
    <td>2049</td>
    <td>nfs</td>
  </tr>
  <tr>
    <td>100005</td>
    <td>3</td>
    <td>udp</td>
    <td>53964</td>
    <td>mountd</td>
  </tr>
  <tr>
    <td>100005</td>
    <td>3</td>
    <td>tcp</td>
    <td>39835</td>
    <td>mountd</td>
  </tr>
</table>

При помощи portmapper организуется обнаружение NFS-серверов в локальной сети посредством широковещательного (-b, broadcast) поиска 1 зарегистрированных RPC-программ NFS v3 (листинг 6.29). Кроме этого, некоторые серверы NFS (например, сетевые устройства хранения данных W:[NAS] или сетевые видеорегистраторы W:[NVR]) регистрируются в службе mDNS/DNS-SD, что обнаруживается 2 при помощи avahi-browse(1).

Листинг 6.29. Обнаружение NFS-серверов

1 lumpy@ubuntu:~$ rpcinfo -b nfs 3
   192.168.17.90.8.1      NVR.local

2 lumpy@ubuntu:~$ avahi-browse -rcl _nfs._tcp
   + eth0 IPv4 NVR(NFS)
   = eth0 IPv4 NVR(NFS)
     hostname = [NVR.local]
     address = [192.168.17.90]
     port = [2049]
     txt = []

¹ Порт самой RPC-программы portmapper все же закреплен за номером 111 TCP/UDP, что позволяет клиентам обращаться portmapper сервера и находить порты других RPC-программ по их номерам.