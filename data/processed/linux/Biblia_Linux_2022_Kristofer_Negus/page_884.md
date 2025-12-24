---
source_image: page_884.png
page_number: 884
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.71
tokens: 7567
characters: 1645
timestamp: 2025-12-24T05:10:01.320466
finish_reason: stop
---

884 Приложения

    e   extended
    p   primary partition (1-4)
p
Partition number (1-4): 1
First sector (2048-15667199, default 2048): <ENTER>
Last sector, +sectors or +size{K,M,G} (default 15667199): +100M
Command (m for help): n
Command action
    e   extended
    p   primary partition (1-4)
p
Partition number (1-4): 2
First sector (616448-8342527, default 616448): <ENTER>
Last sector, +sectors or +size{K,M,G} (default 15667199): +200M
Command (m for help): n
Command action
    e   extended
    p   primary partition (1-4)
p
Partition number (1-4): 3
First sector (616448-15667199, default 616448): <ENTER>
Using default value 616448
Last sector, +sectors or +size{K,M,G} (default 15667199): +500M
Command (m for help): t
Partition number (1-4): 2
Hex code (type L to list codes): 82
Changed system type of partition 2 to 82 (Linux swap / Solaris)
Command (m for help): t
Partition number (1-4): 3
Hex code (type L to list codes): 8e
Changed system type of partition 3 to 8e (Linux LVM)
Command (m for help): w
# partprobe /dev/sdb
# grep sdb /proc/partitions
    8      16     7833600  sdb
    8      17     102400  sdb1
    8      18     204800  sdb2
    8      19     512000  sdb3

5. Чтобы поместить файловую систему ext4 в раздел Linux, введите следующее:

# mkfs -t ext4 /dev/sdb1

6. Чтобы создать точку монтирования с именем /mnt/mypart и смонтировать на ней раздел Linux, выполните следующее:

# mkdir /mnt/mypart
# mount -t ext4 /dev/sdb1 /mnt/mypart

7. Чтобы включить раздел подкачки таким образом, чтобы дополнительное пространство подкачки сразу же стало доступно, введите следующее:

# mkswap /dev/sdb2
# swapon /dev/sdb2