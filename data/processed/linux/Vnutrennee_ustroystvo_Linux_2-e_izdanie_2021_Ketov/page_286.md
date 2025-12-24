---
source_image: page_286.png
page_number: 286
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.66
tokens: 7687
characters: 2073
timestamp: 2025-12-24T04:40:22.485111
finish_reason: stop
---

Nmap scan report for 192.168.0.1
Host is up, received syn-ack (0.054s latency).
Scanned at 2019-11-24 11:46:18 MSK for 1s
Not shown: 996 closed ports
Reason: 996 conn-refused

<table>
  <tr>
    <th>PORT</th>
    <th>STATE</th>
    <th>SERVICE</th>
    <th>REASON</th>
  </tr>
  <tr>
    <td>22/tcp</td>
    <td>open</td>
    <td>ssh</td>
    <td>syn-ack</td>
  </tr>
  <tr>
    <td>80/tcp</td>
    <td>open</td>
    <td>http</td>
    <td>syn-ack</td>
  </tr>
  <tr>
    <td>1900/tcp</td>
    <td>open</td>
    <td>upnp</td>
    <td>syn-ack</td>
  </tr>
  <tr>
    <td>49152/tcp</td>
    <td>open</td>
    <td>unknown</td>
    <td>syn-ack</td>
  </tr>
</table>

6.5.3. Мониторинг сетевых соединений процессов

Интерфейс сокетов в целом является продолжением идеи «файлов», специально предназначенных для межпроцессного взаимодействия, некоторым развитием «файловой» природы простейших именованных и неименованных каналов.

Таким образом, сокеты сетевых семейств ip(7), ipv6(7) и прочие обладают «файловыми» свойствами точно так же, как и локальные сокеты unix(7). Например, каждый сетевой сокет идентифицируется при помощи файлового (!) дескриптора в таблице открытых файлов процесса, что проиллюстрировано в листинге 6.38 при помощи lsof(1) и ss(8).

Листинг 6.38. Файловые дескрипторы сетевых сокетов

lumpy@ubuntu:~$ pgrep lftp
6056
lumpy@ubuntu:~$ lsof -i 4 -a -p 6056
COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
lftp 6056 lumpy 4u IPv4 88150 0t0 TCP ubuntu.local:43578->napoleon.ftp.acc.umu.se:ftp (ESTABLISHED)

lumpy@ubuntu:~$ ss -p dport = :ftp
Netid State Recv-Q Send-Q Local Address:Port Peer Address:Port
tcp ESTAB 0 0 192.168.0.101:43578 194.71.11.173:ftp users:(("lftp",pid=6056,fds=4))

Более детально проследить за жизненным циклом сетевого сокета позволяет трассировка «сокетных» системных вызовов socket(2), connect(2), bind(2), listen(2), accept(2), send(2) и recv(3).

В примере из листинга 6.39 показана трассировка «клиентского» сокета пользовательского агента curl(1), загружающего Web-ресурс http://www.gnu.org/graphics/agnuheadterm-xterm.txt.