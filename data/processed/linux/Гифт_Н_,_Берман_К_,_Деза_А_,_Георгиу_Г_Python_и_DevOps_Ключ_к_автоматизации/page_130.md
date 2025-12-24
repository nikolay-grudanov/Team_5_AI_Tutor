---
source_image: page_130.png
page_number: 130
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.89
tokens: 7527
characters: 1545
timestamp: 2025-12-24T03:04:15.334644
finish_reason: stop
---

Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0x0009d9ce

Device Boot    Start       End   Blocks Id System
/dev/sda1      *        2048  83886079 41942016  83 Linux

Утилита blkid схожа с fdisk в том, что требует прав доступа суперпользователя:

$ blkid /dev/sda

$ sudo blkid /dev/sda
/dev/sda: PTYPE="dos"

Утилита lsblk дает возможность получить ту же информацию, не имея повышенных полномочий:

$ lsblk /dev/sda
NAME   MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
sda     8:0   0 40G  0 disk
└─sda1  8:1   0 40G  0 part /
$ sudo lsblk /dev/sda
NAME   MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
sda     8:0   0 40G  0 disk
└─sda1  8:1   0 40G  0 part /

Утилита blkid с флагом -p для низкоуровневого исследования устройств делает работу очень тщательно и предоставляет много информации об устройствах:

$ blkid -p /dev/sda1
UUID="8e4622c4-1066-4ea8-ab6c-9a19f626755c" TYPE="xfs" USAGE="filesystem"
PART_ENTRY_SCHEME="dos" PART_ENTRY_TYPE="0x83" PART_ENTRY_FLAGS="0x80"
PART_ENTRY_NUMBER="1" PART_ENTRY_OFFSET="2048" PART_ENTRY_SIZE="83884032"

Команда lsblk по умолчанию выводит некоторые интересные свойства устройств:

$ lsblk -P /dev/nvme0n1p1
NAME="nvme0n1p1" MAJ:MIN="259:1" RM="0" SIZE="512M" RO="0" TYPE="part"

Она позволяет и указывать специальные флаги для запроса информации о конкретных свойствах:

lsblk -P -o SIZE /dev/nvme0n1p1
SIZE="512M"

Подобный доступ к свойствам очень упрощает написание сценариев и даже потребление данных со стороны Python.