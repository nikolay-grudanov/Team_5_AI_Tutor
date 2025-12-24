---
source_image: page_310.png
page_number: 310
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.38
tokens: 7375
characters: 1488
timestamp: 2025-12-24T04:53:51.167134
finish_reason: stop
---

добавляются для пользователей, групп, масок и других объектов, которые берутся из списков ACL каталога:

[mary]$ mkdir /tmp/mary/test
[mary]$ getfacl /tmp/mary/test
# file: tmp/mary/test
# owner: mary
# group: mary
user::rwx
group::rwx
group:sales:rwx
group:market:rwx
mask::rwx
other::r-x
default:user::rwx
default:group::rwx
default:group:sales:rwx
default:group:market:rwx
default:mask::rwx
default:other::r-x

Обратите внимание на то, что при создании файла в этом каталоге передаваемые права различаются. Поскольку обычный файл создается без права execute, действующие права уменьшаются до rw-:

[mary@cnegus ~]$ touch /tmp/mary/file.txt
[mary@cnegus ~]$ getfacl /tmp/mary/file.txt
# file: tmp/mary/file.txt
# owner: mary
# group: mary
user::rw-
group::rwx    #effective:rw-
group:sales:rwx    #effective:rw-
group:market:rwx    #effective:rw-
mask::rw-
other::r--

Включение списков ACL

В современных системах Fedora и RHEL типы файловых систем xfs и ext (ext2, ext3 и ext4) создаются автоматически с поддержкой ACL. В других системах Linux или в файловых системах, созданных в них, для этого можно добавить параметр монтирования acl несколькими способами.

● Добавьте параметр acl в пятое поле строки файла /etc/fstab, который автоматически монтирует файловую систему при загрузке системы.
● Вставьте строку acl в поле Default mount options в суперблоке файловой системы, чтобы параметр acl использовался независимо от того, монтируется файловая система автоматически или вручную.