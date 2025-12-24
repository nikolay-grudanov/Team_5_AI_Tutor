---
source_image: page_382.png
page_number: 382
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.05
tokens: 7464
characters: 1989
timestamp: 2025-12-24T04:43:19.818514
finish_reason: stop
---

I: Valid Release signature (key id F6ECB3762474EDA9D21B702287192001991BC93C)
I: Retrieving Packages
I: Validating Packages
I: Resolving dependencies of required packages...
I: Resolving dependencies of base packages...

I: Base system installed successfully.

morty@ubuntu:~$ sudo chroot /mnt
root@ubuntu:# apt update
Hit:1 http://archive.ubuntu.com/ubuntu eoan InRelease
Get:2 http://archive.ubuntu.com/ubuntu eoan/main Translation-en [505 kB]
Fetched 505 kB in 2s (306 kB/s)
Reading package lists... Done
Building dependency tree... Done
All packages are up to date.
root@ubuntu:# apt install nano

root@ubuntu:# nano /etc/fstab
/dev/disk/by-uuid/71002c88-0b02-4ac0-8cd4-65c4eb0e454b   /   ext4   defaults 0 0
/dev/disk/by-uuid/08C8-BDB9   /boot/efi   vfat   defaults 0 0

root@ubuntu:# useradd -m -s /bin/bash morty
root@ubuntu:# passwd morty
New password: plumbus
Retype new password: plumbus
passwd: password updated successfully
root@ubuntu:# apt install sudo

root@ubuntu:# gpasswd -a morty sudo
Adding user morty to group sudo
root@ubuntu:# exit

Необходимо отметить, что на разделы носителей, содержащие нужные файловые системы, лучше всегда ссылаться не при помощи специальных файлов устройств /dev/sdc1 и /dev/sdc2, а посредством их псевдонимов ① и ② т.е. их символьских ссылок из каталога /dev/disk/by-uuid, которые там создает служба udev(7). Так как заранее неизвестно, к какому USB-разъему (контроллеру, каналу) и в каком аппаратном окружении будет подключен этот накопитель для загрузки, и, как следствие, неизвестно, в каком порядке он будет опрошен и обнаружен, то и имя специального файла его устройства заранее определить невозможно. Несмотря на такую неопределенность, идентификаторы файловых систем останутся неизменными, и, как следствие, псевдонимы их разделов тоже.

Завершает минимальную конфигурацию ③ процесс создания первой пользовательской учетной записи, назначения ей пароля и добавления ее в группу sudo для использования sudo(1) в устанавливаемой системе.