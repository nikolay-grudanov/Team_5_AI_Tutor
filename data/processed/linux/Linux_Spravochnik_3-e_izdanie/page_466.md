---
source_image: page_466.png
page_number: 466
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.31
tokens: 11599
characters: 1265
timestamp: 2025-12-24T03:36:02.512115
finish_reason: stop
---

Приведем пример полного файла /etc/lilo.conf для системы, раздел /dev/hda2 которой содержит Linux.

## Глобальные параметры
boot = /dev/hda2
map = /boot/map
delay = 30
timeout = 50
prompt
vga=ask

## Раздел образа: обычная загрузка Linux
image = /boot/vmlinuz
label = linux
root = /dev/hda2
install = /boot/boot.b
map = /boot/map
read-only

## Раздел образа: для тестирования нового ядра Linux
image=/testvmlinuz
label = testlinu
root = /dev/hda2
install = /boot/boot.b
map = /boot/map
read-only
optional      # Пропустить образ, если он недоступен во время создания карты

## Раздел образа: загрузка DOS
other = /dev/hda1
label = dos
loader = /boot/chain.b
table = /dev/hda    # Текущая таблица разделов диска

## Раздел образа: загрузка Windows 95
other = /dev/hda1
label = win95
loader = /boot/chain.b
table = /dev/hda

Глобальные параметры

Помимо описанных ниже, в качестве глобальных параметров для LILO также могут использоваться параметры ядра append, read-only, read-write, root и vga (описанные далее в разделе «Параметры, передаваемые ядру»).

backup=backup-file
Создавать резервную копию загрузочного сектора в файле backup-file, тогда как обычно резервная копия получает имя /boot/boot.nnnn, где nnnn — число, соответствующее типу дискового устройства.