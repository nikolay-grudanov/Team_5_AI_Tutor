---
source_image: page_324.png
page_number: 324
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.16
tokens: 7483
characters: 1719
timestamp: 2025-12-24T04:54:15.042886
finish_reason: stop
---

kernel: usb 4-1: Product: Ultra
kernel: usb 4-1: Manufacturer: SanDisk
...
kernel: sd 6:0:0:0: Attached scsi generic sg2 type 0
kernel: sdb: sdb1
kernel: sd 6:0:0:0: [sdb] Attached SCSI removable disk
udisksd[809]: Mounted /dev/sdb1 at /run/media/chris/7DEB-B010
    on behalf of uid 1000

3. Из выходных данных видно, что USB-накопитель был найден и назначен файлу /dev/sdb. (Имя вашего устройства может отличаться.) Он также содержит один форматированный раздел sdb1. Убедитесь, что вы точно определили нужный диск, иначе можете потерять все данные с других дисков.

4. Если USB-накопитель монтируется автоматически, размонтируйте его. Пример иллюстрирует, как найти разделы USB и размонтировать их:

# mount | grep sdb
/dev/sdb1 on /run/media...
# umount /dev/sdb1

5. С помощью команды parted создайте разделы на USB-накопителе. Например, если вы форматируете второй диск USB, SATA или SCSI (sdb), введите следующее:

# parted /dev/sdb
GNU Parted 3.2
Using /dev/sdb
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted)

Теперь вы находитесь в режиме команды parted, в котором можно применять набор однобуквенных команд для работы с разделами.

6. У нового, чистого USB-накопителя может быть один раздел, полностью отведенный для файловой системы, совместимой с системой Windows, например VFAT или FAT32. Используйте команду p для просмотра всех разделов, чтобы удалить раздел. Вот как это выглядело у меня:

(parted) p
Model: SanDisk Ultra (scsi)
Disk /dev/sdb: 123GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags:

Number    Start   End     Size   Type   File system   Flags
1         16.4kB  123GB   123GB  primary  fat32        lba
(parted) rm
Partition number? 1