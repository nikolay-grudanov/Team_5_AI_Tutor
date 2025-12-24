---
source_image: page_268.png
page_number: 268
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.35
tokens: 7907
characters: 2432
timestamp: 2025-12-24T04:39:46.374635
finish_reason: stop
---

lumpy@ubuntu:~$ ssh jake@grex.org ldd /usr/bin/ssh

/usr/bin/ssh:

<table>
  <tr>
    <th>Start</th>
    <th>End</th>
    <th>Type</th>
    <th>Open</th>
    <th>Ref</th>
    <th>GrpRef</th>
    <th>Name</th>
  </tr>
  <tr>
    <td>17645000</td>
    <td>37681000</td>
    <td>exe</td>
    <td>1</td>
    <td>0</td>
    <td>0</td>
    <td>/usr/bin/ssh</td>
  </tr>
  <tr>
    <td>0b348000</td>
    <td>2b3c5000</td>
    <td>rlib</td>
    <td>0</td>
    <td>1</td>
    <td>0</td>
    <td>/usr/lib/libcrypto.so.43.1</td>
  </tr>
  <tr>
    <td>06757000</td>
    <td>2675c000</td>
    <td>rlib</td>
    <td>0</td>
    <td>1</td>
    <td>0</td>
    <td>/usr/lib/libutil.so.13.0</td>
  </tr>
  <tr>
    <td>00799000</td>
    <td>207a1000</td>
    <td>rlib</td>
    <td>0</td>
    <td>1</td>
    <td>0</td>
    <td>/usr/lib/libz.so.5.0</td>
  </tr>
  <tr>
    <td>0f668000</td>
    <td>2f698000</td>
    <td>rlib</td>
    <td>0</td>
    <td>1</td>
    <td>0</td>
    <td>/usr/lib/libc.so.92.3</td>
  </tr>
  <tr>
    <td>0ab98000</td>
    <td>0ab98000</td>
    <td>ld.so</td>
    <td>0</td>
    <td>1</td>
    <td>0</td>
    <td>/usr/libexec/ld.so</td>
  </tr>
</table>

lumpy@ubuntu:~$ env | grep SSH
SSH_AGENT_PID=21655
SSH_AUTH_SOCK=/tmp/ssh-Eehhsbx21654/agent.21654

lumpy@ubuntu:~$ ls -l /tmp/ssh-Eehhsbx21654/agent.21654
srw------- 1 lumpy lumpy 0 марта 28 23:07 /tmp/ssh-Eehhsbx21654/agent.21654

Протокол SSH получил широкое распространение далеко за рамками своего изначального предназначения. Кроме непосредственного удаленного доступа, он используется другими командами для своих нужд. Например (см. листинг 6.19), команды scp(1) и sftp(1) используют ssh(1) для безопасного сетевого копирования файлов ①②, а команда rsync(1) — для сетевой синхронизации (копирование изменяющихся) файлов ③.

Все эти (и другие, подобные им) команды используют ssh(1) для запуска некоторой «серверной» программы на удаленном узле (в частности, scp и rsync запускают сами себя, а sftp запускает sftp-server(8)), с которой и взаимодействуют через защищенное соединение.

Листинг 6.19. Копирование файлов поверх SSH

① lumpy@ubuntu:~$ scp *.pdf jake@grex.org:
tcpdump.pdf                100%   37KB  37.3KB/s  00:00
Wireshark_Display_Filters.pdf 100%  38KB  38.0KB/s  00:00
② lumpy@ubuntu:~$ sftp jake@grex.org
Connected to grex.org.
sftp> ls
OPENME.txz                README.gz
Wireshark_Display_Filters.pdf linuxperftools.png
tcpdump.pdf
sftp> exit