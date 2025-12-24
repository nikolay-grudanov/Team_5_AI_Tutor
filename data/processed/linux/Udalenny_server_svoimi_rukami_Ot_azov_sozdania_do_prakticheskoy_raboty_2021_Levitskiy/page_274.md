---
source_image: page_274.png
page_number: 274
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.43
tokens: 6388
characters: 1325
timestamp: 2025-12-24T04:02:04.897591
finish_reason: stop
---

Обязательно должны присутствовать директивы ServerName, DocumentRoot, ServerAdmin и ErrorLog.

Виртуальные серверы можно идентифицировать по имени или по IP-адресу. Идентификация по имени имеет существенное преимущество перед идентификацией по IP-адресу: вы не ограничены количеством адресов, имеющимся у вас в распоряжении. Вы можете использовать любое количество виртуальных серверов, и при этом вам не потребуются дополнительные адреса. Такое возможно благодаря использованию протокола HTTP/1.1. Данный протокол давно поддерживается всеми современными браузерами.

В листинге 15.1 приведен файл конфигурации реального виртуального узла, изменено только имя сервера.

Листинг 15.1. Конфигурация виртуального узла

# Поддерживаем протокол HTTP (порт 80) для перенаправления на HTTPS-версию
# Если клиент вводит адрес http://example.com, выполняем перенаправление на https://example.com
<VirtualHost *:80>
    ServerName example.com
    Redirect permanent / https://example.com/
</VirtualHost>

# Основная конфигурация
<VirtualHost *:443>
    ServerAdmin it@example.com
    # Имя узла
    ServerName example.com
    # Псевдоним и IP-адрес
    ServerAlias www.example.com 111.111.111.115
    # Каталог документов
    DocumentRoot /srv/www/example.com/htdocs
    # Журнал ошибок
    ErrorLog /srv/www/example.com/logs/error_log