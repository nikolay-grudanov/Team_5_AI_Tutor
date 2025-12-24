---
source_image: page_369.png
page_number: 369
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.79
tokens: 7699
characters: 1952
timestamp: 2025-12-24T04:42:56.721554
finish_reason: stop
---

Так, например, модуль snd_intel8x0 поддерживает много конкретных PCI-устройств от Intel (v00008086), включая AC97 Audio Controller (d0002415), причем остальные идентификаторы устройств (sv, subvendor, sd — subdevice и пр.) не имеют значения (*).

Информация о псевдонимах извлекается из модулей драйверов при их инсталляции и помещается в файлы /lib/modules/`uname -r`/modules.alias и /lib/modules/`uname -r`/modules.alias.bin для дальнейшего использования утилитой modprobe(8) и службой udev(7).

В листинге 10.7 показан мониторинг событий, которые доставляются из ядра в udev(7) при подключении накопителя USB-флэш.

Листинг 10.7. Служба udev

morty@ubuntu:~$ udevadm monitor -k
monitor will print the received events for:
KERNEL - the kernel uevent

KERNEL[20373.565718] add /devices/pci0000:00/0000:00:0b.0/usb1/1-1 (usb)
KERNEL[20373.572489] add /devices/pci0000:00/0000:00:0b.0/usb1/1-1/1-1:1.0 (usb)
KERNEL[20373.573204] bind /devices/pci0000:00/0000:00:0b.0/usb1/1-1 (usb)
KERNEL[20373.599217] add /module/usb_storage (module)
KERNEL[20373.601776] add /bus/usb/drivers/usb-storage (drivers)
KERNEL[20373.604020] add /module/uas (module)
KERNEL[20373.604112] add /bus/usb/drivers/uas (drivers)

morty@ubuntu:~$ mount -t sysfs
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)

morty@ubuntu:~$ cat /sys/devices/pci0000:00/0000:00:0b.0/usb1/1-1/1-1:1.0/uevent
DEVTYPE=usb_interface
DRIVER=usb-storage
PRODUCT=58f/6387/100
TYPE=0/0/0
INTERFACE=8/6/80
MODALIAS=usb:v058Fp6387d0100dc00dsc00dp00ic08isc06ip50in00

morty@ubuntu:~$ grep -i v058Fp6387 /lib/modules/`uname -r`/modules.*
/lib/modules/5.3.0-24-generic/modules.alias:alias usb:v058Fp6387d0141dc*dsc*dp*... ① usb_storage
morty@ubuntu:~$ grep -i lc08isc06ip50/lib/modules/`uname -r`/modules.*
/lib/modules/5.3.0-24-generic/modules.alias:alias usb:v*p*d*dc*dsc*dp*ic08isc06ip50in* uas ②
/lib/modules/5.3.0-24-generic/modules.alias:alias usb:v*p*d*dc*dsc*dp*ic08isc06ip50in* usb_storage