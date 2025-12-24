---
source_image: page_403.png
page_number: 403
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.69
tokens: 7952
characters: 2174
timestamp: 2025-12-24T04:30:38.633082
finish_reason: stop
---

# For details of the format look at autofs(8).
# Для дополнительной информации выполните команду man autofs
/misc    /etc/auto.misc    --timeout=60

Если не считать комментариев, в этом файле только одна содержательная строка — последняя. В вашей системе она может быть закомментирована, и для включения автоматического монтирования необходимо убрать знак "#".

У конфигурационной строки следующий формат:

точка_монтирования   карта   настройки

В данном случае точкой монтирования выступает каталог /misc. Это немного затрудняет работу, потому что при ручном подключении используется каталог /mnt. Второй параметр определяет карту монтирования. В данном случае это файл /etc/auto.misc. Формат и назначение файла чем-то похожи на файл /etc/fstab, который применяется для команды mount. Содержимое файла /etc/auto.misc можно увидеть в листинге 14.3.

Последний параметр --timeout=60 — это время простоя. Если в течение этого периода в каталоге, использованном под подключение, не будет активности, то устройство будет размонтировано. По умолчанию установлено значение 60 секунд. В большинстве случаев это вполне приемлемо.

Листинг 14.3. Содержимое файла /etc/auto.misk

# $Id: auto.misc,v 1.2 1997/10/06 21:52:04 hpa Exp $
# This is an automounter map and it has the following format:
# Это карта автомонтирования, которая имеет следующий формат:
# key [ -mount-options-separated-by-comma ] location
# Details may be found in the autofs(5) manpage
# Дополнительную информацию можно получить, выполнив man autofs

cd    -fstype=iso9660,ro,nosuid,nodev    :/dev/cdrom

# The following entries are samples to pique your imagination
# Следующие записи являются примерами для возбуждения воображения
#linux    -ro,soft,intr    ftp.example.org:/pub/linux
#boot    -fstype=ext2    :/dev/hda1
#floppy    -fstype=auto    :/dev/fd0
#floppy    -fstype=ext2    :/dev/fd0
#e2floppy    -fstype=ext2    :/dev/fd0
#jaz    -fstype=ext2    :/dev/sdc1
#removable    -fstype=ext2    :/dev/hdd

Теперь рассмотрим содержимое файла /etc/auto.misc. Здесь только одна строка без комментария, которая описывает команды подключения компакт-диска:

cd    -fstype=iso9660,ro,nosuid,nodev    :/dev/cdrom