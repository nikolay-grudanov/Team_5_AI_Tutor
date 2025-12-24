---
source_image: page_083.png
page_number: 83
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.42
tokens: 7541
characters: 1595
timestamp: 2025-12-24T04:34:16.823980
finish_reason: stop
---

псевдофайловой системой proc, в чем позволяет убедиться трассировка системных вызовов open(2) (листинг 3.24).

Листинг 3.24. Псевдофайловая система proc

finn@ubuntu:~$ strace -fe open,openat uptime
openat(AT_FDCWD, "/proc/sys/kernel/osrelease", O_RDONLY) = 3
openat(AT_FDCWD, "/proc/uptime", O_RDONLY) = 3
openat(AT_FDCWD, "/proc/loadavg", O_RDONLY) = 4
15:42:32 up 12 days, 5:27, 7 users, load average: 0.48, 0.33, 0.32
finn@ubuntu:~$ cat /proc/uptime
1056774.23 1667210.55
finn@ubuntu:~$ cat /proc/loadavg
0.48 0.33 0.32 1/623 14277

Аналогично, утилиты, показывающие список устройств на шинах PCI, USB и SCSI — lspci(8), lsusb(8) и lsscsi(8), пользуются псевдофайловой системой sysfs (листинг 3.25).

Листинг 3.25. Псевдофайловая система sysfs

finn@ubuntu:~$ strace -fe open,openat lspci -nn
openat(AT_FDCWD, "/sys/bus/pci/devices/0000:00:02.0/resource", O_RDONLY) = 4
openat(AT_FDCWD, "/sys/bus/pci/devices/0000:00:02.0/irq", O_RDONLY) = 4
openat(AT_FDCWD, "/sys/bus/pci/devices/0000:00:02.0/vendor", O_RDONLY) = 4
openat(AT_FDCWD, "/sys/bus/pci/devices/0000:00:02.0/device", O_RDONLY) = 4
openat(AT_FDCWD, "/sys/bus/pci/devices/0000:00:02.0/class", O_RDONLY) = 4
openat(AT_FDCWD, "/sys/bus/pci/devices/0000:00:02.0/config", O_RDONLY) = 3
00:02.0 VGA compatible controller [0300]: Intel Corporation 2nd Generation Core Processor Family Integrated Graphics Controller [8086:0116] (rev 09)
finn@ubuntu:~$ cat /sys/bus/pci/devices/0000:00:02.0/vendor
0x8086
finn@ubuntu:~$ cat /sys/bus/pci/devices/0000:00:02.0/device
0x0116
finn@ubuntu:~$ cat /sys/bus/pci/devices/0000:00:02.0/class
0x030000