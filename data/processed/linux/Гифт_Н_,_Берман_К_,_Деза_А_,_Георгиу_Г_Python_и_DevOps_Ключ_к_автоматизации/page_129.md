---
source_image: page_129.png
page_number: 129
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.57
tokens: 7483
characters: 1608
timestamp: 2025-12-24T03:04:08.090071
finish_reason: stop
---

Command (m for help): w
The partition table has been altered!

Calling ioctl() to re-read partition table.
Syncing disks.

Утилита parted позволяет получить тот же результат, но ее интерфейс иной:

$ sudo parted /dev/sdaa
GNU Parted 3.1
Using /dev/sdaa
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted) mklabel
New disk label type? gpt
(parted) mkpart
Partition name? [ ]?
File system type? [ext2]?
Start? 0
End? 40%

Для выхода в конце необходимо нажать клавишу q. Создать разделы из командной строки без каких-либо интерактивных приглашений к вводу можно с помощью нескольких команд:

$ parted --script /dev/sdaa mklabel gpt
$ parted --script /dev/sdaa mkpart primary 1 40%
$ parted --script /dev/sdaa print
Disk /dev/sdaa: 11.5GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags:

<table>
  <tr>
    <th>Number</th>
    <th>Start</th>
    <th>End</th>
    <th>Size</th>
    <th>File system</th>
    <th>Name</th>
    <th>Flags</th>
  </tr>
  <tr>
    <td>1</td>
    <td>1049kB</td>
    <td>4614MB</td>
    <td>4613MB</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

Получение информации о конкретном устройстве

Для получения информации о каком-то конкретном устройстве иногда отлично подойдут утилиты lsblk или blkid. fdisk не захочет работать без прав доступа суперпользователя. В следующем примере fdisk выводит информацию об устройстве /dev/sda:

$ fdisk -l /dev/sda
fdisk: cannot open /dev/sda: Permission denied

$ sudo fdisk -l /dev/sda
Disk /dev/sda: 42.9 GB, 42949672960 bytes, 83886080 sectors
Units = sectors of 1 * 512 = 512 bytes