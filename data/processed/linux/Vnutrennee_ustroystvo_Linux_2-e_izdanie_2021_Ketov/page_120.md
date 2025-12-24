---
source_image: page_120.png
page_number: 120
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.31
tokens: 7598
characters: 1963
timestamp: 2025-12-24T04:35:16.960388
finish_reason: stop
---

i915      1949696   4
btusb      57344    0
uvcvideo   98304    0
e1000e     258048   0

fitz@ubuntu:~$ modinfo i915
filename: /lib/modules/5.3.0-23-generic/kernel/drivers/gpu/drm/i915/i915.ko
license: GPL and additional rights
description: Intel Graphics

fitz@ubuntu:~$ file /lib/modules/5.3.0-23-generic/kernel/drivers/gpu/drm/i915/i915.ko
/lib/modules/5.3.0-23-generic/kernel/drivers/gpu/drm/i915/i915.ko: ELF 64-bit LSB relocatable, x86-64, version 1 (SYSV),
BuildID[sha1]=49e59590c1a718074b76b6541702f6f794ea7eae, not stripped

Динамические модули ядра зачастую являются драйверами устройств, что проиллюстрировано в листинге 4.7 при помощи утилит lspci(8) и lsusb(8), которые сканируют посредством псевдофайловой системы sysfs списки обнаруженных ядром на шинах PCI и USB устройств и обслуживающих их драйверов.

Листинг 4.7. Драйверы устройств

fitz@ubuntu:~$ lspci -k
00:02.0 VGA compatible controller: Intel Corporation 2nd Generation Core Process or Family Integrated Graphics Controller (rev 09)
    Subsystem: Dell 2nd Generation Core Processor Family Integrated Graphics Controller
    Kernel driver in use: i915
    Kernel modules: i915
00:19.0 Ethernet controller: Intel Corporation 82579LM Gigabit Network Connection (Lewisville) (rev 04)
    Subsystem: Dell 82579LM Gigabit Network Connection (Lewisville)
    Kernel driver in use: e1000e
    Kernel modules: e1000e

fitz@ubuntu:~$ lsusb -t
/: Bus 01.Port 1: Dev 1, Class=root_hub, Driver=ehci-pci/3p, 480M
    |__ Port 1: Dev 2, If 0, Class=Hub, Driver=hub/6p, 480M
        |__ Port 4: Dev 3, If 2, Class=Vendor Specific Class, Driver=, 12M
        |__ Port 4: Dev 3, If 0, Class=Wireless, Driver=btusb, 12M
        |__ Port 4: Dev 3, If 3, Class=Application Specific Interface, Driver=, 12M
        |__ Port 4: Dev 3, If 1, Class=Wireless, Driver=btusb, 12M
        |__ Port 5: Dev 4, If 0, Class=Video, Driver=uvcvideo, 480M
        |__ Port 5: Dev 4, If 1, Class=Video, Driver=uvcvideo, 480M