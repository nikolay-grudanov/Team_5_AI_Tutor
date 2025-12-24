---
source_image: page_347.png
page_number: 347
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.93
tokens: 7415
characters: 1409
timestamp: 2025-12-24T04:55:00.892799
finish_reason: stop
---

# mkfs -t ext4 /dev/sdc2
mke2fs 1.44.6 (5-Mar-2019)
Creating filesystem with 524288 4k blocks and 131072 inodes
Filesystem UUID: 6379d82e-fa25-4160-8ffa-32bc78d410eee
Superblock backups stored on blocks:
    32768, 98304, 163840, 229376, 294912
Allocating group tables: done
Writing inode tables: done
Creating journal (16384 blocks): done
Writing superblocks and filesystem accounting information: done

Теперь можете монтировать любую из этих файловых систем (например, mkdir /mnt/myusb, mount /dev/sdc1 /mnt/myusb), сделать /mnt/myusb текущим каталогом (cd /mnt/myusb) и создавать в нем файлы.

Управление хранилищем с помощью Cockpit

Большинство описанных в этой главе функций для работы с разделами диска и файловыми системами можно выполнить с помощью веб-интерфейса Cockpit. Запустите Cockpit, откройте веб-интерфейс (имя хоста: 9090) и выберите вкладку Storage (Хранилище). На рис. 12.2 показана вкладка Storage (Хранилище) в Cockpit в системе Fedora.

![На вкладке Storage (Хранилище) находятся устройства хранения данных, файловые системы и действия](../images/ch12_02.png)

Рис. 12.2. На вкладке Storage (Хранилище) находятся устройства хранения данных, файловые системы и действия

Вкладка Storage (Хранилище) дает полный обзор хранилища вашей системы. Она отображает активность чтения и записи устройствами, обновляя данные каждую минуту, а также показывает локальные файловые системы, хранилища