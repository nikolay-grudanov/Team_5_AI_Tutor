---
source_image: page_093.png
page_number: 93
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.22
tokens: 7524
characters: 1870
timestamp: 2025-12-24T04:34:29.123843
finish_reason: stop
---

Подсистема управления файлами и вводом-выводом

finn@ubuntu:~$ chmod g-r,o-r README.finn
finn@ubuntu:~$ ls -la README.finn
-rw------- 1 finn admin 2471 окт. 11 01:12 README.finn
finn@ubuntu:~$ chmod g-r,o-r README.jake
chmod: изменение прав доступа для 'README.jake': Операция не позволена

Семантика режима доступа разных типов файлов

Права доступа r, w, x для обычных файлов представляются чем-то интуитивно понятным, но для других типов файлов это не совсем так. Например, каталог (см. рис. 3.2) содержит список имен файлов, поэтому право w для каталога — это право записи в этот список и право стирания из этого списка, что трансформируется в право удаления файлов из каталога и создания файлов в каталоге. Аналогично, право r для каталога — это право просмотра списка имен его файлов. И наконец, право x для каталога является правом прохода в каталог, т. е. позволяет обращаться к файлам внутри каталога по их имени (листинг 3.38).

Листинг 3.38. Права доступа к каталогу

finn@ubuntu:~$ mkdir folder
finn@ubuntu:~$ ls -lad folder/
drwxrwxr-x 2 finn finn 4096 окт. 12 00:37 folder/
finn@ubuntu:~$ cp /etc/magic folder
finn@ubuntu:~$ chmod u-w folder
finn@ubuntu:~$ ls -lad folder/
dr-xrwxr-x 2 finn finn 4096 окт. 12 00:40 folder/
finn@ubuntu:~$ cp /etc/localtime folder/
cp: невозможно создать обычный файл «folder/localtime»: Отказано в доступе
finn@ubuntu:~$ rm folder/magic
rm: невозможно удалить «folder/magic»: Отказано в доступе
finn@ubuntu:~$ ls -li folder/
итого 4
20318203 -rw-r--r-- 1 finn finn 111 окт. 12 00:40 magic
finn@ubuntu:~$ chmod u-r folder
finn@ubuntu:~$ ls -lad folder/
d--xrwrx-x 2 finn finn 4096 окт. 12 00:40 folder/
finn@ubuntu:~$ ls -li folder/
ls: невозможно открыть каталог folder/: Отказано в доступе
finn@ubuntu:~$ ls -li folder/magic
! 20318203 -rw-r--r-- 1 finn finn 111 окт. 12 00:40 folder/magic
finn@ubuntu:~$ chmod u-x folder/