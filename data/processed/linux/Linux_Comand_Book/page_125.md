---
source_image: page_125.png
page_number: 125
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.14
tokens: 6034
characters: 1461
timestamp: 2025-12-24T04:07:28.484364
finish_reason: stop
---

#umount /dev/hdalO
#fsck -f /dev/hdalO
Pass 1: Checking inodes, blocks, and sizes Pass 2: Checking directory structure Pass 3: Checking directory connectivity Pass 4: Checking reference counts Pass 5: Checking group summary information /home: 172/1281696 files (11.6% noncontiguous), 1405555/2562359 blocks

Программа fsck - это интерфейс для ряда программ проверки файловых систем из директории /sbin с названиями, начинающимися с "fsck". Поддерживаются только определенные типы файловых систем; вы можете вывести их список с помощью следующей команды.

$ ls /sbin/fsck.* | cut -d. -f2 fc."

Полезные опции
- A    Проверить все диски, перечисленные в файле /etc/fstab, по порядку
-N    Вывести описание проверки, которая будет проведена, но завершить работу, не проводя ее
- r   Исправлять ошибки интерактивно, запрашивая подтверждение перед каждым исправлением
- a   Исправлять ошибки автоматически (только если вы действительно знаете, что делаете; в противном случае вы можете серьезно повредить файловую систему)

sync    coreutils
/bin   stdin stdout -file -opt --help --version

Команда sync сбрасывает на диски содержимое всех дисковых кэшей. В нормальном режиме ядро может буферизовать в памяти операции чтения, записи, изменений атрибутов и другие операции с диском. Команда sync записывает накопленные изменения на диск. Как правило, вам не нужно выполнять эту команду, но если (скажем) вы собираетесь проделать какую-то рискованную операцию, которая