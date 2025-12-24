---
source_image: page_385.png
page_number: 385
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.78
tokens: 7484
characters: 1838
timestamp: 2025-12-24T04:43:22.461323
finish_reason: stop
---

The following NEW packages will be installed:

busybox-initramfs cpio initramfs-tools ① initramfs-tools-bin
initramfs-tools-core klibc-utils kmod libklibc
libkmod2 linux-base linux-image-5.3.0-18-generic linux-modules-5.3.0-18-generic ②
lz4 udev ③

0 upgraded, 14 newly installed, 0 to remove and 0 not upgraded.
Need to get 24.6 MB of archives.
After this operation, 93.9 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y

Setting up linux-image-5.3.0-18-generic (5.3.0-18.19+1) ...
Processing triggers for initramfs-tools (0.133ubuntu10) ...
update-initramfs: Generating /boot/initrd.img-5.3.0-18-generic
root@ubuntu:# ls /boot/*5.3.0*
/boot/System.map-5.3.0-18-generic /boot/initrd.img-5.3.0-18-generic ①
/boot/config-5.3.0-18-generic /boot/vmlinuz-5.3.0-18-generic ②

Нужно отметить, что образ «временной» корневой ФС, в который включаются модули ядра, необходимые для ее монтирования, создается «на лету» ① сразу при его установке. Остается только сообщить об установленном ядре загрузчику GRUB и указать параметры bootparam(7), которые должны сообщаться при передаче ему управления, что проиллюстрировано в листинге 10.20.

Листинг 10.20. Конфигурирование загрузчика

root@ubuntu:# nano /boot/grub/grub.conf
① insmod efi_uga
insmod efi_gop
② set gfxpayload=auto

menuentry 'My Flash Linux' {
    echo Loading /boot/vmlinuz-5.3.0-18-generic...
    linux /boot/vmlinuz-5.3.0-18-generic root=/dev/disk/by-uuid/e74422dd-b74a-40bf-a6c4-e1abd516c570 ro
    echo Loading /boot/initrd.img-5.3.0-18-generic...
    initrd /boot/initrd.img-5.3.0-18-generic
    echo Booting.
    boot
}

Конфигурационный файл загрузчика является сценарием на его командном языке. При отсутствии такового загрузчик перейдет при старте в режим интерактивного взаимодействия с пользователем, выведет приглашение к вводу команд grub> и бу-