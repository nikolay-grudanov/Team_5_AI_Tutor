---
source_image: page_428.png
page_number: 428
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.40
tokens: 7649
characters: 2317
timestamp: 2025-12-24T04:57:28.480193
finish_reason: stop
---

<table>
  <tr>
    <th>cryptsetup.target</th>
    <td>loaded active active</td>
    <td>Encrypted Volumes</td>
  </tr>
  <tr>
    <th>getty.target</th>
    <td>loaded active active</td>
    <td>Login Prompts</td>
  </tr>
  <tr>
    <th>graphical.target</th>
    <td>loaded active active</td>
    <td>Graphical Interface</td>
  </tr>
  <tr>
    <th>local-fs-pre.target</th>
    <td>loaded active active</td>
    <td>Local File Systems (Pre)</td>
  </tr>
  <tr>
    <th>local-fs.target</th>
    <td>loaded active active</td>
    <td>Local File Systems</td>
  </tr>
  <tr>
    <th>multi-user.target</th>
    <td>loaded active active</td>
    <td>Multi-User</td>
  </tr>
  <tr>
    <th>network.target</th>
    <td>loaded active active</td>
    <td>Network</td>
  </tr>
  <tr>
    <th>remote-fs.target</th>
    <td>loaded active active</td>
    <td>Remote File Systems</td>
  </tr>
  <tr>
    <th>sockets.target</th>
    <td>loaded active active</td>
    <td>Sockets</td>
  </tr>
  <tr>
    <th>sound.target</th>
    <td>loaded active active</td>
    <td>Sound Card</td>
  </tr>
  <tr>
    <th>swap.target</th>
    <td>loaded active active</td>
    <td>Swap</td>
  </tr>
  <tr>
    <th>sysinit.target</th>
    <td>loaded active active</td>
    <td>System Initialization</td>
  </tr>
  <tr>
    <th>syslog.target</th>
    <td>loaded active active</td>
    <td>Syslog</td>
  </tr>
</table>

Файлы конфигурации системы Linux находятся в каталогах /lib/systemd/system и /etc/systemd/system. Вы можете использовать команду ls для просмотра этих каталогов, но предпочтительнее делать это с помощью параметров команды systemctl следующим образом:

# systemctl list-unit-files --type=service
UNIT FILE	STATE
...
cups.service	enabled
...
dbus.service	static
...
NetworkManager.service	enabled
...
poweroff.service	static
...
sshd.service	enabled
sssd.service	disabled
...
276 unit files listed.

Все файлы конфигурации юнита, показанные в предыдущем примере, связаны с сервисным юнитом. Файлы конфигурации для целевых юнитов отображаются следующим образом:

# systemctl list-unit-files --type=target
UNIT FILE	STATE
anaconda.target	static
basic.target	static
bluetooth.target	static
cryptsetup.target	static
ctrl-alt-del.target	disabled
default.target	enabled
...
shutdown.target	static
sigpwr.target	static
smartcard.target	static