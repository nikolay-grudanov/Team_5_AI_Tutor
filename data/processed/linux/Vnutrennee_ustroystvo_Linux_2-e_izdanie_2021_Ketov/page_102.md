---
source_image: page_102.png
page_number: 102
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.66
tokens: 7433
characters: 1744
timestamp: 2025-12-24T04:34:47.595607
finish_reason: stop
---

0 finn@ubuntu:/srv/kingdom$ chmod g-w stash/
finn@ubuntu:/srv/kingdom$ ls -lad stash/
1 drwxr-s-- 2 finn candy 4096 нояб. 4 13:05 stash/
finn@ubuntu:/srv/kingdom$ getfacl stash/
...
user::rwx
! user:jake:rwx #effective:r-x
! group::rwx #effective:r-x
mask::r-x
other::---

Права по умолчанию

При создании новых файлов в каталогах с индивидуальными правами пользователей в списках доступа зачастую складывается ситуация, когда пользователи (имеющие доступ в каталоги) не получают нужных прав доступа к создаваемым файлам в этих каталогах. В большинстве случаев это противоречит здравому смыслу, т. к. все файлы некоторого каталога являются в определенном смысле «общими» для множества пользователей, которым разрешен доступ в сам каталог.

В примере из листинга 3.46 в каталоге stash, куда пользователю jake предоставлен индивидуальный доступ (см. листинг 3.45) при создании файла README, он в силу SGID для каталога (см. листинг 3.42) передается группе candy. В группу candy пользователь jake не входит (именно поэтому ему назначены индивидуальные права в листинге 3.44), в результате чего файл ему никак не будет доступен.

Проблема решается назначением 2 каталогу stash прав доступа «по умолчанию» (default), которые будут унаследованы 3 файлами, создающимися в этом каталоге.

Листинг 3.46. Права по умолчанию

finn@ubuntu:/srv/kingdom$ cd stash/
finn@ubuntu:/srv/kingdom$ umask 0007
finn@ubuntu:/srv/kingdom/stash$ touch README
finn@ubuntu:/srv/kingdom/stash$ ls -la README
-rw-rw---- 1 finn candy 0 нояб. 4 14:16 README
finn@ubuntu:/srv/kingdom/stash$ id jake
uid=1002(jake) gid=1002(jake) группы=1002(jake)
finn@ubuntu:/srv/kingdom/stash$ setfacl -m d:u:jake:rw .
finn@ubuntu:/srv/kingdom/stash$ getfacl .
# file: .
...
default:user::rwx