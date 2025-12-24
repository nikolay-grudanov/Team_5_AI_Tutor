---
source_image: page_332.png
page_number: 332
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.56
tokens: 7610
characters: 1966
timestamp: 2025-12-24T04:54:35.917325
finish_reason: stop
---

Allocatable        yes (but full)
PE Size           4.00 MiB
Total PE          38021
Free PE           0
Allocated PE      38021
PV UUID           wlvuIv-UiI2-pNND-f39j-oH0X-9too-AOII7R

В примере видно, что физический том LVM, представленный /dev/sda2, занимает 148,52 Гбайт и все это пространство выделено группе томов с именем vg_abc. Наименьшая единица хранения, которая может быть использована из этого физического тома, составляет 4 Мбайт, что называется физическим экстентом (Physical Extent, PE).

ПРИМЕЧАНИЕ
Обратите внимание на то, что утилиты LVM отображают дисковое пространство в мебибайтах (МиБ) и гибибайтах (ГиБ). Один мегабайт составляет 1 000 000 байт (106), а 1 МиБ — 1 048 576 байт (220). Мебибайт — это более точная единица отражения того, как данные хранятся на компьютере. Но маркетологи, как правило, используют мегабайт, потому что так кажется, что жесткие диски, CD и DVD имеют большую емкость, чем на самом деле. Имейте в виду, что большинство инструментов в Linux отображают данные хранилища в мебибайтах и гибибайтах, хотя некоторые могут отображать также в мегабайтах и гигабайтах.

Далее рассмотрим данные о группе томов:

# vgdisklay vg_abc
--- Volume group ---
VG Name                vg_abc
System ID              lvm2
Format                 lvm2
Metadata Areas         1
Metadata Sequence No   4
VG Access              read/write
VG Status              resizable
MAX LV                 0
Cur LV                 3
Open LV                3
Max PV                 0
Cur PV                 1
Act PV                 1
VG Size                148.52 GiB
PE Size                4.00 MiB
Total PE               38021
Alloc PE / Size        38021 / 148.52 GiB
Free PE / Size         0 / 0
VG UUID                c2SGHM-KU9H-wbXM-sgca-EtBr-UXAq-UnnSTh

В примере видно, что выделен 38 021 PE (физический экстент). Используя команду lvdisplay, как показано далее, можно увидеть, где они были распределены (я сократил некоторые выходные данные):