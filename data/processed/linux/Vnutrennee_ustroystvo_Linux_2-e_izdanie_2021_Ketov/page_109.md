---
source_image: page_109.png
page_number: 109
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.40
tokens: 7394
characters: 1808
timestamp: 2025-12-24T04:34:54.202713
finish_reason: stop
---

Листинг 3.52. Мандатные метки файлов программ

[lich@centos ~]$ ls -Z /usr/sbin/httpd
-rwxr-xr-x. root root system_u:object_r:httpd_exec_t:s0 /usr/sbin/httpd

Файлы с данными тоже размечаются своими метками. Например, в листинге 3.53 иллюстрируются метки файлов в домашнем каталоге пользователя lich, где при помощи меток дифференцированы разные пользовательские данные по смыслу.

Листинг 3.53. Мандатные метки файлов

[lich@centos ~]$ ls -Za ~
drwxr-xr-x. lich lich unconfined_u:object_r:user_home_t:s0 Desktop
drwxr-xr-x. lich lich unconfined_u:object_r:audio_home_t:s0 Music
drwx------. lich lich unconfined_u:object_r:ssh_home_t:s0 .ssh

В частности, пользовательские ключи SSH в каталоге ~/.ssh имеют метку с типом ssh_home_t, на основании чего и можно ограничить к ним доступ таких программ как skype или firefox. Для этого нужно просто выполнять эти программы в процессах с такими типами в их метках, доступ которых к файлам с метками, имеющими тип ssh_home_t, ограничен правилами политики.

В листинге 3.54 при помощи команды sesearch(1) производится поиск разрешительных (-A, allow) правил в политике безопасности, разрешающих (-p, permissions) всем субъектам с исходным (-s, source) типом unconfined_t открывать (open) объекты файлового (file) класса (-c, class), имеющие целевой (-t, target) тип ssh_home_t.

Листинг 3.54. Мандатные правила типа unconfined_t

[lich@centos ~]$ sesearch -A -s unconfined_t -t ssh_home_t -c file -p open
Found 2 semantic av rules:
allow files_unconfined_type file_type: file { ioctl read ... open audit_access } ;
① allow unconfined_t user_home_type: file { ioctl read write create ... rename open } ;
[lich@centos ~]$ seinfo -tssh_home_t -x
    ssh_home_t
    ...
② user_home_type
[lich@centos ~]$ seinfo -auser_home_type -x
    user_home_type
        audio_home_t