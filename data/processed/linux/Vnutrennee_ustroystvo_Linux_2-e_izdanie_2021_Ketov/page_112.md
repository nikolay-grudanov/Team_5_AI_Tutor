---
source_image: page_112.png
page_number: 112
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.41
tokens: 7387
characters: 1604
timestamp: 2025-12-24T04:34:57.074932
finish_reason: stop
---

finn@ubuntu:~$ getfattr -d -m - /usr/bin/gnome-keyring-daemon
getfattr: Удаление начальных '/' из абсолютных путей
# file: usr/bin/gnome-keyring-daemon

security.capability=0sAQAAAABAAAAAAAAAAAAAAA=

finn@ubuntu:~$ cd /srv/kingdom/stash
finn@ubuntu:/srv/kingdom/stash$ ls -l README.jake
-rw-rw----+ 1 finn candy 0 нояб. 4 14:17 README.jake
finn@ubuntu:/srv/kingdom/stash$ getfacl README.jake
# file: README.jake
# owner: finn
# group: candy
user::rw-
user:jake:r--
group::rwx #effective:r--
mask::rw-
other::---
finn@ubuntu:/srv/kingdom/stash$ getfattr -d -m - README.jake
# file: README.jake
system.posix_acl_access=0sAgAAAAEABgD//////AgAGAOcDAAAEEAcA//////xAABgD//////IAAAAP////8=

finn@ubuntu:/srv/kingdom/stash$ setfattr -n user.color -v orange README.jake
finn@ubuntu:/srv/kingdom/stash$ setfattr -n user.flavour -v vanilla README.jake
finn@ubuntu:/srv/kingdom/stash$ getfattr -d README.jake
# file: README.jake
user.color="orange"
user.flavour="vanilla"

В примере из листинга 3.56 показано, что привилегии исполняемых программ ① на самом деле сохранены в атрибуте security.capability, списки контроля доступа ② — в атрибуте system.posix_acl_access, а в атрибутах пространства имен user можно разместить любые значения. Наиболее известным применением пользовательских атрибутов (листинг 3.57) являются атрибуты user.xdg.origin.url и user.xdg.referrer.url, используемые браузером chromium-browser(1) для сохранения URL файлов, которые были загружены из Интернета.

Листинг 3.57. Расширенные пользовательские атрибуты файлов

finn@ubuntu:~/Downloads$ getfattr -d TLCL-13.07.pdf
# file: TLCL-13.07.pdf