---
source_image: page_380.png
page_number: 380
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.28
tokens: 7697
characters: 2223
timestamp: 2025-12-24T04:43:22.106919
finish_reason: stop
---

[1:0:0:0] cd/dvd TSSTcorp DVD+-RW TS-U633J D600 /dev/sr0
[4:0:0:0] disk JetFlash Transcend 2GB 8.07 /dev/sdc

morty@ubuntu:~$ sudo parted /dev/sdc
GNU Parted 3.2
Using /dev/sdc
Welcome to GNU Parted! Type 'help' to view a list of commands.

(parted) mklabel gpt
Warning: The existing disk label on /dev/sdc will be destroyed and all data on this disk will be lost. Do you want to continue?
Yes/No? Yes

(parted) mkpart loaders fat16 @ 128M
Warning: The resulting partition is not properly aligned for best performance.
Ignore/Cancel? Ignore

(parted) mkpart rootfs ext4 128M 100%
Warning: The resulting partition is not properly aligned for best performance.
Ignore/Cancel? Ignore

(parted) print
Model: JetFlash Transcend 2GB (scsi)
Disk /dev/sdc: 2020MB
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
    <td>17,4kB</td>
    <td>128MB</td>
    <td>128MB</td>
    <td>fat16</td>
    <td>loaders</td>
    <td></td>
  </tr>
  <tr>
    <td>2</td>
    <td>128MB</td>
    <td>2020MB</td>
    <td>1892MB</td>
    <td>ext4</td>
    <td>rootfs</td>
    <td></td>
  </tr>
</table>

(parted) set 1 esp on
(parted) print

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
    <td>17,4kB</td>
    <td>128MB</td>
    <td>128MB</td>
    <td>fat16</td>
    <td>loaders</td>
    <td>boot, esp</td>
  </tr>
  <tr>
    <td>2</td>
    <td>128MB</td>
    <td>2020MB</td>
    <td>1892MB</td>
    <td>ext4</td>
    <td>rootfs</td>
    <td></td>
  </tr>
</table>

(parted) quit
Information: You may need to update /etc/fstab.

После создания эти разделы «форматируются» (листинг 10.16), т.е. на них создаются файловые системы: ① FAT для ESP и ② EXT4 для корневой ФС. Нужно отметить, что конкретные экземпляры файловых систем в Linux идентифицируются или универсально-уникальными идентификаторами W:[UUID], или просто уникальным Volume ID. Эти идентификаторы позволяют найти файловую систему вне зависимо-