---
source_image: page_483.png
page_number: 483
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.69
tokens: 11483
characters: 1079
timestamp: 2025-12-24T03:36:42.403475
finish_reason: stop
---

держкой загрузки RAM-дисков (CONFIG_BLK_DEV_INITRD=y). Затем необходимо подготовить обычную корневую файловую систему и создать образ RAM-диска. Возможно, ваш дистрибутив Linux включает утилиты, выполняющие некоторые установки за вас; например, в дистрибутив Red Hat входит утилита mkinitrd, предназначенная для создания initrd-образа. Более подробную информацию можно почерпнуть на страницах руководства (man-page) по initrd и в файле initrd.txt (путь может отличаться, но обычно это нечто вроде /usr/src/linux/Documentation/initrd.txt).

Если система Linux подготовлена к использованию initrd, то можно выполнить одно из следующих действий (в зависимости от применяемого загрузчика):

• Если загрузчиком является LILO, добавьте параметр initrd в соответствующий раздел образа:

image = /vmlinuz
initrd = /boot/initrd    # Файл, загружаемый в качестве содержимого /dev/initrd

Выполните команду /sbin/lilo и можете перезагружать систему с помощью initrd.

• Если используется Loadlin, добавьте параметр initrd к командной строке:

loadlin c:\linux\vmlinuz initrd=c:\linux\initrd