---
source_image: page_883.png
page_number: 883
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.87
tokens: 7453
characters: 1436
timestamp: 2025-12-24T05:09:57.395675
finish_reason: stop
---

Глава 12. Управление дисками и файлами

1. Чтобы определить имя устройства USB-накопителя, введите следующее и вставьте USB-накопитель (нажмите сочетание клавиш Ctrl+C после того, как увидите соответствующие сообщения):

# journalctl -f
kernel: [sdb] 15667200 512-byte logical blocks:
    (8.02 GB/7.47 GiB)
Feb 11 21:55:59 cnegus kernel: sd 7:0:0:0:
    [sdb] Write Protect is off
Feb 11 21:55:59 cnegus kernel: [sdb] Assuming
    drive cache: write through
Feb 11 21:55:59 cnegus kernel: [sdb] Assuming
    drive cache: write through

2. Чтобы перечислить разделы на флеш-накопителе USB в системе RHEL 6, введите следующую команду:

# fdisk -c -u -l /dev/sdb

Чтобы перечислить разделы в системе RHEL 7, RHEL 8 или Fedora, введите:

# fdisk -l /dev/sdb

3. Чтобы удалить разделы на накопителе USB, предположив, что это device/dev/sdb, выполните следующие действия:

# fdisk /dev/sdb
Command (m for help): d
Partition number (1-6): 6
Command (m for help): d
Partition number (1-5): 5
Command (m for help): d
Partition number (1-5): 4
Command (m for help): d
Partition number (1-4): 3
Command (m for help): d
Partition number (1-4): 2
Command (m for help): d
Selected partition 1
Command (m for help): w
# partprobe /dev/sdb

4. Чтобы добавить на USB-накопитель Linux-раздел объемом 100 Мбайт, раздел подкачки объемом 200 Мбайт и LVM-раздел объемом 500 Мбайт, введите следующее:

# fdisk /dev/sdb

Command (m for help): n
Command action