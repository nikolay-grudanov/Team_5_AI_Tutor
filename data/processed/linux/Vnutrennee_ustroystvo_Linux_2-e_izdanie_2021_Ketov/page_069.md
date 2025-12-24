---
source_image: page_069.png
page_number: 69
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.70
tokens: 7608
characters: 1860
timestamp: 2025-12-24T04:33:55.555686
finish_reason: stop
---

20357139 drwxr-xr-x 2 finn finn 4096 апр. 1 01:59 folder

finn@ubuntu:~$ cd folder
finn@ubuntu:~/folder$ ls -lat
итого 8

20357139 drwxr-xr-x 2 finn finn 4096 апр. 1 01:59 .
20332580 drwxr-xr-x 4 finn finn 4096 апр. 1 01:59 ..
finn@ubuntu:~/folder$ mkdir child
finn@ubuntu:~/folder$ cd child
finn@ubuntu:~/folder/child$ ls -lat
итого 8

20357140 drwxr-xr-x 2 finn finn 4096 апр. 1 02:02 .
20357139 drwxr-xr-x 3 finn finn 4096 апр. 1 02:02 ..
finn@ubuntu:~/folder/child$ cd ../..
finn@ubuntu:~/folder$ stat folder/
    Файл: «folder/»
    Размер: 4096     Блоков: 8     Блок В/В: 4096 каталог
    Устройство: fc00h/64512d     Inode: 20357139     Ссылки: 3

finn@ubuntu:~$ rmdir folder
rmdir: не удалось удалить «folder»: Каталог не пуст

Существенным ограничением жесткой ссылки в дереве каталогов, куда смонтирована более чем одна файловая система, является локальность жесткой ссылки в пределах своей файловой системы в силу локальной значимости номеров индексных дескрипторов. Так как на каждой новой файловой системе номера индексных дескрипторов начинают нумероваться с нуля, то жесткая ссылка всегда указывает на метаданные файла в «своей» файловой системе и не может указывать на метаданные файла в «чужой» файловой системе общего дерева каталогов. Для преодоления этого ограничения служит символическая ссылка symlink(7), являющаяся самостоятельным служебным типом (см. ① на рис. 3.2) и содержащая путевое имя (см. ③ на рис. 3.2 и ★ в листинге 3.9) к целевому файлу.

Листинг 3.9. Символическая ссылка

finn@ubuntu:~$ ln -s read.me readme.1st
finn@ubuntu:~$ ls -li read*
20318653 -rw-r--r-- 1 finn finn 0 апр. 1 01:22 read.me
20319944 l-rw-rw-rwx 1 finn finn 7 апр. 2 00:03 readme.1st -> read.me ★

В случае с символической ссылкой при удалении целевого файла сама ссылка будет указывать в никуда и называться «сиротой» (orphan). Попытка прочитать (лис-