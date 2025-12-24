---
source_image: docs_tutorials-evolution_list_topics_bare-metal__onlyoffice.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 72.21
tokens: 10490
characters: 4788
timestamp: 2025-12-24T05:30:04.150835
finish_reason: stop
---

### Установка Onlyoffice Community на выделенный сервер Bare Metal

С помощью этого руководства вы развернете экосистему приложений для совместной работы Onlyoffice. Доступ к приложениям обеспечивается через онлайн-портал.

Вы установите и настроите два модуля пакета Onlyoffice Community Edition:

• Сервер документов
• Сервер совместной работы

Шаги:

1. Разверните инфраструктуру.
2. Настройте систему для работы.
3. Настройте базу данных.
4. Настройте контейнеры с модулями Onlyoffice.
5. Запустите и настройте Onlyoffice.

1. Разверните инфраструктуру

1. Арендуйте сервер Bare Metal. В блоке Сетевые параметры выберите подсеть по умолчанию и активируйте опцию Подключить публичный IP:

![Сетевые настройки](https://example.com/screenshot_1.png)

2. Убедитесь, что на сервере работает интернет:

3. Подключитесь к серверу по SSH или через виртуальную консоль.

4. Установите Docker.

Пример установки Docker на ОС Debian 10:

```
sudo apt update
sudo apt install docker.io
```

2. Настройте систему для работы

1. Подготовьте каталоги для проекта:

```bash
sudo mkdir -p "/app/onlyoffice/mysql/conf.d";
sudo mkdir -p "/app/onlyoffice/mysql/data";
sudo mkdir -p "/app/onlyoffice/mysql/initdb";
sudo mkdir -p "/app/onlyoffice/mysql/logs";
chown 999:999 /app/onlyoffice/mysql/logs;

sudo mkdir -p "/app/onlyoffice/communityserver/data";
sudo mkdir -p "/app/onlyoffice/communityserver/logs";

sudo mkdir -p "/app/onlyoffice/documentserver/data";
sudo mkdir -p "/app/onlyoffice/documentserver/logs";
```

2. Создайте сеть для связности Docker-контейнеров:

```bash
sudo docker network create --driver bridge onlyoffice
```

3. Настройте базу данных

1. Создайте файл с конфигурацией SQL-сервера:

```sql
echo "mysqld!
sql_mode = 'NO_ENGINE_SUBSTITUTION'
max_connections = 1000
max_allowed_packet = 1048576000
group_concat_max_len = 2048
log-error = /var/log/mysql/error.log" > /app/onlyoffice/mysql/conf.d/onlyoffice.cnf
sudo chmod 0644 /app/onlyoffice/mysql/conf.d/onlyoffice.cnf
```

Примечание
В примере использованы минимальные настройки. Для лучшей производительности рекомендуется использовать mysqltuner и другие инструменты оптимизации.

2. Создайте файл для оптимизации создания пользователей:

```sql
echo "CREATE USER 'onlyoffice_user'@'localhost' IDENTIFIED BY 'onlyoffice_pass';
CREATE USER 'mail admin'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'onlyoffice_user'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'mail admin'@'%' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;" > /app/onlyoffice/mysql/initdb/setup.sql
```

Где <password> — пароли пользователей.

3. Установите и запустите контейнер с базой данных:

```bash
sudo docker run --net onlyoffice -i -t -d --restart=always --name onlyoffice-mysql-server -p 3306:3306 \
-v /app/onlyoffice/mysql/conf.d:/etc/mysql/conf.d \
-v /app/onlyoffice/mysql/data:/var/lib/mysql \
-v /app/onlyoffice/mysql/initdb:/docker-entrypoint-initdb.d \
-v /app/onlyoffice/mysql/logs:/var/log/mysql \
-e MYSQL_ROOT_PASSWORD=my-secret-pw \
-e MYSQL_DATABASE=onlyoffice \
mysql:5.7
```

Пример выполнения команд:

4. Настройте контейнеры с модулями Onlyoffice

1. Установите и запустите контейнер с сервером документов:

```bash
sudo docker run --net onlyoffice -i -t -d --restart=always --name onlyoffice-document-server \
-v /app/onlyoffice/documentServer/logs:/var/log/onlyoffice \
-v /app/onlyoffice/documentServer/data:/var/www/onlyoffice/data \
-v /app/onlyoffice/documentServer/lib:/var/lib/postgresql \
onlyoffice/documentserver
```

2. Установите и запустите контейнер с сервером совместной работы:

```bash
sudo docker run --net onlyoffice -i -t -d --restart=always --name onlyoffice-community-server -p 80:80 \
-e MYSQL_SERVER_ROOT_PASSWORD=my-secret-pw \
-e MYSQL_SERVER_DB_NAME=onlyoffice \
-e MYSQL_SERVER_USER=onlyoffice_user \
-e MYSQL_SERVER_PASS=onlyoffice_pass \
-e DOCUMENT_SERVER_PORT_80_TCP_ADDR=onlyoffice-document-server \
-v /app/onlyoffice/CommunityServer/data:/var/www/onlyoffice/Data \
-v /app/onlyoffice/CommunityServer/logs:/var/log/onlyoffice \
onlyoffice/communityserver
```

5. Запустите и настройте Onlyoffice

1. В браузере перейдите на страницу https://<IP-адрес_сервера>:4443. Дождитесь окончания загрузки:

![Окно OnlyOffice Portal](https://example.com/screenshot_2.png)

Если загрузка не завершается

Откроется окно с настройками Onlyoffice:

![Настройки OnlyOffice Portal](https://example.com/screenshot_3.png)

2. В блоке Password введите пароль.
3. В поле Language выберите язык.
4. В поле Time Zone выберите часовой пояс.
5. Нажмите Continue.

Вы попадете в главное меню Onlyoffice, из которого можно настроить все необходимые компоненты для совместной работы. Установка и настройка завершена.