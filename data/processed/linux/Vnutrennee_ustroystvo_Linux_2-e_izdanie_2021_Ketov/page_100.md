---
source_image: page_100.png
page_number: 100
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.33
tokens: 7138
characters: 719
timestamp: 2025-12-24T04:34:36.220651
finish_reason: stop
---

Рис. 3.4. Списки контроля доступа к файлам

Листинг 3.44. Списки контроля доступа

finn@ubuntu:/srv/kingdom$ ls -lad .
drwxrwsr-t 2 bubblegum candy 4096 окт. 23 21:19 .

finn@ubuntu:/srv/kingdom$ id
uid=1001(finn) gid=1001(finn) группы=1001(finn),1007(candy)

finn@ubuntu:/srv/kingdom$ mkdir stash
finn@ubuntu:/srv/kingdom$ chmod o= stash/
finn@ubuntu:/srv/kingdom$ ls -lad stash/
drwxrws--- 2 finn candy 4096 нояб. 4 13:05 stash/

finn@ubuntu:/srv/kingdom$ id jake
? uid=1002(jake) gid=1002(jake) группы=1002(jake)

finn@ubuntu:/srv/kingdom$ setfacl -m u:jake:rwx stash/
finn@ubuntu:/srv/kingdom$ ls -lad stash/
drwxrws---+ * 2 finn candy 4096 нояб. 4 13:05 stash/

finn@ubuntu:/srv/kingdom$ getfacl stash/
... ... ...