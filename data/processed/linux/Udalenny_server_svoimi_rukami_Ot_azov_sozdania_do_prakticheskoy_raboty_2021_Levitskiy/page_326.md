---
source_image: page_326.png
page_number: 326
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.02
tokens: 6302
characters: 1026
timestamp: 2025-12-24T04:03:13.104106
finish_reason: stop
---

Далее будет показано, как настроить Pagespeed и Memcached для сервера Apache.

18.4.1. Настройка Pagespeed

Первым делом нужно определить разрядность операционной системы. Конечно, сегодня найти 32-разрядный VDS — еще та задача, но все же. Введите команду:

uname -a

Если увидите в выводе x86_64 — ваша система 64-разрядная и нужно ввести следующие команды:

cd /tmp
wget https://dl-ssl.google.com/dl/linux/direct/mod-pagespeed-stable_current_amd64.deb
sudo dpkg -i mod-pagespeed-stable_current_amd64.deb

Для 32-разрядной системы нужно ввести команды:

cd /tmp
wget https://dl-ssl.google.com/dl/linux/direct/mod-pagespeed-stable_current_i386.deb
sudo dpkg -i mod-pagespeed-stable_current_i386.deb

Хотя, как правило, ваша система окажется 64-разрядной и последний абзац можно было бы и не писать. Но мало ли. Вдруг кому-то пришла в голову светлая мысль организовать веб-сервер на 32-битной машине.

После этого нужно перезапустить Apache:
sudo service apache2 restart

Собственно, на этом все. Больше ничего делать не нужно.