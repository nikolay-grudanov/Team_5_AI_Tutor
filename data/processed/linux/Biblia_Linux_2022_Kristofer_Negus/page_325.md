---
source_image: page_325.png
page_number: 325
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.55
tokens: 7611
characters: 2083
timestamp: 2025-12-24T04:54:23.408947
finish_reason: stop
---

7. Переименуйте диск на диск с таблицами разделов gpt.

(parted) mklabel gpt
Warning: The existing disk label on /dev/sdb will be destroyed and all data on this disk will be lost. Do you want to continue?
Yes/No? Yes
(parted)

8. Чтобы создать новый раздел, введите команду mkpart. Вам будет предложено задать тип файловой системы, а затем начало и конец раздела. В примере далее раздел называется alldisk, тип файловой системы — xfs, начинается с 1М и заканчивается на 123GB:

(parted) mkpart
Partition name? []? alldisk
File system type? [ext2]? xfs
Start? 1
End? 123GB

9. Дважды проверьте, что диск разделен так, как нужно, нажав клавишу p. (Ваши выходные данные будут отличаться — они зависят от размера диска.)

(parted) p
Model: SanDisk Ultra (scsi)
Disk /dev/sdb: 123GB
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
    <td>123GB</td>
    <td>123GB</td>
    <td>xfs</td>
    <td>alldisk</td>
    <td></td>
  </tr>
</table>

10. Разбиение диска выполнено, однако новый раздел еще не готов к применению. Далее нужно создать в нем файловую систему. Чтобы создать файловую систему в новом разделе диска, возьмите команду mkfs. По умолчанию она создает файловую систему ext2, которую можно использовать в Linux. Однако в большинстве случаев лучше задействовать файловую систему с возможностью ведения журнала, например, ext3, ext4 или xfs. Чтобы создать файловую систему xfs в первом разделе второго жесткого диска, введите следующее:

# mkfs -t xfs /dev/sdb1

СОВЕТ
Вы можете использовать различные команды или параметры этой команды для создания других типов файловых систем. Например, примените команду mkfs.exfat, чтобы создать файловую систему VFAT, mkfs.msdos — для создания DOS, mkfs.ext — для ext4. Файловая система VFAT или exFAT (доступная с Ubuntu) может понадобиться, если нужно обмениваться файлами между системами Linux, Windows и Mac.