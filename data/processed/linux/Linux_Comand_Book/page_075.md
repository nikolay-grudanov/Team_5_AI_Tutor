---
source_image: page_075.png
page_number: 75
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.82
tokens: 6061
characters: 1271
timestamp: 2025-12-24T04:06:20.757254
finish_reason: stop
---

$ umask
0002    " "" "" "
$ umask -S
u=rwx,g=rwx,o=rx
Сначала несколько технических деталей. Значение umask - это маска, т. е. двоичное значение, которое комбинируется (посредством двоичной операции XOR) со значением Об б б для файлов и 0777 для директорий, в результате чего получаются права доступа по умолчанию . Например, операция 0002 XOR 0666 дает права 0664 для файлов, а 0002 XOR 0777 - режим 0775 для директорий.
Если такое объяснение вам не понятно, то вот простой рецепт. Используйте маску 0022, чтобы предоставить себе полные права, а всем остальным - права только на чтение/исполнение.

$ umask 0022
$ touch newfile && mkdir dir
$ Is -Id newfile dir
-rw-r--r— 1 smith smith  0 Nov 11 12:25 newfile
drwxr-xr-x 2 smith smith 4096 Nov 11 12:25 dir

Чтобы предоставить себе и вашей группе полные права, а всем остальным права только на чтение/исполнение, используйте маску 0 002.

$ umask 0002
$ touch newfile && mkdir dir
$ Is -Id newfile dir
-rw-rw-r-- 1 smith smith   0 Nov 11 12:26 newfile
drwxrwxr-x 2 smith smith 4096 Nov 11 12:26 dir

Чтобы предоставить себе полные права, а всем остальным не предоставлять никаких прав, используйте маску 0077.

$ umask 0077
$ touch newfile && mkdir dir
$ Is -Id newfile dir
-rw     1 smith smith   0 Nov 11 12:27 newfile