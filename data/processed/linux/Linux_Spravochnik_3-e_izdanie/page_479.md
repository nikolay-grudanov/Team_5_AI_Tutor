---
source_image: page_479.png
page_number: 479
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.10
tokens: 11788
characters: 1903
timestamp: 2025-12-24T03:36:42.524513
finish_reason: stop
---

5. Скопируйте bootsect.lnx на дискету, отформатированную в DOS.

% mount -t msdos /dev/fd0 /mnt
% cp /bootsect.lnx /mnt
% umount /mnt

6. Перезагрузитесь в Windows NT и скопируйте загрузочный сектор с дискеты на диск. Например, с помощью команды копирования:

C:> copy a:\bootsect.lnx c:\bootsect.lnx

Неважно, где на диске будет расположен загрузочный сектор, потому что это расположение указывается загрузчику NT на шаге 8.

7. Измените атрибуты файла boot.ini¹, сняв атрибуты «системный» и «только для чтения», чтобы его было можно редактировать.

C:> attrib -s -r c:\boot.ini

8. Измените файл boot.ini с помощью текстового редактора, добавив следующую строку:

C:\bootsect.lnx="Linux"

В результате Linux будет добавлен в меню загрузки, а загрузчик Windows NT «узнает», где находится загрузочный сектор. Строка может находиться в любом месте раздела [operating systems] файла boot.ini. Расположение строки в файле определяет и расположение ее в меню загрузки, которое отображает загрузчик NT. К примеру, если добавить строку в конец секции, получится приблизительно следующее (вторая строка multi(0) разбита на две строки, чтобы соответствовать формату книги):

[boot loader]
timeout = 30
default=multi(0)disk(0)rdisk(0)partition(1)\WINNT
[operating systems]
multi(0)disk(0)rdisk(0)partition(1)\WINNT="Windows NT Server Version 4.00"
multi(0)disk(0)rdisk(0)partition(1)\WINNT="Windows NT Server Version 4.00
    [VGA mode]" /basevideo /sos
C:\bootsect.lnx="Linux"

Для того чтобы сделать Linux системой, загружаемой по умолчанию, измените значение строки default= на следующее:

default=C:\bootsect.lnx

9. Повторно выполните команду attrib, чтобы восстановить атрибуты файла («системный» и «только для чтения»):

C:> attrib +s +r c:\boot.ini

¹ boot.ini является аналогом /etc/lilo.conf в Windows NT. В этом файле определяются операционные системы, которые можно загружать с помощью загрузчика NT.