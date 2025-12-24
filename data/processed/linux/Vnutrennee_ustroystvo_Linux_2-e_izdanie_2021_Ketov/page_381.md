---
source_image: page_381.png
page_number: 381
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.62
tokens: 7505
characters: 1897
timestamp: 2025-12-24T04:43:17.281465
finish_reason: stop
---

сти от порядковых номеров устройства и раздела, на котором она расположена, что крайне полезно при использовании на съемном накопителе, таком как USB-флеш.

Листинг 10.16. Форматирование разделов (создание файловых систем)

1 morty@ubuntu:~$ sudo mkfs -t vfat -v /dev/sdc1
mkfs.fat 4.1 (2017-01-24)
...
Volume ID is 08c8bdb9 , no volume label.
2 morty@ubuntu:~$ sudo mkfs -t ext4 /dev/sdc2
mke2fs 1.45.3 (14-Jul-2019)
Creating filesystem with 461801 4k blocks and 115680 inodes
Filesystem UUID: 71002c88-0b02-4ac0-8cd4-65c4eb0e454b
Superblock backups stored on blocks:
    32768, 98304, 163840, 229376, 294912
Allocating group tables: done
Writing inode tables: done
Creating journal (8192 blocks): done
Writing superblocks and filesystem accounting information: done

Следующим логичным шагом является, собственно, помещение компонент ОС в корневую файловую систему, что можно сделать вручную, дублируя их программы, библиотеки, конфигурационные файлы и данные из исходной системы (например, как было показано в листинге 9.2). При необходимости выборочного копирования компонент ручной подход чрезвычайно трудоемок, поэтому на данном этапе используют разнообразные автоматизированные средства, например (уже знакомый по главе 9) debootstrap(9), что проиллюстрировано ①② в листинге 10.17.

Кроме инсталляции минимального набора компонент будущей системы ее необходимо минимально сконфигурировать, а именно — указать ③ в таблице файловых систем fstab(5) то, какая ФС является «настоящей» корневой ①, т. е. должна монтироваться в корень дерева каталогов. Точно так же поступают и с файловой системой ② ESP-раздела, который по соглашению монтируют в каталог /boot/efi.

Листинг 10.17. Инсталляция минимальной системы

1 morty@ubuntu:~$ sudo mount /dev/sdc2 /mnt
2 morty@ubuntu:~$ sudo debootstrap --variant=minbase --include=lsb-release eoan /mnt
I: Retrieving InRelease
I: Checking Release signature