---
source_image: page_279.png
page_number: 279
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.96
tokens: 7705
characters: 2202
timestamp: 2025-12-24T04:40:02.585701
finish_reason: stop
---

Сервер NFS предоставляет клиентам некоторое количество RPC-услуг (-s, services), показанных в листинге 6.30, при помощи rpcinfo(8). Выделяют базовые RPC-программы mountd (2) и nfs (1), позволяющие монтировать файловые системы NFS и обращаться к их файлам, и дополнительные RPC-программы¹ nlockmgr (3) и status (4), реализующие механизм блокировки файлов.

Листинг 6.30. RPC-программы службы NFS

lumpy@ubuntu:~$ rpcinfo -s NVR.local

<table>
  <tr>
    <th>program</th>
    <th>version(s)</th>
    <th>netid(s)</th>
    <th>service</th>
    <th>owner</th>
  </tr>
  <tr>
    <td>100000</td>
    <td>4,3,2</td>
    <td>tcp6,tcp,udp,udp6</td>
    <td>portmapper</td>
    <td>superuser</td>
  </tr>
  <tr>
    <td>100003</td>
    <td>4,3,2</td>
    <td>udp6,tcp6,udp,tcp</td>
    <td>nfs</td>
    <td>superuser</td>
  </tr>
  <tr>
    <td>100005</td>
    <td>3,2,1</td>
    <td>tcp6,udp6,tcp,udp</td>
    <td>mountd</td>
    <td>superuser</td>
  </tr>
  <tr>
    <td>100021</td>
    <td>4,3,2,1</td>
    <td>tcp6,udp6,tcp,udp</td>
    <td>nlockmgr</td>
    <td>superuser</td>
  </tr>
  <tr>
    <td>100024</td>
    <td>1</td>
    <td>tcp6,udp6,tcp,udp</td>
    <td>status</td>
    <td>superuser</td>
  </tr>
</table>

6.4.6. Служба SMB/CIFS

Служба W:[CIFS] (common internet file system), заимствованная из семейства операционных систем Windows, предназначена (аналогично «родной» NFS) для совместного использования файлов. Основным протоколом службы CIFS является протокол SMB (server message blocks), который аналогично NFS ретранслирует системные вызовы к файлам.

Имена NetBIOS

Отличительной особенностью протокола SMB, доставшейся ему в наследство от транспорта W:[NetBIOS], является возможность использования еще одного вида имен узлов (в дополнение к DNS- и mDNS-именам, см. разд. 6.3) — так называемых «имен NetBIOS» — и собственной службы NBNS² (netbios name service), отображающей имена NetBIOS на IP-адреса.

Листинг 6.31. Имена узлов NetBIOS и их IP-адреса

lumpy@ubuntu:~$ nmblookup WINXP
querying WINXP on 192.168.100.255
192.168.100.3 WINXP<00>

¹ См. W:[NLM], network lock manager и W:[NSM], network status monitor.
² Служба NBNS похожа на DNS и mDNS одновременно, но несовместима с ними.