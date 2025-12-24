---
source_image: page_333.png
page_number: 333
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.25
tokens: 7581
characters: 2120
timestamp: 2025-12-24T04:54:35.974569
finish_reason: stop
---

# lvdisplay vg_abc
--- Logical volume ---
LV Name                /dev/vg_abc/lv_root
VG Name                vg_abc
LV UUID                33VeDc-jd01-hlCc-RMuB-tkcw-QvFi-cKCZqa
LV Write Access        read/write
LV Status              available
# open                 1
LV Size                50.00 GiB
Current LE             12800
Segments               1
Allocation             inherit
Read ahead sectors     auto
- currently set to     256
Block device           253:0
--- Logical volume ---
LV Name                /dev/vg_abc/lv_home
VG Name                vg_abc
...
LV Size                92.64 GiB
--- Logical volume ---
LV Name                /dev/vg_abc/lv_swap
VG Name                vg_abc
...
LV Size                5.88 GiB

Существует три логических тома, определяющих пространство из vg_abc. Каждый логический том связан с именем устройства, которое включает имя группы томов и имя логического тома: /dev/vg_abc/lv_root (50 Гбайт), /dev/vg_abc/lv_home (92,64 Гбайт) и /dev/vg_abc/lv_swap (5,88 Гбайт). Другие устройства, связанные с этими именами, находятся в каталогах /dev/mapper: vg_abc-lv_home, vg_abc-lv_root и vg_abc-lv_swap. Чтобы ссылаться на эти логические тома, можно использовать любой набор имен.

Корневой и домашний логические тома форматируются как файловые системы ext4, а логический том подкачки — как раздел подкачки. Заглянем в файл /etc/fstab, чтобы увидеть, как применяются эти логические тома:

# grep vg_ /etc/fstab
/dev/mapper/vg_abc-lv_root /      ext4 defaults 1 1
/dev/mapper/vg_abc-lv_home /home   ext4 defaults 1 2
/dev/mapper/vg_abc-lv_swap swap    swap defaults 0 0

На рис. 12.1 показано, как различные разделы, группы томов и логические тома соотносятся со всей файловой системой Linux. Устройство sda1 форматируется как файловая система и монтируется в каталог /boot. Устройство sda2 предоставляет место для группы томов vg_abc. Затем логические тома lv_home и lv_root монтируются в каталоги /home и / соответственно.

Если вам не хватает места в любом из логических томов, можно назначить больше места из группы томов. Если в группе томов не хватает места, можно добавить