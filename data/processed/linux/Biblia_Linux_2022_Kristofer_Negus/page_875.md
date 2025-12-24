---
source_image: page_875.png
page_number: 875
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.01
tokens: 7680
characters: 1850
timestamp: 2025-12-24T05:09:52.749583
finish_reason: stop
---

а) выполните команду journalctl -f от имени суперпользователя в окне Terminal (Терминал) и проследите за выводом в течение следующих нескольких шагов:

# journalctl -f
Jan 25 16:07:59 host2 kernel: usb 1-1.1: new high-speed USB device number 16 using ehci-pci
Jan 25 16:07:59 host2 kernel: usb 1-1.1: New USB device found, idVendor=0ea0, idProduct=2168
Jan 25 16:07:59 host2 kernel: usb 1-1.1: New USB device strings:
    Mfr=1, Product=2, SerialNumber=3
Jan 25 16:07:59 host2 kernel: usb 1-1.1: Product: Flash Disk
Jan 25 16:07:59 host2 kernel: usb 1-1.1: Manufacturer: USB
...
Jan 25 16:08:01 host2 kernel: sd 18:0:0:0: [sdb] Write Protect is off
Jan 25 16:08:01 host2 kernel: sd 18:0:0:0: [sdb]
    Assuming drive cache: write through
Jan 25 16:08:01 host2 kernel: sdb: sdb1
Jan 25 16:08:01 host2 kernel: sd 18:0:0:0: [sdb]
    Attached SCSI removable disk

б) подключите USB-накопитель, который автоматически монтирует файловую систему с этого диска. Если этого не происходит, выполните на втором терминале следующие команды (от имени суперпользователя), чтобы создать каталог точки монтирования и смонтировать устройство:

$ mkdir /mnt/test
$ mount /dev/sdb1 /mnt/test
$ umount /dev/sdb1

8. Чтобы узнать, какие USB-устройства подключены к вашему компьютеру, введите команду:

$ lsusb

9. Чтобы загрузить модуль bttv, укажите модули, которые уже были загружены, и загрузите его, введя следующее:

# modprobe -a bttv
# lsmod | grep bttv
ttv           167936   0
tea575x       16384   1 bttv
tveeprom      28672   1 bttv
videobuf_dma_sg 24576   1 bttv
videobuf_core 32768   2 videobuf_dma_sg,bttv
v4l2_common   16384   1 bttv
videodev     233472   3 tea575x,v4l2_common,bttv
i2c_algo_bit  16384   1 bttv

Обратите внимание на то, что при загрузке bttv другие модули (v4l2_common, videodev и др.) также были загружены с помощью команды modprobe -a.