---
source_image: page_067.png
page_number: 67
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.42
tokens: 7602
characters: 1803
timestamp: 2025-12-24T04:33:52.136098
finish_reason: stop
---

3.2.4. Ссылки

Каталог как файл-список имен других файлов, которым сопоставлены номера индексных дескрипторов, не запрещает иметь два разных имени файла, указывающих на одни и те же метаданные (см. 3 на рис. 3.2). Такой эффект носит название жесткой ссылки, создать которую можно при помощи команды ln(1) (листинг 3.5).

Листинг 3.5. Жесткая ссылка

finn@ubuntu:~$ touch readme
finn@ubuntu:~$ ls -li readme
20318653 -rw-r--r-- 1 finn finn 0 апр. 1 01:22 readme
finn@ubuntu:~$ ln readme readme.txt
finn@ubuntu:~$ touch README
finn@ubuntu:~$ ls -li readme readme.txt README
20318653 -rw-r--r-- 2 finn finn 0 апр. 1 01:22 readme
20319121 -rw-r--r-- 1 finn finn 0 апр. 1 01:23 README
20318653 -rw-r--r-- 2 finn finn 0 апр. 1 01:22 readme.txt

Более того, оба имени являются равнозначными, и нет возможности узнать, какое из них создано первым, из чего нужно заключить, что первое и единственное имя файла уже является его жесткой ссылкой (на номер индексного дескриптора). При добавлении файлу нового имени (жесткой ссылки) в его метаданных увеличивается счетчик количества имен (см. 1 в листинге 3.6), а при удалении файла сначала удаляется имя и уменьшается счетчик количества имен 2, и только при удалении последнего имени высвобождаются метаданные и данные файла.

Листинг 3.6. Счетчик имен файла

finn@ubuntu:~$ ln readme read.me
finn@ubuntu:~$ ls -li read*
20318653 -rw-r--r-- 3 finn finn 0 апр. 1 01:22 readme
20318653 -rw-r--r-- 3 finn finn 0 апр. 1 01:22 read.me
20318653 -rw-r--r-- 3 finn finn 0 апр. 1 01:22 readme.txt
finn@ubuntu:~$ rm readme
finn@ubuntu:~$ ls -li read*
20318653 -rw-r--r-- 2 finn finn 0 апр. 1 01:22 read.me
20318653 -rw-r--r-- 2 finn finn 0 апр. 1 01:22 readme.txt
finn@ubuntu:~$ rm readme.txt
finn@ubuntu:~$ ls -li read*
20318653 -rw-r--r-- 1 finn finn 0 апр. 1 01:22 read.me