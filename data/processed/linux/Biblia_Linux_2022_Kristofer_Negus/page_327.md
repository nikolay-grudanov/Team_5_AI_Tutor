---
source_image: page_327.png
page_number: 327
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.89
tokens: 7650
characters: 2254
timestamp: 2025-12-24T04:54:27.618719
finish_reason: stop
---

В данном случае я настроил раздел Master Boot Record (MBR), чтобы проиллюстрировать работу расширенных разделов и применить более старую команду fdisk. Я создал два раздела по 5 Гбайт (sdb1 и sdb2), два по 3 Гбайт (sdb3 и sdb5) и один на 4 Гбайт (sdb6). Устройство sdb4 будет использоваться как расширенный раздел, который занимает все оставшееся дисковое пространство. Пространство для разделов sdb5 и sdb6 берется из расширенного раздела. Таким образом, остается достаточно места для создания новых разделов.

Как и в предыдущем примере, вставьте USB-накопитель и определите имя устройства (в моем случае это /dev/sdb). Кроме того, обязательно отключите все разделы, которые монтируются автоматически при подключении USB-накопителя.

СОВЕТ
При указании размера каждого раздела введите знак плюс и количество мегабайт или гигабайт, которые вы хотите ему назначить. Например, укажите +1024M для создания 1024-мегабайтного раздела или +10G — для 10-гигабайтного. Обязательно используйте знак плюс (+) и букву M или G! Если забыть их указать, команда fdisk будет разделять диск на секторы, что может привести к неожиданным результатам.

1. Я начал процесс с перезаписи USB-накопителя командой dd (dd if=/dev/zero of=/dev/sd<number> bs=1M count=100). Это позволило начать с новой главной загрузочной записи. Будьте осторожны и указывайте правильный номер диска, иначе можно стереть всю операционную систему!

2. Создайте шесть новых разделов.

# fdisk /dev/sdb
Welcome to fdisk (util-linux 2.33.2).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Device does not contain a recognized partition table.
Created a new DOS disklabel with disk identifier 0x8933f665.
Command (m for help): n
Partition type
    p   primary (0 primary, 0 extended, 4 free)
    e   extended (container for logical partitions)
Select (default p): p
Partition number (1-4, default 1): 1
First sector (2048-240254975, default 2048):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-240254975, default 240254975): +5G

Created a new partition 1 of type 'Linux' and of size 5 GiB.

Command (m for help): n
Partition type
    p   primary (1 primary, 0 extended, 3 free)
    e   extended (container for logical partitions)