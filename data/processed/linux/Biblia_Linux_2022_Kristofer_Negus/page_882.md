---
source_image: page_882.png
page_number: 882
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.23
tokens: 7303
characters: 1116
timestamp: 2025-12-24T05:09:48.133530
finish_reason: stop
---

# file: tmp/mydir
# owner: mjones
# group: mjones
user::rwx
group::rwx
other::r-x
default:user::rwx
default:user:adm:rwx
default:group::rwx
default:mask::rwx
default:other::r-x
[mjones]$ mkdir /tmp/mydir/testing
[mjones]$ touch /tmp/mydir/newfile.txt
[mjones]$ getfacl /tmp/mydir/testing/
# file: tmp/mydir/testing/
# owner: mjones
# group: mjones
user::rwx
user:adm:rwx
group::rwx
mask::rwx
other::r-x
default:user::rwx
default:user:adm:rwx
default:group::rwx
default:mask::rwx
default:other::r-x
[mjones]$ getfacl /tmp/mydir/newfile.txt
# file: tmp/mydir/newfile.txt
# owner: mjones
# group: mjones
user::rw-
user:adm:rwx    #effective:rwg-
roup::rwx       #effective:rw-
mask::rw-
other::r--

Обратите внимание на то, что пользователь adm фактически имеет только права на запись. Чтобы исправить это, нужно расширить права доступа маски. Один из способов сделать это — применить команду chmod следующим образом:

[mjones]$ chmod 775 /tmp/mydir/newfile.txt
[mjones]$ getfacl /tmp/mydir/newfile.txt
# file: tmp/mydir/newfile.txt
# owner: mjones
# group: mjones
user::rwx
user:adm:rwx
group::rwx
mask::rwx
other::r-x