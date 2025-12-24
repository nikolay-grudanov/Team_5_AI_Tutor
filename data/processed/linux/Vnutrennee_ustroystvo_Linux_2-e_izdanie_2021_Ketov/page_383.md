---
source_image: page_383.png
page_number: 383
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.27
tokens: 7793
characters: 2560
timestamp: 2025-12-24T04:43:33.311001
finish_reason: stop
---

После того как корневая ФС наполнена требуемым содержимым, нужно припомнить, что согласно процессу загрузки (см. разд. 10.1) корневая файловая система монтируется в дерево каталогов после загрузки ядра, ядро загружается загрузчиком, а он, в свою очередь, получает управление от UEFI. Таким образом, необходимо инсталлировать загрузчик и ядро ОС, что проиллюстрировано в листингах 10.18 и 10.19 соответственно.

Инсталляция загрузчика начинается с формирования дерева каталогов инсталлируемой ОС так, как оно будет сформировано в процессе ее работы. Для этого ниже точки монтирования ее корневой ФС (каталог /mnt, см. ① в листинге 10.17) монтируется ESP-раздел ① в /mnt/boot/efi, а затем псевдофайловые системы ① proc, sysfs и специальные файлы устройств /dev. При этом они попросту «заимствуются» из исходной ОС путем «связующего» --bind монтирования. Другими словами, каталоги /sys, /proc и /dev просто отображаются в еще одно место дерева, а именно ниже каталога /mnt. Для инсталляции загрузчика осуществляется чрутизация (см. разд. 9.1) в сформированное окружение, где сначала устанавливается ③ пакет с компонентами загрузчика в систему, а затем сам загрузчик ④ на ESP-раздел.

Листинг 10.18. Инсталляция загрузчика GRUB

morty@ubuntu:~$ sudo mkdir /mnt/boot/efi
① morty@ubuntu:~$ sudo mount /dev/sdc1 /mnt/boot/efi
② morty@ubuntu:~$ sudo mount --bind /dev /mnt/dev
③ morty@ubuntu:~$ sudo mount --bind /proc /mnt/proc
④ morty@ubuntu:~$ sudo mount --bind /sys /mnt/sys
morty@ubuntu:~$ sudo chroot /mnt
root@ubuntu:# apt install grub-efi
⑤ root@ubuntu:# grub-install --removable --no-uefi-secure-boot -v
Installing for x86_64-efi platform.
① grub-install: info: copying '/.../grub/x86_64-efi/ext2.mod' -> '/boot/grub/x86_64-efi/ext2.mod'.
① grub-install: info: copying '/.../grub/x86_64-efi/part_gpt.mod' -> '/boot/grub/x86_64-efi/part_gpt.mod'.
① grub-install: info: copying '/.../grub/x86_64-efi/efi_gop.mod' -> '/boot/grub/x86_64-efi/efi_gop.mod'.
① grub-install: info: copying '/.../grub/x86_64-efi/font.mod' -> '/boot/grub/x86_64-efi/font.mod'.
① grub-install: info: copying '/usr/share/grub/unicode.pf2' -> '/boot/grub/fonts/unicode.pf2'.
② grub-install: info: grub-mkimage --directory '/usr/lib/grub/x86_64-efi' --prefix '(',gpt2)/boot/grub' --output '/boot/grub/x86_64-efi/core.efi' --dtb '' --format 'x86_64-efi' --compression 'auto' 'ext2' 'part_gpt'
② grub-install: info: reading /usr/lib/grub/x86_64-efi/kernel.img.
② grub-install: info: reading /usr/lib/grub/x86_64-efi/fshelp.mod.
② grub-install: info: reading /usr/lib/grub/x86_64-efi/ext2.mod.