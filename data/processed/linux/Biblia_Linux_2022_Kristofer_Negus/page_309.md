---
source_image: page_309.png
page_number: 309
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.40
tokens: 7416
characters: 1633
timestamp: 2025-12-24T04:53:52.841074
finish_reason: stop
---

групп в файле задается маска максимальных привилегий, которые пользователь или группа ACL могут иметь для файла. Таким образом, даже если вы предоставляете пользователю больше прав ACL, чем позволяют права группы, его права не будут превышать прав группы, как в следующем примере:

[mary]$ chmod 644 /tmp/memo.txt
[mary]$ getfacl /tmp/memo.txt
# file: tmp/memo.txt
# owner: mary
# group: mary
user::rw-
user:bill:rw-    #effective:r--
group::rw-       #effective:r--
group:sales:rw-  #effective:r--
mask::r--
other::r--

Обратите внимание на то, что, даже если пользователь bill и группа sales имеют права rw-, их действительные права — это r--. Таким образом, пользователь bill или кто-либо в группе sales не сможет изменить файл, если пользователь mary снова не откроет права, например набрав команду chmod 664 /tmp/memo.txt.

Настройка списков ACL по умолчанию

Настройка списков ACL по умолчанию в каталоге позволяет работать с ними в будущем. Это означает, что при создании новых файлов и каталогов в этом каталоге им будут назначаться одни и те же списки ACL. Чтобы назначить пользователю или группе права в ACL по умолчанию, добавьте параметр d: к пользователю или группе, например:

[mary]$ mkdir /tmp/mary
[mary]$ setfacl -m d:g:market:rwx /tmp/mary/
[mary]$ getfacl /tmp/mary/
# file: tmp/mary/
# owner: mary
# group: mary
user::rwx
group::rwx
other::r-x
default:user::rwx
default:group::rwx
default:group:sales:rwx
default:group:market:rwx
default:mask::rwx
default:other::r-x

Чтобы убедиться, что список ACL по умолчанию работает, создайте подкаталог. Затем запустите команду getfacl. Вы увидите, что строки по умолчанию