---
source_image: page_329.png
page_number: 329
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.21
tokens: 7795
characters: 1917
timestamp: 2025-12-24T04:54:39.963982
finish_reason: stop
---

3. Перед сохранением проверьте разбиение, введя параметр p. Обратите внимание на то, что существует пять разделов (sdc1, sdc2, sdc3, sdc5 и sdc6) и между столбцами Start и End сектор sdc4 поглощается секторами sdc5 и sdc6:

Command (m for help): p
...
Device   Boot   Start   End   Sectors   Size Id Type
/dev/sdb1        2048 10487807 10485760 5G 83 Linux
/dev/sdb2    10487808 20973567 10485760 5G 82 Linux swap / Solaris
/dev/sdb3    20973568 27265023 6291456 3G 83 Linux
/dev/sdb4    27265024 240254975 212989952 101.6G 5 Extended
/dev/sdb5    27267072 33558527 6291456 3G 83 Linux
/dev/sdb6    33560576 41949183 8388608 4G 83 Linux

4. Тип раздела по умолчанию — это Linux. Я решил, что хочу использовать некоторые разделы для пространства подкачки (введите 82), FAT32 (введите x) и Linux LVM (введите 8e). Для этого набрал параметр t и указал нужный тип раздела. Введите параметр L, чтобы просмотреть список типов разделов:

Command (m for help): t
Partition number (1-6): 2
Hex code (type L to list codes): 82
Changed type of partition 'Linux' to 'Linux swap / Solaris'.

Command (m for help): t
Partition number (1-6): 5
Hex code (type L to list codes): c
Changed type of partition 'Linux' to 'W95 FAT32 (LBA)'.

Command (m for help): t
Partition number (1-6): 6
Hex code (type L to list codes): 8e
Changed type of partition 'Linux' to 'Linux LVM'.

5. Теперь следует проверить, соответствует ли таблица разделов тому, что нужно, а затем записать изменения:

Command (m for help): p
...
Device   Boot   Start   End   Sectors   Size Id Type
/dev/sdb1        2048 10487807 10485760 5G 83 Linux
/dev/sdb2    10487808 20973567 10485760 5G 82 Linux swap / Solaris
/dev/sdb3    20973568 27265023 6291456 3G 83 Linux
/dev/sdb4    27265024 240254975 212989952 101.6G 5 Extended
/dev/sdb5    27267072 33558527 6291456 3G c W95 FAT32 (LBA)
/dev/sdb6    33560576 41949183 8388608 4G 8e Linux LVM

Command (m for help): w