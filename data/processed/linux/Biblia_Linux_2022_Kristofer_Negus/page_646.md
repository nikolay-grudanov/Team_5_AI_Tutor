---
source_image: page_646.png
page_number: 646
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.45
tokens: 7713
characters: 2240
timestamp: 2025-12-24T05:03:31.332536
finish_reason: stop
---

Большинство файлов журнала отображаются с помощью команд cat, head, tail, more или less. Однако некоторые из них нуждаются в специальных командах для просмотра (табл. 22.4).

Таблица 22.4. Файлы журнала, требующие специальных команд

<table>
  <tr>
    <th>Имя файла</th>
    <th>Команда просмотра</th>
  </tr>
  <tr>
    <td>btmp</td>
    <td>dump-utmp btmp</td>
  </tr>
  <tr>
    <td>dmesg</td>
    <td>dmesg</td>
  </tr>
  <tr>
    <td>lastlog</td>
    <td>lastlog</td>
  </tr>
  <tr>
    <td>wtmp</td>
    <td>dump-utmp wtmp</td>
  </tr>
</table>

С переходом Fedora, RHEL, Ubuntu и других дистрибутивов Linux на systemd, который управляет процессом загрузки и службами, как отмечалось ранее, изменился механизм сбора и отображения сообщений журнала, связанных с ядром и системными службами. Эти сообщения направляются в журнал systemd и могут быть отображены с помощью команды journalctl.

Вы можете просматривать сообщения журнала непосредственно из журнала systemd, а не просто перечислять содержимое файлов /var/log. На самом деле в последней версии Fedora просто нет файла /var/log/messages, в который многие службы по умолчанию направляют сообщения журнала. Вместо этого вы можете использовать команду journalctl для отображения сообщений журнала различными способами. Чтобы просмотреть сообщения ядра, введите следующую команду:

# journalctl -k
Logs begin at Sun 2019-06-09 18:59:23 EDT, end at Sun 2019-10-20 18:11:06 EDT.
Oct 19 11:43:04 localhost.localdomain kernel:
    Linux version 5.0.9-301.fc30.x86_64
    (mockbuild@bkernel04.phx2.fedoraproject.org)
    (gcc version 9.0.1 20190312 (Red Hat 9.0.1-0.10) (GCC))
    #1 SMP Tue Apr 23 23:57:35 UTC 2019
Oct 19 11:43:04 localhost.localdomain kernel: Command line:
    BOOT_IMAGE=(hd0,msdos1)/vmlinuz-5.0.9-301.fc30.x86_64
    root=/dev/mapper/fedora_localhost--live-root ro
    resume=/dev/mapper/fedora_localhost--live-swap
    rd.lvm.lv=fedora_localhost-live/root
    rd.lvm.lv=fedora_localhost-live/swap rhgb quiet
...

Чтобы просмотреть сообщения, связанные с определенной службой, используйте параметр -u, после которого указано имя службы, как в этом примере:

# journalctl -u NetworkManager.service
# journalctl -u httpd.service
# journalctl -u avahi-daemon.service