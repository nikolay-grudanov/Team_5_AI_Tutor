---
source_image: page_086.png
page_number: 86
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.73
tokens: 7613
characters: 1798
timestamp: 2025-12-24T04:34:26.912584
finish_reason: stop
---

Создание нового зашифрованного раздела.

Выберите одну из следующих букв:
введите "x" для режима эксперта,
введите "p" для режима максимальной секретности,
любой другая буква для выбора стандартного режима.
?->

Выбрана стандартная конфигурация.

Конфигурация завершена. Создана файловая система со следующими свойствами:
шифр файловой системы: "ssl/aes", версия 3:0:2
шифр файла: "nameio/block", версия 4:0:1
Размер ключа: 192 бит
Размер блока: 1024 байт
Каждый файл содержит 8-байтный заголовок с уникальными IV данными.
Файловые имена зашифрованы с использованием режима сцепления вектора инициализации.
File holes passed through to ciphertext.

Введите пароль для доступа к файловой системе.
Запомните пароль, так как в случае утери его будет невозможно восстановить данные. Тем не менее этот пароль можно изменить с помощью утилиты encfsctl.

Новый пароль EncFS: $ecret
Повторите пароль EncFS: $ecret
finn@ubuntu:~$ mount
encfs on /home/finn/mnt/exposed type fuse.encfs (rw,...)
finn@ubuntu:~$ cp ~/Изображения/IMG_20150801*.jpg ~/mnt/exposed
finn@ubuntu:~$ ls -l ~/mnt/exposed/
... ... ... ...
-rw-r--r-- 1 finn finn 1014408 окт. 10 19:06 IMG_20140801_123522.jpg
... ... ... ...
-rw-r--r-- 1 finn finn 1728838 окт. 10 19:06 IMG_20140801_124215.jpg
finn@ubuntu:~$ ls -l /media/flash/secret
... ... ... ...
-rw-rw-r-- 1 finn finn 0 ноя 18 00:57 JEG0j8acowSgiyCueyqqAbohACIKSEMAJShALYNc6PF1l0
... ... ... ...
-rw-rw-r-- 1 finn finn 0 ноя 18 00:57 znchYIQd4VP1q7u5UkH2wNqzeYhFeLzTpKDN455rf1o8T1
finn@ubuntu:~$ file ~/mnt/exposed/IMG_20140801_123522.jpg
IMG_20140801_123522.jpg: JPEG image data, EXIF standard
finn@ubuntu:~$ file /media/flash/secret/9WgX2m6hiNNz8,ii7UI1AIpetU3qGuLbRHyww9eHTiNNi-9WgX2m6hiNNz8,ii7UI1AIpetU3qGuLbRHyww9eHTiNNi-: data
finn@ubuntu:~$ fusermount -u /media/flash/secret