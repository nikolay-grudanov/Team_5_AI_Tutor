---
source_image: page_085.png
page_number: 85
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.22
tokens: 7540
characters: 1878
timestamp: 2025-12-24T04:34:21.239879
finish_reason: stop
---

finn@ubuntu:~/mnt/archive/linux-5.3.9/Documentation/filesystems$ less fuse.txt
finn@ubuntu:~/mnt/archive/linux-5.3.9/Documentation/filesystems$ cd ~
finn@ubuntu:~ $ fusermount -u ~/mnt/archive

В примере из листинга 3.27 показано, как при помощи сетевого протокола SSH (см. разд. 6.4.1) можно смонтировать часть дерева каталогов (домашний каталог пользователя jake) с удаленного узла jake@grex.org в каталог ~/mnt/net локального дерева каталогов.

Листинг 3.27. Внеядерная файловая система «fuse.sshfs»

finn@ubuntu:~$ sshfs jake@grex.org: ~/mnt/net
The authenticity of host 'grex.org (75.61.90.157)' can't be established.
ECDSA key fingerprint is SHA256:pM03fe6UTyqtqzUMq5SmTmH5tquUuN9WdvLwdpcEJhSU.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
jake@grex.org's password: P@ssw0rd

finn@ubuntu:~$ mount
jake@grex.org: on /home/finn/mnt/net type fuse.sshfs (rw,...)
finn@ubuntu:~$ cd ~/mnt/net
finn@ubuntu:~/mnt/net$ ls -l
итого 488
-rw-r--r-- 1 156620 131077 495604 окт. 10 20:28 OPENME.txz
-rw-r--r-- 1 156620 131077 106 окт. 10 20:30 README.gz
finn@ubuntu:~/mnt/net$ zless README.gz
finn@ubuntu:~/mnt/net$ cd ~
finn@ubuntu:~ $ fusermount -u ~/mnt/net

В примере из листинга 3.28 показано, как можно смонтировать зашифровываемый каталог /media/flash/secret USB-flash-накопителя (уже смонтированного в каталог /media/flash при помощи дисковой файловой системы vfat) в каталог ~/mnt/exposed и скопировать туда файлы, подлежащие зашифровыванию. Теперь при утере накопителя можно не беспокоиться об информации, попавшей третьим лицам.

Листинг 3.28. Внеядерная файловая система «fuse.encfs»

finn@ubuntu:~ $ mount
/dev/sdc1 on /media/flash type vfat (rw,...)
finn@ubuntu:~ $ encfs /media/flash/secret ~/mnt/exposed
Директория "/media/flash/secret" не существует. Создать ее? (y,n) y
Директория "/home/finn/mnt/exposed" не существует. Создать ее? (y,n) y