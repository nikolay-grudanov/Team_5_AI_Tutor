---
source_image: page_336.png
page_number: 336
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.25
tokens: 7512
characters: 1855
timestamp: 2025-12-24T04:54:40.338998
finish_reason: stop
---

Расширение логических томов LVM

Если на логическом томе не хватает места, его можно добавить, и для этого не требуется размонтировать том. Нужно лишь иметь свободное место в группе томов, а также увеличить логический том и файловую систему. Основываясь на процессе, описанном в предыдущем разделе, вот как можно расширить логический том.

1. Обратите внимание на то, сколько места в данный момент на логическом томе, а затем проверьте, доступно ли оно в группе томов логического тома:

# vgdisplay myvg0
...
VG Size                <4.00 MiB
PE Size                4.00 MiB
Total PE               1023
Alloc PE / Size        256 / 1.00 GiB
Free PE / Size         767 / <3.00 GiB
# df -h /mnt/mymusic/
Filesystem            Size Used Avail Use% Mounted on
/dev/mapper/myvg0-music    976M 2.6M 987M 1% /mnt/mymusic

2. Разверните логический том с помощью команды lvextend:

# lvextend -L +1G /dev/mapper/myvg0-music
Size of logical volume myvg0/music changed
from 1.00GiB to 2.00 GiB (512 extents).
Logical volume myvg0/music successfully resized

3. Измените размер файловой системы в соответствии с новым размером логического тома:

# resize2fs -p /dev/mapper/myvg0-music

4. Убедитесь, что файловая система изменена и включает в себя дополнительное пространство диска:

# df -h /mnt/mymusic/
Filesystem            Size Used Avail Use% Mounted on
/dev/mapper/myvg0-music    2.0G 3.0M 1.9G 1% /mnt/mymusic

Из примера видно, что файловая система теперь больше примерно на 1 Гбайт.

Монтирование файловых систем

Теперь, когда мы рассмотрели варианты разделения диска и файловых систем, я хочу сделать шаг назад и поговорить о том, как настраиваются файловые системы для постоянного подключения к системе Linux.
Большинство разделов жесткого диска, созданных при установке Linux, монтируются автоматически при загрузке системы. При установке Fedora, Ubuntu,