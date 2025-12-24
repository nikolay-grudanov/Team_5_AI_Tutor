---
source_image: page_568.png
page_number: 568
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 52.10
tokens: 8144
characters: 2859
timestamp: 2025-12-24T05:01:39.034519
finish_reason: stop
---

Для упрощения процесса блокировки портов сервера NFS можно добавить строку в файл /etc/sysconfig/nfs и назначить службам определенные номера портов. Далее приведены примеры параметров, содержащихся в файле /etc/sysconfig/nfs, с заданными статическими номерами портов:

RQUOTAD_PORT=49001
LOCKD_TCPPORT=49002
LOCKD_UDPPORT=49003
MOUNTD_PORT=49004
STATD_PORT=49005
STATD_OUTGOING_PORT=49006
RDMA_PORT=49007

Установив эти порты, я перезапустил службу nfs (service nfs restart). Используя команду netstat, в выводе вы увидите процессы, которые прослушивают назначенные порты:

<table>
  <tr>
    <th>tcp</th>
    <th>0</th>
    <th>0.0.0.0:49001</th>
    <th>0.0.0.0:*</th>
    <th>LISTEN</th>
    <th>4682/rpc.rquotad</th>
  </tr>
  <tr>
    <td>tcp</td>
    <td>0</td>
    <td>0.0.0.0:49002</td>
    <td>0.0.0.0:*</td>
    <td>LISTEN</td>
    <td>-</td>
  </tr>
  <tr>
    <td>tcp</td>
    <td>0</td>
    <td>0.0.0.0:49004</td>
    <td>0.0.0.0:*</td>
    <td>LISTEN</td>
    <td>4698/rpc.mountd</td>
  </tr>
  <tr>
    <td>tcp</td>
    <td>0</td>
    <td>:::49002</td>
    <td>:::*</td>
    <td>LISTEN</td>
    <td>-</td>
  </tr>
  <tr>
    <td>tcp</td>
    <td>0</td>
    <td>:::49004</td>
    <td>:::*</td>
    <td>LISTEN</td>
    <td>4698/rpc.mountd</td>
  </tr>
  <tr>
    <td>udp</td>
    <td>0</td>
    <td>0.0.0.0:49001</td>
    <td>0.0.0.0:*</td>
    <td></td>
    <td>4682/rpc.rquotad</td>
  </tr>
  <tr>
    <td>udp</td>
    <td>0</td>
    <td>0.0.0.0:49003</td>
    <td>0.0.0.0:*</td>
    <td></td>
    <td>-</td>
  </tr>
  <tr>
    <td>udp</td>
    <td>0</td>
    <td>0.0.0.0:49004</td>
    <td>0.0.0.0:*</td>
    <td></td>
    <td>4698/rpc.mountd</td>
  </tr>
  <tr>
    <td>udp</td>
    <td>0</td>
    <td>:::49003</td>
    <td>:::*</td>
    <td></td>
    <td>-</td>
  </tr>
  <tr>
    <td>udp</td>
    <td>0</td>
    <td>:::49004</td>
    <td>:::*</td>
    <td></td>
    <td>4698/rpc.mountd</td>
  </tr>
</table>

Теперь, когда эти номера портов установлены и применяются различными службами, можете добавить правила iptables, как было сделано с портами 2049 и 111 для настройки базовой службы NFS.

Доступ к службе NFS из TCP-оболочек

Для таких служб, как vsftpd и sshd, TCP-оболочки в Linux позволяют добавлять информацию в файлы /etc/hosts.allow и /etc/hosts.deny, чтобы указать, какие хосты могут или не могут получить доступ к службе. Сам демон сервера nfsd не включен для TCP-оболочек, но служба rpcbind включена.

Для NFS 3 и более ранних версий просто добавьте в файл /etc/hosts.deny следующую строку, которая будет запрещать доступ к службе rpcbind, а также к службе NFS:

rpcbind: ALL

Однако для серверов под управлением версии NFS 4 по умолчанию строка rpcbind: ALL не позволяет внешним хостам получать информацию о службах RPC (например, NFS) с помощью таких команд, как showmount. Но это не помешает монтировать общий каталог NFS.