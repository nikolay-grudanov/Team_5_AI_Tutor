---
source_image: page_281.png
page_number: 281
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.11
tokens: 7835
characters: 2302
timestamp: 2025-12-24T04:40:11.863552
finish_reason: stop
---

ровать общие файловые ресурсы (share) серверов CIFS непосредственно в дерево каталогов клиента, что дает возможность любым его программам использовать серверные файлы.

В примерах из листинга 6.33 показано использование CIFS-клиента smbclient(1) для получения списка (-L, list) разделяемых ресурсов ① (share) узла WINXP, равно как и для подключения ② к его публичному (-N, по password) разделяемому ресурсу media с последующим скачиванием файлов целиком.

Листинг 6.33. Клиент SMB/CIFS

① lumpy@ubuntu:~$ smbclient -NL //WINXP
Domain=[WINXP] OS=[Windows 5.1] Server=[Windows 2000 LAN Manager]

<table>
  <tr>
    <th>Sharename</th>
    <th>Type</th>
    <th>Comment</th>
  </tr>
  <tr>
    <td>---</td>
    <td>---</td>
    <td>---</td>
  </tr>
  <tr>
    <td>C$</td>
    <td>Disk</td>
    <td>Стандартный общий ресурс</td>
  </tr>
  <tr>
    <td>D$</td>
    <td>Disk</td>
    <td>Стандартный общий ресурс</td>
  </tr>
  <tr>
    <td>ADMIN$</td>
    <td>Disk</td>
    <td>Удаленный Admin</td>
  </tr>
  <tr>
    <td>IPC$</td>
    <td>IPC</td>
    <td>IPC Service</td>
  </tr>
  <tr>
    <td>media</td>
    <td>Disk</td>
    <td>Фото, видео, и т. д.</td>
  </tr>
</table>

② lumpy@ubuntu:~$ smbclient -N //WINXP/media
Domain=[WINXP] OS=[Windows 5.1] Server=[Windows 2000 LAN Manager]
smb: \> cd DCIM\
smb: \DCIM\> dir

<table>
  <tr>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td>Dd595.jpg</td>
    <td>A</td>
    <td>4494092</td>
    <td>Sun Feb 13 16:24:04 2011</td>
  </tr>
  <tr>
    <td>Dd596.jpg</td>
    <td>A</td>
    <td>3842680</td>
    <td>Sun Feb 13 16:14:56 2011</td>
  </tr>
  <tr>
    <td>Dd680.jpg</td>
    <td>A</td>
    <td>4087313</td>
    <td>Sun Feb 13 03:10:45 2011</td>
  </tr>
  <tr>
    <td>Dd681.jpg</td>
    <td>A</td>
    <td>4108278</td>
    <td>Sun Feb 13 15:58:38 2011</td>
  </tr>
</table>

61192 blocks of size 1048576. 10915 blocks available

smb: \DCIM\> get Dd680.jpg
getting file \DCIM\Dd680.jpg of size 4087313 as Dd680.jpg (72572,9 KiloBytes/sec)
(average 72573,0 KiloBytes/sec)

smb: \DCIM\> quit

Листинг 6.34 иллюстрирует использование ядерного модуля cifs для монтирования публичного (-o guest) ресурса media с узла WINXP в каталог /mnt/network/winxp/media.