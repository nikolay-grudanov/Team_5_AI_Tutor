---
source_image: page_275.png
page_number: 275
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.04
tokens: 6377
characters: 1511
timestamp: 2025-12-24T04:02:11.682240
finish_reason: stop
---

# Журнал доступа
CustomLog /srv/www/example.com/logs/access_log combined

# Включаем поддержку SSL
SSLEngine on

# Подключаем SSL-сертификат
SSLCertificateFile /etc/ssl/sert.pem
SSLCertificateKeyFile /etc/ssl/server.key
SSLCertificateChainFile /etc/ssl/chain.pem

# Настройка каталога документов
<Directory /srv/www/example.com/htdocs/>
    DirectoryIndex index.php
    Options FollowSymLinks
    AllowOverride All
    Order allow,deny
    Allow from All
</Directory>
</VirtualHost>

15.6. Пользовательские каталоги

Директива UserDir включает поддержку пользовательских каталогов. Эта директива определяет общее название подкаталога в домашних каталогах всех пользователей. По умолчанию используется каталог public_html. Данная возможность очень удобна при использовании ее в большой корпорации, где каждый сотрудник имеет собственную страничку. Аналогичное решение можно использовать для сервера кампуса, где администратору лень создавать отдельный виртуальный узел для каждого студента.

Раньше эта возможность часто использовалась на серверах, предоставляющих бесплатных хостинг. Может быть, помните адреса вида http://www.chat.ru/~mypage? Сейчас же все чаще используется технология виртуальных серверов, которую мы рассмотрели ранее, но знать что такое каталоги пользователей и как с ними работать тоже не помешает. Тем более что домашние каталоги настраиваются намного быстрее и проще, чем виртуальный сервер -- нужно всего лишь определить директиву UserDir и указать месторасположения домашних каталогов.