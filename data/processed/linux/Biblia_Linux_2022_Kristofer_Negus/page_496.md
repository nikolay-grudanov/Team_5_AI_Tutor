---
source_image: page_496.png
page_number: 496
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.06
tokens: 7464
characters: 1999
timestamp: 2025-12-24T04:59:17.511318
finish_reason: stop
---

1. Создайте блок <IfModule mod_userdir.c>. Измените chris на любое имя пользователя, чтобы разрешить пользователям создать собственный каталог public_html. Можно добавить несколько имен:

<IfModule mod_userdir.c>
    UserDir enabled chris
    UserDir public_html
</IfModule>

2. Создайте блок директивы <Directory /home/*/public_html> и измените настройки по своему усмотрению. Пример того, как блок будет выглядеть:

<Directory "/home/*/public_html">
    Options Indexes Includes FollowSymLinks
    Require all granted
</Directory>

3. Пусть ваши пользователи создадут каталоги public_html в своих домашних каталогах:

$ mkdir $HOME/public_html

4. Установите права на выполнение (как суперпользователь), чтобы демон httpd мог получить доступ к домашнему каталогу:

# chmod +x /home /home/*

5. Если система SELinux находится в принудительном режиме (по умолчанию в дистрибутивах Fedora and RHEL), то правильный контекст файла SELinux (httpd_user_content_t) должен быть установлен в каталогах /home/*/www, /home/*/web и /home/*/public_html, чтобы SELinux позволял демону httpd автоматически получать доступ к содержимому. Если по какой-то причине контекст не задан, установите его следующим образом:

ttpd_user_content_t to /home/*
# chcon -R --reference=/var/www/html/ /home/*/public_html

6. Установите логический тип SELinux, чтобы пользователи могли обмениваться HTML-содержимым из своих домашних каталогов:

# setsebool -P httpd_enable_homedirs true

7. Перезапустите или перезагрузите службу httpd. На этом этапе появляется возможность получить доступ к содержимому каталога public_html пользователя, набрав в браузере //hostname/~user.

Защита веб-трафика с помощью технологии SSL/TLS

Все данные, которыми вы делитесь со своего сайта с помощью стандартного протокола HTTP, отправляются в виде открытого текста. Это означает, что любой, кто наблюдает за трафиком в сети между сервером и клиентом, может просматривать ваши незащищенные данные. Чтобы обезопасить эту информацию, можно добавить