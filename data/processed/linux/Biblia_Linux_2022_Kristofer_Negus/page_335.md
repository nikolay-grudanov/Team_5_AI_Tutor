---
source_image: page_335.png
page_number: 335
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.58
tokens: 7581
characters: 2050
timestamp: 2025-12-24T04:54:42.783601
finish_reason: stop
---

1. Возьмите диск с некоторым количеством свободного пространства и создайте на нем раздел типа LVM (8e). Затем возьмите команду pvcreate, чтобы идентифицировать этот раздел как физический том LVM. Процесс с использованием устройства /dev/sdb6 описан ранее в разделе «Создание диска с несколькими разделами».

2. Чтобы добавить этот физический том в новую группу томов, примените команду vgcreate. Как создать группу томов myvg0 с помощью устройства /dev/sdb6, показывает следующая команда:

# vgcreate myvg0 /dev/sdc6
    Volume group "myvg0" successfully created

3. Чтобы просмотреть новую группу томов, введите:

# vgdisplay myvg0
--- Volume group ---
VG Name                myvg0
...
VG Size                <4.00 GiB
PE Size                 4.00 MiB
Total PE               1023
Alloc PE / Size         0 / 0
Free  PE / Size        1023 / <4.00 MiB

4. Доступны все 1023 физических экстента (по 4 МиБ каждый). Далее приведен пример того, как создать логический том из части пространства в этой группе томов, а затем проверить, существует ли устройство для этого логического тома:

# lvcreate -n music -L 1G myvg0
    Logical volume "music" created
# ls /dev/mapper/myvg0*
/dev/mapper/myvg0-music

5. Как видно в примере, было создано устройство с именем /dev/mapper/myvg0-music. Теперь его можно использовать для установки и монтирования файловой системы, как и обычные разделы в начале этой главы, например:

# mkfs -t ext4 /dev/mapper/myvg0-music
# mkdir /mnt/mymusic
# mount /dev/mapper/myvg0-music /mnt/mymusic
# df -h /mnt/mymusic
Filesystem           Size  Used Avail Use% Mounted on
/dev/mapper/myvg0-music 976M  2.6M  987M   1% /mnt/mymusic

6. Как и в случае с обычными разделами, логические тома можно монтировать постоянно, добавив запись в файл /etc/fstab, например:

/dev/mapper/myvg0-music /mnt/mymusic ext4 defaults 1 2

При следующей перезагрузке логический том автоматически монтируется в каталоге /mnt/mymusic. (Обязательно размонтируйте логический том и удалите эту строку, если хотите отсоединить USB-накопитель от компьютера.)