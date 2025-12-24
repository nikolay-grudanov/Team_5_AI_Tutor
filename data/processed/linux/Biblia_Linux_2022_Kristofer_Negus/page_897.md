---
source_image: page_897.png
page_number: 897
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.29
tokens: 7527
characters: 2128
timestamp: 2025-12-24T05:10:22.105006
finish_reason: stop
---

8. Чтобы задействовать браузер для создания HTTPS-соединения с веб-сервером и просмотра содержимого созданного сертификата, в системе, работающей на сервере Apache, введите https://localhost в адресную строку браузера. Появится сообщение о ненадежности соединения. Чтобы завершить подключение:
а) нажмите кнопку I Understand the Risks (Принять риск и продолжить);
б) нажмите кнопку Add Exception (Добавить исключение);
в) нажмите кнопку Get Certificate (Получить сертификат);
г) нажмите кнопку Confirm Security Exception (Добавить исключение безопасности).

9. Создайте файл /etc/httpd/conf.d/example.org.conf, который включает виртуальный хостинг на основе имени и создает виртуальный хост, который: 1) прослушивает 80-й порт во всех интерфейсах; 2) имеет администратора joe@example.org на сервере; 3) имеет сервер joe.example.org; 4) имеет каталог DocumentRoot с файлом /var/www/html/joe.example.org; 5) имеет директиву DirectoryIndex. Она включает в себя по крайней мере файл index.html и создает в каталоге DocumentRoot файл index.html с фразой Welcome to the House of Joe.

Создайте файл example.org.conf, который выглядит следующим образом:

NameVirtualHost *:80
<VirtualHost *:80>
    ServerAdmin joe@example.org
    ServerName joe.example.org
    ServerAlias web.example.org
    DocumentRoot /var/www/html/joe.example.org/
    DirectoryIndex index.html
</VirtualHost>

Чтобы создать нужную фразу в файле index.html, введите:

# echo "Welcome to the House of Joe" > \
    /var/www/html/joe.example.org/index.html

10. Добавьте joe.example.org в конец записи localhost в файле /etc/hosts на компьютере, где запущен веб-сервер, и проверьте его, набрав http://joe.example.org в адресной строке браузера, чтобы увидеть фразу Welcome to the House of Joe при отображении страницы. Для этого:
а) перезагрузите файл httpd.conf, измененный в предыдущем упражнении, одним из двух способов:

# apachectl graceful
# systemctl restart httpd

б) отредактируйте файл /etc/hosts с помощью любого текстового редактора, чтобы строка локального хоста выглядела следующим образом:

127.0.0.1   localhost.localdomain localhost joe.example.org