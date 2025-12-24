---
source_image: page_508.png
page_number: 508
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.41
tokens: 7139
characters: 793
timestamp: 2025-12-24T04:59:24.431339
finish_reason: stop
---

9. Создайте файл с именем /etc/httpd/conf.d/example.org.conf, который включает виртуальный хостинг на основе имен и создает виртуальный хост, который должен:
   ▪ прослушивать все интерфейсы на порте 80;
   ▪ иметь администратора сервера joe@example.org;
   ▪ иметь имя сервера joe@example.org;
   ▪ иметь директиву DocumentRoot в каталоге /var/www/html/example.org;
   ▪ иметь директиву DirectoryIndex, которая включает в себя как минимум файл index.html.

10. В каталоге DocumentRoot создайте файл Index.html, содержащий фразу: Welcome to the House of Joe. Добавьте текст joe.example.org в конец строки localhost в файле /etc/hosts на компьютере, на котором запущен веб-сервер. Затем введите в браузере joe.example.org. На первой странице вы должны увидеть фразу Welcome to the House of Joe.