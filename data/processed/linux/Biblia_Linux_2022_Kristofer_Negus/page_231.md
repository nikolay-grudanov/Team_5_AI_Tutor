---
source_image: page_231.png
page_number: 231
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.59
tokens: 7791
characters: 2623
timestamp: 2025-12-24T04:51:51.926578
finish_reason: stop
---

[79.177854] sd 9:0:0:0: [sdb]
    8343552 512-byte logical blocks: (4.27 GB/3.97 GiB)
[79.178593] sd 9:0:0:0: [sdb] Write Protect is off

Из этого вывода сначала отображается версия ядра Linux, а затем параметры командной строки ядра. В последних строках — описание подключенного USB-накопителя на 4 Гбайт.

Если при обнаружении или загрузке драйверов что-то пойдет не так, используйте эту информацию, чтобы увидеть название и номер модели оборудования. Затем поищите информацию на форумах Linux или в документации, чтобы решить проблему. Существует также несколько дополнительных команд, которые позволяют просмотреть подробную информацию об оборудовании компьютера после запуска системы. Команда lspci выводит список шин ввода-вывода для подключения устройств (PCI) на компьютере. Фрагмент вывода:

$ lspci
00:00.0 Host bridge: Intel Corporation
    5000X Chipset Memory ControllerHub
00:02.0 PCI bridge: Intel Corporation 5000 Series Chipset
    PCI Express x4 Port 2
00:1b.0 Audio device: Intel Corporation 631xESB/632xESB
    High Definition Audio Controller (rev 09)
00:1d.0 USB controller: Intel Corporation 631xESB/632xESB/3100
    Chipset UHCI USBController#1 (rev 09)
07:00.0 VGA compatible controller: nVidia Corporation NV44
0c:02.0 Ethernet controller: Intel Corporation 82541PI
    Gigabit Ethernet Controller (rev 05)

Мост хоста соединяет локальную шину с другими компонентами моста PCI. Я сократил список, чтобы показать информацию о подключенных устройствах с разными функциями: звук (аудиоустройство — audio device), накопители и другие USB-устройства (USB-контроллер — USB controller), видеодисплеи (VGA-совместимый контроллер — VGA compatible controller) и проводные сетевые карты (Ethernet-контроллер — Ethernet controller). Если возникают проблемы с работой любого из этих устройств, обратите внимание на их модели и номера и поищите информацию о них в Интернете.

Чтобы получить более подробный вывод из lspci, добавьте один или несколько параметров -v. Например, используя lspci -vvv, я получил сведения о своем контроллере Ethernet, включая отклик, возможности контроллера и драйвер Linux (e1000), применяемый для устройства.

Команда lsusb особенно хорошо подходит для вывода информации о USB-устройствах. По умолчанию lsusb перечисляет информацию о USB-концентраторах, установленных на компьютере, и всех подключенных USB-устройствах:

$ lsusb
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 002 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 003 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 004 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub